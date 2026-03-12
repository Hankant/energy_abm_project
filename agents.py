"""
模块名称：微观代理模块 (Micro-Agent Module)
核心作用：定义系统中所有离散个体（如家庭）的异质性状态与微观决策逻辑。

【能力边界与开发规范】
1. 只读宏观事实：Agent 只能读取 model 层的公开环境属性（如当前电价、气温、政策信号），
   绝不允许其内部方法直接修改 model 层的全局变量。
2. 独立行为决策：Agent 的决策行为 (step) 只能基于自身属性（如价格敏感度、家电保有量）、
   感知到的环境条件，以及自身历史记忆独立做出响应。
3. 状态数据封装：Agent 的内部状态对外封闭，不由外界直接改写，只能由 model 层的
   DataCollector 被动抓取和汇总。
4. 记忆驱动（含重要性评分）：
   - Agent 具备带权重的记忆系统，每条记忆在存储时会计算"重要性评分"（0~10分）。
   - 评分依据：气温极端程度、电价偏离基准幅度、政策信号强度。
   - 在构造 LLM Prompt 时，综合"重要性 × 0.6 + 近期度 × 0.4"排序，
     优先呈现最值得参考的历史记忆，而非简单截取最近 N 条。
   - 参考：Park et al. (2023) Generative Agents 的记忆流重要性检索机制。
"""
import mesa


class HouseholdAgent(mesa.Agent):
    """
    家庭决策 Agent。
    具备异质性属性、带重要性评分的记忆系统，支持 LLM 推理决策与规则树两套决策机制。
    """

    def __init__(self, unique_id, model, agent_data):
        super().__init__(unique_id, model)

        # --- 个体异质性属性 ---
        self.location             = agent_data.get('location', '长三角')
        self.income_level         = agent_data.get('income_level', '中')
        self.house_area           = agent_data.get('house_area', 80)
        self.has_ac               = int(agent_data.get('has_ac', 1))
        self.has_ev               = int(agent_data.get('has_ev', 0))
        self.environmental_awareness = agent_data.get('env_awareness', '中')
        self.price_sensitivity    = agent_data.get('price_sensitivity', '中')

        # --- 动态状态 ---
        self.current_power_consumption = 0.0
        self.wtp = 0.0

        # --- 记忆模块 ---
        # 每条记录格式: {day, temperature, price, policy_type, policy_announcement,
        #               consumption, wtp, importance}
        self.memory: list[dict] = []

        # --- 分层 Prompt：不变的 Persona 设定（初始化时只需构造一次） ---
        self._system_persona = f"""
你是一个家庭的户主，正在决定今天的用电行为。
请你始终牢记以下固定的家庭特征，并基于这些条件进行思考：

【家庭属性】
- 所在地区：{self.location}
- 收入水平：{self.income_level}
- 住房面积：{self.house_area}平米
- 拥有空调数量：{self.has_ac}台
- 拥有电动车数量：{self.has_ev}辆
- 环保意识：{self.environmental_awareness}
- 价格敏感度：{self.price_sensitivity}
"""

    # ──────────────────────────────────────────
    # 主决策入口
    # ──────────────────────────────────────────

    def step(self):
        """执行每日决策推演，并将结果（附重要性评分）存入记忆。"""
        self.llm_decision()

        importance = self._compute_memory_importance(
            temperature=self.model.current_temperature,
            price=self.model.current_price,
            policy_type=self.model.current_policy.policy_type,
        )

        self.memory.append({
            "day":                  self.model.schedule.steps,
            "temperature":          self.model.current_temperature,
            "price":                self.model.current_price,
            "policy_type":          self.model.current_policy.policy_type,
            "policy_announcement":  self.model.current_policy.announcement,
            "consumption":          self.current_power_consumption,
            "wtp":                  self.wtp,
            "importance":           importance,
        })

    # ──────────────────────────────────────────
    # 记忆重要性评分模块（参考 Generative Agents）
    # ──────────────────────────────────────────

    def _compute_memory_importance(self, temperature: float, price: float, policy_type: str) -> float:
        """
        计算一条记忆的重要性评分（0~10分，越高越值得在未来 Prompt 中优先引用）。

        【评分维度】
        1. 气温极端度（0~4分）：偏离舒适区（18~26°C）越远得分越高。
           每偏离 10°C 得约 4 分，上限 4 分。
        2. 电价偏离度（0~3分）：超过基准电价 0.6 元越多得分越高。
           每超 0.5 元得 3 分，上限 3 分。
        3. 政策强度（0~3分）：
           - carbon_tax / power_control → 3 分（强干预）
           - subsidy → 1.5 分（温和激励）
           - news → 1 分（信息类）
           - none → 0 分
        """
        # 气温极端度
        temp_deviation = abs(temperature - 22.0)
        temp_score = min(temp_deviation / 10.0 * 4, 4.0)

        # 电价偏离度
        price_deviation = max(0, price - 0.6)
        price_score = min(price_deviation / 0.5 * 3, 3.0)

        # 政策强度
        policy_score_map = {
            "carbon_tax":    3.0,
            "power_control": 3.0,
            "subsidy":       1.5,
            "news":          1.0,
            "none":          0.0,
        }
        policy_score = policy_score_map.get(policy_type, 0.0)

        return round(min(temp_score + price_score + policy_score, 10.0), 2)

    def _retrieve_salient_memories(self, top_n: int = 3) -> list:
        """
        按"重要性 × 0.6 + 近期度 × 0.4"加权综合评分，
        从全部历史记忆中检索最值得引用的 top_n 条。

        【检索逻辑】
        - 近期度：越晚的记忆近期度坐标越高（线性归一化 0~1）。
        - 重要性：来自 _compute_memory_importance() 的 0~10 分，归一化到 0~1。
        - 综合评分 = 0.6 × 重要性归一化 + 0.4 × 近期度
          → 重要事件即便较久远也会被优先选出；近期平淡的日子权重会被适度压低。
        """
        if not self.memory:
            return []
        n = len(self.memory)
        scored = []
        for idx, rec in enumerate(self.memory):
            recency_score   = idx / (n - 1) if n > 1 else 1.0
            importance_norm = rec["importance"] / 10.0
            composite       = 0.6 * importance_norm + 0.4 * recency_score
            scored.append((composite, rec))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [rec for _, rec in scored[:top_n]]

    # ──────────────────────────────────────────
    # LLM 决策（阶段二核心）
    # ──────────────────────────────────────────

    def llm_decision(self):
        """
        通过 LLM API 进行真实决策推理。
        Prompt 中注入：家庭属性、今日环境、今日政策信号、邻居行为、以及按重要性加权筛选的历史记忆。
        """
        import requests
        import json

        base_load = 3 + (self.house_area / 50)
        temperature = self.model.current_temperature
        price = self.model.current_price
        policy = self.model.current_policy

        # -- 构建历史记忆摘要（按重要性+近期度加权检索，最多 3 条）--
        memory_text = "无历史记录（今天是第一天）。"
        if self.memory:
            salient = self._retrieve_salient_memories(top_n=3)
            lines = []
            for rec in salient:
                importance_label = (
                    "高" if rec["importance"] >= 7
                    else "中" if rec["importance"] >= 3
                    else "低"
                )
                lines.append(
                    f"  第{rec['day']}天 [重要性:{importance_label} {rec['importance']}分] "
                    f"| 气温:{rec['temperature']}°C "
                    f"| 电价:{rec['price']}元 "
                    f"| 政策:{rec['policy_type']} "
                    f"| 我的用电:{rec['consumption']}kWh "
                    f"| WTP:{rec['wtp']}元"
                )
            memory_text = "\n".join(lines)

        # -- 构建社区邻居行为摘要（如果社交网络模块已启用）--
        neighbor_text = "社区网络模块未启用，无邻里信息。"
        if self.model.use_social_network:
            neighbors = self.model.get_neighbors(self.unique_id)
            if neighbors:
                nb_lines = []
                for nb in neighbors:
                    if nb.memory:
                        last = nb.memory[-1]
                        nb_lines.append(
                            f"  邻居(收入:{nb.income_level}) — "
                            f"昨日用电:{last['consumption']}kWh，"
                            f"WTP:{last['wtp']}元，"
                            f"所在天气:{last['temperature']}°C"
                        )
                    else:
                        nb_lines.append(f"  邻居(收入:{nb.income_level}) — 暂无历史记录")
                neighbor_text = "\n".join(nb_lines)
            else:
                neighbor_text = "暂无直接邻居数据。"

        # -- 动态层 Prompt：每日变动的环境/记忆/政策信号 --
        daily_prompt = f"""
【今日环境数据】
- 气温：{temperature}摄氏度
- 当前电价：{price}元/千瓦时（平时正常基准电价约为0.6元/千瓦时）
- 基础刚性耗电（照明/冰箱等）：{base_load:.1f}千瓦时

【社区邻居的近期行为（社会规范参考）】
{neighbor_text}
（注：可参考邻居行为来校准自己的用电决策，例如若邻居普遍节电你会感受到社会压力；
 但你也可以基于自身条件做出独立判断，无需无条件从众。）

【今日政策/新闻信号】
{policy.describe()}

【你最值得参考的历史记忆（已按重要性+近期度加权筛选，非简单截取最近几天）】
{memory_text}
（注：重要性越高代表该天环境冲击越大，对今天决策的参考价值越高）

【决策任务】
请结合你的家庭条件、历史消费记忆（例如：如果昨天电费很高你会反思是否减少用电）、
今日气候压力，以及今日的政策/新闻信号，综合决定：
1. 今天家里一共需要消耗多少千瓦时的电？
2. 假设极端天气下供电紧张，你每月最高愿意额外支付多少钱（RMB）保证不被拉闸限电（WTP）？

【必须遵守的输出格式】
只输出一段合法的 JSON，不要输出任何额外的文字解释或 markdown 符号。
{{
    "decision_reasoning": "用一句话简述你做出该用电决策的核心原因（可引用历史记忆或政策影响）",
    "total_daily_kwh": (数字，今天总耗电量，必须 >= {base_load:.1f}),
    "wtp_rmb": (数字，愿意额外支付的保电费，可以为0)
}}
"""

        url = "https://vip.yi-zhan.top/v1/chat/completions"
        headers = {
            "Authorization": "Bearer sk-ffRiFOhBshgeGL4n18Ea3835Ed8e4dD7Ad97C7F92f1aBd8f",
            "Content-Type": "application/json"
        }
        
        # 组装分层 Prompt：System Persona + User Daily Context
        messages = [
            {"role": "system", "content": self._system_persona.strip()},
            {"role": "user", "content": daily_prompt.strip()}
        ]
        
        payload = {
            "model": "gemini-2.5-pro",
            "messages": messages,
            "temperature": 0.5
        }

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            if response.status_code == 200:
                result = response.json()
                content = result['choices'][0]['message']['content']
                content = content.replace("```json", "").replace("```", "").strip()
                data = json.loads(content)

                self.current_power_consumption = round(float(data.get("total_daily_kwh", base_load)), 1)
                self.wtp = float(data.get("wtp_rmb", 0.0))
                print(
                    f"  [Agent {self.unique_id} {self.location}{self.income_level}收入] "
                    f"思维链: {data.get('decision_reasoning')} | "
                    f"耗电:{self.current_power_consumption}kWh | WTP:{self.wtp}元"
                )
            else:
                print(f"  [API Error {response.status_code}] 调用失败，退回至规则决策...")
                self.human_like_decision()
        except Exception as e:
            print(f"  [API Exception] {e}，退回至规则决策...")
            self.human_like_decision()

    # ──────────────────────────────────────────
    # 规则树决策（备选方案 / 阶段一）
    # ──────────────────────────────────────────

    def human_like_decision(self):
        """
        基于人类直觉的条件响应树（当 LLM 不可用时的备选方案）。
        注意：规则树不感知记忆和政策，仅作为降级保障。
        """
        base_load = 3 + (self.house_area / 50)
        temperature = self.model.current_temperature
        price = self.model.current_price

        ac_load = 0
        ev_load = 0

        if temperature >= 35:
            if self.location == '大湾区':
                if self.price_sensitivity == '高':
                    ac_load = 5 * min(self.has_ac, 1) if price > 1.0 else 10 * min(self.has_ac, 1)
                else:
                    ac_load = 15 * self.has_ac
            elif self.location == '长三角':
                if self.income_level == '高':
                    ac_load = 20 * self.has_ac
                elif self.income_level == '中':
                    ac_load = 8 * self.has_ac if (price > 1.0 and self.environmental_awareness == '高') else 12 * self.has_ac
                else:
                    ac_load = 3 if temperature >= 38 else 0

        elif temperature <= 5:
            if self.location == '长三角':
                ac_load = 4 if (self.income_level == '低' and price > 0.8) else 18 * self.has_ac
            elif self.location == '大湾区':
                ac_load = 10 * self.has_ac

        if self.has_ev:
            ev_load = 0 if (price > 1.0 and self.price_sensitivity == '高') else (15 if price > 1.0 else 20)

        self.current_power_consumption = round(base_load + ac_load + ev_load, 1)

        if temperature >= 38 or temperature <= 0:
            if self.income_level == '高':
                self.wtp = 50
            elif self.income_level == '中':
                self.wtp = 10 if self.price_sensitivity == '高' else 20
            else:
                self.wtp = 0
        else:
            self.wtp = 0

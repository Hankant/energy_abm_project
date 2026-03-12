"""
模块名称：宏观环境与调度模块 (Macro-Environment & EBM Scheduler Module)
核心作用：充当仿真世界的"造物主"，管理全局时间线、下发环境波动信号（气候、电价、政策）
        以及汇总微观个体的宏观表现。

【能力边界与开发规范】
1. 全局单向控制：只负责控制时间的推演机制 (step)，向所有 Agent 单向广播宏观信号。
2. 禁止微观干预：绝不允许包含任何个体的经济学偏爱与决策逻辑。
3. 数据无状态汇聚：将微观 Agent 零散输出聚合为宏观指标，自身不编造底层数据。
4. 资源生命周期：接收外部传入的 Agent 数据列表完成批量实例化（数据加载职责已剥离至 run.py）。
5. 政策信号透传：持有当天的 PolicySignal 对象，由 run.py 的政策剧本在每步前注入。
6. 社区网络（可选）：若启用社交网络拓扑，则构建并持有 networkx.Graph，Agent 可借此
   查询邻居昨日行为，模拟社会影响与绿色行为扩散。
"""
import mesa
from agents import HouseholdAgent
from policy import PolicySignal, NO_POLICY


class EnergyTransitionModel(mesa.Model):
    """
    宏观能源与微观家庭混合模型 (EBM + ABM)。

    【初始化参数】
    agent_data_list     (list[dict]): 由 run.py 加载并传入的 Agent 初始属性字典列表。
    use_social_network  (bool):       是否启用社区网络拓扑模块（默认关闭）。
                                      开启后 Agent 可感知邻居昨日行为，影响 LLM 决策。
    network_k           (int):        WS 网络每节点初始邻居数（默认4）。
    network_p           (float):      WS 网络随机重连概率（默认0.2）。
    """

    def __init__(
        self,
        agent_data_list: list,
        use_social_network: bool = False,
        network_k: int = 4,
        network_p: float = 0.2,
    ):
        super().__init__()
        self.schedule = mesa.time.RandomActivation(self)

        self.datacollector = mesa.DataCollector(
            model_reporters={
                "Total_Consumption":   "total_consumption",
                "Avg_WTP":             "avg_wtp",
                "Current_Price":       "current_price",
                "Current_Temp":        "current_temperature",
                "Policy_Type":         lambda m: m.current_policy.policy_type,
                "Social_Network_On":   "use_social_network",
            },
            agent_reporters={
                "Consumption":         "current_power_consumption",
                "WTP":                 "wtp",
                "Income":              "income_level",
                "Location":            "location",
                "Price_Sensitivity":   "price_sensitivity",
            }
        )

        # --- 宏观环境变量 ---
        self.current_temperature = 25
        self.current_price       = 0.6
        self.total_consumption   = 0.0
        self.avg_wtp             = 0.0

        # --- 政策信号（由 run.py 每步注入） ---
        self.current_policy: PolicySignal = NO_POLICY

        # --- 社区网络模块（可选开关） ---
        self.use_social_network = use_social_network
        self.social_network     = None   # networkx.Graph，启用后由下方初始化

        # --- 批量实例化 Agent ---
        for index, agent_data in enumerate(agent_data_list):
            agent_id = agent_data.get('id', index)
            agent = HouseholdAgent(agent_id, self, agent_data)
            self.schedule.add(agent)

        # --- 构建社区网络（在所有 Agent 注册完成后） ---
        if self.use_social_network:
            from network import build_community_network, describe_network
            agent_ids = [a.unique_id for a in self.schedule.agents]
            self.social_network = build_community_network(
                agent_ids, k=network_k, p=network_p
            )
            print(f"[社区网络] 已启用 Watts-Strogatz 小世界网络：{describe_network(self.social_network)}")
        else:
            print("[社区网络] 已关闭（独立决策模式）。")

        print(f"[Model] 成功初始化 {len(agent_data_list)} 个家庭 Agent。")

    def get_neighbors(self, agent_id) -> list:
        """
        返回指定 Agent 的社区邻居 Agent 对象列表。
        仅在社区网络模块启用时有效，否则返回空列表。
        """
        if not self.use_social_network or self.social_network is None:
            return []
        neighbor_ids = list(self.social_network.neighbors(agent_id))
        # 将 id 映射回 Agent 对象
        id_to_agent = {a.unique_id: a for a in self.schedule.agents}
        return [id_to_agent[nid] for nid in neighbor_ids if nid in id_to_agent]

    def step(self):
        """环境推演的每一个时间步（例如：1天）。"""
        if self.current_policy.policy_type != "none":
            print(f"\n[政策播报] {self.current_policy.announcement}")

        self.schedule.step()

        agents = self.schedule.agents
        self.total_consumption = round(sum(a.current_power_consumption for a in agents), 1)
        self.avg_wtp = round(
            sum(a.wtp for a in agents) / len(agents) if agents else 0.0, 2
        )
        self.datacollector.collect(self)

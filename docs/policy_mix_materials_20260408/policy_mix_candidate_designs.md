# 居民侧需求响应政策组合：ABM微观参数映射与预选方案设计 (V2.0 具象化版)

本版本旨在将宏观政策包严丝合缝地转化为 ABM 系统中的**类（Class）属性配置**和**单步（Step）计算公式**。不再仅仅描述政策文本，而是清晰定义这些方案如何在代码沙盒中运行以及如何与不同属性的智能体进行碰撞。

## 1. 异质性 Agent 的具体分类维度与代码化属性

在环境中，居民 `HouseholdAgent` 不能是同质的。必须根据文献将他们分为以下特征去进行响应能力的客观限制：

### 1.1 核心客观状态 (State Attributes)
- `income_group`: 枚举值 `[Low, Medium, High]`。
  - **核心影响**：决定预算约束。当 `income_group == "Low"` 时，触发特定政策如加州CARE（低收入保护）或英国的冬季特别豁免。
- `housing_type`: 枚举值 `[Renter, Owner]` 以及房屋新旧。
  - **核心影响**：改造权（Split-incentive 租户/房东矛盾）。`Renter` 无法响应“房屋保温升级”、“屋顶光伏安装”等前置补贴政策。
- `tech_level`: 设备的自动化干预潜力。
  - `Low`: 纯手动响应，负荷转移极限 `max_shiftable_ratio = 5%~10%`，且主观疲劳成本（Hassle Cost）极高，转移用电需要手动关闭电器。
  - `Medium`: 拥有智能电表，但不具备大功率柔性可控设备。`max_shiftable_ratio = 15%`。
  - `High`: 拥有电动汽车（EV）、电热泵或储能电池。`max_shiftable_ratio = 30%~40%`，在自动控制下转移负荷主观疲劳成本几乎为 0。

### 1.2 主观认知与行为属性 (Cognitive & Behavioral Parameters)
- `trust_threshold`: `float` 取值 `[0.0, 1.0]`。
  - 对外部聚合商或电网接管家庭智能设备的警惕度。政策中只要涉及“第三方平台自动控制”功能，计算参与率 `Enrollment` 时，若方案未提供信任补偿且 `trust_threshold < 0.6`，Agent 拒绝托管。
- `price_elasticity`: 价格弹性常数，高收入群体通常对低级别的电价涨幅缺乏痛感。

---

## 2. 具体方案的 ABM 逻辑表现（最具代表性的机制拆解）

### P2：加州“动态响应+低收入重奖”原型 (California Prototype)

**环境触发机制**：
- 系统环境（`GlobalEnvironment`）每小时或者特定高峰时段下发一次动态电价 `price(t)`。高峰期电价可能飙升至平谷的 3-5倍。
- 同时下发削峰事件信号 `dr_event_active = True`。

**Agent 计算逻辑伪代码**：
```python
# 1. 基础计费模块（动态电价直接传导至终端）
baseline_cost = electricity_usage(t) * price(t)

# 2. 定向低收入保护网验证 (CARE/FERA项目机制)
if self.income_group == "Low":
    # 只要符合条件，自动享受全额电费 30% 到 35% 的刚性价格折扣
    final_cost = baseline_cost * (1 - 0.3) 
else:
    final_cost = baseline_cost

# 3. 需求响应重奖模块 (DR Incentive 返现机制)
if dr_event_active:
    # 决定能让出的空负荷，受设备极限与价格弹性的制约
    shifted_kwh = min(self.base_load * self.price_elasticity * price(t), 
                      self.max_shiftable_ratio * self.base_load)
    
    # 直接计算退费补偿。California DR 模式常用倒贴返利法
    dr_reward = shifted_kwh * REWARD_RATE_PER_KWH
    final_cost -= dr_reward
```
**ABM 测试目的**：我们要在这个情景下观察，缺乏设备的 **Low/Renter/LowTech** 家庭，即使拿到 30% 保护折扣，是否依然因为无法躲避晚间极致的动态高电价而遭受实质破产？具有光伏电池的 **High/Owner/HighTech** 是否无脑狂吃 `dr_reward`，导致系统发生了严重的“劫贫济富”（财富逆向再分配）倒错？通过 ABM 获取该政策下的系统 **Gini（基尼）系数变化**。

---

### P6：中国“社区虚拟电厂(VPP)聚集”原型 (Shanghai VPP Prototype)

**环境触发机制**：
- 电力系统不再向个体直接下放令人生畏的动态电价波动，而是发送一个总控信号给 `CommunityAggregatorAgent`（社区平台/物业集成智能体）。

**Agent/Aggregator 计算逻辑伪代码**：
```python
# 1. 基于居委会/邻里的信任接管授权
pool_shift_capacity = 0
for household in community_households:
    # VPP带有“社区和公信力平台背书”，能极大降低底层门槛。
    # 甚至不需要理解电价图，只需简单的“您是否允许电网在高峰调低空调半度”。
    if household.trust_threshold > 0.4 and household.tech_level in ["Medium", "High"]: 
        household.enroll_in_vpp()
        pool_shift_capacity += household.max_shiftable_ratio * household.base_load
        
# 2. 宏观削峰与内部平权分红
if pool_shift_capacity >= GRID_TARGET_REDUCTION:
    # 社区统一向电网上报削减量赚走奖金
    vpp_total_revenue = pool_shift_capacity * VPP_REWARD_RATE
    
    # VPP进行内部公平分账或公共电费减免（具有强烈的平抑缓冲作用）
    for household in community_households:
        if household.enrolled:
            household.bill -= (vpp_total_revenue / len(enrolled_households))
```
**ABM 测试目的**：观察将“直接暴露个体的达尔文法则（P2）”降级为“社区缓冲墙打包（P6）”，是否能显著调动 `Medium Tech` 群体的参与热情？虽然单兵削峰极值不如加州方案，是否能在长时间（多 Tick）模拟下，达成最稳健、退群率最低的整体社会效果？

---

### P1：英国“事前兜底深度干预”时序原型 (UK Prototype)

**环境触发机制**：
- 本方案重在**时序性（Sequencing Variables）**模拟。把 8760 个小时分为前期和后期。前 $T_0$ 到 $T_1$ 优先注入“改造资金”；在 $T_1$ 之后，才向这些家庭强行切换真正的“分时电价方案”。

**Agent 计算逻辑伪代码**：
```python
# T0 阶段：能力前置注入 (先武装，后打仗)
if current_tick < POLICY_TIPPING_POINT:
    if self.income_group == "Low" or self.housing_type == "Old_Building":
        # 政府无差别强注资充当缓冲（如 Warm Home Discount发放150英镑）
        self.wallet += 150 
        
        # 强制性设备升级干预
        if random.random() < RETROFIT_ACCEPTANCE_RATE and self.housing_type == "Owner":
            self.tech_level = "Medium" 
            self.max_shiftable_ratio += 0.15 # 如做完外墙保温保热，降低采暖敏感度
            self.retrofit_completed = True
            
# T1 阶段：价格机制接管切换
if current_tick >= POLICY_TIPPING_POINT:
    # 此时全面覆盖双峰谷差甚至动态价
    # 系统考核：在前置阶段未能成功改造的低薪用户，这一步是否会因为惩罚性价格跌落绝境(Energy Poverty)。
    self.bill = calculate_tou_bill(electricity_usage(t))
```
**ABM 测试目的**：ABM 将通过“先注入再收割”的时序流验证**顺序效应假说**：比起硬着陆同推，强行拿重金垫高用户的防御阈值，最终核算下来的系统全周期效益（全生命周期运行成本+电力基建延缓投资效益）是否划算？

---

## 3. ABM 中的组合实验比对参数矩阵 (Scenario Matrix)

当以上 Agent 画像和函数准备就绪，我们就可以定义几大对冲赛道：

1. **机制柔刚度赛道：市场化强力剥削（P2） vs. 平台组织打包缓冲（P6）**
   * 测算系统最大峰荷骤降响应速率 vs. 测试最终留存的公平度底线。
   
2. **干预顺序赛道：赋能导向组（P1） vs. 同步鞭策组**
   * 测试高强度弱势补贴先期投放的投资回报率，观测能效陷阱（破户更破）的避免。
   
3. **混合终极测试：六合一理想政策包（P7） vs. 基线无扰动组（P0）**
   * 测算在将 底层兜底 (CARE) + 设施注入 (UK) + 分时定标 (China) + 自动托管返现 (Aus) 堆叠使用时，这几种要素之间是相辅相成产生几何级削峰，还是发生了严重的制度内耗、造成居民躺平效应（挤出效应）。

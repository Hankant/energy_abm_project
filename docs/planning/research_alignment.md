# 问卷-论文问题-ABM 机制同构校准

## 1. 研究定位

本项目的研究对象不是一般性的居民低碳态度，而是：

> 在极端天气、市场电价波动与政策干预共同作用下，不同异质性家庭如何调整用电行为、形成低碳产品支付意愿 (WTP)，并在社会网络中产生行为扩散。

因此，`survey/electronic_lowcarbon_survey_v10.html` 中的 D/E 模块不应被解释为普通描述性问卷题，而应被解释为 stated preference / survey experiment：它通过个性化账单反馈、极热持续时间和政策组合操纵，测量家庭在特定信息环境中的 WTP 与采用决策。

## 2. WTP 构念边界

当前项目中需要区分两类 WTP：

| 构念 | 含义 | 问卷来源 | ABM 用途 |
| :--- | :--- | :--- | :--- |
| 低碳产品 WTP | 家庭愿意为高能效/低碳产品相对普通产品承担的额外成本 | C0 基线、D/E 情境后购买意愿、可接受回本期 | 低碳产品采用概率、产品替换决策、政策补贴敏感度 |
| 保供/可靠性 WTP | 极端天气供电紧张时，家庭愿意额外支付以避免限电或保障舒适性的金额 | 当前代码 Prompt 中已有，但问卷 v10 尚未直接测量 | 短期用电维持、限电政策响应、舒适性约束 |

论文主线建议以“低碳产品 WTP 与行为转型”为核心，保供/可靠性 WTP 可作为极端天气下的辅助变量。代码中应避免继续用单一 `wtp` 同时承载这两个含义。

## 3. 问卷模块到 Agent 参数的映射

| 问卷模块 | 测量内容 | Agent 参数建议 | 说明 |
| :--- | :--- | :--- | :--- |
| A. 基本信息 | 年龄、性别、教育、地区、人口、收入 | `location`, `income_level`, `education`, `household_size` | 用于构建家庭异质性和群体分层。 |
| B. 家庭能源使用 | 月用电量、月份、空调/冰箱/热水器数量 | `baseline_kwh`, `billing_month`, `ac_count`, `fridge_count`, `heater_count` | 用于校准基础负荷和极热天气额外负荷。 |
| C. 低碳用电偏好 | 节电 vs 产品升级倾向、生活质量偏好 | `lowcarbon_path_preference`, `upgrade_preference` | 用于决定 Agent 更偏向行为节电还是设备替换。 |
| C0. 干预前 WTP 基线 | 初始采用意愿、额外支付意愿、可接受回本期 | `baseline_adoption_intention`, `wtp_lowcarbon_extra_base`, `acceptable_payback_base` | 用于和 D/E 情境后响应比较。 |
| D/E. 极热与政策情境 | 7天/30天极热，四类政策组合下的路径选择、购买意愿、节电意愿 | `heat_duration_response`, `subsidy_sensitivity`, `penalty_sensitivity`, `saving_intensity`, `adoption_probability` | 核心 stated preference 数据，用于估计政策和极端天气对 WTP/采用意愿的影响。 |
| F. 社会影响 | 影响易感性、讨论人数、周围低碳比例 | `social_susceptibility`, `network_exposure`, `social_influence_score` | 用于校准邻居行为对采用概率和 WTP 更新的影响。 |

## 4. Agent 决策输出建议

当前 `agents.py` 主要输出：

```text
total_daily_kwh
wtp_rmb
```

为了对应论文问题，建议扩展为：

```text
total_daily_kwh
saving_intensity
adoption_probability
adopted_product
wtp_lowcarbon_extra
acceptable_payback
reliability_wtp
decision_reasoning
```

其中：

- `saving_intensity` 表示短期节电强度。
- `adoption_probability` 表示在当前天气、电价、政策和邻居行为下采用低碳产品的概率。
- `adopted_product` 表示可能采用的低碳产品类型，如高能效空调、节能冰箱、热泵热水器、分布式光伏。
- `wtp_lowcarbon_extra` 表示为低碳产品额外支付的 WTP。
- `acceptable_payback` 表示可接受回本期。
- `reliability_wtp` 保留当前代码中的保供/避免限电支付意愿，但不与低碳产品 WTP 混用。

## 5. 论文假设到 ABM 机制的对应

| 论文假设方向 | 问卷证据 | ABM 机制 | 仿真输出 |
| :--- | :--- | :--- | :--- |
| H1: 极热持续时间越长，家庭 WTP 与行为调整越强 | D 7天 vs E 30天 | 提高气候压力和记忆重要性 | 平均 WTP、节电强度、采用概率随极热持续时间变化 |
| H2: 补贴政策提高低碳产品采用意愿 | 情境2/4 与情境1/3 对比 | 降低净额外成本，提高采用概率 | 补贴组采用率高于无补贴组 |
| H3: 惩罚政策提高节电意愿，但对产品采用可能存在异质性 | 情境3/4 与情境1/2 对比 | 提高用电成本压力，触发节电或设备替换 | 节电强度、用电量下降、采用率变化 |
| H4: 收入、价格敏感度和基线 WTP 调节政策响应 | A/B/C0 与 D/E 联合分析 | 不同 Agent 具有不同预算约束与阈值 | 群体分层后的 WTP/采用率差异 |
| H5: 社会影响放大低碳采用扩散 | F 模块社会影响指数 | 邻居采用行为提高个体采用概率 | 社交网络开启组比关闭组更快收敛或扩散 |

## 6. 当前推进难点

1. **WTP 命名与构念需要拆分**  
   代码中的 `wtp` 更接近保供 WTP，问卷 v10 更接近低碳产品 WTP。二者需要分别建模。

2. **问卷输出格式需要转成模型输入格式**  
   v10 当前生成 JSON，`run.py` 当前读取 CSV。需要定义 JSON/CSV 清洗脚本，把问卷字段转换成 Agent 初始化字段。

3. **Agent 行为空间需要扩展**  
   目前模型可以解释用电量和保供支付意愿，但还不能充分解释低碳产品采用、补贴响应和回本阈值。

4. **D/E 模块应明确作为信息处理实验**  
   个性化账单和回本计算会产生框架效应和锚定效应。研究设计中应将其定义为 information treatment，而不是中性背景说明。

5. **社会影响指数需要接入扩散规则**  
   F 模块已经能生成社会影响指数，但 ABM 还需要明确它如何改变邻居影响权重、采用概率或 WTP 更新幅度。

## 7. 下一步最小闭环

建议按以下顺序推进：

1. 确认 WTP 主构念：以低碳产品额外支付意愿和可接受回本期为主，保供 WTP 作为辅助变量。
2. 编写问卷 JSON/CSV 清洗脚本，输出 Agent 初始化所需字段。
3. 修改 `agents.py` Prompt 和 Fallback 规则，使 Agent 同时输出用电行为、低碳产品采用行为和两类 WTP。
4. 用 5-10 个样本跑通一次小规模仿真，检查输出是否能对应 H1-H5。
5. 再进入 `batch_run.py` 和 `analysis.py` 的批量实验与图表阶段。

关于“如果问卷已经能测 WTP，为什么还需要 ABM”以及“问卷塑造的 Agent 结果是否可靠”的方法论边界，见 [survey_abm_discussion_summary.md](./survey_abm_discussion_summary.md)。

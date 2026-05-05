# 能源生态系统 ABM - 下一阶段实施计划

当前基于大语言模型的具备分层次理解与带权记忆系统架构已在 `model.py`, `agents.py`, `network.py`, `policy.py` 完成。
为了支撑本研究“模拟不同异质性家庭在极端天气、市场电价波动及政策干预下的用电行为转型及支付意愿 (WTP)”这一主线，下一阶段的发展重心应先从**问卷-论文问题-ABM 机制同构校准**开始，再推进实验流程系统化和量化结果分析可视化。

## 待用户确认 (User Review Required)

> [!NOTE]
> 当前优先级已调整：在批量仿真和图表产出之前，先明确问卷变量如何进入 Agent 参数、Agent 如何输出 WTP/节电/采用决策、仿真结果如何对应论文假设。否则容易出现“问卷收集了情境实验数据，但模型仍只输出每日用电量和保供 WTP”的错位。

## 已完成的架构 (Completed Architecture)

> [!TIP]
> ~项目的微观推演架构已跑通，包含：多维度户主特征采样、双层 LLM Prompt（基础个性化+单日环境）、带重要性打分检索的记忆系统，以及基于 NetworkX 的小世界拓扑社交模块。并且已经打通了 `run.py` 从问卷加载到 CSV 导出的完整闭环。~

---

## 拟推进功能与代码变更计划

### 1. 问卷-论文-ABM 同构校准

先建立从 `electronic_lowcarbon_survey_v10.html` 到 Agent 初始化参数、决策输出和论文假设的映射表。

#### [NEW] [docs/planning/research_alignment.md](file:///c:/Users/69596/.gemini/antigravity/scratch/energy_abm_project/docs/planning/research_alignment.md)
明确以下内容：
- 研究主问题：极端天气、电价波动和政策干预如何影响异质性家庭的用电行为转型与 WTP。
- WTP 构念边界：区分“低碳产品额外支付意愿”和“保供/避免限电支付意愿”，避免混用。
- 问卷模块映射：A/B/C/C0/D/E/F 分别映射到家庭异质性、基线偏好、情境响应、社会影响指数。
- Agent 输出扩展：从单一 `WTP` 扩展为 `wtp_lowcarbon_extra`、`acceptable_payback`、`saving_intensity`、`adoption_probability`、`reliability_wtp` 等。
- 论文假设路径：O1 异质性、O2 极端天气响应、O3 政策组合敏感度、O4 社会规范扩散。

#### [MODIFY] [agents.py](file:///c:/Users/69596/.gemini/antigravity/scratch/energy_abm_project/agents.py)
- 将当前 `wtp` 字段拆分或命名澄清，避免把“保供 WTP”和“低碳产品 WTP”混为同一变量。
- Persona 层增加问卷校准参数：基线额外支付意愿、可接受回本期、补贴敏感度、惩罚敏感度、社会影响易感性。
- Daily Context 层增加低碳产品采用决策输出，而不仅是日用电量和保供 WTP。

### 2. 实验自动化执行框架

在同构校准完成后，为解决 `run.py` 只能进行单次手动仿真的局限性，引入批量推演脚本。

#### [NEW] [batch_run.py](file:///c:/Users/69596/.gemini/antigravity/scratch/energy_abm_project/batch_run.py)
实现一套循环执行脚本自动化生成不同干预对照组数据的逻辑，涵盖以下典型场景：
- **场景A (Baseline，基线组)**：无重大政策冲击，不开启社交网络。
- **场景B (Social Influence，网络效应组)**：无重大政策冲击，开启小世界社交网络。
- **场景C (Policy Intervention，政策干预组)**：开启强干预（如高额碳税及限电警告）+ 开启社交网络。

### 3. 数据可视化与图表绘制

使用输出的 `results/*.csv` 作为入参，面向学术报告需要进行多层次展示和绘图分析。

#### [NEW] [analysis.py](file:///c:/Users/69596/.gemini/antigravity/scratch/energy_abm_project/analysis.py)
运用 `matplotlib` / `seaborn` / `plotly` 库，设计图表：
- **宏观时间序列**：整体用电负荷与平均 WTP 对各种异动天气的时序响应曲线图。
- **微观群像分形**：箱线图 / Violin 提琴图，从家庭收入（高/中/低）、房屋所在地（长三角/大湾区）剖析消费者的不同弹性表现。
- **传播效应观测**：绘制图谱反映社会网络效应（有/无）情况下的行为收敛过程差异。

### 4. 系统推演并发性能优化 (可选功能)

由于现有的 LLM 为同步串行调用，面对大规模 Agent 时，实验时长会急剧膨胀。

#### [MODIFY] [agents.py](file:///c:/Users/69596/.gemini/antigravity/scratch/energy_abm_project/agents.py)
- 重构调用方法：由现存的 `requests.post()` 升级为异步协程 `aiohttp`。
- 使所有的 `HouseholdAgent` 在 `step()` 时并发触发问询，最终由 `Model` 以 `asyncio.gather` 进行同步数据采集。

## 验证计划清单

### 自动化 / 代码运行预期
- 检查问卷 JSON/CSV 字段能否完整映射到 Agent 初始化参数，尤其是基线 WTP、情境后采用意愿、社会影响指数。
- 用极小样本执行一次模型，确认输出同时包含用电行为、低碳产品采用行为和不同类型 WTP。
- 用极小样本（例如：N=5 Agent）执行 `python batch_run.py`，验证流程是否能够闭环、并且为每种不同条件自动输出不同的场景路径 CSV 结果文件组合。
- 测试 `python analysis.py` 脚本能自动读入对应的 CSV 并稳定保存输出为图表文件（.png/.pdf）。

### 人工复查逻辑验证
- 核对绘图渲染输出的 X、Y 轴标签及图例说明。
- 复盘场景组 A 和情况 B 之间的逻辑收敛现象是否如理论设计的预期。

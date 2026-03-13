# 能源生态系统 ABM - 下一阶段实施计划

当前基于大语言模型的具备分层次理解与带权记忆系统架构已在 `model.py`, `agents.py`, `network.py`, `policy.py` 完成。
为了支撑本研究的目标（例如：**O1-异质性决策分化验证；O2-社会规范扩散影响；O3-政策长效敏感度**），下一阶段的发展重心是**实验流程系统化**和**量化结果分析可视化**。

## 待用户确认 (User Review Required)

> [!NOTE]
> 请注意，该计划主要针对论文所需的**图表支撑**与**实验分组对比**构建模块。 如果您现阶段对核心 Agent Prompt 或其他环境机制有进一步修改意向，我们可以灵活推迟可视化模块的开发优先级。确认无误后，我们将继续推进代码实现。

## 已完成的架构 (Completed Architecture)

> [!TIP]
> ~项目的微观推演架构已跑通，包含：多维度户主特征采样、双层 LLM Prompt（基础个性化+单日环境）、带重要性打分检索的记忆系统，以及基于 NetworkX 的小世界拓扑社交模块。并且已经打通了 `run.py` 从问卷加载到 CSV 导出的完整闭环。~

---

## 拟推进功能与代码变更计划

### 1. 实验自动化执行框架

为解决 `run.py` 只能进行单次手动仿真的局限性，引入批量推演脚本。

#### [NEW] [batch_run.py](file:///c:/Users/69596/.gemini/antigravity/scratch/energy_abm_project/batch_run.py)
实现一套循环执行脚本自动化生成不同干预对照组数据的逻辑，涵盖以下典型场景：
- **场景A (Baseline，基线组)**：无重大政策冲击，不开启社交网络。
- **场景B (Social Influence，网络效应组)**：无重大政策冲击，开启小世界社交网络。
- **场景C (Policy Intervention，政策干预组)**：开启强干预（如高额碳税及限电警告）+ 开启社交网络。

### 2. 数据可视化与图表绘制

使用输出的 `results/*.csv` 作为入参，面向学术报告需要进行多层次展示和绘图分析。

#### [NEW] [analysis.py](file:///c:/Users/69596/.gemini/antigravity/scratch/energy_abm_project/analysis.py)
运用 `matplotlib` / `seaborn` / `plotly` 库，设计图表：
- **宏观时间序列**：整体用电负荷与平均 WTP 对各种异动天气的时序响应曲线图。
- **微观群像分形**：箱线图 / Violin 提琴图，从家庭收入（高/中/低）、房屋所在地（长三角/大湾区）剖析消费者的不同弹性表现。
- **传播效应观测**：绘制图谱反映社会网络效应（有/无）情况下的行为收敛过程差异。

### 3. 系统推演并发性能优化 (可选功能)

由于现有的 LLM 为同步串行调用，面对大规模 Agent 时，实验时长会急剧膨胀。

#### [MODIFY] [agents.py](file:///c:/Users/69596/.gemini/antigravity/scratch/energy_abm_project/agents.py)
- 重构调用方法：由现存的 `requests.post()` 升级为异步协程 `aiohttp`。
- 使所有的 `HouseholdAgent` 在 `step()` 时并发触发问询，最终由 `Model` 以 `asyncio.gather` 进行同步数据采集。

## 验证计划清单

### 自动化 / 代码运行预期
- 用极小样本（例如：N=5 Agent）执行 `python batch_run.py`，验证流程是否能够闭环、并且为每种不同条件自动输出不同的场景路径 CSV 结果文件组合。
- 测试 `python analysis.py` 脚本能自动读入对应的 CSV 并稳定保存输出为图表文件（.png/.pdf）。

### 人工复查逻辑验证
- 核对绘图渲染输出的 X、Y 轴标签及图例说明。
- 复盘场景组 A 和情况 B 之间的逻辑收敛现象是否如理论设计的预期。

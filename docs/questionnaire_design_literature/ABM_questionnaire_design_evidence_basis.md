# 家庭能源政策组合ABM问卷：参考原型与设计依据

## 1. 文件目的

本文件为 `energy_abm_project` 的问卷设计提供可核验的方法依据，主要回答两个问题：

1. 哪些公开问卷、量表和调查材料可以作为题项设计参考；
2. 面向经验校准型Agent-Based Model（ABM）的问卷必须识别什么，以及应遵守哪些设计原则。

需要特别说明：目前没有发现一份能够直接覆盖“家庭属性—心理机制—政策组合评价—政策支持—参与/遵从—家庭行为—ABM参数”的权威整卷。因此，本项目采用“权威模块组合”的方式：客观家庭模块、行为模块和心理模块优先借鉴公开调查或量表；政策组合公众感知题项和政策情景实验则依据理论自行开发，并通过认知访谈、预测试和统计验证建立效度。

本文归纳的ABM问卷原则是对多篇经验型ABM方法文献的综合，不代表某一篇论文已经提出了一套现成的“ABM问卷标准”。

## 2. 可参考的问卷和题项原型

### 2.1 第一层：公开程度较高、可直接查看题项的材料

| 材料 | 权威性与公开情况 | 可借鉴内容 | 在本项目中的用途 | 使用限制 |
|---|---|---|---|---|
| Kaiser（2020）GEB-50 | 公开的环境行为量表；本地已保存英文问卷；CC BY-SA 4.0 | 节能、消费、社会参与等具体行为题；行为频率和难度差异 | 构造HAB题项池，并选择少量与EIB、IFB有关的行为题 | 是一般生态行为量表，不是中国家庭能源专用量表；改变措辞或计分逻辑时必须明确说明 | 
| OECD（2023）EPIC环境政策与个人行为调查 | OECD跨国官方调查，本地已保存报告及问卷材料 | 住房能源、设备投资、行为、障碍、政策暴露和环境态度 | 家庭行为、节能投资、约束和政策经验模块 | 调查覆盖多个环境领域，正式问卷只能抽取能源相关部分 |
| WHO/World Bank（2019）家庭能源核心问题 | WHO和世界银行官方调查工具；本地已保存精简问卷 | 烹饪、供暖、照明、燃料、技术和能源可及性 | 客观能源系统、燃料叠加和设备模块 | 更偏能源可及性与清洁燃料，不足以测量城市居民的政策态度 |
| EIA（2020）RECS | 美国能源信息署官方居民能源消费调查；本地已保存调查表网页 | 住房、设备、供暖制冷、温控、热水、照明、账单和新能源汽车充电 | 家庭住房、设备、账单及能源服务需求模块 | 美国设备分类和住房情境需要中国化，不能直接照搬 |
| UK DECC（2012）45项家庭节能行为清单 | 英国政府技术报告；本地已保存PDF | 日常使用、舒适度调整和技术升级行为及其潜在节能影响 | 为HAB、QTB、EIB生成具体候选行为清单 | 是技术行为清单，不是心理量表；英国供暖情境较强 |
| Yue等（2019）江苏家庭节能研究 | 中国家庭情境的同行评议开放论文；本地已保存HTML | HAB、QTB、EIB、IFB四类行为及部分具体行为示例；政策与行为结果变量 | 四行为域的中国情境原型和分类依据 | 没有独立、完整的受访者问卷附件，不能称为成熟量表 |
| Liu等（2020）西北地区家庭TPB研究 | 同行评议开放论文；本地已保存PDF | Table 2公开的态度、主观规范、知觉行为控制和行为意愿共16个英文题项 | 中国家庭节能TPB构念和英文题项参考 | 没有公开受访者实际看到的中文原版问卷；只能标记为“依据公开英文题项翻译或改编” |

本地文献索引见 [`index.csv`](index.csv) 和 [`index.json`](index.json)。Liu等（2020）的问卷可获得性核查见 [`Liu_2020_questionnaire_audit.md`](link_records/Liu_2020_questionnaire_audit.md)。

### 2.2 第二层：提供测量结构或设计原则，但完整题项尚未确认公开

| 文献 | 可借鉴内容 | 证据边界 |
|---|---|---|
| Boudet et al.（2015） | 区分当前实际行为、未来意愿、客观上无法实施和不适用 | 完整题项及复用条件仍需核验 |
| Stragier et al.（2012） | 家庭能源效率行为量表的结构与验证方法 | 尚未确认存在可公开复用的完整题项附件 |
| Barr, Gilg, and Ford（2005） | 区分习惯/削减型行为与购买/效率投资行为 | 提供经典分类依据，但不是Yue四行为域的完整问卷 |
| Yue et al.（2016, 2020） | HAB、QTB、EIB、IFB的早期定义及其在ANN/ABM中的应用 | Yue（2020）没有公开完整e1–e11心理变量及映射，不足以复现问卷—参数转换 |
| CRECS | 中国家庭、住房、设备、能源消费和账单的本土调查框架 | 具体版本问卷的公开性及授权条件需要通过正式申请确认 |

### 2.3 不应混淆的三种“参考”

为了防止来源等级被夸大，所有候选题项必须标注为以下类别之一：

1. **原样采用**：原始题项公开、授权允许、构念和使用情境基本一致；
2. **翻译或情境适配**：来源题项公开，但语言、对象、时间窗口或政策情境发生改变；
3. **本研究自行开发**：没有成熟公众量表，依据理论定义自行形成题项。

Policy mix的consistency、coherence、credibility和comprehensiveness目前应归入第三类。Rogge与Reichardt的框架能够提供理论定义，但不能被描述成已经验证过的居民问卷量表。

## 3. 支撑ABM问卷设计的方法文献

### 3.1 经验数据与Agent行为的连接

Janssen和Ostrom（2006）指出，经验型ABM可以综合调查、案例研究、实验、参与式方法和现实统计数据，不应仅凭研究者直觉设定Agent行为。该文的意义在于确立“多来源经验约束”的原则，而不是要求一份问卷独自识别所有模型机制。

Smajgl et al.（2011）进一步系统讨论了人类行为的经验刻画与参数化，并区分Agent characterization、behaviour characterization和parameterization。对本项目而言，这意味着必须先说明家庭类型和决策机制，再决定怎样把问卷变量转成Agent参数；不能把每一道题机械地当成一个模型参数。

Bruch和Atwell（2015）讨论了将调查数据、人口数据、离散选择模型和统计估计用于经验社会ABM的方法。特别是，当ABM需要模拟选择行为时，可以用revealed preference或针对假设情景的stated preference数据估计选择模型，再将估计结果嵌入Agent规则。

### 3.2 行为理论必须显式化

Schlüter et al.（2017）提出MoHuB框架，要求行为模型明确说明Agent感知什么、评价什么、如何选择、如何学习，以及社会和环境因素怎样影响决策。这为问卷提供了一个直接检查框架：心理题不能只是一般态度清单，而应对应决策过程中的感知、评价、选择或更新机制。

### 3.3 模型记录、校准与验证

Grimm et al.（2020）的ODD协议要求ABM完整说明模型目的、实体与状态变量、过程与调度、设计概念、初始化、输入数据和子模型。问卷—Agent映射应成为ODD中“初始化、输入数据和子模型”的可追溯证据。

Windrum, Fagiolo, and Moneta（2007）指出，经验验证对象可能是微观或宏观、定量或定性、过渡过程或长期结果；验证目标不同，所需数据和统计方法也不同。因此，问卷设计之前必须先规定模型声称预测什么。

Grimm et al.（2005）的pattern-oriented modeling主张用多个相对独立的现实模式约束复杂ABM，而不是仅拟合一个总量。对应到本项目，模型不应只拟合“平均节能意愿”，还应同时检验家庭类型分布、不同政策下的参与率、各类行为发生率、群体差异和宏观能源结果。

## 4. 本项目应坚守的ABM问卷设计核心点

### 原则一：从模型目的和行为规则反推问题，不从现成量表堆砌整卷

每一道题必须至少对应以下对象之一：

- Agent初始化属性；
- Agent当前状态；
- 感知、信念或偏好；
- 行为机会和客观约束；
- 决策规则中的解释变量；
- 学习或状态更新机制；
- 独立的模型验证指标。

如果一个题项无法说明其模型用途，就不应仅因“与节能有关”而进入正式问卷。

### 原则二：严格区分变量角色

问卷数据进入模型前必须分类为：

| 变量角色 | 含义 | 示例 |
|---|---|---|
| 描述变量 | 刻画家庭和环境，不直接代表心理机制 | 收入、家庭规模、住房面积、产权、设备 |
| 潜变量测量指标 | 多题共同测量不可直接观察的构念 | 态度、规范、控制感、可信度、公平感 |
| 处理变量 | 由研究设计随机改变 | 补贴水平、价格信号、强制程度、信息方式、工具组合 |
| 结果变量 | 比较政策情景产生的响应 | 支持、参与/遵从、投资选择、预计行为变化 |
| 模型状态变量 | 可在模拟过程中更新 | 信念、可支配预算、设备存量、经验、行为习惯 |

政策支持、参与/遵从意愿和实际行为必须分别测量，不能共同称为“节能意愿”。

### 原则三：多个题项先形成测量构念，再进入Agent规则

推荐的映射链为：

```text
来源题项 → 翻译/适配 → 测量模型 → 潜变量或类型 → Agent参数 → 行为规则
```

态度、公平、可信度等构念应先经过认知访谈、预测试、信度分析以及EFA/CFA或适当的潜变量模型，再转成少量Agent参数。除直接事实题外，不采用“一题一参数”。

### 原则四：同时识别家庭异质性和行为机制

客观人口、住房和设备变量只能回答“家庭有什么条件”，不能解释“家庭为什么响应政策”。问卷至少需要同时覆盖：

- 家庭资源、住房、设备和能源服务需求；
- 既有行为及其频率；
- 态度、规范、控制感及必要扩展心理变量；
- 政策经验、有效性感知、公平、负担与可信度；
- 随机政策情景下的支持、参与和行为响应；
- 社会互动、信息接触或结果反馈对后续决策的影响。

### 原则五：把行为机会和客观约束写进问卷

家庭拥有不同的可行行为集合。租户可能无权进行住房改造，无车家庭不适用新能源汽车问题，资金不足也不同于不支持政策。具体行为题应尽可能区分：

- 已经实施；
- 有条件但没有实施；
- 未来愿意实施；
- 因产权、资金、设备或住房条件无法实施；
- 对本家庭不适用。

否则ABM会把结构性约束错误地解释成偏好或态度差异。

### 原则六：保留家庭属性之间的联合异质性

收入、产权、住房类型、设备、家庭规模、年龄、政策态度和行为能力通常彼此相关。Agent初始化时不能从每一个变量的边际分布独立抽样。优先考虑：

- 从匿名问卷微观记录重抽样；
- 潜类别、聚类或原型家庭；
- 联合概率模型或合成总体方法。

因此，问卷数据结构必须能够恢复变量间相关性，并保留抽样权重、地区和关键分层信息。

### 原则七：政策情景必须提供可识别的反事实比较

一般态度题不能识别某个政策工具或属性的边际效应。政策组合模块应采用factorial vignette、conjoint或stated-choice思路，并满足：

- 随机分配政策属性和水平；
- 设置清晰的基准或可比较方案；
- 属性和水平具有现实政策及policy mix理论依据；
- 各情景使用一致的核心结果题；
- 保存随机分配概率、版本、题序和呈现顺序；
- 每位受访者只回答有限数量情景，控制疲劳和学习效应。

### 原则八：动态模型必须明确状态如何变化

横截面问卷主要识别初始分布和条件性响应，不能自动识别长期学习速度、习惯形成或社会扩散。若ABM包含动态机制，问卷应尽可能测量：

- 信息来源及其影响强度；
- 对邻居、亲友和社会多数行为的敏感程度；
- 行为结果如何影响下一期评价与选择；
- 既有设备投资和习惯形成的路径依赖；
- 政策持续时间和采取行动的时点。

无法由问卷识别的更新规则必须标记为理论假设、文献参数或待校准参数，并进入敏感性分析。

### 原则九：校准数据和验证数据必须分开

建议第一轮调查用于构念识别、家庭分类、参数估计和Agent初始化；第二轮重复横截面、留出情景或其他外部数据用于群体分布更新、外部校准和预测验证。不得使用同一批数据同时证明模型拟合能力和预测能力。

对传统统计/ABM、聚类Agent和LLM-Agent的比较，应使用相同训练信息、相同留出情景和相同评价指标。LLM只有在未调查政策组合、复杂文本、多阶段决策、社会互动或路径依赖的预测上表现出稳定增量价值时，才作为扩展模型。

### 原则十：使用多个微观和宏观模式验证模型

模型至少应尝试同时再现：

- 家庭客观属性和Agent类型的联合分布；
- 不同家庭类型的基线行为率；
- 随政策属性变化的支持与参与率；
- HAB、QTB、EIB、IFB的差异响应；
- 公平、收入或住房群体之间的分配效应；
- 总体能源、排放或政策参与结果；
- 若有数据，第二轮调查中的群体分布或政策响应。

只拟合平均意愿或单一总体结果不足以证明行为机制可靠。

### 原则十一：完整公开映射、估计过程和不确定性

正式成果应公开以下链条：

```text
题项来源与原文
→ 中文翻译与修改理由
→ 构念、量尺和编码
→ 测量模型与计分
→ 家庭类型或参数分布
→ Agent决策方程
→ 状态更新规则
→ 模型输出
→ 校准与验证指标
```

同时报告抽样误差、测量误差、参数区间、不可识别参数、情景不确定性和敏感性分析。模型本身按ODD协议记录。

## 5. 问卷的最低识别模块

| 最低必需模块 | 主要内容 | 进入ABM的方式 |
|---|---|---|
| A. 筛选与决策角色 | 知情同意、地区、年龄、家庭能源决策参与程度 | 样本资格、回答可靠性和决策权重 |
| B. 家庭与客观约束 | 人口、收入、住房、产权、设备、能源账单、舒适需求 | Agent初始化、预算和行为可行集 |
| C. 既有能源行为 | HAB、QTB、EIB、IFB及不适用/无法实施原因 | 基线行为状态、类型识别和行为概率 |
| D. 心理与社会机制 | 态度、命令性规范、描述性规范、知觉行为控制、道德规范、初始意愿 | 潜变量、Agent类型和决策参数 |
| E. 制度与公平背景 | 政府信任、政策经验、程序公平观和分配偏好 | 初始信念、评价异质性和控制变量 |
| F. 随机政策组合情景 | 具有理论与现实依据的政策工具属性和水平 | 外生处理变量、反事实政策输入 |
| G. 情景后响应 | 有效性、分配公平、负担、可信度、支持、参与、预计行为变化 | 政策评价、决策输出和条件行为规则 |
| H. 数据质量 | 注意力检验、答题时长、开放意见 | 样本质量控制和机制补充解释 |

## 6. 问卷设计的准入检查

一个题项进入正式问卷前，应当全部回答以下问题：

1. 它测量的是事实、潜变量、处理、结果还是模型状态？
2. 理论定义和题项原文来自哪里？
3. 它是原样采用、翻译/情境适配，还是自行开发？
4. 受访者回答时对应的对象、行为和时间窗口是否明确？
5. 如何计分或估计，是否需要多题形成潜变量？
6. 它进入哪个Agent属性、参数、决策规则或验证指标？
7. 第一轮用于估计，还是第二轮/留出情景用于验证？
8. 如果删除这道题，会损失哪一项模型识别能力？

无法回答第6或第8项的题目，原则上不进入正式问卷。

## 7. 参考文献与公开链接

- Barr, S., Gilg, A. W., & Ford, N. (2005). The household energy gap: Examining the divide between habitual- and purchase-related conservation behaviours. *Energy Policy, 33*(11), 1425–1444. https://doi.org/10.1016/j.enpol.2003.12.016
- Boudet, H. S., Flora, J. A., & Armel, K. C. (2015). Measuring household energy efficiency behaviors with attention to behavioral plasticity in the United States. *Energy Research & Social Science, 10*, 133–140. https://doi.org/10.1016/j.erss.2015.07.014
- Bruch, E., & Atwell, J. (2015). Agent-based models in empirical social research. *Sociological Methods & Research, 44*(2), 186–221. https://pmc.ncbi.nlm.nih.gov/articles/PMC4430112/
- Grimm, V., et al. (2005). Pattern-oriented modeling of agent-based complex systems: Lessons from ecology. *Science, 310*(5750), 987–991. https://doi.org/10.1126/science.1116681
- Grimm, V., et al. (2020). The ODD protocol for describing agent-based and other simulation models: A second update to improve clarity, replication, and structural realism. *Journal of Artificial Societies and Social Simulation, 23*(2), 7. https://doi.org/10.18564/jasss.4259
- Janssen, M. A., & Ostrom, E. (2006). Empirically based, agent-based models. *Ecology and Society, 11*(2), 37. https://www.ecologyandsociety.org/vol11/iss2/art37/
- Kaiser, F. G. (2020). GEB-50: General Ecological Behavior Scale—English questionnaire. PsychArchives. https://doi.org/10.23668/psycharchives.4489
- Liu, X., Wang, Q., Wei, H.-H., Chi, H.-L., Ma, Y., & Jian, I. Y. (2020). Psychological and demographic factors affecting household energy-saving intentions: A TPB-based study in Northwest China. *Sustainability, 12*(3), 836. https://doi.org/10.3390/su12030836
- OECD. (2023). *How green is household behaviour? Sustainable choices in a time of interlocking crises*. OECD Publishing. https://doi.org/10.1787/2bbbb663-en
- Schlüter, M., et al. (2017). A framework for mapping and comparing behavioural theories in models of social-ecological systems. *Ecological Economics, 131*, 21–35. https://doi.org/10.1016/j.ecolecon.2016.08.008
- Smajgl, A., Brown, D. G., Valbuena, D., & Huigen, M. G. A. (2011). Empirical characterisation of agent behaviours in socio-ecological systems. *Environmental Modelling & Software, 26*(7), 837–844. https://doi.org/10.1016/j.envsoft.2011.02.011
- Stragier, J., Hauttekeete, L., De Marez, L., & Brondeel, R. (2012). Measuring energy-efficient behavior in households: The development of a standardized scale. *Ecopsychology, 4*(1), 64–71. https://doi.org/10.1089/eco.2012.0026
- UK Department of Energy and Climate Change. (2012). *How much energy could be saved by making small changes to everyday household behaviours?* https://www.gov.uk/government/publications/how-much-energy-could-be-saved-by-making-small-changes-to-everyday-household-behaviours
- U.S. Energy Information Administration. (2020). *Residential Energy Consumption Survey: Microdata and survey forms*. https://www.eia.gov/consumption/residential/data/2020/index.php?view=microdata
- Windrum, P., Fagiolo, G., & Moneta, A. (2007). Empirical validation of agent-based models: Alternatives and prospects. *Journal of Artificial Societies and Social Simulation, 10*(2), 8. https://www.jasss.org/10/2/8.html
- World Health Organization & World Bank. (2019). *Harmonized survey questions for monitoring household energy use and SDG indicators 7.1.1 and 7.1.2*. https://www.who.int/tools/core-questions-for-household-energy-use
- Yue, T., Long, R., Chen, H., & Zhao, X. (2019). Empirical study on households' energy-conservation behavior of Jiangsu Province in China: The role of policies and behavior results. *International Journal of Environmental Research and Public Health, 16*(6), 939. https://doi.org/10.3390/ijerph16060939
- Yue, T., Long, R., Chen, H., Liu, J., Liu, H., & Gu, Y. (2020). Energy-saving behavior of urban residents in China: A multi-agent simulation. *Journal of Cleaner Production, 252*, 119623. https://doi.org/10.1016/j.jclepro.2019.119623

## 8. 当前证据边界

1. 现有材料足以支撑问卷的模块结构和ABM识别原则，但不足以证明存在一份可直接照搬的权威整卷。
2. HAB、QTB、EIB、IFB可作为行为域分类框架，尚不能作为已经验证的四维量表直接宣称使用。
3. Liu等（2020）可支持TPB构念选择和英文题项参考，但不能证明本项目获得了其中文原版问卷。
4. Policy mix公众感知题项属于本项目的重要方法创新，必须清楚标注为理论驱动的自行开发题项，并经过完整的认知和统计验证。
5. 两轮重复横截面不能被解释为个体面板；第二轮主要承担群体分布更新、外部校准和留出预测验证。

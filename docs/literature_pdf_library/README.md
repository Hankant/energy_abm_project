# Literature PDF Library

本目录用于保存项目引用文献的 PDF 原文，并登记已核验但暂未取得全文的文献。文件采用“第一作者等_年份_期刊_卷页或文章编号”的稳定命名方式。新增文件时应登记 DOI、来源、获取状态和 SHA-256；没有合法可直接下载的全文时，不以摘要页冒充 PDF。

| 文件／状态 | 文献信息 | DOI | 来源与获取状态 | SHA-256 |
|---|---|---|---|---|
| `Nieddu_et_al_2024_Energy_Policy_114276.pdf` | Nieddu, M., Raberto, M., Ponta, L., Teglio, A., & Cincotti, S. (2024). *Evaluating policy mix strategies for the energy transition using an agent-based macroeconomic model*. Energy Policy, 193, 114276. | `10.1016/j.enpol.2024.114276` | 用户提供的原文 PDF；[出版商页面](https://www.sciencedirect.com/science/article/pii/S0301421524002969) | `A587BB69BACB4FB30B473C89BEFFA79C3080FE7111F5F0FE60A5244694273F22` |
| `An in-depth analysis of the evolution of the policy mix for the sustainable energy transition in China from 1981 to 2020.pdf` | Li, L., & Taeihagh, A. (2020). *An in-depth analysis of the evolution of the policy mix for the sustainable energy transition in China from 1981 to 2020*. Applied Energy, 263, 114611. | `10.1016/j.apenergy.2020.114611` | 用户提供的原文 PDF；[出版商页面](https://www.sciencedirect.com/science/article/pii/S0306261920301239) | `908AEB0F45EC3678415C4D422091772CDC5D10F754A4956D21A6203BDCC11DE3` |
| `Yue_et_al_2020_Journal_of_Cleaner_Production_252_119623.pdf` | Yue, T., Long, R., Chen, H., Liu, J., Liu, H., & Gu, Y. (2020). *Energy-saving behavior of urban residents in China: A multi-agent simulation*. Journal of Cleaner Production, 252, 119623. | `10.1016/j.jclepro.2019.119623` | 用户提供的原文 PDF；[出版商页面](https://www.sciencedirect.com/science/article/pii/S0959652619344932) | `F36BDAD43D5D827C5EB52540D931A5D59B09010A5C33E3EDFB143459FF217230` |
| 全文待获取 | Tian, S., & Chang, S. (2020). *An agent-based model of household energy consumption*. Journal of Cleaner Production, 242, 118378. | `10.1016/j.jclepro.2019.118378` | [出版商页面](https://www.sciencedirect.com/science/article/pii/S0959652619332482)；已核验元数据，出版商标示需机构访问或购买 | — |
| 全文待获取 | Liang, X., Yu, T., Hong, J., & Shen, G. Q. (2019). *Making incentive policies more effective: An agent-based model for energy-efficiency retrofit in China*. Energy Policy, 126, 177–189. | `10.1016/j.enpol.2018.11.029` | [香港理工大学研究门户](https://research.polyu.edu.hk/en/publications/making-incentive-policies-more-effective-an-agent-based-model-for/)；已核验同行评审、卷期页码与 DOI，当前未发现可合法直接下载的开放全文 | — |
| `Khanna_et_al_2016_Energy_Policy_95_113-125.pdf` | Khanna, N. Z., Guo, J., & Zheng, X. (2016). *Effects of demand side management on Chinese household electricity consumption: Empirical findings from Chinese household survey*. Energy Policy, 95, 113–125. | `10.1016/j.enpol.2016.04.049` | [Lawrence Berkeley National Laboratory 开放稿件](https://eta-publications.lbl.gov/sites/default/files/lbnl-1005836.pdf)；LBNL-1005836 | `33DC79F08806328B5AE120D868438E893F3E4B7B85FB41E9691F228CAEF9F5A6` |
| 全文待获取 | Liu, J., Wilson, C., Zhang, Y., & Zhuge, C. (2026). *Dynamic micro-simulation of domestic electricity consumption: A case of Beijing*. Computational Urban Science, 6, Article 42. | `10.1007/s43762-026-00277-2` | [Springer 开放获取页面](https://link.springer.com/article/10.1007/s43762-026-00277-2)；全文为开放获取，但自动下载触发站点验证，未保存无效文件 | — |

## 与本项目的用途

- Yue 等（2020）：用 ABM、人工神经网络和 NetLogo 模拟中国城市居民节能意向、行为及政策情境。
- Tian 与 Chang（2020）：表示家庭、设备、收入、技术与地方补贴等异质性，用于清洁能源替代情境分析。
- Liang 等（2019）：模拟政府与建筑业主的节能改造决策，并比较激励政策情境。
- Khanna 等（2016）：基于中国 27 个省份 1,450 户调查数据评估阶梯电价、能效标签与信息反馈，可作为 DSM 参数校准的微观证据；该研究不是 ABM。
- Liu 等（2026）：以北京为例，将问卷支持的经验用电模型嵌入 SelfSim 城市微观模拟，联动合成人口、土地利用与家庭属性。论文正文将其描述为回归型用电模型；未将随机森林列为核心初始化方法。

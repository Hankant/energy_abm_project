# LLM-Powered Energy Transition ABM 
### 大语言模型驱动的能源转型代理仿真系统

本项目旨在通过结合 **宏观能源系统大模型 (EBM)** 与 **微观个体代理模型 (ABM)**，模拟不同异质性家庭在极端天气、市场电价波动及政策干预下的用电行为转型及支付意愿 (WTP)。

---

## 🌟 核心特性

- **LLM 决策大脑**：每个 Agent 均由大语言模型驱动，具备独立思考、逻辑归因及 Fallback 规则树机制。
- **带权记忆系统**：参考 *Generative Agents*，实现重要性评分（气温极端性、电价偏差、政策强度）与加权记忆检索。
- **社交网络拓扑**：内置 Watts-Strogatz 小世界网络，模拟社会规范（邻里压力）对个体行为的扩散效应。
- **动态政策剧本**：支持碳税、补贴、错峰限电及新闻舆论等多种宏观干预方案的灵活配置。

---

## 🏗️ 系统架构

项目的详细架构逻辑已在 [visual_logic_guide.md](./visual_logic_guide.md) 中完整拆解。

- `run.py`: 全局调度中心，管理实验流程与 IO。
- `model.py`: 宏观环境引擎（Mesa 框架），负责时序演化。
- `agents.py`: 微观 Agent 实现，包含 LLM 提示词工程与记忆算法。
- `network.py`: 社区连接拓扑实现。
- `policy.py`: 政策信号定义。

---

## 🚀 快速开始

### 1. 环境准备
确保已安装 Python 3.9+，并安装必要依赖：
```bash
pip install mesa pandas networkx requests
```

### 2. 配置 API Key
在 `agents.py` 中配置您的 LLM API 端点及秘钥（本项目默认支持基于 OpenAI 格式的 API 适配器）。

### 3. 运行仿真
```bash
python run.py
```
仿真结束后，结果将自动生成在 `results/` 目录下，包含宏观统计 `macro_result_*.csv` 和微观轨迹 `micro_result_*.csv`。

---

## 📊 研究目标映射 (Research Objectives)

| 目标 | 实现模块 | 核心点 |
| :--- | :--- | :--- |
| **异质性验证** | `agents.py` | 地区/收入/环保意识的多维异质性 Prompt。 |
| **社会规范效应** | `network.py` | 小世界网络下的邻里行为感知。 |
| **政策敏感度** | `policy.py` & 记忆系统 | 政策重要性评分对长期决策的引导。 |

---

## 📝 许可证
MIT License

## ✉️ 联系方式
如有研究合作意向，请联系项目维护者。

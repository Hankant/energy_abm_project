"""
模块名称：社区网络拓扑模块 (Community Network Topology Module)
核心作用：构建家庭 Agent 之间的社会影响网络，模拟邻里信息传播与"绿色行为扩散"效应。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
【网络拓扑构建原理 — Watts-Strogatz 小世界网络】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

本模型采用 Watts-Strogatz（WS）小世界网络（Watts & Strogatz, 1998, Nature）作为
社区人际关系的拓扑结构，原因如下：

1. 【现实契合度】
   真实社区中，居民的社会关系兼具两个特性：
   (a) 高聚类性（Local Clustering）：同一楼栋/社区的邻居彼此相识，形成密集局部圈；
   (b) 短路径性（Short Average Path）：通过朋友的朋友，信息可以在整个社区快速传播
       （"六度分隔"现象）。
   WS 网络通过"规则环图 + 随机重连"恰好同时满足上述两点。

2. 【参数说明】
   - n    : 节点数量（= Agent 数量）
   - k    : 每个节点在规则环图中的初始邻居数（代表一个家庭直接认识的平均邻居数，
             通常设为 4~6，即同层楼的左右两户 + 楼上楼下）
   - p    : 随机重连概率（0=纯规则环，1=完全随机图；建议 0.1~0.3，模拟偶尔的
             跨社区联系，如微信群、亲戚往来等）

3. 【影响机制】
   - 每个 Agent 在做决策前，可以查询其网络邻居"昨天"的用电量与 WTP 信息；
   - 这些邻居信息将以自然语言形式注入 LLM Prompt，形成"社会规范压力"或
     "从众/逆反效应"，模拟绿色行为扩散与信息茧房等社会现象。

4. 【对照实验开关】
   在 run.py 中将 ENABLE_SOCIAL_NETWORK 设置为 True/False，可以对比有无社会网络
   影响时的宏观用电结果差异，作为因果推断的对照组。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

参考文献：
  Watts, D. J., & Strogatz, S. H. (1998). Collective dynamics of 'small-world' networks.
  Nature, 393(6684), 440–442. https://doi.org/10.1038/30918
"""

import networkx as nx


def build_community_network(
    agent_ids: list,
    k: int = 4,
    p: float = 0.2,
    seed: int = 42
) -> nx.Graph:
    """
    构建 Watts-Strogatz 小世界网络。

    参数:
        agent_ids (list): 所有 Agent 的 unique_id 列表，作为网络节点。
        k (int):          规则环图中每个节点的初始邻居数（建议 4~6）。
        p (float):        随机重连概率（建议 0.1~0.3）。
        seed (int):       随机数种子，保证实验可复现。

    返回:
        nx.Graph: 节点为 agent_id 的无向小世界网络图。
    """
    n = len(agent_ids)

    # 防御：k 必须小于 n，且为偶数
    k = min(k, n - 1)
    if k % 2 != 0:
        k = max(2, k - 1)

    # 构建 WS 网络（节点索引为 0..n-1）
    G_raw = nx.watts_strogatz_graph(n=n, k=k, p=p, seed=seed)

    # 将节点索引重映射为真实 agent_id
    mapping = {i: agent_ids[i] for i in range(n)}
    G = nx.relabel_nodes(G_raw, mapping)

    return G


def describe_network(G: nx.Graph) -> str:
    """输出网络基本统计信息，供运行日志打印。"""
    avg_clustering = nx.average_clustering(G)
    avg_path = nx.average_shortest_path_length(G) if nx.is_connected(G) else float('inf')
    return (
        f"节点数: {G.number_of_nodes()} | "
        f"边数: {G.number_of_edges()} | "
        f"平均聚类系数: {avg_clustering:.3f} | "
        f"平均最短路径: {avg_path:.2f}"
    )

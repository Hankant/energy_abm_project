"""
模块名称：模拟运行入口与配置导出模块 (Execution, IO & Configuration Module)
核心作用：系统的唯一启动脚本，负责数据加载、参数配置、剧本注入与最终结果的输出保存。

【能力边界与开发规范】
1. 业务逻辑高度隔离：任何关于"用电行为规则"、"个体决策"的具体仿真逻辑严禁写在此处，
   必须沉淀至 model.py 或 agents.py。
2. 纯调度工作流：承担"读取问卷数据 -> 初始化 Model -> 按剧本推进 -> 导出结果"流水线。
3. 唯一的配置中心：所有超参数（模拟天数、问卷路径、输出目录）均在此处配置。
4. 问卷数据加载职责完全归属本模块：确保 Model 层只接收已加载好的数据列表，不感知文件路径。
5. 政策剧本管理：与天气剧本并列，由本模块统一调度，每步前注入 Model。
"""
import os
import pandas as pd
from datetime import datetime
from model import EnergyTransitionModel
from policy import NO_POLICY, SUBSIDY_LOW_INCOME, CARBON_TAX_HIGH, POWER_CONTROL_ALERT, NEWS_GREEN_ENERGY


def load_questionnaire(data_path: str) -> list[dict]:
    """
    从 CSV 加载问卷数据，转换为 Agent 初始化所需的字典列表。
    【职责说明】数据加载完全由 run.py 负责，model.py 不感知文件路径。
    """
    df = pd.read_csv(data_path)
    print(f"[数据加载] 成功读取问卷数据，共 {len(df)} 条记录。")
    return df.to_dict(orient='records')


def main():
    # ─── 配置区（超参数集中管理）───
    DATA_PATH   = os.path.join(os.path.dirname(__file__), 'data', 'sample_questionnaire.csv')
    RESULTS_DIR = os.path.join(os.path.dirname(__file__), 'results')

    # 社区网络拓扑模块开关（True = 启用邻里社会影响；False = 独立决策对照组）
    ENABLE_SOCIAL_NETWORK = True
    NETWORK_K = 4    # 每节点初始邻居数（WS 网络参数）
    NETWORK_P = 0.2  # 随机重连概率（WS 网络参数）

    # ─── 1. 加载问卷数据 ───
    agent_data_list = load_questionnaire(DATA_PATH)

    # ─── 2. 初始化模型（仅传入 Agent 数据列表，无文件路径） ───
    print("\n=== 开始初始化能源转型模拟系统 ===")
    env_model = EnergyTransitionModel(
        agent_data_list=agent_data_list,
        use_social_network=ENABLE_SOCIAL_NETWORK,
        network_k=NETWORK_K,
        network_p=NETWORK_P,
    )

    # ─── 3. 天气剧本（每天的气温与基础电价） ───
    # 格式: (day_label, temperature_°C, base_price_元/kWh)
    weather_script = [
        (1,  25,  0.6),  # 第1天：正常天气
        (2,  -1,  1.2),  # 第2天：极寒，电价飙升
        (3,  41,  1.5),  # 第3天：酷暑，电网负荷爆炸
    ]

    # ─── 4. 政策剧本（每天对应的政策信号，与天气剧本对齐） ───
    # 格式: PolicySignal 对象（来自 policy.py 的预置模板或自定义）
    policy_script = [
        NO_POLICY,           # 第1天：无政策，基准日
        POWER_CONTROL_ALERT, # 第2天：极寒 + 电网管控通知
        CARBON_TAX_HIGH,     # 第3天：酷暑 + 碳税征收公告
    ]

    simulation_days = len(weather_script)
    print(f"=== 开始运行大模型 Agent 模拟，设定时长：{simulation_days}天 ===")

    # ─── 5. 主仿真循环 ───
    for day_idx in range(simulation_days):
        day_label, temp, price = weather_script[day_idx]
        policy = policy_script[day_idx]

        # 注入当天宏观环境到 Model
        env_model.current_temperature = temp
        env_model.current_price       = price
        env_model.current_policy      = policy

        print(f"\n>>>> 推演 第 {day_label} 天 | 气温: {temp}°C | 电价: {price}元/度 | 政策: {policy.policy_type}")

        # 触发仿真步进
        env_model.step()

        print(f"====> 当日宏观总能耗: {env_model.total_consumption:.1f} kWh | 平均WTP: {env_model.avg_wtp:.1f} 元")

    print("\n=== 模拟结束 ===")

    # ─── 6. 收集并打印宏观数据摘要 ───
    df_macro = env_model.datacollector.get_model_vars_dataframe()
    df_micro = env_model.datacollector.get_agent_vars_dataframe()

    print("\n[统计结果] 宏观数据记录：")
    print(df_macro.to_string())

    # ─── 7. 保存实验结果到 CSV ───
    os.makedirs(RESULTS_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    macro_path = os.path.join(RESULTS_DIR, f'macro_result_{timestamp}.csv')
    micro_path = os.path.join(RESULTS_DIR, f'micro_result_{timestamp}.csv')

    df_macro.to_csv(macro_path, index=True, encoding='utf-8-sig')
    df_micro.to_csv(micro_path, index=True, encoding='utf-8-sig')

    print(f"\n[保存成功] 实验结果已保存至 {RESULTS_DIR}：")
    print(f"  -> {os.path.basename(macro_path)}")
    print(f"  -> {os.path.basename(micro_path)}")


if __name__ == "__main__":
    main()

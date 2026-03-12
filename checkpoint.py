"""
模块名称：状态存档与恢复模块 (Checkpointing Module)
核心作用：在仿真过程中定期或在发生网络异常时序列化保存整个计算节点（环境+全部Agent）的内存状态。
         当 LLM API 熔断或网络断开时，可从最近的存档点加载并恢复执行，不仅保证了实验的纯粹性
         （禁止降级为规则决策），而且保护了已消耗的 API 成本与运行时间。
"""

import pickle
import os
import datetime
import mesa


def save_checkpoint(model: mesa.Model, base_dir: str = "checkpoints", filename: str = None) -> str:
    """
    保存当前的仿真模型状态到硬盘。
    包含：进度时钟、所有 Agent 的记忆和属性、DataCollector 已收集的数据、社会网络拓扑等。
    """
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    if filename is None:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        day = model.schedule.steps
        filename = f"sim_checkpoint_day{day}_{timestamp}.pkl"

    filepath = os.path.join(base_dir, filename)

    try:
        with open(filepath, 'wb') as f:
            pickle.dump(model, f)
        print(f"\n[Checkpoint] 💾 实验状态已成功存档：{filepath}")
        return filepath
    except Exception as e:
        print(f"\n[Checkpoint Error] ❌ 存档失败: {e}")
        return None


def load_checkpoint(filepath: str) -> mesa.Model:
    """
    从硬盘加载指定的仿真模型状态。
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"找不到指定的存档文件：{filepath}")

    print(f"\n[Checkpoint] 🔄 正在从源点恢复实验状态：{filepath}...")
    try:
        with open(filepath, 'rb') as f:
            model = pickle.load(f)
        day = model.schedule.steps
        print(f"[Checkpoint] ✅ 成功恢复至第 {day} 天的状态。Agent 记忆与历史数据均已就绪。")
        return model
    except Exception as e:
        print(f"\n[Checkpoint Error] ❌ 读档失败: {e}")
        raise e

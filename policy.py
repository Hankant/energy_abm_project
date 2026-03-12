"""
模块名称：政策环境模块 (Policy Environment Module)
核心作用：定义并管理政府层面的宏观政策信号（如补贴、碳税、新闻播报等），
        作为宏观环境的组成部分，随时间步注入 Model 并透传给 Agent 感知。

【政策信号类型】
1. 电价补贴 (subsidy)：对特定人群的用电成本进行直接补贴
2. 碳税征收 (carbon_tax)：对高耗电行为附加额外的碳排放税
3. 限电管控 (power_control)：政府强制拉闸/错峰用电等行政手段
4. 新闻播报 (news)：模拟媒体对能源形势的宣传与舆论引导
5. 无政策 (none)：基准对照状态
"""
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class PolicySignal:
    """
    单日政策信号数据类。
    通过 run.py 的政策剧本（policy_script）驱动，每天由外部注入 Model。
    """
    # 政策类型标识
    policy_type: str = "none"  # 可选: "none" / "subsidy" / "carbon_tax" / "power_control" / "news"

    # 给 LLM Agent 感知的政策播报正文（自然语言，将直接注入 Prompt）
    announcement: str = "目前无特殊政策通知。"

    # 可选：对电价的直接调整幅度（正数=涨价/税负，负数=补贴）
    price_adjustment: float = 0.0

    # 可选：补贴或税收的目标群体（如 "低收入", "高收入", "全部"）
    target_group: str = "全部"

    # 可选：附加的数值参数（如碳税税率、补贴金额上限等）
    parameter: Optional[float] = None

    def describe(self) -> str:
        """
        生成可读的政策摘要，用于注入 Agent 的 Prompt 上下文。
        """
        return (
            f"[政策信号] 类型: {self.policy_type} | "
            f"目标群体: {self.target_group} | "
            f"公告: {self.announcement}"
        )


# ─────────────────────────────────────────────
# 预置政策模板库（可直接在 run.py 的政策剧本中复用）
# ─────────────────────────────────────────────

NO_POLICY = PolicySignal(
    policy_type="none",
    announcement="今日无特殊能源政策通知，电力系统正常运行。",
)

SUBSIDY_LOW_INCOME = PolicySignal(
    policy_type="subsidy",
    announcement="国家发改委发布通知：本月起对低收入家庭实施居民电价补贴，每度电补贴0.1元，请低收入用户持证申请。",
    price_adjustment=-0.1,
    target_group="低收入",
    parameter=0.1,
)

CARBON_TAX_HIGH = PolicySignal(
    policy_type="carbon_tax",
    announcement="生态环境部公告：高耗电家庭（月用电超过500度）将从本月起征收碳排放附加税，税率为每度0.05元。",
    price_adjustment=0.05,
    target_group="高耗电",
    parameter=0.05,
)

POWER_CONTROL_ALERT = PolicySignal(
    policy_type="power_control",
    announcement="电网公司紧急通知：受极端天气影响，今日14:00-20:00将对部分工业用电实施错峰限电，请居民用户减少非必要大功率电器使用，共同保障民生用电。",
    price_adjustment=0.0,
    target_group="全部",
)

NEWS_GREEN_ENERGY = PolicySignal(
    policy_type="news",
    announcement="【新闻播报】今日央视报道：我国光伏发电装机容量再创历史新高，绿色电力占比持续上升，专家呼吁居民积极响应节能减排号召，优先选择低碳用电行为。",
    price_adjustment=0.0,
    target_group="全部",
)

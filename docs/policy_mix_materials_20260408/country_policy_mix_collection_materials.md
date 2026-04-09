# 国家/地区政策组合收集材料（居民侧能源转型与需求响应）

## 0. 文档说明

本材料库用于支撑实验设计中的“真实政策包原型”构造。  
收集原则如下：

- 优先使用**官方政府、监管机构或法令文本**来源
- 尽量覆盖不同类型的居民侧政策组合
- 以“国家/地区—政策包—可编码属性—实验启发”的方式整理

**时间说明：**  
以下材料按 **2026 年 4 月 9 日** 可查到的官方或准官方信息整理。部分项目在不同地区的正式实施时间不完全一致，因此在编码时建议使用“政策是否已明确、是否已实施、实施阶段”三类变量区分。

## 1. 编码维度

建议将每个政策包按以下字段编码：

- `jurisdiction`：国家/州/城市/监管区
- `policy_name`
- `document_date`
- `price_signal`：固定电价 / 峰谷电价 / TOU / 动态价格 / 免费时段
- `tech_requirement`：双费率电表 / 智能电表 / 自动化设备 / 聚合平台
- `financial_support`：账单折扣 / 返现 / 补贴 / 低息贷款 / 改造支持
- `equity_protection`：低收入保护 / 脆弱用户防断供 / 自动识别补贴资格
- `efficiency_support`：能效改造 / 热泵 / 保温 / 电池 / 光伏 / 社区能源
- `response_mode`：手动 / 可选自动 / 平台聚合 / 虚拟电厂
- `enrollment`：自愿申请 / 自动识别 / 默认加入可退出
- `sequencing`：同步推出 / 技术先行 / 支持先行 / 试点后推广
- `policy_goal`

## 2. 案例总表

| 编号 | 国家/地区 | 代表政策包 | 核心组合特征 | 最适合提炼的实验属性 |
|---|---|---|---|---|
| C1 | 英国 | Warm Home Discount + Warm Homes Plan + Economy 7 / smart meter | 分时电价、智能电表、低收入账单支持、住宅升级、热泵/保温支持 | 价格 + 补贴 + 改造 + 自动识别 |
| C2 | 美国加州 | Dynamic Hourly Rates + Demand Response + CARE/FERA + DAC solar | 动态电价、需求响应激励、低收入折扣、社区太阳能 | 动态价格 + 参与奖励 + 定向保护 |
| C3 | 澳大利亚 | TOU / smart home + battery rebate + concessions rule + Solar Sharer Offer | 灵活电价、智能设备自动化、电池补贴、补贴资格识别、午间免费电力 | 智能化 + TOU + 储能支持 + 补贴识别 |
| C4 | 欧盟 | Electricity Market Design reform | 固定与动态合同并存、脆弱用户保护、energy sharing | 选择权 + 动态合同 + 保护机制 |
| C5 | 中国（国家层面） | 电力需求侧管理办法（2023版） | 需求响应优先、有序用电兜底、虚拟电厂/储能/电动汽车等纳入资源库 | 市场化响应 + 资源聚合 + 基本民生优先 |
| C6 | 中国辽宁（居民电采暖） | 居民电采暖峰谷分时电价升级版 | 居民峰谷分时电价、免费换表、三种套餐、补贴和能效改造协同 | 价格套餐 + 民生保障 + 改造配套 |
| C7 | 中国上海 | 虚拟电厂高质量发展与居民社区试点 | 平台聚合、自动调节、V2G、社区场景、响应补贴 | 聚合式自动响应 + 社区参与 + 激励 |

## 3. 各案例详细材料

## C1 英国：账单支持 + 住宅升级 + 分时电价

### 3.1 政策组合概况

截至 **2026 年 1 月 29 日**，英国政府确认：

- `Warm Home Discount` 将持续到 `2030/2031`
- 每年冬季向符合条件家庭提供 `£150` 账单折扣
- 同时推进规模化 `Warm Homes Plan`

英国居民侧政策组合的特点是：

- 使用账单补贴缓解能源贫困
- 通过住宅升级和低碳供热降低长期能耗
- 通过双时段/智能电表支持差异化电价
- 低收入家庭尽量实现自动识别

### 3.2 可编码的政策要素

- 价格机制：`Economy 7` 等双时段/分时电价
- 技术要求：双费率电表或智能电表
- 财政支持：`£150` 冬季账单折扣
- 改造支持：保温、热泵、低息贷款、地方升级项目
- 目标群体：低收入、燃料贫困、脆弱家庭
- 实施特征：越来越强调自动识别和减少申请障碍

### 3.3 对实验设计的启发

英国案例最适合抽象成：

- “价格 + 账单保护 + 住宅升级”的政策包
- 重点测试：**如果先提供支持，再引入价格机制，居民是否更容易接受**

### 3.4 官方链接

- GOV.UK, *Energy bill support extended for millions of families*, **29 January 2026**  
  <https://www.gov.uk/government/news/energy-bill-support-extended-for-millions-of-families>

- GOV.UK, *Warm Homes Plan*, **21 January 2026**  
  <https://www.gov.uk/government/publications/warm-homes-plan>

- GOV.UK, *Warm Homes Plan: Technical annex*, **21 January 2026**  
  <https://www.gov.uk/government/publications/warm-homes-plan/warm-homes-plan-technical-annex>

- Ofgem, *Warm Home Discount (WHD) - Eligibility*  
  <https://www.ofgem.gov.uk/environmental-and-social-schemes/warm-home-discount-whd/warm-home-discount-whd-eligibility>

- Ofgem, *Economy 7 tariff guidance*  
  <https://www.ofgem.gov.uk/information-consumers/energy-advice-households/economy-7-consumer-guide>

- GOV.UK, *Apply for the Boiler Upgrade Scheme*  
  <https://www.gov.uk/apply-boiler-upgrade-scheme>

## C2 美国加州：动态价格 + 需求响应 + 低收入保护 + 社区清洁电力

### 3.5 政策组合概况

加州居民侧政策组合非常适合做“价格—激励—公平”组合原型。  
截至 **2025 年 8 月 28 日**，CPUC 已就动态小时电价给出明确指导，要求大电力公司为 `2027` 年前的可选动态费率做好准备。

同时，加州长期存在：

- 自愿式需求响应项目
- 低收入账单折扣（CARE/FERA）
- 面向弱势社区的社区太阳能与折扣项目

### 3.6 可编码的政策要素

- 价格机制：动态小时电价、TOU、需求响应激励
- 参与方式：住户可自愿加入 DR 项目
- 经济激励：参与 DR 可获得账单优惠或补偿
- 公平保护：CARE 电费 30–35% 折扣，FERA 18% 折扣
- 社区清洁电力：DAC-GT/CSGT 为弱势社区提供 20% 电费折扣和清洁电力
- 实施主体：电力公司、社区聚合买方、聚合商、第三方 DR 提供商

### 3.7 对实验设计的启发

加州案例最适合提炼为：

- “动态价格 + 自愿响应奖励 + 低收入折扣”政策包
- 重点测试：**居民在看到有明确电费折扣与参与补偿时，是否更愿意接受动态价格和自动化**

### 3.8 官方链接

- CPUC, *CPUC Issues Guidance for Utility Dynamic Hourly Rates*, **28 August 2025**  
  <https://www.cpuc.ca.gov/news-and-updates/all-news/cpuc-issues-guidance-for-utility-dynamic-hourly-rates>

- CPUC, *Demand Response*  
  <https://www.cpuc.ca.gov/industries-and-topics/electrical-energy/electric-costs/demand-response-dr>

- CPUC, *CARE/FERA Program*  
  <https://www.cpuc.ca.gov/consumer-support/financial-assistance-savings-and-discounts/family-electric-rate-assistance-program>

- CPUC, *Family Electric Rate Assistance Program (FERA)*  
  <https://www.cpuc.ca.gov/fera/>

- CPUC, *Solar in Disadvantaged Communities*  
  <https://www.cpuc.ca.gov/solarindacs>

## C3 澳大利亚：TOU + 智能家居 + 电池支持 + 补贴识别

### 3.9 政策组合概况

澳大利亚的居民侧政策组合近年来明显转向：

- 智能电表普及
- TOU / flexible tariff
- 家庭电池和储能支持
- 自动化和 demand response
- 补贴资格识别与账单减负

### 3.10 可编码的政策要素

- 价格机制：time-of-use / flexible tariff
- 技术支持：智能电表、IHD、智能家居控制
- 自动化：设备可根据峰谷电价和远程信号自动控制
- 补贴：家庭电池补贴、家庭能效升级融资支持
- 权益保护：零售商需帮助识别 concession/rebate 资格
- 新型价格方案：太阳能高发时段免费电力窗口

### 3.11 对实验设计的启发

澳大利亚案例最适合提炼为：

- “灵活电价 + 自动化 + 电池/升级支持 + 补贴识别”政策包
- 重点测试：**如果居民不需要自己主动申请，而是由零售商帮助识别资格，政策接受度是否更高**

### 3.12 官方链接

- energy.gov.au, *Smart homes*  
  <https://www.energy.gov.au/households/smart-homes>

- energy.gov.au, *Reduce your energy bills*  
  <https://www.energy.gov.au/households/household-guides/reduce-energy-bills>

- energy.gov.au, *Rule change to help energy consumers access concessions*, **29 September 2025**  
  <https://www.energy.gov.au/news/rule-change-help-energy-consumers-access-concessions>

- energy.gov.au, *Discounted batteries for households through the Cheaper Home Batteries Program*, **20 May 2025**  
  <https://www.energy.gov.au/news/discounted-batteries-households-through-the-cheaper-home-batteries-program>

- energy.gov.au, *Household Energy Upgrades Fund*  
  <https://www.energy.gov.au/rebates/household-energy-upgrades-fund>

- energy.gov.au, *Solar Sharer Offer to cut electricity bills*, **23 January 2026**  
  <https://www.energy.gov.au/news/solar-sharer-offer-cut-electricity-bills>

## C4 欧盟：合同选择权 + 动态价格 + 脆弱用户保护 + 能源共享

### 3.13 政策组合概况

欧盟层面的居民侧政策组合并不是一个单一项目，而是一套监管框架。  
`Directive (EU) 2024/1711` 及其国家转化要求明确强调：

- 动态电价合同权利
- 固定价合同权利
- 脆弱用户和能源贫困用户保护
- energy sharing

### 3.14 可编码的政策要素

- 价格机制：固定价合同与动态价合同并存
- 选择权：居民可根据自身情况选择合同类型，甚至组合使用
- 公平保护：脆弱用户和能源贫困用户防断供
- 社区机制：energy sharing / energy communities
- 信息透明：加强签约前信息披露与消费者权利保护

### 3.15 对实验设计的启发

欧盟案例最适合提炼为：

- “合同选择权 + 动态价格 + 脆弱用户保护”的组合
- 重点测试：**当居民拥有明确选择权时，对动态价格的接受度是否提高**

### 3.16 官方链接

- European Commission, *Electricity Market Design: Deadline for transposing new rules into national law*, **17 January 2025**  
  <https://energy.ec.europa.eu/news/electricity-market-design-deadline-transposing-new-rules-national-law-2025-01-17_en>

- EUR-Lex, *Directive (EU) 2024/1711*  
  <https://eur-lex.europa.eu/eli/dir/2024/1711/oj>

- European Commission, *In focus: Protecting and empowering energy consumers*, **18 June 2024**  
  <https://energy.ec.europa.eu/news/focus-protecting-and-empowering-energy-consumers-2024-06-18_en>

## C5 中国（国家层面）：需求响应优先 + 资源库 + 民生保障底线

### 3.17 政策组合概况

中国国家层面的居民侧相关政策组合，更像是一个需求侧治理框架，而不是单一零售电价政策。  
`电力需求侧管理办法（2023年版）` 及国家能源局解读强调：

- 需求响应优先
- 有序用电作为兜底
- 建立需求响应资源库
- 鼓励新型储能、分布式电源、电动汽车、空调负荷等参与
- 优先保障居民和重要公共服务用电

### 3.18 可编码的政策要素

- 响应方式：市场化需求响应优先
- 技术基础：资源库、负荷聚合、虚拟电厂
- 支持主体：储能、空调、分布式资源、电动车
- 政策逻辑：优先用市场化响应削峰，而非直接行政限电
- 底线约束：居民、农业和重要公益服务优先保障

### 3.19 对实验设计的启发

中国国家层面案例最适合提炼为：

- “市场化需求响应 + 民生兜底”的政策框架变量
- 可用于情景说明中的制度背景设定，而不一定直接作为一个单独居民方案

### 3.20 官方链接

- 中国政府网，*国家发展改革委等部门关于印发《电力需求侧管理办法（2023年版）》的通知*  
  <https://www.gov.cn/zhengce/zhengceku/202310/content_6907311.htm>

- 国家能源局，*电力供需怎么“稳”？需求侧来支撑*，**27 October 2023**  
  <https://www.nea.gov.cn/2023-10/27/c_1310747686.htm>

## C6 中国辽宁：居民电采暖峰谷分时电价 + 补贴 + 能效提升

### 3.21 政策组合概况

辽宁 2025 年底发布的居民电采暖政策，非常适合作为居民侧“价格 + 设施 + 改造”组合包案例。  
政策特点是：

- 采暖期居民峰谷分时电价
- 三种计费套餐可选
- 免费安装/更换分时电表
- 不再执行阶梯电价
- 配套清洁取暖项目投资补贴和房屋节能改造

### 3.22 可编码的政策要素

- 价格机制：采暖期峰谷分时电价
- 套餐设计：三类套餐，适配不同调节能力
- 技术支持：免费装表、单独计量
- 配套支持：清洁取暖投资补贴、房屋节能改造
- 目标群体：居民电采暖、煤改电用户
- 政策目标：清洁取暖、降低居民负担、促进新能源消纳

### 3.23 对实验设计的启发

辽宁案例很适合转化为：

- “峰谷价格 + 免费换表 + 多套餐 + 改造支持”的政策包
- 可用于检验：**当居民可自主选择不同价格套餐时，支持度是否提升**

### 3.24 官方链接

- 朝阳市人民政府，*《关于完善居民电采暖用户执行峰谷分时电价政策有关事项的通知》政策解读*，**26 December 2025**  
  <https://www.chaoyang.gov.cn/html/CYSZF/202512/1176672950590130.html>

- 辽宁省政府网转载，*居民电采暖用户将执行峰谷分时电价*  
  <https://www.ln.gov.cn/web/ywdt/msrd/2025120309171675367/index.shtml>

## C7 中国上海：虚拟电厂 + 社区试点 + 自动调节 + 响应补贴

### 3.25 政策组合概况

上海虚拟电厂案例最有价值的地方在于，它把居民侧需求响应从“价格信号”推进到了“平台聚合 + 自动调节 + 社区试点”。

截至 **2025 年 8 月**：

- 上海虚拟电厂平台接入 `49` 家运营商
- 总申报可调能力达 `203.24 万千瓦`
- 首次实现居民社区虚拟电厂响应
- 社区设备通过 AI 和平台实现自动错峰策略
- 参与方可获得经济补贴

### 3.26 可编码的政策要素

- 响应方式：虚拟电厂、聚合商、平台调控
- 技术支持：AI 动态分析、自动控制、V2G
- 场景：社区公共负荷、楼宇、产业园区、充电场站
- 激励：参与响应可获得补贴
- 政策目标：削峰填谷、保供、促进新能源消纳

### 3.27 对实验设计的启发

上海案例适合提炼为：

- “社区聚合 + 自动调节 + 激励补偿”的政策包
- 重点测试：**如果自动化调节被框定为‘社区共同参与、并有补偿’而非个人被强制控制，接受度是否更高**

### 3.28 官方链接

- 上海市政府，*上海虚拟电厂今夏实现多个“首次” 最大响应负荷首破百万千瓦*，**16 August 2025**  
  <https://www.shanghai.gov.cn/nw4411/20250816/d0e15b73a42c400f8876d83061db7d50.html>

## 4. 可直接用于实验编码的属性清单

根据以上案例，最适合抽出来进入实验的属性有 6 组：

### 4.1 价格机制

- 固定单一电价
- 峰谷/TOU 电价
- 动态小时电价
- 中午免费电力窗口

### 4.2 支持方式

- 无支持
- 季节性账单折扣
- 参与需求响应现金返还
- 能效/电池/热泵补贴
- 低息贷款/升级融资

### 4.3 技术配置

- 无特殊技术要求
- 双费率或智能电表
- 实时反馈/家庭显示界面
- 自动控制设备
- 聚合平台/虚拟电厂

### 4.4 公平保护

- 无专门保护
- 低收入电费折扣
- 脆弱用户防断供
- 自动识别补贴资格
- 社区共享或弱势社区定向支持

### 4.5 参与方式

- 用户自愿报名
- 默认加入可退出
- 自动识别后提供支持
- 聚合商/社区代理参与

### 4.6 顺序安排

- 同时推出
- 先补贴/改造，后价格调整
- 先技术基础，后动态价格
- 先试点，后推广

## 5. 推荐的原型化处理组映射

为了方便实验设计，建议将以上材料原型化为 6–8 个政策包：

- P0：无政策控制组
- P1：英国型“账单保护 + 改造支持”
- P2：加州型“动态价格 + 响应奖励 + 低收入折扣”
- P3：澳大利亚型“智能化 + TOU + 储能支持”
- P4：欧盟型“价格选择权 + 脆弱用户保护”
- P5：中国清洁取暖型“峰谷价格 + 免费换表 + 多套餐”
- P6：中国虚拟电厂型“社区聚合 + 自动调节 + 补贴”
- P7：优化组合型“价格 + 改造 + 自动化 + 定向保护 + 支持先行”

## 6. 备注

- 这份材料库的目标不是穷尽所有国家，而是建立一套**足够真实、足够有差异、足够适合实验转化**的初始案例库。
- 如果后续需要扩展，可以优先增加：
  - 北欧或德国的动态电价与热泵协同政策
  - 日本的需求响应与家电控制
  - 法国的社会电价/能效补贴
  - 韩国的居民用能与智慧社区项目


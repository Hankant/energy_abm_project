# 家庭能源问卷设计文献库

## 用途

本目录集中保存用于 `energy_abm_project` 问卷设计的原始量表、问卷原型、官方调查表、行为清单和来源记录。它与 `docs/literature_pdf_library/` 的综合论文库分开维护，重点回答：某个题项从哪里来、原文是什么、是否可公开使用、可支持哪个构念，以及应如何进入问卷和 ABM。

## 目录

- `files/behavior_scales/`：公开量表和行为测量工具。
- `files/china_household_studies/`：中国家庭能源行为及心理测量研究。
- `files/official_surveys/`：政府或国际组织调查问卷。
- `files/technical_behavior_lists/`：具有工程或政策依据的家庭行为清单。
- `link_records/`：未取得合法公开全文、仅保存官方链接的来源说明。
- `index.csv`、`index.json`：相同内容的人工可读和机器可读索引。

## 收录状态

- `full_file_saved`：已保存公开原文件，并检查文件格式。
- `official_html_saved`：已保存官方或开放全文网页快照；网页可能包含外部资源链接。
- `existing_project_file`：全文已在项目其他文献目录中，索引只做交叉引用。
- `link_only`：没有保存受版权限制的全文，仅记录 DOI、官方页面和用途。

## 使用规则

1. 不能把“借鉴或改写题项”表述成“直接使用成熟量表”。
2. 每个正式题项必须继续维护：来源原文、中文翻译、修改理由、构念、量尺、编码、适用条件、ABM用途和调查轮次。
3. HAB、QTB、EIB、IFB 首先是行为域。具体行为常受设备、产权、气候和家庭角色限制，不应自动当作反映式潜变量。
4. 行为题应尽量区分“已经实施”“未来愿意”“客观上无法实施”和“不适用”。
5. GEB-50 文件按其 CC BY-SA 4.0 条款使用；其他材料按各出版者或机构的版权与引用要求处理。
6. 对付费或未公开附件的论文只保存链接和元数据，不从非授权站点复制全文。
7. 新增材料时同步更新 `index.csv` 和 `index.json`，并记录核验日期。

## 当前优先级

### 一级：直接用于题项设计

- Kaiser (2020) GEB-50 英文完整问卷。
- Yue et al. (2019) HAB、QTB、EIB、IFB 四行为域的中国家庭研究原型。
- Liu et al. (2020) 正文 Table 2 公开的16个英文 TPB 题项。论文没有附独立问卷，也没有公开受访者实际看到的中文原版。
- OECD EPIC、WHO household energy questions、EIA RECS。
- UK DECC 45项家庭能源行为清单。

### 二级：用于结构、分类和效度依据

- Boudet et al. (2016)：区分实际行为、行为意愿与客观不可实施。
- Stragier et al. (2012)：住宅 Energy-Efficient Behaviour Scale 的结构与验证。
- Barr et al. (2005)：习惯/削减行为与购买/效率投资行为的经典区分。
- Yue et al. (2016, 2020)：四行为域的早期定义和 ABM 应用。

## 维护日期

首建：2026-07-20。

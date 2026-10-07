# 本体论分析报告 - 2604.04804

生成时间: 2026-04-12 21:10:44

## 分析结果

### paper_info

- **title**: SkillX: Automatically Constructing Skill Knowledge Bases for Agents
- **arxiv_id**: 2604.04804
- **year**: 2025

### new_concepts

- **memory_types**: ['规划技能 (Planning Skill)', '功能技能 (Functional Skill)', '原子技能 (Atomic Skill)']
- **memory_structures**: ['多层级技能知识库 (Multi-Level Skill Knowledge Base)', '伪计划 (Pseudo-Plan)']
- **memory_operations**: ['技能提取 (Skill Extraction)', '迭代技能优化 (Iterative Skill Optimization)', '探索性技能扩展 (Exploratory Skill Expansion)', '两阶段检索 (Two-Stage Retrieval)']
- **memory_carriers**: ['技能知识库 (文本/结构化描述)']

### new_relations

- **is_a**: [{'source': '规划技能', 'target': '技能', 'description': '规划技能是技能的一种高层抽象类型，用于任务分解'}, {'source': '功能技能', 'target': '技能', 'description': '功能技能是技能的中层实现类型，用于具体功能模块'}, {'source': '原子技能', 'target': '技能', 'description': '原子技能是技能的底层执行类型，用于 API 细节调用'}]
- **part_of**: [{'source': '技能', 'target': '技能知识库', 'description': '单个技能是技能知识库的基本组成单元'}, {'source': '原子技能', 'target': '功能技能', 'description': '原子技能作为功能技能的底层细节支撑与补充'}]
- **related_to**: [{'source': '执行反馈', 'target': '迭代技能优化', 'description': '执行反馈数据直接驱动技能的迭代优化过程'}, {'source': '伪计划', 'target': '规划技能检索', 'description': '伪计划作为规划技能检索后的中间查询产物，不注入最终 Prompt'}]

### new_axioms

- **theoretical**: ['结构化技能表示在经验迁移中的效率优于原始轨迹记忆', '多层级技能设计能适配不同粒度的任务需求并提升泛化性']
- **validation**: ['弱模型通过蒸馏强模型技能库可显著扩展能力边界', '技能库的迭代优化能有效提升技能文档与内容质量']

### technical_contributions

- **method_innovation**: 提出规划、功能、原子三层技能设计及自动化迭代优化与扩展机制，解决经验泛化差问题
- **architecture_design**: 设计 SkillX 自动化流水线（提取、优化、扩展）及推理时两阶段检索机制（规划检索 + 功能/原子检索）
- **experimental_validation**: 在多基准（BFCL-v3, AppWorld 等）和多模型上验证了跨模型迁移的有效性与鲁棒性，弱模型提升显著

### coverage_dimensions

- **form**: ['记忆的结构化表示', '多层级技能组织']
- **function**: ['提升任务成功率', '实现跨模型经验迁移', '减少执行步骤']
- **dynamics**: ['基于反馈的迭代优化', '经验引导的探索扩展', '技能生命周期管理（提取/更新/检索）']


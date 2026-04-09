# 本体论分析报告 - 2510.12635

生成时间: 2026-04-09 02:16:15

## 分析结果

### paper_info

- **title**: Memory as Action: Autonomous Context Curation for Long-Horizon Agentic Tasks
- **arxiv_id**: 2510.12635
- **year**: 2025

### new_concepts

- **memory_types**: ['Working Memory (工作记忆)', 'Curated Memory (策展记忆)', 'Task-Integrated Memory (任务整合记忆)']
- **memory_structures**: ['Interaction Record Sequence (交互记录序列)', 'Segmented Trajectory (轨迹分段)', 'Prune&Write Memory Primitives (记忆原语结构)']
- **memory_operations**: ['Prune (删除冗余上下文 ID)', 'Write (写入总结内容)', 'Context Curation (上下文策展)', 'Inline Memory Action (原地记忆动作执行)']
- **memory_carriers**: ['Token-based Context Window (基于 Token 的上下文窗口)', 'Model Policy Parameters (模型策略参数)', 'Interaction Logs (交互日志)']

### new_relations

- **is_a**: [{'source': 'Memory Action', 'target': 'Learnable Policy Action', 'description': '记忆动作被定义为可学习的策略动作，而非固定规则'}, {'source': 'Working Memory', 'target': 'MDP State', 'description': '工作记忆被建模为马尔可夫决策过程中的状态表示'}]
- **part_of**: [{'source': 'Prune&Write Primitives', 'target': 'MemAct Framework', 'description': '记忆原语是 MemAct 框架的核心组成部分'}, {'source': 'Memory Actions', 'target': 'Agent Action Space', 'description': '记忆动作与任务动作共同构成智能体的动作空间'}]
- **related_to**: [{'source': 'Context Curation', 'target': 'Task Performance', 'description': '上下文策展与任务性能通过强化学习联合优化'}, {'source': 'Memory Compression', 'target': 'Inference Efficiency', 'description': '记忆压缩直接影响推理延迟和 Token 消耗'}]

### new_axioms

- **theoretical**: ['记忆管理可作为核心推理能力被端到端学习', '上下文管理可建模为 MDP 中的可学习动作而非固定规则', '小模型通过记忆动作优化可超越大模型被动保留策略的性能']
- **validation**: ['RL 优化相比 SFT 在多目标任务上准确率提升 10.6% (48.5%→59.1%)', '记忆动作使 14B 模型准确率超越 235B 模型 (59.1% vs 53.1%)', '主动上下文管理可减少 51% 上下文长度和 40% 推理延迟']

### technical_contributions

- **method_innovation**: 提出 Memory-as-Action (MemAct) 框架，将记忆管理从固定规则转变为可学习的策略动作，引入 DCPO 算法解决上下文动态变化导致的训练错位问题
- **architecture_design**: 设计 Prune&Write 记忆原语实现原地上下文编辑，记忆动作与推理过程 inline 同步执行，无需额外推理 passes
- **experimental_validation**: 在 6 个数据集上验证，证明 14B 模型通过 MemAct 可超越 235B 大模型性能，同时降低 51-57% Token 消耗和 40% 推理延迟

### coverage_dimensions

- **form**: ['交互记录序列的结构化表示', 'Prune&Write 原语的形式化定义', '轨迹分段的训练表示']
- **function**: ['平衡推理质量与上下文成本', '解决长程任务注意力稀释问题', '实现信息保留与任务性能的联合优化']
- **dynamics**: ['RL 驱动的记忆生命周期管理', '自适应修剪与总结策略', '任务执行过程中的动态上下文更新']


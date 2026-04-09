# 本体论分析报告 - 2510.24699

生成时间: 2026-04-09 07:47:27

## 分析结果

### paper_info

- **title**: AgentFold: Long-Horizon Web Agents with Proactive Context Management
- **arxiv_id**: 2510.24699
- **year**: 2025

### new_concepts

- **memory_types**: ['动态上下文工作区 (Dynamic Context Workspace)', '折叠记忆 (Folded Memory)']
- **memory_structures**: ['推理 - 动作 - 观察三元组 (Reasoning-Action-Observation Triplet)', '多尺度历史轨迹 (Multi-scale History Trajectory)']
- **memory_operations**: ['主动折叠 (Proactive Folding)', '细粒度浓缩 (Granular Condensation)', '深度整合 (Deep Consolidation)']
- **memory_carriers**: ['LLM 上下文窗口 (LLM Context Window)', '上下文 Token (Context Tokens)']

### new_relations

- **is_a**: [{'source': '细粒度浓缩', 'target': '折叠操作', 'description': '一种保留关键细节的特定折叠类型'}, {'source': '深度整合', 'target': '折叠操作', 'description': '一种抽象多步子任务的特定折叠类型'}]
- **part_of**: [{'source': '折叠操作', 'target': '主动上下文管理', 'description': '管理框架中的核心机制'}]
- **related_to**: [{'source': '回顾性巩固 (人类认知)', 'target': '主动折叠', 'description': '启发技术机制的人类认知过程'}]

### new_axioms

- **theoretical**: ['上下文应被视为动态认知工作区而非被动日志', '长程任务需要在上下文全面性与简洁性之间进行权衡']
- **validation**: ['30B 参数的 AgentFold 模型在 BrowseComp 上性能超越 671B 基线模型', '100 轮交互后的上下文可被压缩至约 7k tokens']

### technical_contributions

- **method_innovation**: 受人类回顾性巩固启发的主动上下文折叠机制
- **architecture_design**: 具有动态上下文工作区和双层折叠（细粒度/深度）的 AgentFold 范式
- **experimental_validation**: 在 BrowseComp/ZH 基准上验证，30B 模型达到 36.2% 准确率，超越更大规模模型

### coverage_dimensions

- **form**: ['结构化上下文三元组表示', '折叠后的上下文表示']
- **function**: ['缓解上下文饱和', '保持信息完整性']
- **dynamics**: ['动态折叠生命周期管理', '多尺度轨迹管理']


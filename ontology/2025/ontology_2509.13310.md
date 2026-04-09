# 本体论分析报告 - 2509.13310

生成时间: 2026-04-08 20:45:13

## 分析结果

### paper_info

- **title**: Scaling Agents via Continual Pre-training
- **arxiv_id**: 2509.13310
- **year**: 2025

### new_concepts

- **memory_types**: ['Agent Behavior Trajectories (智能体行为轨迹)', 'Tool Invocation Sequences (工具调用序列)', 'Multi-step Reasoning Chains (多步推理链)']
- **memory_structures**: ['Agent Foundation Model Architecture (智能体基座模型架构)', 'Two-stage Training Pipeline (两阶段训练管道)']
- **memory_operations**: ['Agentic Continual Pre-training (智能体持续预训练)', 'Post-training Alignment via SFT/RL (后训练对齐)']
- **memory_carriers**: ['AgentFounder-30B Model', 'Agent Behavior Pre-training Data']

### new_relations

- **is_a**: [{'source': 'AgentFounder-30B', 'target': 'Deep Research Agent', 'description': 'AgentFounder-30B 是深度研究智能体的具体实现'}, {'source': 'Agentic CPT', 'target': 'Continual Pre-training Method', 'description': '智能体持续预训练是持续预训练方法的智能体专用变体'}]
- **part_of**: [{'source': 'Agentic CPT', 'target': 'Agent Training Pipeline', 'description': '智能体持续预训练是智能体训练管道的核心阶段'}, {'source': 'SFT/RL', 'target': 'Post-training Stage', 'description': 'SFT 和 RL 是后训练阶段的对齐方法'}]
- **related_to**: [{'source': 'Agent Behaviors', 'target': 'Tool Invocation', 'description': '智能体行为与工具调用能力密切相关'}, {'source': 'Foundation Model', 'target': 'Agent Capabilities', 'description': '基座模型质量直接影响智能体能力上限'}]

### new_axioms

- **theoretical**: ['通用基座模型缺乏鲁棒的智能体基础，导致后训练阶段存在优化张力', '解耦行为学习与对齐（先构建智能体基座，再后训练）可提升智能体性能上限']
- **validation**: ['Agentic CPT 方法在多个基准测试（BrowseComp、HLE 等）上优于现有开源领先模型', '30B 参数规模的智能体基座模型在性能与成本间取得较好平衡']

### technical_contributions

- **method_innovation**: 首创将智能体持续预训练 (Agentic CPT) 引入深度研究智能体训练管道，而非仅依赖后训练方法 (SFT/RL)
- **architecture_design**: 提出两阶段训练架构：先通过 Agentic CPT 构建智能体基座模型，再进行后训练对齐，解耦行为学习与对齐优化
- **experimental_validation**: 在 10 个基准测试上验证方法有效性，包括 BrowseComp-en、BrowseComp-zh、HLE 等，刷新开源智能体 SOTA

### coverage_dimensions

- **form**: ['智能体行为轨迹的结构化预训练数据表示', '工具调用序列与多步推理链的编码方式']
- **function**: ['动态环境下的行为一致性', '复杂任务自主编排与工具使用能力']
- **dynamics**: ['训练管道生命周期管理（预训练→后训练→部署）', '智能体基座模型的能力演进与迭代']


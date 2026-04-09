# 本体论分析报告 - 2510.04851

生成时间: 2026-04-09 00:27:09

## 分析结果

### paper_info

- **title**: LEGOMem: Modular Procedural Memory for Multi-agent LLM Systems for Workflow Automation
- **arxiv_id**: 2510.04851
- **year**: 2025

### new_concepts

- **memory_types**: ['Orchestrator Memory (编排器记忆)', 'Task Agent Memory (任务代理记忆)', 'Modular Procedural Memory (模块化过程记忆)']
- **memory_structures**: ['Memory Units (记忆单元)', 'Task Trajectories (任务轨迹)']
- **memory_operations**: ['Memory Allocation (记忆分配)', 'Memory Decomposition (记忆分解)', 'Semantic Retrieval (语义检索)']
- **memory_carriers**: ['Central Memory Database (中央记忆库)', 'Agent Context Window (代理上下文窗口)']

### new_relations

- **is_a**: [{'source': 'Orchestrator Memory', 'target': 'Procedural Memory', 'description': '编排器记忆是过程记忆的一种特定类型，用于规划'}, {'source': 'Task Agent Memory', 'target': 'Procedural Memory', 'description': '任务代理记忆是过程记忆的一种特定类型，用于执行'}]
- **part_of**: [{'source': 'Memory Units', 'target': 'Task Trajectories', 'description': '记忆单元是任务轨迹分解后的组成部分'}, {'source': 'LEGOMem Framework', 'target': 'Multi-agent LLM Systems', 'description': 'LEGOMem 是多智能体 LLM 系统的增强组件'}]
- **related_to**: [{'source': 'Orchestrator Memory', 'target': 'Task Decomposition', 'description': '编排器记忆与任务分解有效性强相关'}, {'source': 'Task Agent Memory', 'target': 'Tool Execution Accuracy', 'description': '任务代理记忆与工具执行准确率强相关'}]

### new_axioms

- **theoretical**: ['Role-specific memory allocation optimizes multi-agent system performance (角色特定的记忆分配优化多智能体系统性能)', 'Procedural memory can compensate for model capacity limitations in workflows (过程记忆可弥补工作流中模型能力的不足)']
- **validation**: ['Orchestrator memory significantly improves planning accuracy (编排器记忆显著提升规划准确性)', 'Small models with LEGOMem approximate large model performance (配备 LEGOMem 的小模型可接近大模型性能)']

### technical_contributions

- **method_innovation**: 提出了模块化记忆分配机制，动态决定记忆投向编排器或任务代理，解决了记忆在多智能体间分配策略不明的问题
- **architecture_design**: 设计了包含中央记忆库、编排器记忆模块和任务代理记忆模块的 LEGOMem 架构，支持结构化记忆检索
- **experimental_validation**: 基于 OfficeBench 基准进行了系统性对比与消融实验，验证了记忆位置对不同类型智能体的差异化影响

### coverage_dimensions

- **form**: ['Structured Memory Units (结构化记忆单元)', 'Vectorized Task Trajectories (向量化任务轨迹)']
- **function**: ['Workflow Planning Support (工作流规划支持)', 'Task Execution Support (任务执行支持)']
- **dynamics**: ['Memory Lifecycle Management (记忆生命周期管理)', 'Dynamic Retrieval & Allocation (动态检索与分配)']


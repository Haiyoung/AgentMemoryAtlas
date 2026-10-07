# 本体论分析报告 - 2604.07791

生成时间: 2026-04-12 20:39:37

## 分析结果

### paper_info

- **title**: SEARL: Joint Optimization of Policy and Tool Graph Memory for Self-Evolving Agents
- **arxiv_id**: 2604.07791
- **year**: 2025

### new_concepts

- **memory_types**: ['Tool Graph Memory', 'Policy-Integrated Memory']
- **memory_structures**: ['Directed Tool Dependency Graph', 'Tool Anchor Clusters']
- **memory_operations**: ['Dynamic Tool Registration', 'Tool Merging', 'Hybrid Retrieval']
- **memory_carriers**: ['External Graph Store', 'Vector Embeddings']

### new_relations

- **is_a**: [{'source': 'Tool Graph Memory', 'target': 'External Memory', 'description': 'A structured form of external memory specifically for tool storage and reuse'}]
- **part_of**: [{'source': 'Tool Node', 'target': 'Tool Graph Memory', 'description': 'Basic functional unit representing a skill or tool within the graph'}]
- **related_to**: [{'source': 'Policy Optimization', 'target': 'Memory Evolution', 'description': 'Jointly optimized through reinforcement learning to enhance generalization'}]

### new_axioms

- **theoretical**: ['Joint optimization of policy and memory enhances agent generalization capabilities', 'Structured memory effectively filters noise in context loading and reduces hallucinations']
- **validation**: ['Step-level grouping is crucial for accurate advantage estimation in long-horizon tasks', 'Fine-grained process reward signals are essential for stable training and credit assignment']

### technical_contributions

- **method_innovation**: Tool Anchor Advantage Estimation and Joint Optimization Framework for credit assignment
- **architecture_design**: Dual-system architecture integrating Policy Model with Tool Graph Memory
- **experimental_validation**: SOTA performance on AIME24 and HotpotQA with comprehensive ablation studies

### coverage_dimensions

- **form**: ['Structured Directed Graph', 'Vector Embeddings']
- **function**: ['Tool Reuse', 'Complex Reasoning']
- **dynamics**: ['Tool Lifecycle Management', 'Policy-Memory Co-evolution']


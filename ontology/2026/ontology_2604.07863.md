# 本体论分析报告 - 2604.07863

生成时间: 2026-04-12 20:09:42

## 分析结果

### paper_info

- **title**: Task-Adaptive Retrieval over Agentic Multi-Modal Web Histories via Learned Graph Memory
- **arxiv_id**: 2604.07863
- **year**: 2025

### new_concepts

- **memory_types**: ['Learned Graph Memory', 'Agentic Multi-Modal Web History Memory']
- **memory_structures**: ['Sparse Correlation Graph', 'Temporal Multi-modal Sequence']
- **memory_operations**: ['Task-Adaptive Retrieval', 'Modality-Specific Decay', 'Policy Gradient Graph Construction']
- **memory_carriers**: ['Webpage Screenshots', 'HTML Content', 'Structured Interaction Signals']

### new_relations

- **is_a**: [{'source': 'ACGM', 'target': 'Learned Graph-Memory Retriever', 'description': 'ACGM is a specific implementation of a retriever based on learned graph memory.'}]
- **part_of**: [{'source': 'Modality-Specific Decay', 'target': 'Graph Memory Construction Module', 'description': 'Visual and text decay mechanisms are components of the graph construction process.'}]
- **related_to**: [{'source': 'Task Success Signal', 'target': 'Policy Gradient Optimization', 'description': 'Task success signals provide the reward feedback for optimizing the graph structure.'}]

### new_axioms

- **theoretical**: ['Relevance in agent history evolves dynamically with task state, rendering static thresholds ineffective.', 'Visual memory decays faster than textual memory in web interaction contexts (λ_visual < λ_text).']
- **validation**: ['ACGM achieves higher nDCG@10 and Precision@10 compared to GPT-4o and traditional dense retrieval baselines.', 'Sparse connectivity (approx. 3.2 edges/node) maintains O(logT) retrieval complexity without significant performance loss.']

### technical_contributions

- **method_innovation**: Introduces modality-specific decay mechanisms and sparse connection learning optimized via policy gradients to capture dynamic relevance.
- **architecture_design**: Proposes ACGM architecture integrating multi-modal encoding, dynamic graph construction, and reinforcement learning-based optimization loop.
- **experimental_validation**: Validated on WebShop, VisualWebArena, and Mind2Web datasets against 19 baselines, demonstrating significant performance gains and efficiency.

### coverage_dimensions

- **form**: ['Graph-structured Representation', 'Multi-modal Embedding Space']
- **function**: ['Task-Adaptive Context Retrieval', 'Long-History Agent Support']
- **dynamics**: ['Temporal Decay Management', 'Reinforcement Learning-Driven Lifecycle Update']


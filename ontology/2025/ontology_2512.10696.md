# 本体论分析报告 - 2512.10696

生成时间: 2026-04-09 12:22:30

## 分析结果

### paper_info

- **title**: Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution
- **arxiv_id**: 2512.10696
- **year**: 2025

### new_concepts

- **memory_types**: ['Dynamic Procedural Memory', 'Experience-Driven Memory', 'Structured Experience Memory']
- **memory_structures**: ['Keypoint-level Experience Structure', 'Memory Pool', 'Scenario-aware Index']
- **memory_operations**: ['Experience Distillation', 'Scenario-aware Retrieval', 'Utility-based Deletion', 'Failure-aware Reflection', 'Experience Rewriting']
- **memory_carriers**: ['LLM Agent Memory System', 'Structured Experience Records', 'Embedding Vectors']

### new_relations

- **is_a**: [{'source': 'Dynamic Procedural Memory', 'target': 'Memory System', 'description': 'A specialized memory system for agent experience management'}, {'source': 'Keypoint-level Experience', 'target': 'Experience Structure', 'description': 'Fine-grained experience representation at key point level'}, {'source': 'Utility-based Deletion', 'target': 'Memory Operation', 'description': 'Operation for removing low-utility experiences'}]
- **part_of**: [{'source': 'Experience Acquisition', 'target': 'Dynamic Procedural Memory Framework', 'description': 'First phase of the three-stage cycle'}, {'source': 'Experience Reuse', 'target': 'Dynamic Procedural Memory Framework', 'description': 'Second phase of the three-stage cycle'}, {'source': 'Experience Refinement', 'target': 'Dynamic Procedural Memory Framework', 'description': 'Third phase of the three-stage cycle'}]
- **related_to**: [{'source': 'Utility Monitoring', 'target': 'Experience Deletion', 'description': 'Monitors retrieval frequency and utility to trigger deletion'}, {'source': 'Scenario-aware Retrieval', 'target': 'Experience Reuse', 'description': 'Enables context-aware experience retrieval'}, {'source': 'Failure Reflection', 'target': 'Experience Acquisition', 'description': 'Allows learning from failed trajectories'}]

### new_axioms

- **theoretical**: ['Memory quality outweighs quantity in agent evolution', 'Dynamic refinement prevents experience pollution', 'Keypoint-level distillation enables better knowledge transfer than trajectory-level', 'Small model with high-quality memory can outperform large model without memory']
- **validation**: ['Dynamic version outperforms fixed version across all settings', 'Retrieval count K=5 is optimal balance point', 'Selective addition (success-only) outperforms full addition', '32B summary model brings significant gains over 8B']

### technical_contributions

- **method_innovation**: Utility-based deletion strategy (removes experience if utility-frequency ratio below threshold), Keypoint-level experience distillation instead of trajectory-level, Three-phase alternating cycle for memory lifecycle management
- **architecture_design**: Three-stage alternating cycle architecture (Acquisition-Reuse-Refinement), Modular design with LLM-as-Judge verification, Scenario-aware embedding retrieval with re-ranking and rewriting
- **experimental_validation**: Dual benchmark testing (BFCL-V3, AppWorld), Multi-model size validation (8B, 14B, 32B), Complete ablation studies proving component necessity, Memory scaling effect demonstration

### coverage_dimensions

- **form**: ['Structured experience representation (scenario, core content, keywords, confidence, tools)', 'Embedding vector representation for scenario-aware retrieval']
- **function**: ['Agent self-evolution based on experience', 'Task success rate improvement', 'Knowledge transfer across tasks', 'Reducing deployment cost through memory scaling effect']
- **dynamics**: ['Memory lifecycle management (acquisition, reuse, refinement)', 'Adaptive experience refinement mechanism', 'Utility monitoring for experience deletion', 'Three-phase alternating cycle execution']


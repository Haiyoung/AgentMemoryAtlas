# 本体论分析报告 - 2505.15962

生成时间: 2026-04-08 07:18:42

## 分析结果

### paper_info

- **title**: Pre-training Limited Memory Language Models with Internal and External Knowledge
- **arxiv_id**: 2505.15962
- **year**: 2025

### new_concepts

- **memory_types**: ['Limited Memory', 'Externalized Factual Memory', 'Internal Linguistic Memory']
- **memory_structures**: ['Knowledge Triplets (Entity-Relation-Value)', 'Special Query Tokens']
- **memory_operations**: ['Loss Masking on Retrieved Values', 'Database-driven Unlearning', 'Query Generation']
- **memory_carriers**: ['External Knowledge Database', 'Model Weights (Linguistic Only)']

### new_relations

- **is_a**: [{'source': 'Limited Memory Language Model (LmLm)', 'target': 'Language Model', 'description': 'LmLm is a specialized type of language model with decoupled memory architecture.'}]
- **part_of**: [{'source': 'External Knowledge Database', 'target': 'LmLm System', 'description': 'The external database functions as an integral component of the overall LmLm architecture.'}]
- **related_to**: [{'source': 'Factual Knowledge', 'target': 'External Database', 'description': 'Factual knowledge is explicitly mapped to and stored in the external database rather than weights.'}, {'source': 'Language Ability', 'target': 'Model Weights', 'description': 'General linguistic capabilities remain encoded within the internal model weights.'}]

### new_axioms

- **theoretical**: ['Factual memory and language ability are theoretically decouplable within transformer architectures.', 'Learning to query external knowledge is more parameter-efficient than memorizing facts internally.']
- **validation**: ['Deleting database entries achieves perfect machine unlearning without requiring model fine-tuning.', 'Shielding retrieved values during loss calculation effectively prevents internal memorization of facts.']

### technical_contributions

- **method_innovation**: Pre-training loss masking mechanism that shields retrieved factual values from gradient updates to force external dependency.
- **architecture_design**: Decoder-only architecture extended with 4 special query tokens and an integrated external knowledge retrieval module.
- **experimental_validation**: Validated on FactScore, T-REx, and TOFU benchmarks showing 382M model matches 7B accuracy and supports instant unlearning.

### coverage_dimensions

- **form**: ['Structured Knowledge Triplets', 'Special Token Sequences for DB Interaction']
- **function**: ['High Factual Accuracy', 'Compliance & Machine Unlearning', 'Real-time Knowledge Updates']
- **dynamics**: ['Database Entry Deletion for Unlearning', 'Training-time Loss Shielding', 'Inference-time Retrieval Injection']


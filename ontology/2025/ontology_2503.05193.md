# 本体论分析报告 - 2503.05193

生成时间: 2026-04-07 18:48:29

## 分析结果

### paper_info

- **title**: Memory-augmented Query Reconstruction for LLM-based Knowledge Graph Reasoning
- **arxiv_id**: 2503.05193
- **year**: 2025

### new_concepts

- **memory_types**: ['Query Memory', 'Semantic Memory']
- **memory_structures**: ['Explicit Query Description', 'Rule-based Decomposed Statements']
- **memory_operations**: ['Semantic Similarity Retrieval', 'Query Reconstruction', 'Memory Augmentation']
- **memory_carriers**: ['Memory Module', 'LLM Context Window', 'Vector Embedding Space']

### new_relations

- **is_a**: [{'source': 'Query Memory', 'target': 'Memory Module', 'description': 'Query Memory is a specialized type of memory module designed for storing query descriptions.'}, {'source': 'MemQ', 'target': 'KGQA Framework', 'description': 'MemQ is a specific framework instance for Knowledge Graph Question Answering.'}]
- **part_of**: [{'source': 'Query Memory', 'target': 'MemQ Architecture', 'description': 'Query Memory is a core component within the MemQ system architecture.'}, {'source': 'Rule Decomposition', 'target': 'Memory Construction Process', 'description': 'Rule-based decomposition is a sub-process involved in constructing the memory content.'}]
- **related_to**: [{'source': 'Tool Invocation', 'target': 'Knowledge Reasoning', 'description': 'Tool invocation is theoretically decoupled from knowledge reasoning to reduce hallucination.'}, {'source': 'Query Description', 'target': 'SPARQL Query', 'description': 'Query descriptions serve as natural language semantic representations of formal SPARQL queries.'}]

### new_axioms

- **theoretical**: ["Decoupling Theory: Tool usage tasks should be separated from the LLM's core knowledge reasoning process.", 'Memory-Augmented Reasoning: Explicit memory retrieval reduces hallucinatory tool invocations in KGQA.']
- **validation**: ['MemQ achieves State-of-the-Art performance on WebQSP and CWQ benchmarks.', 'Decoupling tool invocation from reasoning improves interpretability and accuracy in KGQA tasks.']

### technical_contributions

- **method_innovation**: Proposed the MemQ framework which introduces a query memory module to decouple tool invocation from reasoning via query reconstruction.
- **architecture_design**: Designed a three-stage architecture: Rule-based decomposition with LLM description generation, Semantic similarity retrieval from memory, and Query reconstruction for natural language reasoning.
- **experimental_validation**: Validated effectiveness on WebQSP and CWQ datasets, demonstrating SOTA accuracy and enhanced reasoning interpretability compared to existing LLM-based KGQA methods.

### coverage_dimensions

- **form**: ['Natural Language Descriptions', 'SPARQL Query Structures', 'Vector Embeddings for Retrieval']
- **function**: ['Knowledge Graph Question Answering', 'Hallucination Reduction', 'Reasoning Interpretability Enhancement']
- **dynamics**: ['Memory Generation (Decomposition & Description)', 'Memory Storage', 'Semantic Retrieval', 'Query Reconstruction & Reasoning Lifecycle']


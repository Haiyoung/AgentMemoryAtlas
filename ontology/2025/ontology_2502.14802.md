# 本体论分析报告 - 2502.14802

生成时间: 2026-04-07 18:16:34

## 分析结果

### paper_info

- **title**: From RAG to Memory: Non-Parametric Continual Learning for Large Language Models
- **arxiv_id**: 2502.14802
- **year**: 2025

### new_concepts

- **memory_types**: ['Non-Parametric Continual Learning', 'Associative Memory', 'Fact Memory', 'Contextual Memory']
- **memory_structures**: ['Hybrid Knowledge Graph', 'Phrase-Paragraph Dual Node Structure', 'Query-to-Triple Mapping']
- **memory_operations**: ['Offline Indexing', 'Online Retrieval', 'Personalized PageRank Propagation', 'Recognition Memory Filtering']
- **memory_carriers**: ['Text Passages', 'Knowledge Graph Triples', 'Dense Embeddings']

### new_relations

- **is_a**: [{'source': 'HippoRAG 2', 'target': 'Non-Parametric Continual Learning System', 'description': 'HippoRAG 2 is instantiated as a system for non-parametric continual learning in LLMs.'}, {'source': 'Passage Node', 'target': 'Memory Carrier', 'description': 'Passage nodes serve as carriers for contextual information within the memory structure.'}]
- **part_of**: [{'source': 'Phrase Nodes', 'target': 'Hybrid Knowledge Graph', 'description': 'Phrase nodes constitute the semantic entity layer of the hybrid graph.'}, {'source': 'Passage Nodes', 'target': 'Hybrid Knowledge Graph', 'description': 'Passage nodes constitute the contextual layer of the hybrid graph.'}]
- **related_to**: [{'source': 'Query', 'target': 'Triple', 'description': 'Queries are mapped to triples via Query-to-Triple matching for seed node identification.'}, {'source': 'Passage Nodes', 'target': 'Phrase Nodes', 'description': 'Passage nodes are connected to phrase nodes via synonym detection to preserve context.'}]

### new_axioms

- **theoretical**: ['Hippocampal-Neocortical Complementarity maps to Offline Indexing and Online Retrieval stages.', 'Non-parametric memory storage prevents catastrophic forgetting in continual learning scenarios.']
- **validation**: ['Hybrid graph structure improves multi-hop reasoning without degrading fact memory performance.', 'Token consumption is inversely proportional to retrieval efficiency in structured RAG systems.']

### technical_contributions

- **method_innovation**: Introduces Query-to-Triple matching and integrates Passage Nodes into Knowledge Graphs to balance context and semantics.
- **architecture_design**: Designs HippoRAG 2 with a two-stage Offline Indexing and Online Retrieval flow using PPR and LLM-based filtering.
- **experimental_validation**: Validates on MuSiQue, 2Wiki, and LV-Eval, demonstrating SOTA performance with 92% lower token cost than GraphRAG.

### coverage_dimensions

- **form**: ['Structured Knowledge Graph Representation', 'Unstructured Text Passage Representation']
- **function**: ['Multi-hop Reasoning', 'Fact Memory Recall', 'Meaning Construction']
- **dynamics**: ['Offline Encoding (Indexing)', 'Online Activation (Retrieval/Propagation)', 'Noise Consolidation (Filtering)']


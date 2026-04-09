# 本体论分析报告 - 2511.17208

生成时间: 2026-04-09 10:51:40

## 分析结果

### paper_info

- **title**: A Simple Yet Strong Baseline for Long-Term Conversational Memory of LLM Agents
- **arxiv_id**: 2511.17208
- **year**: 2025

### new_concepts

- **memory_types**: ['Event-Centric Memory (EMem)', 'Long-Term Conversational Memory']
- **memory_structures**: ['Enriched EDU (Elementary Discourse Unit)', 'Heterogeneous Memory Graph']
- **memory_operations**: ['Recall-oriented LLM Filtering', 'Offline Event Extraction', 'Personalized PageRank Propagation']
- **memory_carriers**: ['LLM Agent Context Window', 'Embedding Vector Index']

### new_relations

- **is_a**: [{'source': 'EMem-G', 'target': 'EMem', 'description': 'EMem-G is a graph-enhanced variant of the base EMem framework designed for complex reasoning tasks'}]
- **part_of**: [{'source': 'Arguments', 'target': 'Enriched EDU', 'description': 'Semantic arguments are components that enrich the basic discourse unit with structured information'}]
- **related_to**: [{'source': 'Neo-Davidsonian Semantics', 'target': 'Event-Centric Representation', 'description': 'Provides the theoretical foundation for structuring memory events and their semantic relations'}]

### new_axioms

- **theoretical**: ['Lossless event storage preserves fine-grained details better than lossy summarization or compression methods', 'Reasoning-time effort (inference compute) can compensate for storage simplicity to achieve high accuracy']
- **validation**: ['System performance remains stable across retrieval quantity hyperparameters within the 20-40 range', 'LLM filtering module is the critical determinant for multi-hop reasoning accuracy']

### technical_contributions

- **method_innovation**: Integration of Neo-Davidsonian event semantics with a recall-oriented LLM filtering mechanism to balance precision and recall without complex graph dependencies.
- **architecture_design**: A dual-stage architecture (Offline Construction + Online Retrieval) offering two variants: lightweight EMem for efficiency and graph-enhanced EMem-G for reasoning.
- **experimental_validation**: Established a new performance baseline on LoCoMo and LongMemEval datasets, matching or exceeding complex baselines like HippoRAG 2 with simpler architecture.

### coverage_dimensions

- **form**: ['Structured Event Representation (Enriched EDUs)', 'Heterogeneous Graph Topology (in EMem-G)']
- **function**: ['Long-context Information Retention', 'Multi-hop and Temporal Reasoning Support']
- **dynamics**: ['Offline Memory Construction Lifecycle', 'Online Retrieval and Filtering Lifecycle']


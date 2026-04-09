# 本体论分析报告 - 2404.09982

生成时间: 2026-04-07 09:38:23

## 分析结果

### paper_info

- **title**: INMS: Memory Sharing for Large Language Model based Agents
- **arxiv_id**: 2404.09982
- **year**: 2025

### new_concepts

- **memory_types**: ['Domain-specific Memory Pool', 'Global Memory Pool', 'Candidate Memory']
- **memory_structures**: ['(Prompt, Answer) Pair', 'Enhanced Prompt with Retrieved Context']
- **memory_operations**: ['Retriever Continuous Training', 'Memory Scoring and Filtering', 'Memory Sharing']
- **memory_carriers**: ['Shared Vector Database', 'Rubric-based Scoring System']

### new_relations

- **is_a**: [{'source': 'Domain-specific Memory Pool', 'target': 'Memory Pool', 'description': 'A specialized memory pool restricted to agents within the same domain for optimized sharing'}]
- **part_of**: [{'source': 'Retriever Layer', 'target': 'INMS Framework', 'description': 'Component responsible for memory retrieval and continuous updates within the system'}]
- **related_to**: [{'source': 'Memory Capacity', 'target': 'Agent Performance', 'description': 'Non-linear relationship where performance peaks at an optimal capacity and declines thereafter'}]

### new_axioms

- **theoretical**: ['Memory sharing enables knowledge evolution and reduces isolation across LLM agents', 'Retriever accuracy must evolve dynamically alongside memory distribution changes']
- **validation**: ['Domain-specific memory sharing yields higher performance than global sharing', 'Excessive memory capacity leads to performance degradation due to noise or retrieval difficulty']

### technical_contributions

- **method_innovation**: Introduces continuous retriever training triggered by new memory addition and a dual quality control mechanism (Human Rubrics + LLM scoring)
- **architecture_design**: Proposes a three-layer architecture (Agent, Memory, Retriever) with a closed-loop feedback mechanism for memory evolution
- **experimental_validation**: Validated across 3 domains (Literature, Logic, Planning) with 9 agents, demonstrating significant improvements in ROUGE and BERTScore

### coverage_dimensions

- **form**: ['Vectorized Memory Pairs', 'Structured Rubric Scores']
- **function**: ['Open-domain Query Enhancement', 'Cross-agent Knowledge Reuse']
- **dynamics**: ['Memory Lifecycle Management (Generate-Score-Store)', 'Retriever Evolution and Adaptation']


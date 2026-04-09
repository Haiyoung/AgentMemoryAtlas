# 本体论分析报告 - 2505.20231

生成时间: 2026-04-08 10:13:33

## 分析结果

### paper_info

- **title**: MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi-Session LLM Agents
- **arxiv_id**: 2505.20231
- **year**: 2025

### new_concepts

- **memory_types**: ['Intent-Driven Memory', 'Multi-Session Task Memory']
- **memory_structures**: ['Structured QA Memory Unit (Intent + Slots)', 'Memory Bank']
- **memory_operations**: ['Intent-Aligned Retrieval', 'Missing-Slot Guided Filtering']
- **memory_carriers**: ['Dense Vector Index', 'LLM Context Window']

### new_relations

- **is_a**: [{'source': 'Intent-Driven Memory', 'target': 'Long-term Memory', 'description': 'Intent-Driven Memory is a specialized form of long-term memory focused on task goals.'}]
- **part_of**: [{'source': 'Missing-Slot Guided Filtering', 'target': 'Two-Stage Memory Selection', 'description': 'Filtering is the second stage of the MemGuide selection process.'}]
- **related_to**: [{'source': 'Intent Hypothesis', 'target': 'Missing Slot Identification', 'description': 'Intent hypothesis generation guides the identification of information gaps.'}]

### new_axioms

- **theoretical**: ['Memory retrieval effectiveness is determined by intent alignment and information gaps rather than semantic similarity alone.', 'Cross-session task tracking requires structured memory units linking intents to slot facts.']
- **validation**: ['Intent alignment improves retrieval recall by 7.7% compared to standard RAG.', 'Slot-guided filtering reduces dialogue turns by up to 47% while maintaining 99% task success rate.']

### technical_contributions

- **method_innovation**: Proposes a two-stage memory selection mechanism combining intent-aligned retrieval with missing-slot guided filtering.
- **architecture_design**: Designs the MemGuide framework integrating Intent Hypothesis Generation, CoT-based Slot Gap Identification, and Fine-tuned Filter Re-ranking.
- **experimental_validation**: Establishes the MS-TOD benchmark and validates performance across multiple LLM backbones with 99% success rate.

### coverage_dimensions

- **form**: ['Structured QA Representation', 'Vector Embeddings']
- **function**: ['Goal-Oriented Task Completion', 'Cross-Session Long-Term Tracking']
- **dynamics**: ['Memory Selection Lifecycle', 'Information Gap Resolution']


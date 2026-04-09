# 本体论分析报告 - 2512.02425

生成时间: 2026-04-09 11:32:00

## 分析结果

### paper_info

- **title**: WorldMM: Dynamic Multimodal Memory Agent for Long Video Reasoning
- **arxiv_id**: 2512.02425
- **year**: 2025

### new_concepts

- **memory_types**: ['Episodic Memory', 'Semantic Memory', 'Visual Memory']
- **memory_structures**: ['Multi-temporal Granularity Index', 'External Vector Database']
- **memory_operations**: ['Adaptive Retrieval', 'Iterative Retrieval Stop', 'Memory Construction']
- **memory_carriers**: ['Video Frames', 'Text Summaries', 'Time Segments']

### new_relations

- **is_a**: [{'source': 'Episodic Memory', 'target': 'Memory Type', 'description': 'Stores multi-granularity factual events indexed by time'}, {'source': 'Semantic Memory', 'target': 'Memory Type', 'description': 'Stores high-level conceptual knowledge updated from video'}, {'source': 'Visual Memory', 'target': 'Memory Type', 'description': 'Stores raw scene detail information to prevent text abstraction loss'}]
- **part_of**: [{'source': 'Adaptive Retrieval Agent', 'target': 'WorldMM Architecture', 'description': 'Core component responsible for dynamic memory source selection'}, {'source': 'Memory Construction Module', 'target': 'WorldMM Architecture', 'description': 'Pre-processing stage transforming video into memory stores'}]
- **related_to**: [{'source': 'User Query', 'target': 'Memory Source Selection', 'description': 'Query content dictates the choice of memory type and temporal granularity'}, {'source': 'Visual Memory', 'target': 'Text Summaries', 'description': 'Complementary relationship ensuring visual details are not lost in text abstraction'}]

### new_axioms

- **theoretical**: ['Dynamic multimodal memory enhances long video reasoning capability beyond text-only summaries', 'Adaptive retrieval based on information sufficiency optimizes context window usage compared to fixed strategies']
- **validation**: ['WorldMM achieves an average 8.4% performance improvement over SOTA on five long-video QA benchmarks', 'Retrieving fewer relevant memories reduces input tokens while maintaining or improving accuracy']

### technical_contributions

- **method_innovation**: Proposed three complementary memory types (Episodic, Semantic, Visual) with an adaptive retrieval agent that dynamically selects memory sources and temporal granularity based on query needs.
- **architecture_design**: Two-stage architecture comprising Memory Construction (video to memory transformation) and Memory Retrieval (iterative agent with sufficiency check loop).
- **experimental_validation**: Validated on five long-video question answering benchmarks showing significant improvement over baseline methods with reduced token consumption.

### coverage_dimensions

- **form**: ['Multi-modal Representation', 'Structured Memory Indexing']
- **function**: ['Long Video Question Answering', 'Context Retention']
- **dynamics**: ['Iterative Retrieval Lifecycle', 'Adaptive Stop Mechanism']


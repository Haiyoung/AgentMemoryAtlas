# 本体论分析报告 - 2305.13304

生成时间: 2026-04-06 23:43:02

## 分析结果

### paper_info

- **title**: RecurrentGPT: Interactive Generation of (Arbitrarily) Long Text
- **arxiv_id**: 2305.13304
- **year**: 2025

### new_concepts

- **memory_types**: ['Long-term Memory', 'Short-term Memory']
- **memory_structures**: ['Vector Database Storage', 'Natural Language Summary Buffer']
- **memory_operations**: ['Semantic Retrieval', 'State Summarization', 'Plan Generation']
- **memory_carriers**: ['Natural Language Text', 'Vector Embeddings']

### new_relations

- **is_a**: [{'source': 'Long-term Memory', 'target': 'Memory Type', 'description': 'Stores historical content via vector database for long-range coherence'}, {'source': 'Short-term Memory', 'target': 'Memory Type', 'description': 'Stores recent step summaries for immediate context'}]
- **part_of**: [{'source': 'Short-term Memory', 'target': 'Generation Context', 'description': 'Short-term memory is integrated into the prompt context'}, {'source': 'Long-term Memory', 'target': 'Generation Context', 'description': 'Retrieved long-term memory is integrated into the prompt context'}]
- **related_to**: [{'source': 'Plan', 'target': 'Content Generation', 'description': 'The plan guides the generation of the current paragraph'}, {'source': 'Memory Mechanism', 'target': 'Text Coherence', 'description': 'Memory mechanisms directly influence the coherence of long text'}]

### new_axioms

- **theoretical**: ['LLM computational states can be externalized and managed as natural language', 'RNN recurrent mechanisms can be simulated via prompt engineering without model training']
- **validation**: ['Ablation of memory components significantly reduces text coherence', 'Generation quality scales with the capability of the base LLM model']

### technical_contributions

- **method_innovation**: Simulates RNN/LSTM recurrent computation using prompt engineering and external memory, enabling infinite length generation without fine-tuning.
- **architecture_design**: A recurrent workflow comprising content generation, plan generation, and memory update loops, utilizing VectorDB for long-term storage and natural language for state representation.
- **experimental_validation**: Conducted human pairwise evaluations across 6 novel genres, demonstrating significant superiority in interestingness and coherence compared to sliding window and hierarchical baselines.

### coverage_dimensions

- **form**: ['Explicit Natural Language State Representation', 'Vectorized Historical Content Indexing']
- **function**: ['Arbitrary Length Text Generation', 'Interactive Human-AI Collaboration']
- **dynamics**: ['Iterative Memory Update and Retrieval', 'Dynamic Plan Adjustment and Execution']


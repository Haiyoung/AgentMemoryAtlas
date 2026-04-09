# 本体论分析报告 - 2512.14244

生成时间: 2026-04-09 13:35:05

## 分析结果

### paper_info

- **title**: From Context to EDUs: Faithful and Structured Context Compression via Elementary Discourse Unit Decomposition
- **arxiv_id**: 2512.14244
- **year**: 2025

### new_concepts

- **memory_types**: ['EDU-based Context Memory', 'Structured Discourse Memory']
- **memory_structures**: ['Elementary Discourse Unit (EDU) Tree', 'Query-Relevant Sub-Tree']
- **memory_operations**: ['EDU Decomposition', 'Sub-Tree Ranking', 'Tree-to-Text Linearization']
- **memory_carriers**: ['Source Index Anchored EDU Nodes', 'Compressed Token Sequence']

### new_relations

- **is_a**: [{'source': 'Elementary Discourse Unit', 'target': 'Atomic Context Unit', 'description': 'EDU is defined as the minimal semantic unit for context memory representation'}]
- **part_of**: [{'source': 'EDU Node', 'target': 'Structural Relationship Tree', 'description': 'Individual EDUs constitute the nodes within the hierarchical discourse tree'}]
- **related_to**: [{'source': 'User Query', 'target': 'Selected Sub-Tree', 'description': 'The query guides the ranking and selection of relevant EDU sub-trees for compression'}]

### new_axioms

- **theoretical**: ['Structure-then-Select preserves semantic fidelity better than token-level deletion', 'Explicit structural representation reduces hallucination compared to implicit encoding']
- **validation**: ['High EDU structure prediction accuracy correlates with improved downstream task performance', 'Explicit anchoring ensures traceability and reduces information loss during compression']

### technical_contributions

- **method_innovation**: Proposes a 'Structure-then-Select' compression paradigm using RST-based EDU decomposition instead of token-level pruning
- **architecture_design**: Designs an EDU-based Context Compressor comprising LingoEDU parser, lightweight ranking module, and linearization module
- **experimental_validation**: Validates on StructBench dataset showing SOTA structure prediction and cost reduction compared to frontier LLMs

### coverage_dimensions

- **form**: ['Hierarchical Tree Representation', 'Linearized Text Sequence']
- **function**: ['Token Cost Reduction', 'Semantic Faithfulness Preservation', 'Noise Elimination']
- **dynamics**: ['Context Parsing (Creation)', 'Relevance Ranking (Update/Selection)', 'Context Reconstruction (Usage)']


# 本体论分析报告 - 2510.02375

生成时间: 2026-04-09 00:03:30

## 分析结果

### paper_info

- **title**: Pretraining with hierarchical memories: separating long-tail and common knowledge
- **arxiv_id**: 2510.02375
- **year**: 2025

### new_concepts

- **memory_types**: ['Parametric Memory', 'Long-tail Knowledge Memory', 'Common Knowledge Memory']
- **memory_structures**: ['Hierarchical Memory Bank', 'Feed-Forward Memory Blocks']
- **memory_operations**: ['Context-dependent Memory Block Fetching', 'Parameter Injection']
- **memory_carriers**: ['Transformer Parameters', 'Anchor Model Parameters']

### new_relations

- **is_a**: [{'source': 'Hierarchical Memory Bank', 'target': 'Parametric Memory', 'description': 'The memory bank is a specific implementation of parametric memory storing knowledge as weights'}]
- **part_of**: [{'source': 'Feed-Forward Memory Blocks', 'target': 'Hierarchical Memory Bank', 'description': 'Small memory blocks constitute the larger hierarchical bank structure'}]
- **related_to**: [{'source': 'Anchor Model', 'target': 'Common Knowledge', 'description': 'The anchor model is primarily responsible for storing common knowledge and reasoning capabilities'}, {'source': 'Memory Bank', 'target': 'Long-tail Knowledge', 'description': 'The memory bank is specialized for storing infrequent long-tail facts'}]

### new_axioms

- **theoretical**: ['Knowledge and reasoning capabilities can be decoupled at the parameter level within neural networks', 'Long-tail knowledge can be stored externally in parameters without retraining the main anchor model']
- **validation**: ['A 160M model augmented with 18M memory parameters performs comparably to a dense model with 2x parameters', 'Long-tail knowledge accuracy improves significantly (e.g., 17% to 83%) with hierarchical memory augmentation']

### technical_contributions

- **method_innovation**: Proposes Hierarchical Feed-Forward Memories to separate long-tail and common knowledge during pretraining
- **architecture_design**: Designs an Anchor Model + Hierarchical Memory Bank architecture with context-dependent parameter fetching
- **experimental_validation**: Validates on trillion token scale pretraining demonstrating improved parameter efficiency and long-tail retention

### coverage_dimensions

- **form**: ['Structured Parameter Blocks', 'Hierarchical Organization of Weights']
- **function**: ['Knowledge Separation', 'Parameter Efficiency Optimization', 'Edge Device Deployment Support']
- **dynamics**: ['Dynamic Memory Fetching during Inference', 'Post-hoc Memory Addition', 'Lifecycle Management of Memory Blocks']


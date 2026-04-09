# 本体论分析报告 - 2508.19236

生成时间: 2026-04-08 18:46:08

## 分析结果

### paper_info

- **title**: MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation
- **arxiv_id**: 2508.19236
- **year**: 2025

### new_concepts

- **memory_types**: ['Perceptual Memory', 'Cognitive Memory', 'Working Memory', 'Perceptual-Cognitive Memory']
- **memory_structures**: ['Perceptual-Cognitive Memory Bank (PCMB)', 'Dual-stream Memory Structure']
- **memory_operations**: ['Cross-Attention Retrieval', 'Memory Consolidation', 'Gated Fusion', 'Token Merging']
- **memory_carriers**: ['Perceptual Tokens', 'Cognitive Tokens', 'RGB Observation Frames']

### new_relations

- **is_a**: [{'source': 'Perceptual-Cognitive Memory', 'target': 'Temporal Memory Mechanism', 'description': 'A specialized memory mechanism for VLA models handling temporal dependencies'}]
- **part_of**: [{'source': 'PCMB', 'target': 'MemoryVLA Architecture', 'description': 'The core memory storage component within the MemoryVLA framework'}, {'source': 'Perceptual Tokens', 'target': 'Working Memory', 'description': 'Fine-grained visual details stored in short-term working memory'}]
- **related_to**: [{'source': 'Memory Consolidation', 'target': 'Memory Capacity Control', 'description': 'Consolidation strategy directly manages memory bank size to prevent explosion'}]

### new_axioms

- **theoretical**: ['Human memory mechanisms (Working + Hippocampus) inspire effective robotic memory design', 'Separating perceptual details from semantic cognition improves information integrity in long-horizon tasks']
- **validation**: ['Dual-stream memory achieves higher success rates than single-stream alternatives', 'Token merging consolidation outperforms FIFO strategies in retaining relevant history']

### technical_contributions

- **method_innovation**: Introduces dual-stream memory storage and dynamic token merging consolidation strategy.
- **architecture_design**: End-to-end Cognition-Memory-Action framework with Gated Fusion and Diffusion Transformer Action Expert.
- **experimental_validation**: Comprehensive validation on 6 benchmarks, 3 robots, 150+ tasks showing SOTA performance with minimal latency overhead.

### coverage_dimensions

- **form**: ['Token-based Structured Representation', 'Time-step Positional Encoding']
- **function**: ['Long-horizon Robotic Manipulation', 'Temporal Dependency Modeling', 'OOD Generalization']
- **dynamics**: ['Memory Lifecycle Management (Store-Retrieve-Consolidate)', 'Real-time Inference Dynamics']


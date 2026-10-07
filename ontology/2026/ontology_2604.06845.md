# 本体论分析报告 - 2604.06845

生成时间: 2026-04-12 22:46:10

## 分析结果

### paper_info

- **title**: HingeMem: Boundary Guided Long-Term Memory with Query Adaptive Retrieval for Scalable Dialogues
- **arxiv_id**: 2604.06845
- **year**: 2025

### new_concepts

- **memory_types**: ['Boundary Guided Long-Term Memory', 'Scalable Dialogue Memory']
- **memory_structures**: ['Hyperedge Index Structure (Person/Time/Location/Topic)', 'Event-Boundary Based Memory Segments']
- **memory_operations**: ['Boundary Extraction', 'Query Adaptive Retrieval', 'Retrieval Planning (What/How Much)']
- **memory_carriers**: ['Dialogue Text', 'Super-edge Index Interface']

### new_relations

- **is_a**: [{'source': 'Boundary Guided Long-Term Memory', 'target': 'Long-Term Memory', 'description': 'A specialized memory type for managing long-context dialogues'}]
- **part_of**: [{'source': 'Memory Segment', 'target': 'Memory Structure', 'description': 'Segments constitute the stored content within the memory structure'}]
- **related_to**: [{'source': 'Event Boundary', 'target': 'Memory Write Trigger', 'description': 'Changes in four elements trigger the boundary and memory writing'}]

### new_axioms

- **theoretical**: ['Event Segmentation Theory operationalized as memory boundary construction mechanism', 'Changes in Person, Time, Location, or Topic define an event boundary']
- **validation**: ['Boundary guidance yields approximately 20% relative performance improvement', 'Adaptive retrieval reduces QA token cost by 68% compared to baselines']

### technical_contributions

- **method_innovation**: Integration of boundary-guided indexing with query-adaptive retrieval to overcome fixed Top-k limitations
- **architecture_design**: Two-stage framework comprising Boundary-Guided Memory Construction and Query-Adaptive Retrieval modules
- **experimental_validation**: Demonstrated effectiveness on LOCOMO dataset across multiple model scales with significant cost reduction

### coverage_dimensions

- **form**: ['Structured Representation via Hyperedge Index', 'Segmented Memory Fragments']
- **function**: ['Improved Retrieval Accuracy', 'Reduced Computational Token Cost']
- **dynamics**: ['Event-Driven Memory Lifecycle Management', 'Dynamic Retrieval Depth Control']


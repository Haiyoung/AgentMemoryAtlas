# 本体论分析报告 - 2507.06229

生成时间: 2026-04-08 11:38:28

## 分析结果

### paper_info

- **title**: Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving
- **arxiv_id**: 2507.06229
- **year**: 2025

### new_concepts

- **memory_types**: ['Cross-Domain Experience (跨域经验)', 'Planning Seeds (规划种子)', 'Feedback Diagnosis (反馈诊断)']
- **memory_structures**: ['Structured Knowledge Base (结构化知识库)', 'Agent KB Infrastructure (Agent KB 基础设施)']
- **memory_operations**: ['Hybrid Retrieval (混合检索)', 'Disagreement Gating (分歧门控)', 'Trajectory Aggregation (轨迹聚合)']
- **memory_carriers**: ['Agent Execution Trajectories (智能体执行轨迹)', 'Lightweight API Interface (轻量级 API 接口)']

### new_relations

- **is_a**: [{'source': 'Agent KB', 'target': 'Universal Memory Infrastructure', 'description': 'Agent KB is defined as a universal infrastructure enabling memory sharing across heterogeneous agent frameworks.'}, {'source': 'Planning Seeds', 'target': 'Cross-Domain Experience', 'description': 'Planning seeds are a specific subtype of cross-domain experience used for workflow guidance.'}]
- **part_of**: [{'source': 'Disagreement Gate', 'target': 'Hybrid Retrieval Engine', 'description': 'The disagreement gate is a functional component within the retrieval process designed to filter interfering knowledge.'}]
- **related_to**: [{'source': 'Heterogeneous Agent Frameworks', 'target': 'Structured Knowledge Base', 'description': 'Frameworks contribute trajectories to the KB and retrieve knowledge from it to enhance reasoning.'}]

### new_axioms

- **theoretical**: ['Cross-framework collective intelligence can be achieved through a shared memory infrastructure without model re-training.', 'Experience sharing effectively avoids repeated errors by leveraging cross-domain knowledge.']
- **validation**: ['Hybrid retrieval mechanisms significantly improve agent performance compared to baseline frameworks (e.g., +18.7pp in pass@3).', 'Automatically generated experiences are comparable in quality to human-curated ones for agent enhancement.']

### technical_contributions

- **method_innovation**: Proposes a Hybrid Retrieval mechanism (Planning Seeds + Feedback Diagnosis) and a Disagreement Gate to prevent knowledge interference during reasoning.
- **architecture_design**: Designs Agent KB as a lightweight API service that aggregates trajectories into a structured KB, compatible with heterogeneous frameworks like smolagents and OpenHands.
- **experimental_validation**: Validated on benchmarks including GAIA, SWE-bench, GPQA, and Humanity's Last Exam, demonstrating significant performance gains across multiple agent frameworks.

### coverage_dimensions

- **form**: ['Structured Knowledge Entries', 'Execution Trajectories Representation']
- **function**: ['Cross-Framework Experience Sharing', 'Error Avoidance & Performance Enhancement']
- **dynamics**: ['Trajectory Aggregation (Write Phase)', 'Hybrid Retrieval & Gating (Read/Filter Phase)']


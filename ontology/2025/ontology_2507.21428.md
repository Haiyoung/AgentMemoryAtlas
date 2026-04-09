# 本体论分析报告 - 2507.21428

生成时间: 2026-04-08 12:14:43

## 分析结果

### paper_info

- **title**: MemTool: Optimizing Short-Term Memory Management for Dynamic Tool Calling in LLM Agent Multi-Turn Conversations
- **arxiv_id**: 2507.21428
- **year**: 2025

### new_concepts

- **memory_types**: ['Short-Term Tool Memory', 'Autonomous Memory', 'Workflow Memory']
- **memory_structures**: ['Tool Context Window', 'Dynamic Tool Pool']
- **memory_operations**: ['Tool Search', 'Tool Remove', 'Context Count Check']
- **memory_carriers**: ['MCP Server Tool List', 'LLM Context Window']

### new_relations

- **is_a**: [{'source': 'Autonomous Mode', 'target': 'Memory Management Mode', 'description': 'Agent fully controls memory operations'}, {'source': 'Workflow Mode', 'target': 'Memory Management Mode', 'description': 'System deterministically controls memory operations'}, {'source': 'Hybrid Mode', 'target': 'Memory Management Mode', 'description': 'System removes tools, Agent searches tools'}]
- **part_of**: [{'source': 'Tool Context', 'target': 'LLM Input Context', 'description': 'Tools occupy a portion of the context window'}, {'source': 'Memory Management Module', 'target': 'LLM Agent Architecture', 'description': 'Module manages tool lifecycle within agent'}]
- **related_to**: [{'source': 'Model Reasoning Capability', 'target': 'Management Mode Selection', 'description': 'Stronger models support autonomous mode'}, {'source': 'Tool Removal Rate', 'target': 'Context Overflow Risk', 'description': 'Higher removal rate reduces overflow risk'}]

### new_axioms

- **theoretical**: ['Tool count must remain within API limit (e.g., 128) to prevent failure', 'Small models lack reliability for autonomous tool context management']
- **validation**: ['Hybrid mode achieves >90% removal rate with high task completion on reasoning models', 'System prompt must include dynamic tool count variable for effective removal']

### technical_contributions

- **method_innovation**: Proposed explicit tool removal mechanism and three management modes (Autonomous, Workflow, Hybrid) for short-term memory.
- **architecture_design**: Designed a Memory Management Module that intercepts tool search and remove operations based on context count.
- **experimental_validation**: Validated on 13+ SOTA models using ScaleMCP benchmark, measuring removal rate, residual tools, and task completion.

### coverage_dimensions

- **form**: ['Structured Tool List Representation', 'Context Window Counting']
- **function**: ['Prevent API Context Overflow', 'Maintain Multi-Turn Task Completion']
- **dynamics**: ['Dynamic Tool Addition (Search)', 'Dynamic Tool Removal (Prune)', 'Lifecycle Monitoring']


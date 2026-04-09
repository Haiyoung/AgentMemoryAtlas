# 本体论分析报告 - 2403.17134

生成时间: 2026-04-07 09:30:47

## 分析结果

### paper_info

- **title**: RepairAgent: An Autonomous, LLM-Based Agent for Program Repair
- **arxiv_id**: 2403.17134
- **year**: 2025

### new_concepts

- **memory_types**: ['Repair State Memory', 'Tool Feedback Memory', 'Code Context Memory']
- **memory_structures**: ['Finite State Machine (FSM) Flow', 'Dynamic Prompt Context Buffer']
- **memory_operations**: ['State Transition', 'Tool Invocation', 'Context Update']
- **memory_carriers**: ['LLM Context Window', 'Execution Logs', 'Source Code Repository']

### new_relations

- **is_a**: [{'source': 'RepairAgent', 'target': 'Autonomous LLM Agent', 'description': 'RepairAgent is a specialized instantiation of an autonomous agent designed specifically for program repair tasks'}]
- **part_of**: [{'source': 'FSM Controller', 'target': 'RepairAgent Architecture', 'description': "The FSM module is a core component governing the agent's decision logic and flow control"}, {'source': 'Tool Set', 'target': 'RepairAgent Architecture', 'description': "External tools such as compile, test, and search are integrated parts of the agent's capability"}]
- **related_to**: [{'source': 'Tool Feedback', 'target': 'Dynamic Prompt', 'description': "Execution results from tools are fed back into the prompt to guide the agent's next steps"}, {'source': 'Bug Fix', 'target': 'Test Case', 'description': 'A valid fix is ontologically defined by its ability to pass the associated test cases'}]

### new_axioms

- **theoretical**: ['Autonomous planning surpasses fixed feedback loops in flexibility for complex repair tasks', 'FSM guidance constrains agent actions to valid repair phases reducing hallucination and invalid states']
- **validation**: ['Agent fixes unique bugs compared to prior techniques (39 unique fixes on Defects4J)', 'Token cost is a measurable constraint for autonomy (avg 270k tokens/bug)']

### technical_contributions

- **method_innovation**: Integration of Finite State Machine (FSM) with LLM for autonomous decision making in Automated Program Repair (APR)
- **architecture_design**: Modular architecture comprising LLM Core, Tool Interface, and FSM-based State Controller with Dynamic Prompting
- **experimental_validation**: Evaluation on Defects4J benchmark demonstrating 164 fixed bugs and cost-benefit analysis of token usage

### coverage_dimensions

- **form**: ['Structured FSM States', 'Dynamic Prompt Templates']
- **function**: ['Automated Program Repair', 'Bug Localization and Verification']
- **dynamics**: ['Iterative Repair Loop', 'State Transition Lifecycle']


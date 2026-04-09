# 本体论分析报告 - 2504.06821

生成时间: 2026-04-07 19:01:59

## 分析结果

### paper_info

- **title**: Inducing Programmatic Skills for Agentic Tasks
- **arxiv_id**: 2504.06821
- **year**: 2025

### new_concepts

- **memory_types**: ['Programmatic Skills (Procedural Memory)', 'Text-based Skills (Declarative Memory)']
- **memory_structures**: ['Verified Skill Library', 'Action Trajectory Buffer']
- **memory_operations**: ['Skill Induction (Encoding)', 'Program Verification (Validation)', 'Skill Reuse (Retrieval & Execution)']
- **memory_carriers**: ['Executable Code Snippets', 'Web Interaction Traces']

### new_relations

- **is_a**: [{'source': 'Programmatic Skill', 'target': 'Agent Memory Entry', 'description': 'Programmatic skills are a specific type of storable memory entry for agents.'}]
- **part_of**: [{'source': 'Verification Module', 'target': 'ASI Framework', 'description': 'The verification module is a core component of the Agent Skill Induction framework.'}]
- **related_to**: [{'source': 'Action Trajectory', 'target': 'Programmatic Skill', 'description': 'Action trajectories serve as the raw data source for inducing programmatic skills.'}]

### new_axioms

- **theoretical**: ['Executability implies Verifiability: Programmatic representations allow for automatic correctness validation unlike text.', 'Composability enables Generalization: Modular programmatic skills can be combined to solve complex, unseen tasks.']
- **validation**: ['Verified Skills reduce Hallucination: Skills passing execution tests yield higher task success rates than unverified text prompts.', 'Online Induction mitigates Distribution Shift: Dynamically induced skills adapt better to test-time environments than offline trained policies.']

### technical_contributions

- **method_innovation**: Proposes Agent Skill Induction (ASI), a method to convert raw action trajectories into verified, reusable executable programs online.
- **architecture_design**: Designs a closed-loop architecture comprising Trajectory Generation, Skill Induction, Automated Verification, and Library-based Reuse.
- **experimental_validation**: Demonstrates 23.5% success rate improvement over static baselines and 11.3% over text-skill baselines on the WebArena benchmark.

### coverage_dimensions

- **form**: ['Structured Code Representation', 'Hierarchical Skill Abstraction']
- **function**: ['Web Navigation Automation', 'Cross-domain Skill Transfer']
- **dynamics**: ['Online Lifecycle Management (Generate-Verify-Store)', 'Adaptive Skill Updating']


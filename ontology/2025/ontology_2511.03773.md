# 本体论分析报告 - 2511.03773

生成时间: 2026-04-09 08:14:44

## 分析结果

### paper_info

- **title**: Scaling Agent Learning via Experience Synthesis
- **arxiv_id**: 2511.03773
- **year**: 2025

### new_concepts

- **memory_types**: ['Synthetic Experience', 'Abstract State', 'Reasoning-based Feedback']
- **memory_structures**: ['Hybrid Replay Buffer', 'Experience Model']
- **memory_operations**: ['Experience Synthesis', 'Adaptive Task Generation', 'Sim-to-Real Transfer']
- **memory_carriers**: ['Reasoning Model', 'Replay Buffer']

### new_relations

- **is_a**: [{'source': 'Synthetic Experience', 'target': 'Training Data', 'description': 'Synthesized trajectories are treated as valid training data for RL agents'}]
- **part_of**: [{'source': 'Experience Model', 'target': 'DreamGym Framework', 'description': 'Core component responsible for distilling environment dynamics and generating transitions'}]
- **related_to**: [{'source': 'Experience Synthesis', 'target': 'Real Environment Interaction', 'description': 'Substitutes expensive real interactions with reasoning-based synthesis to reduce cost'}]

### new_axioms

- **theoretical**: ['Environment dynamics can be distilled into a reasoning-based experience model', 'Synthetic experiences can effectively substitute real rollouts for RL training without significant performance loss']
- **validation**: ['Performance on WebArena improves >30% using synthetic experience compared to baselines', 'Policies trained on pure synthetic experience can successfully transfer to real environments (Sim-to-Real)']

### technical_contributions

- **method_innovation**: Introduces Experience Synthesis via reasoning models to generate consistent state transitions and rewards, replacing costly real environment rollouts.
- **architecture_design**: Designs DreamGym framework integrating an Agent, Reasoning-based Experience Model, Hybrid Replay Buffer, and Adaptive Task Generator.
- **experimental_validation**: Demonstrates >30% performance gain on WebArena and validates Sim-to-Real transfer capability with reduced real-world interaction costs.

### coverage_dimensions

- **form**: ['Structured Experience Trajectories', 'Abstract State Representations']
- **function**: ['RL Training Cost Reduction', 'Sample Efficiency Improvement']
- **dynamics**: ['Offline Initialization to Online Enrichment', 'Synthesis to Real-World Transfer Lifecycle']


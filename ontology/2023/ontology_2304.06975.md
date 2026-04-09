# 本体论分析报告 - 2304.06975

生成时间: 2026-04-06 23:22:11

## 分析结果

### paper_info

- **title**: HuaTuo: Tuning LLaMA Model with Chinese Medical Knowledge
- **arxiv_id**: 2304.06975
- **year**: 2025

### new_concepts

- **memory_types**: ['医疗指令数据 (Medical Instruction Data)', '知识图谱实例 (Knowledge Graph Instances)']
- **memory_structures**: ['SUS 评估体系 (Safety-Usability-Smoothness Framework)', '问答对结构 (QA Pairs Structure)']
- **memory_operations**: ['知识采样 (Knowledge Sampling)', '指令微调 (Instruction Tuning)', 'API 生成清洗 (API Generation & Cleaning)']
- **memory_carriers**: ['LLaMA-7B 模型权重 (LLaMA-7B Weights)', '中国医学知识图谱 (CMeKG)']

### new_relations

- **is_a**: [{'source': 'HuaTuo 模型', 'target': '中文医疗大语言模型', 'description': 'HuaTuo 是专门针对中文医疗领域微调的垂直大模型'}]
- **part_of**: [{'source': 'SUS 指标', 'target': '医疗模型评估体系', 'description': '安全性、可用性、流畅度是评估医疗模型的核心组成部分'}]
- **related_to**: [{'source': 'CMeKG', 'target': '指令微调数据集', 'description': '知识图谱是构建高质量医疗指令数据的基础来源'}]

### new_axioms

- **theoretical**: ['知识图谱注入可显著提升大模型的领域专业性', '医疗场景下安全性与可用性存在权衡关系 (Trade-off)']
- **validation**: ['医学专家人工评估是验证医疗模型安全性的必要公理', 'SUS 评分优于基线模型证明领域适配成功']

### technical_contributions

- **method_innovation**: 提出基于知识图谱 (CMeKG) 采样生成指令数据并结合监督微调 (SFT) 的中文医疗适配方法
- **architecture_design**: 基于 LLaMA-7B Decoder-only 架构，设计数据构建与微调两阶段流程
- **experimental_validation**: 引入医学背景专家进行人工评估，建立 SUS(安全性/可用性/流畅度) 三维指标体系

### coverage_dimensions

- **form**: ['结构化知识图谱表示', '非结构化指令文本表示']
- **function**: ['医疗问答服务', '安全性与专业性平衡']
- **dynamics**: ['知识数据构建生命周期', '模型微调与推理生命周期']


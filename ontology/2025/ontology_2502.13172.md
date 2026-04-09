# 本体论分析报告 - 2502.13172

生成时间: 2026-04-07 18:01:29

## 分析结果

### paper_info

- **title**: Unveiling Privacy Risks in LLM Agent Memory
- **arxiv_id**: 2502.13172
- **year**: 2025

### new_concepts

- **memory_types**: ['交互历史记忆 (Interaction History Memory)', '敏感查询记忆 (Sensitive Query Memory)']
- **memory_structures**: ['检索增强记忆存储 (Retrieval-Augmented Memory Store)', '基于编辑距离的索引 (Edit-Distance Based Index)']
- **memory_operations**: ['记忆提取攻击 (Memory Extraction Attack)', '检索操纵 (Retrieval Manipulation)']
- **memory_carriers**: ['LLM 上下文窗口 (LLM Context Window)', '外部记忆数据库 (External Memory Database)']

### new_relations

- **is_a**: [{'source': 'MEXTRA', 'target': '黑盒提示词攻击 (Black-box Prompt Attack)', 'description': 'MEXTRA 被定义为一种针对记忆模块的特定黑盒攻击方法'}, {'source': '记忆模块 (Memory Module)', 'target': 'LLM 代理组件 (LLM Agent Component)', 'description': '记忆模块是 LLM 代理架构中用于存储历史交互的核心组成部分'}]
- **part_of**: [{'source': '查询 - 解决方案对 (Query-Solution Pair)', 'target': '记忆内容 (Memory Content)', 'description': '用户交互对构成了记忆模块存储的基本数据单元'}]
- **related_to**: [{'source': '检索机制 (Retrieval Mechanism)', 'target': '隐私泄露风险 (Privacy Leakage Risk)', 'description': '不同的检索机制（如编辑距离 vs 余弦相似度）直接影响隐私泄露的严重程度'}]

### new_axioms

- **theoretical**: ['记忆容量与泄露绝对数量呈正相关 (Memory capacity is positively correlated with leakage volume)', '基于格式的检索比语义检索更易受提示词操纵 (Format-based retrieval is more vulnerable to prompt manipulation than semantic retrieval)']
- **validation**: ['提取数量 (EN) 和完全提取率 (CER) 可有效量化隐私风险 (EN and CER effectively quantify privacy risk)', '检索深度 (k 值) 增加会加剧记忆泄露 (Increasing retrieval depth k exacerbates memory leakage)']

### technical_contributions

- **method_innovation**: 提出 MEXTRA 框架，利用定位 (Localization) 与对齐 (Alignment) 提示词自动化生成攻击查询，无需模型权重即可实施攻击
- **architecture_design**: 设计包含攻击者、提示生成器、目标 Agent 及记忆模块的黑盒攻击架构，模拟真实 API 交互场景
- **experimental_validation**: 在医疗 (MIMIC-III) 和网购 (Webshop) 场景下进行多模型、多检索机制的消融实验，验证了配置参数对风险的影响

### coverage_dimensions

- **form**: ['结构化提示词表示 (Structured Prompt Representation)', '查询 - 解决方案对格式 (Query-Solution Pair Format)']
- **function**: ['隐私风险评估 (Privacy Risk Assessment)', '敏感数据提取 (Sensitive Data Extraction)']
- **dynamics**: ['记忆检索生命周期 (Memory Retrieval Lifecycle)', '攻击 - 防御交互动态 (Attack-Defense Interaction Dynamics)']


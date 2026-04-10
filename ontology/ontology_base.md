---
title: Agent Memory 领域本体论
description: Agent Memory 领域本体论模型 v1.0
current_version: '1.0'
based_on_version: '0'
created_at: 2026-04-10
updated_at: '2026-04-10T00:00:00'
papers_covered: 146
---

# Agent Memory 领域本体论 v1.0

## 一、本体论核心基础

Agent Memory 本体遵循"三维正交分类 + 类层级"双轨架构。

### 1.1 三维正交分类

每个记忆概念由三个维度的坐标唯一确定：

| 载体维度 (Carrier) | 功能维度 (Function) | 动态维度 (Dynamic) |
|--------------------|--------------------|--------------------|
| Token-level | Factual | Formation |
| Parametric | Experiential | Evolution |
| External | Procedural | Retrieval |
| Latent | Working | Forgetting |
| | Episodic | Reflection |
| | Semantic | Association |

### 1.2 顶层核心类（8个）

| 顶层类 | 核心定位 |
|--------|---------|
| Agent | 记忆主体 |
| Memory | 记忆载体（含参数/外部/Token） |
| MemorySystem | 记忆管理架构 |
| MemoryEvent | 记忆触发源 |
| MemoryOperation | 记忆操作行为 |
| Context | 记忆关联场景 |
| Entity | 记忆关联对象（含关系） |
| Policy | 记忆操作规则（含安全策略） |

### 1.3 核心原则

- 语义唯一性：每个概念在模型中具有唯一的语义标识
- 层级清晰性：类→子类层级与三维分类正交共存
- 工程适配性：概念设计兼顾理论完整性与工程可实现性
- 可扩展性：新增概念可归入现有维度或触发维度扩展

---

## 二、核心公理体系

### 2.1 存在公理

- 每个记忆实例必须占据至少一个载体维度位置（Token-level/Parametric/External/Latent）
- 没有无来源的记忆：每条记忆必须关联至少一个 MemoryEvent

### 2.2 操作公理

- 检索必有索引：任何 MemoryRetrieval 操作必须有对应的 Index 结构
- 遗忘不可逆：MemoryForgetting 操作不产生可恢复的记忆副本
- 反思产生新知：MemoryReflection 操作必然产生至少一个新增概念实例

### 2.3 质量公理

- 记忆质量 = f(新鲜度, 一致性, 置信度)
- 质量维度作为 Memory 的属性而非独立类

### 2.4 安全公理

- 检索深度与隐私风险正相关（源自 2502.13172）
- 格式化检索比语义检索更易被攻击（源自 2502.13172）

### 2.5 演进公理

- 记忆随使用而强化：accessCount 增加 → importance 增加
- 记忆随时间而衰减：未访问 → importance 递减

---

## 三、概念关系网络

### 3.1 形式维度网络 (Forms)

包含 **322** 个概念，描述记忆的结构化表示形式。

核心子类群：

**Architecture/Framework** (14): 可逆 Transformer 架构, Minimalist Single-Core Architecture, Four-Layer Semantic Architecture, 时空语义系统, 模块化 AI 代理架构, 分层交互系统, SDM Activation Module, Agent Foundation Model Architecture
  ... 及其他 6 个概念
**Buffer/Pool** (9): Natural Language Summary Buffer, Replay Buffer for Offline RL, 备忘录存储, Historical Session Buffer, Action Trajectory Buffer, Dynamic Tool Pool, 经验池, STM Buffer
  ... 及其他 1 个概念
**Context Window** (23): Tool-Augmented Context Window, 滑动窗口上下文, Prompt Sequences, Prompt Context Window, Token Sequence Context, Dynamic Prompt Context Buffer, , Enhanced Prompt with Retrieved Context
  ... 及其他 15 个概念
**Graph/Tree Structure** (44): 知识三元组, Directed Weighted Graph, Hierarchical Community Tree, Dual-view Bipartite Graph, Query-Scene-Tool Interaction Graph, 外部知识图谱, 事实知识三元组, Hierarchical Aggregate Tree
  ... 及其他 36 个概念
**Index Structure** (16): Vector Index, LSH 向量索引表, 神经 API 检索索引, Vector Space Index, Self-Generated Graph Index, 海马体式索引, 原子索引映射, FAISS Vector Index for Video Semantics
  ... 及其他 8 个概念
**Memory Storage** (78): Memory Stream, 混合记忆架构, Structured Memory, Hierarchical Memory Architecture, 记忆原型, Hierarchical Memory Storage, Memory Strength Parameter, 三阶段记忆循环
  ... 及其他 70 个概念
**Network Layer/State** (12): Finite State Machine, Rule-based Decomposed Statements, Three-layer Hierarchical Structure, 代码库状态快照, Distilled Knowledge Statements, Interpolation Integration Layer, 持久化世界状态, Shared State Space
  ... 及其他 4 个概念
**Other Structure** (115): Hyper-network Weight Generator, GRU 隐藏状态, 高分辨率键值对, 自我提示库, SUS 评估体系, 问答对结构, 可学习令牌序列, 深度优先搜索决策树
  ... 及其他 107 个概念
**Vector/Embedding** (11): Perturbation Vector, API-Embedded Text Sequence, Vector Database Storage, 固定长度连续向量, Patch Embedding, 8-Vector Compressed Sequence, Intermediate Layer Embedding Slot, Vector-Text Dual Storage
  ... 及其他 3 个概念

### 3.2 功能维度网络 (Functions)

包含 **325** 个概念，描述记忆的功能定位。

核心功能群：

**Episodic Memory** (9): Episodic Memory, 情景记忆, Local Episodic Memory, Episodic Memory Graph, Episodic Simulation, Episodic Demonstration Memory
  ... 及其他 3 个概念
**Experiential Memory** (8): 经验记忆, Cross-Domain Experience, Experiential Knowledge, Early Experience, 结构化经验, 成功/失败轨迹经验
  ... 及其他 2 个概念
**Factual Memory** (5): 事实记忆, 结构化事实备忘录, 个性化事实知识, Externalized Factual Memory, 世界事实
**Long-Term Memory** (16): Long-Term Memory, 长期记忆, Long-term Memory, Long-term Reflection Memory, 神经生物学启发的长期记忆, 时间敏感长期记忆
  ... 及其他 10 个概念
**Other Memory Type** (233): Agentic Memory, Summarized Memory, User Profile Memory, 持久记忆, Hierarchical Memory, Query Memory
  ... 及其他 227 个概念
**Parametric Memory** (7): Parametric Memory, Parametric Factual Knowledge, 参数化记忆, Non-Parametric Continual Learning, Parametric Knowledge, 非参数化策略记忆
  ... 及其他 1 个概念
**Procedural Memory** (9): 程序记忆, Programmatic Skills, Procedural Skill Memory, 程序性记忆, 技能模式记忆, Procedural Memory
  ... 及其他 3 个概念
**Reflection Memory** (2): Reflection Memory, 反思经验
**Retrieval Memory** (4): 生成式检索记忆, MLP Memory, Retriever-Pretrained Memory, Implicit Retrieval Memory
**Semantic Memory** (13): Semantic Memory, 语义记忆, API 语义记忆, Global Semantic Memory, Semantic-Graph Hybrid Memory, Implicit Semantic Memory
  ... 及其他 7 个概念
**Sensory Memory** (4): 感官记忆, Sensory Memory, 感官情境记忆, SensoryMemory
**Short-Term Memory** (8): Short-Term Memory, Short-term Memory, Short-term Trajectory Memory, 短期记忆, Short-term Operation History, 短期注意力记忆
  ... 及其他 2 个概念
**Working Memory** (7): Working Memory, 工作记忆, Active Working Memory, 动态工作记忆, 动态上下文工作区, 短期工作记忆
  ... 及其他 1 个概念

### 3.3 动态维度网络 (Dynamics)

包含 **445** 个概念，描述记忆的生命周期操作。

核心操作群：

**Association** (8): In-Context Memory Integration, Relation-aware Linking, Context Integration, 概率插值集成, Parameter-Free Model Integration, 记忆整合
  ... 及其他 2 个概念
**Deduplication** (2): API 生成清洗, 语义去重
**Evolution (Update)** (42): 记忆巩固, Memory Update, Memory Consolidation, Update, 动态更新, Constraint-based Editing
  ... 及其他 36 个概念
**Forgetting** (10): Memory Decay, Summarize-and-Forget, 时间衰减, 权重衰减遗忘机制, Forget Operation, Forgetting Curve Decay
  ... 及其他 4 个概念
**Formation (Store/Write)** (16): 轨迹存储, MEM_WRITE, 可微分记忆读写, Read/Write Separation, Gated Write/Update, Overwrite Strategy
  ... 及其他 10 个概念
**Learning** (6): Collaborative Graph Learning, 强化学习路径选择, 约束生成, Database-driven Unlearning, Agentic Continual Pre-training, Post-training Alignment via SFT/RL
**Other Operation** (228): Conflict Resolution, 记忆增强, LFU 淘汰, Autonomous API Invocation, Result Injection & Continuation, Tool Usage Filtering
  ... 及其他 222 个概念
**Reflection** (15): 反思生成, Reflective Synthesis, Reflection Generation, 风险触发式自我反思, Multi-turn Reasoning, 推理困境检测
  ... 及其他 9 个概念
**Retrieval** (79): 记忆检索, Memory Retrieval, Semantic Retrieval, 语义检索, Similarity-based Retrieval, Hierarchical Retrieval
  ... 及其他 73 个概念
**Scoring/Ranking** (6): Importance Scoring, Personalized PageRank Propagation, Weighted Fusion Ranking, 记忆距离加权评分, 动态重要性记忆过滤, Sub-Tree Ranking
**Summarization** (33): State Summarization, 上下文编码压缩, LLM-driven Entity-Relation Extraction, 基于反馈的知识提取, Recursive Summary Aggregation, 记忆编码与压缩
  ... 及其他 27 个概念

---

## 四、跨维度整合网络

### 4.1 三维一体记忆模型

```
[Form] ←→ [Function] ←→ [Dynamics]
   ↑         ↑           ↑
结构化     目标导向     生命周期
表示       应用        管理
```

### 4.2 认知架构集成

- 感知层: 原始输入 → 记忆形成
- 记忆层: 结构化存储 ↔ 动态演化 ↔ 目标检索
- 推理层: 记忆检索 → 上下文合成 → 决策生成
- 行动层: 决策执行 → 经验反馈 → 记忆更新

---

## 五、记忆结构类型

共 **322** 个记忆结构概念，定义记忆的存储组织形式。

| 概念名称 | 来源论文数 | 来源论文 |
|---------|-----------|---------|
| Memory Stream | 3 | `2304.03442`, `2304.13343`, `2310.02172` |
| Vector Index (FAISS) | 2 | `2305.10250`, `2310.08560` |
| 混合记忆架构 (Hybrid Memory Architecture) | 2 | `2406.00057`, `2509.25911` |
| Structured Memory | 2 | `2508.04903`, `2510.21618` |
| Hierarchical Memory Architecture | 2 | `2509.12810`, `2511.13593` |
| Hyper-network Weight Generator | 1 | `2104.08164` |
| Perturbation Vector (Δθ) | 1 | `2104.08164` |
| GRU 隐藏状态 | 1 | `2207.07115` |
| 高分辨率键值对 (Key/Value) | 1 | `2207.07115` |
| 记忆原型 (Prototypes) | 1 | `2207.07115` |
| API-Embedded Text Sequence | 1 | `2302.04761` |
| Tool-Augmented Context Window | 1 | `2302.04761` |
| 滑动窗口上下文 (Sliding Window Context) | 1 | `2303.11366` |
| 自我提示库 (Self-Hint Repository) | 1 | `2303.11366` |
| SUS 评估体系 (Safety-Usability-Smoothness Framework) | 1 | `2304.06975` |
| 问答对结构 (QA Pairs Structure) | 1 | `2304.06975` |
| Hierarchical Memory Storage | 1 | `2305.10250` |
| Memory Strength Parameter | 1 | `2305.10250` |
| Vector Database Storage | 1 | `2305.13304` |
| Natural Language Summary Buffer | 1 | `2305.13304` |
| 知识三元组 (Knowledge Triplets ⟨参数 1, 关系，参数 2⟩) | 1 | `2305.14322` |
| LSH 向量索引表 (LSH Vector Index Table) | 1 | `2305.14322` |
| 固定长度连续向量 (Fixed-length Continuous Vectors) | 1 | `2307.06945` |
| 可学习令牌序列 (Learnable Token Sequence) | 1 | `2307.06945` |
| 深度优先搜索决策树 (DFSDT) | 1 | `2307.16789` |
| 神经 API 检索索引 (Neural API Retrieval Index) | 1 | `2307.16789` |
| 解决方案路径 (Solution Path) | 1 | `2307.16789` |
| Prompt Sequences | 1 | `2308.00352` |
| Structured Artifacts (PRD, Code) | 1 | `2308.00352` |
| Replay Buffer for Offline RL | 1 | `2308.02151` |
| Prompt Context Window | 1 | `2308.02151` |
| 备忘录存储 (Memo Store) | 1 | `2308.08239` |
| 三阶段记忆循环 (Three-Stage Memory Loop) | 1 | `2308.08239` |
| Vector Space Index | 1 | `2308.09597` |
| Token Sequence Context | 1 | `2308.09597` |
| Fine-tuned Parameter Space | 1 | `2308.09597` |
| Compressed Textual Summary | 1 | `2308.15022` |
| Session-based Memory State | 1 | `2308.15022` |
| Option-Action Hierarchy | 1 | `2310.02172` |
| Engram | 1 | `2310.03052` |
| Directed Weighted Graph | 1 | `2310.03052` |
| Queue Structure | 1 | `2310.03052` |
| Hierarchical Memory System | 1 | `2310.08560` |
| FIFO Message Queue | 1 | `2310.08560` |
| Finite State Machine (FSM) Flow | 1 | `2403.17134` |
| Dynamic Prompt Context Buffer | 1 | `2403.17134` |
| (Prompt, Answer) Pair | 1 | `2404.09982` |
| Enhanced Prompt with Retrieved Context | 1 | `2404.09982` |
| Self-Generated Graph Index | 1 | `2404.16130` |
| Hierarchical Community Tree | 1 | `2404.16130` |
| 知识图谱记忆结构 | 1 | `2405.14831` |
| 新皮层式存储 | 1 | `2405.14831` |
| 海马体式索引 | 1 | `2405.14831` |
| Dual-view Bipartite Graph | 1 | `2405.16089` |
| Query-Scene-Tool Interaction Graph | 1 | `2405.16089` |
| 外部知识图谱 (External Knowledge Graph) | 1 | `2405.19686` |
| 事实知识三元组 (Factual Knowledge Triples) | 1 | `2405.19686` |
| 结构化对话日志表 (Structured Conversation Log Table) | 1 | `2406.00057` |
| Hierarchical Aggregate Tree (HAT) | 1 | `2406.06124` |
| Summary-Leaf Node Structure | 1 | `2406.06124` |
| Causal-Temporal Graph | 1 | `2406.10996` |
| Linearized Event Timeline | 1 | `2406.10996` |
| 记忆存储池 (Memory Storage Pool) | 1 | `2407.01178` |
| 记忆编码器 (Memory Encoder) | 1 | `2407.01178` |
| 记忆检索器 (Memory Retriever) | 1 | `2407.01178` |
| 记忆解码器 (Memory Decoder) | 1 | `2407.01178` |
| 记忆 - 注意力融合模块 (Memory-Attention Fusion Module) | 1 | `2407.01178` |
| Knowledge Graph World Model | 1 | `2407.04363` |
| Entity-Relation-Entity Triple | 1 | `2407.04363` |
| 层级化记忆管理 (Hierarchical Memory Management) | 1 | `2407.06567` |
| 基于 Prompt 的策略存储 (Prompt-based Strategy Storage) | 1 | `2407.06567` |
| 可编辑记忆图 (Editable Memory Graph, EMG) | 1 | `2409.19401` |
| 三层分层图谱结构 (MTL/MSL/MGL) | 1 | `2409.19401` |
| 记忆图层 (Memory Graph Layer, MGL) | 1 | `2409.19401` |
| Null-Space Basis | 1 | `2410.02355` |
| Orthogonal Projection Matrix | 1 | `2410.02355` |
| 虚拟令牌词表 (Virtual Token Vocabulary) | 1 | `2410.03439` |
| 原子索引映射 (Atomic Index Mapping) | 1 | `2410.03439` |
| Context State (Vision + Plan) | 1 | `2410.08164` |
| Normalized Action Space (0-1000 Coordinates) | 1 | `2410.08164` |
| Feedback-Integrated Documentation | 1 | `2410.08197` |
| Trial-and-Error Execution Logs | 1 | `2410.08197` |
| Summary Tree | 1 | `2410.12859` |
| STM Storage Area | 1 | `2410.12859` |
| MemTree | 1 | `2410.14052` |
| Depth-Adaptive Threshold Node | 1 | `2410.14052` |
| Folded Tree Node Set | 1 | `2410.14052` |
| Dynamic Social Network Graph | 1 | `2411.11581` |
| Post Information Flow Stream | 1 | `2411.11581` |
| FAISS Vector Index for Video Semantics | 1 | `2411.13093` |
| Decoupled Query Representation | 1 | `2411.13093` |
| Hybrid Memory Map | 1 | `2412.01857` |
| Topological Map | 1 | `2412.01857` |
| Imagination Tree | 1 | `2412.01857` |
| Learnable Persona Dictionary | 1 | `2412.13103` |
| Historical Session Buffer | 1 | `2412.13103` |
| 融合视频与传感器的记忆库 (Video-Sensor Fused Memory Bank) | 1 | `2501.00358` |
| Titans 架构变体 (MAC/MAG/MAL) | 1 | `2501.00663` |
| 测试时可更新权重矩阵 (Test-Time Updatable Weight Matrix) | 1 | `2501.00663` |
| Temporal Knowledge Graph | 1 | `2501.13956` |
| Dynamic Community Structure | 1 | `2501.13956` |
| Age-tagged Memory Pool | 1 | `2502.00592` |
| Latent Space Memory Vectors | 1 | `2502.00592` |
| 64x64 Time Series Image | 1 | `2502.04395` |
| Structured Text Prompt | 1 | `2502.04395` |
| Patch Embedding | 1 | `2502.04395` |
| Independent Memory Bank | 1 | `2502.06049` |
| Gated Memory Unit | 1 | `2502.06049` |
| 检索增强记忆存储 (Retrieval-Augmented Memory Store) | 1 | `2502.13172` |
| 基于编辑距离的索引 (Edit-Distance Based Index) | 1 | `2502.13172` |
| 语义/拓扑地图 (Semantic/Topological Map) | 1 | `2502.14254` |
| 任务相关线索片段 (Task-relevant Clue Fragments) | 1 | `2502.14254` |
| Hybrid Knowledge Graph | 1 | `2502.14802` |
| Phrase-Paragraph Dual Node Structure | 1 | `2502.14802` |
| Query-to-Triple Mapping | 1 | `2502.14802` |
| 层次化压缩结构 (Hierarchical Compression Structure) | 1 | `2502.15957` |
| 可逆 Transformer 架构 (Reversible Transformer Architecture) | 1 | `2502.15957` |
| Explicit Query Description | 1 | `2503.05193` |
| Rule-based Decomposed Statements | 1 | `2503.05193` |
| 代理能力描述表 (Agent Capability Description Table) | 1 | `2503.09263` |
| 历史交互日志 (Historical Interaction Log) | 1 | `2503.09263` |
| Verified Skill Library | 1 | `2504.06821` |
| Action Trajectory Buffer | 1 | `2504.06821` |
| Skill Library | 1 | `2504.07079` |
| Modular Code Repository | 1 | `2504.07079` |
| 动态记忆库 (Dynamic Memory Bank) | 1 | `2504.07952` |
| 策展片段集合 (Curated Snippet Collection) | 1 | `2504.07952` |
| Vectorized Knowledge Index | 1 | `2504.13805` |
| Structured Semantic Description | 1 | `2504.13805` |
| UIA Semantic Tree | 1 | `2504.14603` |
| Visual Grounding Map | 1 | `2504.14603` |
| 实体关系图谱 (Entity-Relation Graph) | 1 | `2504.19413` |
| 向量索引 (Vector Index) | 1 | `2504.19413` |
| Knowledge Triplets (Entity-Relation-Value) | 1 | `2505.15962` |
| Special Query Tokens | 1 | `2505.15962` |
| Three-layer Hierarchical Structure (User->Type->Element) | 1 | `2505.16348` |
| Text Scene Graph | 1 | `2505.16348` |
| 8-Vector Compressed Sequence | 1 | `2505.17670` |
| Intermediate Layer Embedding Slot | 1 | `2505.17670` |
| Structured QA Memory Unit (Intent + Slots) | 1 | `2505.20231` |
| Memory Bank | 1 | `2505.20231` |
| Task-related MCP Graph | 1 | `2505.20286` |
| Minimalist Single-Core Architecture | 1 | `2505.20286` |
| 代码库状态快照 (Codebase State Snapshot) | 1 | `2505.22954` |
| 性能评估记录 (Performance Evaluation Record) | 1 | `2505.22954` |
| Video Latent Sequence | 1 | `2506.03141` |
| Camera Trajectory Map | 1 | `2506.03141` |
| Insight Graph | 1 | `2506.07398` |
| Query Graph | 1 | `2506.07398` |
| Interaction Graph | 1 | `2506.07398` |
| Three-tier Graph Hierarchy | 1 | `2506.07398` |
| Masked Trajectory | 1 | `2506.15841` |
| Control Token Sequence | 1 | `2506.15841` |
| Agent Workflow Pipeline | 1 | `2507.02259` |
| Structured Knowledge Base (结构化知识库) | 1 | `2507.06229` |
| Agent KB Infrastructure (Agent KB 基础设施) | 1 | `2507.06229` |
| 六模块记忆组件架构 | 1 | `2507.07957` |
| 三层代理工作流 (元管理器 + 专用管理器 + 对话代理) | 1 | `2507.07957` |
| 混合存储策略 (端云结合) | 1 | `2507.07957` |
| Tool Context Window | 1 | `2507.21428` |
| Dynamic Tool Pool | 1 | `2507.21428` |
| Four-Layer Semantic Architecture | 1 | `2507.22925` |
| Index Routing Mechanism | 1 | `2507.22925` |
| Vector-Text Dual Storage | 1 | `2507.22925` |
| MLP 记忆模块 (MLP Memory Module) | 1 | `2508.01832` |
| 概率插值机制 (Probability Interpolation Mechanism) | 1 | `2508.01832` |
| 双阶段架构 (训练 - 推理分离架构) | 1 | `2508.01832` |
| Structured Narrative Tuples | 1 | `2508.03341` |
| Distilled Knowledge Statements | 1 | `2508.03341` |
| Dynamic Context State | 1 | `2508.04664` |
| Reversible Context Segment | 1 | `2508.04664` |
| 轨迹序列 (Trajectory Sequence) | 1 | `2508.04700` |
| 软件指南书 (Software Guidebook) | 1 | `2508.04700` |
| YAML Format | 1 | `2508.04903` |
| Graph/Chart Representation | 1 | `2508.04903` |
| Structured Contextual Memory | 1 | `2508.08997` |
| Priority-based Context Window | 1 | `2508.08997` |
| Entity-centric Memory Bank | 1 | `2508.09736` |
| Independent Small Transformer Decoder | 1 | `2508.09874` |
| Interpolation Integration Layer | 1 | `2508.09874` |
| 全局记忆池 (Global Memory Pool) | 1 | `2508.10419` |
| 连贯上下文 (Coherent Context) | 1 | `2508.10419` |
| Structured Memory Entry | 1 | `2508.12630` |
| Hybrid Index Architecture | 1 | `2508.12630` |
| Soft Prompt Vectors | 1 | `2508.15253` |
| Context Memory Embeddings | 1 | `2508.15253` |
| 多记忆片段系统 (Multi-Memory Segment System, MMS) | 1 | `2508.15294` |
| 检索记忆单元 (Retrieval Memory Unit) | 1 | `2508.15294` |
| 上下文记忆单元 (Context Memory Unit) | 1 | `2508.15294` |
| 记忆增强马尔可夫决策过程 (M-MDP) | 1 | `2508.16153` |
| 情景记忆库 (Episodic Memory Bank) | 1 | `2508.16153` |
| 结构化任务序列 (Structured Task Sequences) | 1 | `2508.19005` |
| 持久化世界状态 (Persistent World State) | 1 | `2508.19005` |
| 时空语义系统 (Spatio-Temporal Semantic System) | 1 | `2508.19005` |
| 经验轨迹记录 (Experience Trajectory Records) | 1 | `2508.19005` |
| Perceptual-Cognitive Memory Bank (PCMB) | 1 | `2508.19236` |
| Dual-stream Memory Structure | 1 | `2508.19236` |
| Structured Memory Entries | 1 | `2508.19828` |
| Shared State Space | 1 | `2508.19828` |
| 模块化 AI 代理架构 (Modular AI Agent Architecture) | 1 | `2509.05298` |
| 长期记忆数据库 (Long-term Memory Database) | 1 | `2509.05298` |
| 分层交互系统 (Layered Interaction System) | 1 | `2509.05298` |
| 结构化记忆片段 (Structured Memory Fragments) | 1 | `2509.10852` |
| 记忆图谱 (Memory Graph) | 1 | `2509.10852` |
| 图式 (Schema) | 1 | `2509.10852` |
| 层级化故事线 (Hierarchical Storylines) | 1 | `2509.11860` |
| 键值对记忆库 (Key-Value Memory Bank) | 1 | `2509.11860` |
| SDM Activation Module | 1 | `2509.12760` |
| Empirical CDF Partition | 1 | `2509.12760` |
| Dual-layer Memory Storage | 1 | `2509.12810` |
| Agent Foundation Model Architecture (智能体基座模型架构) | 1 | `2509.13310` |
| Two-stage Training Pipeline (两阶段训练管道) | 1 | `2509.13310` |
| Evidence Memory Bank (证据记忆库) | 1 | `2509.13312` |
| Linked Outline Structure (链接式大纲结构) | 1 | `2509.13312` |
| 对比原则结构 (When/Should/Rather/Because) | 1 | `2509.17459` |
| 结构化文本原则 (Structured Text Principles) | 1 | `2509.17459` |
| Sub-question Sub-answer Sequence | 1 | `2509.22315` |
| Multi-agent Reasoning Trace | 1 | `2509.22315` |
| Confidence Assessment Log | 1 | `2509.22315` |
| Latent Token Sequence | 1 | `2509.24704` |
| ReasoningBank 推理记忆库 | 1 | `2509.25140` |
| 经验池 (Experience Pool) | 1 | `2509.25140` |
| 记忆块 (Memory Block) | 1 | `2509.25911` |
| Compressed Context Sequence | 1 | `2510.00615` |
| Contrastive Trajectory Pair | 1 | `2510.00615` |
| Hierarchical Memory Bank | 1 | `2510.02375` |
| Feed-Forward Memory Blocks | 1 | `2510.02375` |
| 条目化子弹点 (Itemized Bullet Entries) | 1 | `2510.04618` |
| 上下文数据库 (ContextDB) | 1 | `2510.04618` |
| Memory Units (记忆单元) | 1 | `2510.04851` |
| Task Trajectories (任务轨迹) | 1 | `2510.04851` |
| Hierarchical Memory Graph | 1 | `2510.05520` |
| Multi-parent Memory Nodes | 1 | `2510.05520` |
| Proficiency Classification Schema (熟练度分类法) | 1 | `2510.06664` |
| Vector Database Memory Store (向量库记忆存储) | 1 | `2510.06664` |
| Experience-Induced Memory Entries (经验诱导记忆条目) | 1 | `2510.06664` |
| 记忆库 (Memory Bank) | 1 | `2510.07925` |
| 画像模块 (Profile Module) | 1 | `2510.07925` |
| 多源检索模块 (Multi-source Retrieval Module) | 1 | `2510.07925` |
| Rollout Group | 1 | `2510.08191` |
| Semantic Advantage Distribution | 1 | `2510.08191` |
| Action-Future State Pairs (动作 - 未来状态对) | 1 | `2510.08558` |
| Implicit World Model Representations (隐式世界模型表示) | 1 | `2510.08558` |
| Fixed-length Continuous Embedding (固定长度连续嵌入) | 1 | `2510.09038` |
| <conclusion> Tag Structure (结论标签结构) | 1 | `2510.10666` |
| Intermediate Conclusion Storage (中间结论存储) | 1 | `2510.10666` |
| Context-Embedded Memory (上下文嵌入记忆) | 1 | `2510.10666` |
| Interaction Record Sequence (交互记录序列) | 1 | `2510.12635` |
| Segmented Trajectory (轨迹分段) | 1 | `2510.12635` |
| Prune&Write Memory Primitives (记忆原语结构) | 1 | `2510.12635` |
| OWL Knowledge Graph | 1 | `2510.13363` |
| Reasoning Tree (RT) | 1 | `2510.13363` |
| Three-layer Memory State Space | 1 | `2510.16392` |
| Dynamic Knowledge Graph | 1 | `2510.16392` |
| Multi-scale Effective Theory Structure | 1 | `2510.16392` |
| STM Buffer | 1 | `2510.18866` |
| Topic-Summary-Turn Structure | 1 | `2510.18866` |
| Offline Parallel Update Queue | 1 | `2510.18866` |
| Folded Memory Representation | 1 | `2510.21618` |
| Abstracted MCP Repository | 1 | `2510.23601` |
| Semantic Embedding Index | 1 | `2510.23601` |
| 推理 - 动作 - 观察三元组 (Reasoning-Action-Observation Triplet) | 1 | `2510.24699` |
| 多尺度历史轨迹 (Multi-scale History Trajectory) | 1 | `2510.24699` |
| Multi-context Group Structure | 1 | `2511.02805` |
| Iterative Memory Loop | 1 | `2511.02805` |
| Hybrid Replay Buffer | 1 | `2511.03773` |
| Experience Model | 1 | `2511.03773` |
| 结构化经验库 (Structured Experience Library) | 1 | `2511.06449` |
| 经验条目 (Experience Entries) | 1 | `2511.06449` |
| 版本化经验库 (Versioned Experience Library) | 1 | `2511.06449` |
| Environment Profile | 1 | `2511.10395` |
| Interaction Trajectory Log | 1 | `2511.10395` |
| Composite Reward Signal | 1 | `2511.10395` |
| 潜在视觉记忆模块 (Latent Vision Memory Module) | 1 | `2511.11007` |
| 双模块记忆框架 (Dual-module Memory Framework) | 1 | `2511.11007` |
| Attribute-Context Dual Layer | 1 | `2511.13593` |
| Enriched EDU (Elementary Discourse Unit) | 1 | `2511.17208` |
| Heterogeneous Memory Graph | 1 | `2511.17208` |
| Concise Session Snapshot | 1 | `2511.18423` |
| Page-based Storage | 1 | `2511.18423` |
| Optimized Context Window | 1 | `2511.18423` |
| 中央记忆控制器 | 1 | `2512.01710` |
| 模块化记忆服务 | 1 | `2512.01710` |
| 基于 Token 的修剪机制 | 1 | `2512.01710` |
| 信封加密存储 | 1 | `2512.01710` |
| Multi-temporal Granularity Index | 1 | `2512.02425` |
| Multimodal Knowledge Graph (MMKG) | 1 | `2512.03627` |
| Three-layer Memory System | 1 | `2512.03627` |
| Central Memory Orchestrator | 1 | `2512.03627` |
| Expert Adapters | 1 | `2512.04763` |
| Local Memory Bank | 1 | `2512.04763` |
| Keypoint-level Experience Structure | 1 | `2512.10696` |
| Memory Pool | 1 | `2512.10696` |
| Scenario-aware Index | 1 | `2512.10696` |
| Dynamic Session Summary | 1 | `2512.12686` |
| Weighted Knowledge Graph | 1 | `2512.12686` |
| Hybrid Storage Layer (SQLite + ChromaDB) | 1 | `2512.12686` |
| 结构化推理基底 (Structured First-Class Substrate) | 1 | `2512.12818` |
| 时间实体感知记忆层 (Temporal Entity-Aware Memory Layer) | 1 | `2512.12818` |
| 反思层 (Reflection Layer) | 1 | `2512.12818` |
| 四逻辑网络 (Four Logical Networks) | 1 | `2512.12818` |
| 模型权重 (Model Weights) | 1 | `2512.13564` |
| 潜在空间向量 (Latent Space Vectors) | 1 | `2512.13564` |
| 外部向量数据库 (External Vector Database) | 1 | `2512.13564` |
| Elementary Discourse Unit (EDU) Tree | 1 | `2512.14244` |
| Query-Relevant Sub-Tree | 1 | `2512.14244` |
| Context Buffer (上下文缓冲区) | 1 | `2512.18202` |
| File-based State Persistence (基于文件的状态持久化) | 1 | `2512.18202` |
| HTML/Markdown Logs (结构化日志) | 1 | `2512.18202` |
| 模块化记忆空间 (Modular Memory Space) | 1 | `2512.18746` |
| 编码模块 (Encode Module) | 1 | `2512.18746` |
| 存储模块 (Store Module) | 1 | `2512.18746` |
| 检索模块 (Retrieve Module) | 1 | `2512.18746` |
| 管理模块 (Manage Module) | 1 | `2512.18746` |
| Structured Memory Storage | 1 | `2601.01885` |
| Tool-based Memory Interface | 1 | `2601.01885` |
| Intent-Experience-Utility Triplet | 1 | `2601.03192` |
| Structured Triplet (z, e, Q) | 1 | `2601.03192` |
| Time-Varying Directed Multi-Graph | 1 | `2601.03236` |
| Orthogonal Graph Representation | 1 | `2601.03236` |
| Event Graph | 1 | `2601.04726` |
| Logic Map | 1 | `2601.04726` |

---

## 六、记忆操作机制

共 **445** 个记忆操作概念，定义记忆的生命周期行为。

| 概念名称 | 来源论文数 | 来源论文 |
|---------|-----------|---------|
| 记忆检索 (Memory Retrieval) | 4 | `2504.19413`, `2508.16153`, `2509.25140`, `2512.13564` |
| 记忆巩固 (Memory Consolidation) | 3 | `2207.07115`, `2504.19413`, `2507.07957` |
| Memory Update | 3 | `2304.13343`, `2511.02805`, `2512.04763` |
| Memory Retrieval (Embedding Query) | 3 | `2304.13343`, `2505.16348`, `2508.09736` |
| Memory Consolidation (Summarization) | 3 | `2305.10250`, `2508.19236`, `2510.06664` |
| Semantic Retrieval (语义检索) | 3 | `2305.13304`, `2411.13093`, `2510.04851` |
| Importance Scoring | 2 | `2304.03442`, `2508.04903` |
| 语义检索 (Semantic Retrieval) | 2 | `2307.16789`, `2504.07952` |
| Update (State/Network) | 2 | `2411.11581`, `2601.01885` |
| Personalized PageRank Propagation | 2 | `2502.14802`, `2511.17208` |
| 动态更新 (Dynamic Update) | 2 | `2504.07952`, `2511.11007` |
| Similarity-based Retrieval (基于相似度的检索) | 2 | `2504.13805`, `2510.09038` |
| Hierarchical Retrieval | 2 | `2506.07398`, `2511.13593` |
| Hybrid Retrieval (混合检索) | 2 | `2507.06229`, `2508.12630` |
| Conflict Resolution | 2 | `2508.04903`, `2510.13363` |
| Constraint-based Editing | 1 | `2104.08164` |
| Local Weight Update | 1 | `2104.08164` |
| 记忆增强 (Potentiation) | 1 | `2207.07115` |
| 各向异性读取 (Anisotropic Reading) | 1 | `2207.07115` |
| LFU 淘汰 (LFU Eviction) | 1 | `2207.07115` |
| Autonomous API Invocation | 1 | `2302.04761` |
| Result Injection & Continuation | 1 | `2302.04761` |
| Tool Usage Filtering | 1 | `2302.04761` |
| 反思生成 (Reflection Generation) | 1 | `2303.11366` |
| 轨迹存储 (Trajectory Storage) | 1 | `2303.11366` |
| 提示检索 (Hint Retrieval) | 1 | `2303.11366` |
| Relevance Retrieval | 1 | `2304.03442` |
| Reflective Synthesis | 1 | `2304.03442` |
| 知识采样 (Knowledge Sampling) | 1 | `2304.06975` |
| 指令微调 (Instruction Tuning) | 1 | `2304.06975` |
| API 生成清洗 (API Generation & Cleaning) | 1 | `2304.06975` |
| Memory Control Decision | 1 | `2304.13343` |
| Memory Decay (Forgetting) | 1 | `2305.10250` |
| Memory Reinforcement (Retrieval) | 1 | `2305.10250` |
| State Summarization | 1 | `2305.13304` |
| Plan Generation | 1 | `2305.13304` |
| MEM_WRITE (记忆写入) | 1 | `2305.14322` |
| MEM_READ (记忆读取) | 1 | `2305.14322` |
| API 调用拦截 (API Call Interception) | 1 | `2305.14322` |
| 上下文编码压缩 (Context Encoding/Compression) | 1 | `2307.06945` |
| 记忆槽缓存复用 (Memory Slot Caching/Reuse) | 1 | `2307.06945` |
| 基于记忆的解码生成 (Memory-based Decoding) | 1 | `2307.06945` |
| API 调用 (API Invocation) | 1 | `2307.16789` |
| 决策树搜索 (Decision Tree Search) | 1 | `2307.16789` |
| 自动化标注 (Automated Annotation) | 1 | `2307.16789` |
| SOP Encoding | 1 | `2308.00352` |
| Intermediate Validation | 1 | `2308.00352` |
| Feedback Correction | 1 | `2308.00352` |
| Trajectory Analysis | 1 | `2308.02151` |
| Reflection Generation | 1 | `2308.02151` |
| Policy Gradient Update | 1 | `2308.02151` |
| 备忘录撰写 (Memo Writing) | 1 | `2308.08239` |
| 备忘录检索 (Memo Retrieval) | 1 | `2308.08239` |
| 基于备忘录的响应生成 (Memo-Augmented Response) | 1 | `2308.08239` |
| Semantic Embedding Retrieval | 1 | `2308.09597` |
| Instruction-based Prompting | 1 | `2308.09597` |
| Supervised Weight Updating | 1 | `2308.09597` |
| Recursive Memory Update | 1 | `2308.15022` |
| In-Context Memory Integration | 1 | `2308.15022` |
| Summarize-and-Forget | 1 | `2310.02172` |
| Asynchronous Self-Monitoring | 1 | `2310.02172` |
| Retrieval | 1 | `2310.02172` |
| Lifecycle Management | 1 | `2310.03052` |
| DFS Retrieval | 1 | `2310.03052` |
| Hebbian Strengthening | 1 | `2310.03052` |
| Context Paging | 1 | `2310.08560` |
| Memory Eviction | 1 | `2310.08560` |
| Autonomous Retrieval | 1 | `2310.08560` |
| Function Calling | 1 | `2310.08560` |
| State Transition | 1 | `2403.17134` |
| Tool Invocation | 1 | `2403.17134` |
| Context Update | 1 | `2403.17134` |
| Retriever Continuous Training | 1 | `2404.09982` |
| Memory Scoring and Filtering | 1 | `2404.09982` |
| Memory Sharing | 1 | `2404.09982` |
| LLM-driven Entity-Relation Extraction | 1 | `2404.16130` |
| Leiden Community Detection | 1 | `2404.16130` |
| Map-Reduce Answer Generation | 1 | `2404.16130` |
| 离线索引构建 | 1 | `2405.14831` |
| 个性化 PageRank 检索 | 1 | `2405.14831` |
| 跨段落知识整合 | 1 | `2405.14831` |
| Collaborative Graph Learning | 1 | `2405.16089` |
| Semantic-Graph Fusion Retrieval | 1 | `2405.16089` |
| 基于反馈的知识提取 (Knowledge Extraction from Feedback) | 1 | `2405.19686` |
| 无反向传播图谱优化 (Graph Optimization without Back-propagation) | 1 | `2405.19686` |
| 检索增强推理 (Retrieval-Augmented Inference) | 1 | `2405.19686` |
| 链式表过滤 (Chain-of-Tables Filtering) | 1 | `2406.00057` |
| 查询分类路由 (Query Classification Routing) | 1 | `2406.00057` |
| Recursive Summary Aggregation | 1 | `2406.06124` |
| Conditioned Tree Traversal | 1 | `2406.06124` |
| Dynamic Node Update | 1 | `2406.06124` |
| Relation-aware Linking | 1 | `2406.10996` |
| Untangle Retrieval | 1 | `2406.10996` |
| Context-aware Refinement | 1 | `2406.10996` |
| 记忆编码与压缩 (Memory Encoding & Compression) | 1 | `2407.01178` |
| 基于内容的记忆检索 (Content-based Memory Retrieval) | 1 | `2407.01178` |
| 记忆更新策略 (Memory Update Strategy) | 1 | `2407.01178` |
| 记忆淘汰机制 (Memory Elimination Mechanism) | 1 | `2407.01178` |
| 可微分记忆读写 (Differentiable Memory Read/Write) | 1 | `2407.01178` |
| Triple Extraction | 1 | `2407.04363` |
| Graph Update & Fusion | 1 | `2407.04363` |
| Subgraph Retrieval | 1 | `2407.04363` |
| 基于相关性的检索 (Relevance-based Retrieval) | 1 | `2407.06567` |
| 言语强化 Prompt 更新 (Prompt Update via Verbal Reinforcement) | 1 | `2407.06567` |
| 时间衰减 (Time-based Decay) | 1 | `2407.06567` |
| 风险触发式自我反思 (Risk-triggered Self-Reflection) | 1 | `2407.06567` |
| 插入 (Insertion) | 1 | `2409.19401` |
| 删除 (Deletion) | 1 | `2409.19401` |
| 替换 (Replacement) | 1 | `2409.19401` |
| 强化学习路径选择 (RL-guided Path Selection) | 1 | `2409.19401` |
| Null-Space Constrained Editing | 1 | `2410.02355` |
| Orthogonal Projection Update | 1 | `2410.02355` |
| 工具记忆化 (Tool Memorization) | 1 | `2410.03439` |
| 约束生成 (Constrained Generation) | 1 | `2410.03439` |
| Context Summarization/Compression | 1 | `2410.08164` |
| Abstract-to-OS Action Mapping | 1 | `2410.08164` |
| Diversity-Promoting Exploration | 1 | `2410.08197` |
| Feedback-Driven Analysis | 1 | `2410.08197` |
| Iterative Documentation Rewriting | 1 | `2410.08197` |
| Inner Loop Query | 1 | `2410.12859` |
| Dynamic Query Generation | 1 | `2410.12859` |
| Convergence Judgment | 1 | `2410.12859` |
| STM Update | 1 | `2410.12859` |
| Online Top-Down Clustering Insertion | 1 | `2410.14052` |
| Parent Node Aggregation Update | 1 | `2410.14052` |
| Folded Tree Retrieval | 1 | `2410.14052` |
| Perceive (Filter Content) | 1 | `2411.11581` |
| Execute (21 Action Types) | 1 | `2411.11581` |
| Query Decoupling | 1 | `2411.13093` |
| Context Integration | 1 | `2411.13093` |
| Memory Pruning | 1 | `2412.01857` |
| Recursive Imagination | 1 | `2412.01857` |
| Dynamic Weight Fusion | 1 | `2412.01857` |
| Inference-based Persona Update | 1 | `2412.13103` |
| Context-aware Persona Retrieval | 1 | `2412.13103` |
| Session Lifecycle Management | 1 | `2412.13103` |
| VLM 触发式记忆更新 (VLM-Triggered Memory Update) | 1 | `2501.00358` |
| 工具辅助记忆查询 (Tool-Assisted Memory Query) | 1 | `2501.00358` |
| 测试时梯度下降更新 (Test-Time Gradient Descent) | 1 | `2501.00663` |
| 权重衰减遗忘机制 (Weight Decay Forgetting) | 1 | `2501.00663` |
| 惊喜度驱动编码 (Surprise-Driven Encoding) | 1 | `2501.00663` |
| Temporal Invalidation | 1 | `2501.13956` |
| Hybrid Search & Rerank | 1 | `2501.13956` |
| Entity Resolution | 1 | `2501.13956` |
| Memory Migration (STM to LTM) | 1 | `2502.00592` |
| Co-trained Retrieval | 1 | `2502.00592` |
| Read/Write Separation (Multi-LoRA) | 1 | `2502.00592` |
| Self-Augmentation Generation | 1 | `2502.04395` |
| Cross-Modal Attention Fusion | 1 | `2502.04395` |
| Gated Dynamic Weighting | 1 | `2502.04395` |
| Cross-Attention Read | 1 | `2502.06049` |
| Gated Write/Update | 1 | `2502.06049` |
| Forget Operation | 1 | `2502.06049` |
| 记忆提取攻击 (Memory Extraction Attack) | 1 | `2502.13172` |
| 检索操纵 (Retrieval Manipulation) | 1 | `2502.13172` |
| 自适应检索 (Adaptive Retrieval) | 1 | `2502.14254` |
| 全局 - 自我对齐融合 (Global-to-Ego Alignment Fusion) | 1 | `2502.14254` |
| 动态上下文注入 (Dynamic Context Injection) | 1 | `2502.14254` |
| Offline Indexing | 1 | `2502.14802` |
| Online Retrieval | 1 | `2502.14802` |
| Recognition Memory Filtering | 1 | `2502.14802` |
| 正向压缩 (Forward Compression) | 1 | `2502.15957` |
| 反向重建 (Backward Reconstruction) | 1 | `2502.15957` |
| 循环一致性优化 (Cycle Consistency Optimization) | 1 | `2502.15957` |
| Semantic Similarity Retrieval | 1 | `2503.05193` |
| Query Reconstruction | 1 | `2503.05193` |
| Memory Augmentation | 1 | `2503.05193` |
| 状态回滚 (State Rollback) | 1 | `2503.09263` |
| 能力匹配 (Capability Matching) | 1 | `2503.09263` |
| 记忆自进化 (Memory Self-Evolution) | 1 | `2503.09263` |
| Skill Induction (Encoding) | 1 | `2504.06821` |
| Program Verification (Validation) | 1 | `2504.06821` |
| Skill Reuse (Retrieval & Execution) | 1 | `2504.06821` |
| Skill Proposal | 1 | `2504.07079` |
| Skill Synthesis | 1 | `2504.07079` |
| Skill Distillation | 1 | `2504.07079` |
| Skill Honing | 1 | `2504.07079` |
| 自我策展 (Self-Curation) | 1 | `2504.07952` |
| 洞察提取 (Insight Extraction) | 1 | `2504.07952` |
| Demonstration Parsing | 1 | `2504.13805` |
| Context Injection | 1 | `2504.13805` |
| State Synchronization | 1 | `2504.14603` |
| Knowledge Retrieval | 1 | `2504.14603` |
| Speculative Execution | 1 | `2504.14603` |
| 动态显著信息提取 (Dynamic Significant Information Extraction) | 1 | `2504.19413` |
| Loss Masking on Retrieved Values | 1 | `2505.15962` |
| Database-driven Unlearning | 1 | `2505.15962` |
| Query Generation | 1 | `2505.15962` |
| Memory Acquisition (ReAct Triples) | 1 | `2505.16348` |
| Dynamic Knowledge Update | 1 | `2505.16348` |
| VLM Hidden State Extraction | 1 | `2505.17670` |
| Continuous Vector Compression | 1 | `2505.17670` |
| Plug-and-Play Injection | 1 | `2505.17670` |
| Intent-Aligned Retrieval | 1 | `2505.20231` |
| Missing-Slot Guided Filtering | 1 | `2505.20231` |
| Autonomous MCP Generation | 1 | `2505.20286` |
| Capability Refinement | 1 | `2505.20286` |
| Capability Reuse | 1 | `2505.20286` |
| 自我代码修改 (Self-Code Modification) | 1 | `2505.22954` |
| 实证验证 (Empirical Verification) | 1 | `2505.22954` |
| 档案库采样 (Archive Sampling) | 1 | `2505.22954` |
| FOV Overlap Retrieval | 1 | `2506.03141` |
| Latent Dimension Concatenation | 1 | `2506.03141` |
| Bi-directional Memory Traversal | 1 | `2506.07398` |
| Trajectory Assimilation | 1 | `2506.07398` |
| Context Pruning | 1 | `2506.15841` |
| State Consolidation | 1 | `2506.15841` |
| Generate-Reset-Inject Cycle | 1 | `2506.15841` |
| Overwrite Strategy | 1 | `2507.02259` |
| Segmented Ingestion | 1 | `2507.02259` |
| RL Policy Optimization | 1 | `2507.02259` |
| Disagreement Gating (分歧门控) | 1 | `2507.06229` |
| Trajectory Aggregation (轨迹聚合) | 1 | `2507.06229` |
| 主动检索 (Active Retrieval) | 1 | `2507.07957` |
| 记忆自动路由 (Memory Auto-Routing) | 1 | `2507.07957` |
| 并行更新 (Parallel Update) | 1 | `2507.07957` |
| 敏感信息分级访问控制 | 1 | `2507.07957` |
| Tool Search | 1 | `2507.21428` |
| Tool Remove | 1 | `2507.21428` |
| Context Count Check | 1 | `2507.21428` |
| Index Routing Retrieval | 1 | `2507.22925` |
| Dynamic Weight Adjustment | 1 | `2507.22925` |
| Feedback-Driven Update | 1 | `2507.22925` |
| Forgetting Curve Decay | 1 | `2507.22925` |
| 检索器行为模仿 (Retriever Behavior Imitation) | 1 | `2508.01832` |
| 概率插值集成 (Probability Interpolation Integration) | 1 | `2508.01832` |
| 参数化知识内化 (Parametric Knowledge Internalization) | 1 | `2508.01832` |
| Boundary Detection | 1 | `2508.03341` |
| Prediction-Calibration | 1 | `2508.03341` |
| Two-Step Alignment | 1 | `2508.03341` |
| Context Folding | 1 | `2508.04664` |
| Context Compression | 1 | `2508.04664` |
| Context Recovery | 1 | `2508.04664` |
| Context Search | 1 | `2508.04664` |
| Context Fragmentation | 1 | `2508.04664` |
| 自主生成 (Autonomous Generation) | 1 | `2508.04700` |
| 细粒度评估 (Fine-grained Evaluation) | 1 | `2508.04700` |
| 知识蒸馏 (Knowledge Distillation) | 1 | `2508.04700` |
| Context Routing | 1 | `2508.04903` |
| Budget Allocation | 1 | `2508.04903` |
| 程序化构建 (Proceduralization) | 1 | `2508.06433` |
| 基于关键特征平均相似度的检索 (AveFact Retrieval) | 1 | `2508.06433` |
| 纠错更新 (Correction Update/Reflexion) | 1 | `2508.06433` |
| Intrinsic Memory Update | 1 | `2508.08997` |
| Consensus-driven Termination | 1 | `2508.08997` |
| Memorization | 1 | `2508.09736` |
| Multi-turn Reasoning | 1 | `2508.09736` |
| Retriever Behavior Imitation | 1 | `2508.09874` |
| Parameter-Free Model Integration | 1 | `2508.09874` |
| 探索性探针生成 (Exploratory Probing Generation) | 1 | `2508.10419` |
| 知识巩固与整合 (Knowledge Consolidation & Integration) | 1 | `2508.10419` |
| 推理困境检测 (Reasoning Dilemma Detection) | 1 | `2508.10419` |
| Semantic Anchoring | 1 | `2508.12630` |
| Weighted Fusion Ranking | 1 | `2508.12630` |
| Conflict Assessment | 1 | `2508.15253` |
| Adversarial Soft Prompting | 1 | `2508.15253` |
| Knowledge Source Biasing | 1 | `2508.15253` |
| 记忆片段构建 (Memory Segment Construction) | 1 | `2508.15294` |
| 双单元存储 (Dual-Unit Storage) | 1 | `2508.15294` |
| 向量检索匹配 (Vector Retrieval Matching) | 1 | `2508.15294` |
| 单元映射 (Unit Mapping) | 1 | `2508.15294` |
| 记忆重写 (Memory Rewrite) | 1 | `2508.16153` |
| 经验存储 (Experience Storage) | 1 | `2508.16153` |
| 经验探索检索 (Experience Exploration Retrieval) | 1 | `2508.19005` |
| 技能抽象提取 (Skill Abstraction Extraction) | 1 | `2508.19005` |
| 知识内化转换 (Knowledge Internalization Transformation) | 1 | `2508.19005` |
| 记忆距离加权评分 (Memory Distance Weighted Scoring) | 1 | `2508.19005` |
| Cross-Attention Retrieval | 1 | `2508.19236` |
| Gated Fusion | 1 | `2508.19236` |
| Token Merging | 1 | `2508.19236` |
| ADD | 1 | `2508.19828` |
| UPDATE | 1 | `2508.19828` |
| DELETE | 1 | `2508.19828` |
| NOOP | 1 | `2508.19828` |
| 时间二进制压缩 (TBC) | 1 | `2509.05298` |
| 动态重要性记忆过滤 (DIMF) | 1 | `2509.05298` |
| 上下文检索与更新 (Context Retrieval & Update) | 1 | `2509.05298` |
| 预存储推理 (Pre-Storage Reasoning) | 1 | `2509.10852` |
| 记忆提取 (Memory Extraction) | 1 | `2509.10852` |
| 跨会话聚类 (Cross-session Clustering) | 1 | `2509.10852` |
| 图式演化 (Schema Evolution) | 1 | `2509.10852` |
| 混合检索 (Hybrid Retrieval) | 1 | `2509.10852` |
| 层级总结 (Hierarchical Summarization) | 1 | `2509.11860` |
| 竞争 - 抑制遗忘 (Competitive-Inhibitory Forgetting) | 1 | `2509.11860` |
| 键值融合 (Key-Value Fusion) | 1 | `2509.11860` |
| Dense Matching | 1 | `2509.12760` |
| Signal Fusion | 1 | `2509.12760` |
| CDF-based Estimation | 1 | `2509.12760` |
| Hierarchical Hindsight Reflection (H2R) | 1 | `2509.12810` |
| Separate Retrieval | 1 | `2509.12810` |
| Knowledge Fusion | 1 | `2509.12810` |
| Agentic Continual Pre-training (智能体持续预训练) | 1 | `2509.13310` |
| Post-training Alignment via SFT/RL (后训练对齐) | 1 | `2509.13310` |
| Evidence Acquisition (证据获取) | 1 | `2509.13312` |
| Targeted Retrieval (针对性检索) | 1 | `2509.13312` |
| Outline Optimization (大纲优化) | 1 | `2509.13312` |
| 离线自博弈生成 (Offline Self-Play Generation) | 1 | `2509.17459` |
| 语境重解释 (Contextual Re-interpretation) | 1 | `2509.17459` |
| 基于嵌入的检索 (Embedding-based Retrieval) | 1 | `2509.17459` |
| Dynamic Memory Scheduling | 1 | `2509.22315` |
| Uncertainty-based Retrieval | 1 | `2509.22315` |
| Trajectory Reflection | 1 | `2509.22315` |
| Query Decomposition | 1 | `2509.22315` |
| Memory Triggering | 1 | `2509.24704` |
| Memory Weaving | 1 | `2509.24704` |
| Reasoning Augmentation | 1 | `2509.24704` |
| 经验蒸馏 (Experience Distillation) | 1 | `2509.25140` |
| 记忆整合 (Memory Integration) | 1 | `2509.25140` |
| 记忆写入 (Memory Write) | 1 | `2509.25911` |
| 记忆更新 (Memory Update) | 1 | `2509.25911` |
| 记忆读取 (Memory Read) | 1 | `2509.25911` |
| 记忆构建策略 (Memory Construction Strategy) | 1 | `2509.25911` |
| Guideline-Guided Compression | 1 | `2510.00615` |
| Contrastive Feedback Optimization | 1 | `2510.00615` |
| Knowledge Distillation Transfer | 1 | `2510.00615` |
| Context-dependent Memory Block Fetching | 1 | `2510.02375` |
| Parameter Injection | 1 | `2510.02375` |
| 增量 Delta 更新 (Incremental Delta Update) | 1 | `2510.04618` |
| 语义去重 (Semantic Deduplication) | 1 | `2510.04618` |
| 上下文修剪 (Context Pruning) | 1 | `2510.04618` |
| Memory Allocation (记忆分配) | 1 | `2510.04851` |
| Memory Decomposition (记忆分解) | 1 | `2510.04851` |
| Constructivist Assimilation (Node Replication) | 1 | `2510.05520` |
| Constructivist Accommodation (Incremental Clustering) | 1 | `2510.05520` |
| Prune-and-Grow Retrieval | 1 | `2510.05520` |
| Memory Induction (记忆诱导) | 1 | `2510.06664` |
| Retrieve-Refine Update (检索 - 精炼更新) | 1 | `2510.06664` |
| RAG-based Memory Retrieval (基于 RAG 的记忆检索) | 1 | `2510.06664` |
| 多源检索 (Multi-source Retrieval) | 1 | `2510.07925` |
| 自验证 (Self-Validation) | 1 | `2510.07925` |
| 动态演化更新 (Dynamic Evolution Update) | 1 | `2510.07925` |
| 跨交互读写 (Cross-interaction Read/Write) | 1 | `2510.07925` |
| Semantic Advantage Extraction | 1 | `2510.08191` |
| Prior Injection | 1 | `2510.08191` |
| Self-Reflection (自我反思) | 1 | `2510.08558` |
| Implicit World Modeling (隐式世界建模) | 1 | `2510.08558` |
| Future State Collection (未来状态收集) | 1 | `2510.08558` |
| Trajectory Compression (轨迹压缩) | 1 | `2510.09038` |
| Auto-scaling Collection (自动扩展收集) | 1 | `2510.09038` |
| Memory Recording (记忆记录) | 1 | `2510.10666` |
| Memory Compression (记忆压缩) | 1 | `2510.10666` |
| Key Conclusion Extraction (关键结论提取) | 1 | `2510.10666` |
| Prune (删除冗余上下文 ID) | 1 | `2510.12635` |
| Write (写入总结内容) | 1 | `2510.12635` |
| Context Curation (上下文策展) | 1 | `2510.12635` |
| Inline Memory Action (原地记忆动作执行) | 1 | `2510.12635` |
| Neuro-symbolic Knowledge Extraction | 1 | `2510.13363` |
| Beam Search Path Planning | 1 | `2510.13363` |
| Asynchronous Update | 1 | `2510.13363` |
| Renormalization Operators (R_K1, R_K2, R_K3) | 1 | `2510.16392` |
| Threshold-triggered Evolution | 1 | `2510.16392` |
| Coarse-graining | 1 | `2510.16392` |
| Fast-Slow Variable Separation | 1 | `2510.16392` |
| Iterative Pre-compression | 1 | `2510.18866` |
| Topic-Aware Segmentation | 1 | `2510.18866` |
| Buffer-Triggered Summarization | 1 | `2510.18866` |
| Soft Update (Incremental Add) | 1 | `2510.18866` |
| Offline Parallel Update | 1 | `2510.18866` |
| Memory Folding | 1 | `2510.21618` |
| Interaction Compression | 1 | `2510.21618` |
| Tool Retrieval | 1 | `2510.21618` |
| MCP Abstraction (Parameterization) | 1 | `2510.23601` |
| Dual-Strategy Retrieval (Threshold/Top-k) | 1 | `2510.23601` |
| Self-Evolutionary Curation | 1 | `2510.23601` |
| 主动折叠 (Proactive Folding) | 1 | `2510.24699` |
| 细粒度浓缩 (Granular Condensation) | 1 | `2510.24699` |
| 深度整合 (Deep Consolidation) | 1 | `2510.24699` |
| Memory Fusion | 1 | `2511.02805` |
| Trajectory-level Advantage Propagation | 1 | `2511.02805` |
| Experience Synthesis | 1 | `2511.03773` |
| Adaptive Task Generation | 1 | `2511.03773` |
| Sim-to-Real Transfer | 1 | `2511.03773` |
| 经验反思 (Experience Reflection) | 1 | `2511.06449` |
| 经验检索增强 (Experience Retrieval Augmentation) | 1 | `2511.06449` |
| 经验继承 (Experience Inheritance) | 1 | `2511.06449` |
| 经验库演化 (Experience Library Evolution) | 1 | `2511.06449` |
| Self-Questioning | 1 | `2511.10395` |
| Self-Navigating | 1 | `2511.10395` |
| Self-Attributing | 1 | `2511.10395` |
| 推理期无缝调用 (Inference-time Invocation) | 1 | `2511.11007` |
| 信息分流 (Information Shunting) | 1 | `2511.11007` |
| Active Feature Extraction | 1 | `2511.13593` |
| Dynamic Memory Evolution | 1 | `2511.13593` |
| Recall-oriented LLM Filtering | 1 | `2511.17208` |
| Offline Event Extraction | 1 | `2511.17208` |
| Incremental Memory Update | 1 | `2511.18423` |
| Parallel Search | 1 | `2511.18423` |
| Reflective Iteration | 1 | `2511.18423` |
| Context Compilation | 1 | `2511.18423` |
| 异步记忆更新 | 1 | `2512.01710` |
| 动态记忆注入 | 1 | `2512.01710` |
| 冲突解决策略 | 1 | `2512.01710` |
| 选择性遗忘 | 1 | `2512.01710` |
| Adaptive Retrieval | 1 | `2512.02425` |
| Iterative Retrieval Stop | 1 | `2512.02425` |
| Memory Construction | 1 | `2512.02425` |
| Knowledge Distillation | 1 | `2512.03627` |
| Retrieval Augmentation | 1 | `2512.03627` |
| Dynamic Memory Expansion | 1 | `2512.03627` |
| Sliding Window Caching | 1 | `2512.03627` |
| Supervised Fine-tuning (SFT) | 1 | `2512.03627` |
| Memory Extraction | 1 | `2512.04763` |
| Memory Generation | 1 | `2512.04763` |
| Experience Distillation | 1 | `2512.10696` |
| Scenario-aware Retrieval | 1 | `2512.10696` |
| Utility-based Deletion | 1 | `2512.10696` |
| Failure-aware Reflection | 1 | `2512.10696` |
| Experience Rewriting | 1 | `2512.10696` |
| Exponential Time-Decay Weighting | 1 | `2512.12686` |
| User-Input Triple Extraction | 1 | `2512.12686` |
| Incremental Summary Update | 1 | `2512.12686` |
| 保留 (Retain) | 1 | `2512.12818` |
| 回忆 (Recall) | 1 | `2512.12818` |
| 反思 (Reflect) | 1 | `2512.12818` |
| 记忆形成 (Memory Formation) | 1 | `2512.13564` |
| 记忆演化 (Memory Evolution) | 1 | `2512.13564` |
| 记忆遗忘 (Memory Forgetting) | 1 | `2512.13564` |
| EDU Decomposition | 1 | `2512.14244` |
| Sub-Tree Ranking | 1 | `2512.14244` |
| Tree-to-Text Linearization | 1 | `2512.14244` |
| Nightly Self-Critique (夜间自评) | 1 | `2512.18202` |
| Memory Retrieval & Reuse (记忆检索复用) | 1 | `2512.18202` |
| Forward/Backward Learning Integration (前后向学习整合) | 1 | `2512.18202` |
| 元进化 (Meta-Evolution) | 1 | `2512.18746` |
| 联合进化 (Joint Evolution) | 1 | `2512.18746` |
| 元适应 (Meta-Adaptation) | 1 | `2512.18746` |
| 架构优化 (Architecture Optimization) | 1 | `2512.18746` |
| Add | 1 | `2601.01885` |
| Delete | 1 | `2601.01885` |
| Retrieve | 1 | `2601.01885` |
| Summary | 1 | `2601.01885` |
| Filter | 1 | `2601.01885` |
| 情节痕迹形成 (Episodic Trace Formation) | 1 | `2601.02163` |
| 语义巩固 (Semantic Consolidation) | 1 | `2601.02163` |
| 重构式回忆 (Reconstructed Recall) | 1 | `2601.02163` |
| Dual-stage Retrieval | 1 | `2601.03192` |
| Runtime Q-value Update | 1 | `2601.03192` |
| Semantic Gating | 1 | `2601.03192` |
| Fast Path Ingestion | 1 | `2601.03236` |
| Slow Path Consolidation | 1 | `2601.03236` |
| Intent-Aware Routing | 1 | `2601.03236` |
| Adaptive Graph Traversal | 1 | `2601.03236` |
| Incremental Event Segmentation | 1 | `2601.04726` |
| Structured Navigation Retrieval | 1 | `2601.04726` |
| Logical Relation Linking | 1 | `2601.04726` |

---

## 七、记忆载体类型

共 **319** 个记忆载体概念，定义记忆的物质承载形式。

| 概念名称 | 来源论文数 | 来源论文 |
|---------|-----------|---------|
| LLM Context Window (大模型上下文窗口) | 11 | `2308.15022`, `2403.17134`, `2406.06124`, `2503.05193`, `2505.16348` (+6) |
| Vector Embeddings | 10 | `2304.03442`, `2305.13304`, `2310.08560`, `2410.12859`, `2411.13093` (+5) |
| 向量数据库 (Vector Database) | 9 | `2406.00057`, `2504.19413`, `2508.06433`, `2508.15294`, `2509.10852` (+4) |
| Graph Nodes (Memory Snippets) | 4 | `2404.16130`, `2406.10996`, `2506.07398`, `2601.03236` |
| LLM 上下文窗口 (LLM Context Window) | 4 | `2405.14831`, `2405.19686`, `2502.13172`, `2510.24699` |
| Vector Database (向量数据库) | 4 | `2504.13805`, `2509.13312`, `2510.09038`, `2601.03192` |
| Text Embeddings | 3 | `2305.10250`, `2510.05520`, `2512.03627` |
| External Vector Database | 3 | `2308.09597`, `2508.19828`, `2512.02425` |
| Natural Language Text | 2 | `2304.03442`, `2305.13304` |
| Natural Language Instructions | 2 | `2407.04363`, `2410.08164` |
| Agent Interaction Logs (智能体交互日志) | 2 | `2411.11581`, `2510.08558` |
| Video Frames | 2 | `2411.13093`, `2512.02425` |
| 屏幕截图 (Screen Screenshots) | 2 | `2503.09263`, `2507.07957` |
| 对话历史 (Dialogue History) | 2 | `2504.19413`, `2509.10852` |
| External Memory Module | 2 | `2507.02259`, `2601.03192` |
| 外部记忆库 (External Memory Bank) | 2 | `2508.06433`, `2508.16153` |
| Task Execution Logs | 2 | `2509.12810`, `2510.23601` |
| 上下文窗口 (Context Window) | 2 | `2510.04618`, `2512.13564` |
| FAISS Vector Index (FAISS 向量索引) | 2 | `2510.09038`, `2511.13593` |
| MemCells (记忆细胞) | 1 | `2601.02163` |
| MemScenes (记忆场景) | 1 | `2601.02163` |
| Transformer Model Parameters | 1 | `2104.08164` |
| Hyper-network Parameters | 1 | `2104.08164` |
| 视频帧特征图 | 1 | `2207.07115` |
| 显存缓冲区 | 1 | `2207.07115` |
| Special API Tokens (<API>) | 1 | `2302.04761` |
| External API Endpoints | 1 | `2302.04761` |
| 自然语言文本 (Natural Language Text) | 1 | `2303.11366` |
| 任务试错轨迹 (Task Trial Trajectories) | 1 | `2303.11366` |
| LLaMA-7B 模型权重 (LLaMA-7B Weights) | 1 | `2304.06975` |
| 中国医学知识图谱 (CMeKG) | 1 | `2304.06975` |
| Text Sequences | 1 | `2304.13343` |
| Dialogue/Document Records | 1 | `2304.13343` |
| Dialogue Logs | 1 | `2305.10250` |
| Profile Tags | 1 | `2305.10250` |
| 结构化文本三元组 (Structured Text Triplets) | 1 | `2305.14322` |
| 平均向量表示 (Average Vector Representation) | 1 | `2305.14322` |
| LLM 嵌入空间向量 (LLM Embedding Space Vectors) | 1 | `2307.06945` |
| LoRA 适配器参数 (LoRA Adapter Parameters) | 1 | `2307.06945` |
| ToolLLaMA 模型参数 (ToolLLaMA Model Parameters) | 1 | `2307.16789` |
| 外部 API 服务器 (External API Servers) | 1 | `2307.16789` |
| ToolBench 数据集 (ToolBench Dataset) | 1 | `2307.16789` |
| LLM Token Context | 1 | `2308.00352` |
| Shared Environment State | 1 | `2308.00352` |
| Text Prompts | 1 | `2308.02151` |
| Environment Reward Signals | 1 | `2308.02151` |
| 指令微调后的 LLM 参数 (Instruction-Tuned LLM Parameters) | 1 | `2308.08239` |
| 文本备忘录字符串 (Textual Memo Strings) | 1 | `2308.08239` |
| Internal Model Weights | 1 | `2308.09597` |
| Context Window Tokens | 1 | `2308.09597` |
| Prompt Text | 1 | `2308.15022` |
| LyfeGame 3D Environment | 1 | `2310.02172` |
| Text Memory Stream | 1 | `2310.02172` |
| Behavior Logs | 1 | `2310.02172` |
| Engram Unit | 1 | `2310.03052` |
| Token/Character Sequence | 1 | `2310.03052` |
| Text Tokens | 1 | `2310.08560` |
| System Logs | 1 | `2310.08560` |
| Execution Logs | 1 | `2403.17134` |
| Source Code Repository | 1 | `2403.17134` |
| Shared Vector Database | 1 | `2404.09982` |
| Rubric-based Scoring System | 1 | `2404.09982` |
| Community Reports (Text Summaries) | 1 | `2404.16130` |
| 文本段落 | 1 | `2405.14831` |
| 图谱节点与边 | 1 | `2405.14831` |
| PLM Embeddings | 1 | `2405.16089` |
| Graph Neural Network Nodes | 1 | `2405.16089` |
| 外部图数据库 (External Graph Database) | 1 | `2405.19686` |
| 结构化表格 (Structured Table) | 1 | `2406.00057` |
| Textual Tree Nodes | 1 | `2406.06124` |
| Text Embedding Vectors | 1 | `2406.10996` |
| 文本序列 (Text Sequence) | 1 | `2407.01178` |
| 记忆向量表示 (Memory Vector Representation) | 1 | `2407.01178` |
| 可寻址向量数据库 (Addressable Vector Database) | 1 | `2407.01178` |
| Text Interaction Logs | 1 | `2407.04363` |
| 文本 Prompt | 1 | `2407.06567` |
| 多模态金融数据 (文本/音频/表格) | 1 | `2407.06567` |
| 结构化图谱节点 (实体/关系) | 1 | `2409.19401` |
| 非结构化文本记忆 | 1 | `2409.19401` |
| 本地手机端存储 | 1 | `2409.19401` |
| MLP Weight Matrices | 1 | `2410.02355` |
| Hidden State Activations | 1 | `2410.02355` |
| 大模型参数 (LLM Parameters) | 1 | `2410.03439` |
| 扩展特殊令牌 (Extended Special Tokens) | 1 | `2410.03439` |
| Screen Screenshots | 1 | `2410.08164` |
| Operation Logs | 1 | `2410.08164` |
| API Documentation Text | 1 | `2410.08197` |
| Interaction Feedback Signals | 1 | `2410.08197` |
| Natural Language Context | 1 | `2410.08197` |
| Text Chunks | 1 | `2410.12859` |
| Summary Nodes | 1 | `2410.12859` |
| Semantic Embedding Vectors | 1 | `2410.14052` |
| Text Conversation Streams | 1 | `2410.14052` |
| LLM Generated Summaries | 1 | `2410.14052` |
| LLM Token Context Window | 1 | `2411.11581` |
| Simulated Platform Database | 1 | `2411.11581` |
| Extracted Text Chunks | 1 | `2411.13093` |
| Topological Map Nodes | 1 | `2412.01857` |
| RGB-D Features | 1 | `2412.01857` |
| Semantic Features | 1 | `2412.01857` |
| External Persona Database (Key-Value) | 1 | `2412.13103` |
| LLM Prompt Context Window | 1 | `2412.13103` |
| 第一人称视频流 (Egocentric Video Streams) | 1 | `2501.00358` |
| 具身传感器数据 (深度/姿态) (Embodied Sensor Data: Depth/Pose) | 1 | `2501.00358` |
| Token 嵌入序列 (Token Embedding Sequences) | 1 | `2501.00663` |
| 可学习参数向量 (Learnable Parameter Vectors) | 1 | `2501.00663` |
| Graphiti Engine | 1 | `2501.13956` |
| Episode Data Unit | 1 | `2501.13956` |
| GPU VRAM | 1 | `2502.00592` |
| CPU RAM | 1 | `2502.00592` |
| Frozen VLM Encoder | 1 | `2502.04395` |
| Time Series Vector | 1 | `2502.04395` |
| Visual Embedding | 1 | `2502.04395` |
| Text Embedding | 1 | `2502.04395` |
| Memory Vectors | 1 | `2502.06049` |
| Token Representations | 1 | `2502.06049` |
| 外部记忆数据库 (External Memory Database) | 1 | `2502.13172` |
| 视觉语言模型 (Vision-Language Model) | 1 | `2502.14254` |
| 向量或图结构数据库 (Vector/Graph Database) | 1 | `2502.14254` |
| Text Passages | 1 | `2502.14802` |
| Knowledge Graph Triples | 1 | `2502.14802` |
| Dense Embeddings | 1 | `2502.14802` |
| 虚拟记忆令牌 (Virtual Memory Tokens) | 1 | `2502.15957` |
| Adapter 权重 (Adapter Weights) | 1 | `2502.15957` |
| Memory Module | 1 | `2503.05193` |
| Vector Embedding Space | 1 | `2503.05193` |
| UI 元素树 (UI Element Tree) | 1 | `2503.09263` |
| 操作动作序列 (Action Sequences) | 1 | `2503.09263` |
| Executable Code Snippets | 1 | `2504.06821` |
| Web Interaction Traces | 1 | `2504.06821` |
| Python Async Scripts | 1 | `2504.07079` |
| API Function Definitions | 1 | `2504.07079` |
| 文本策略片段 (Text Strategy Snippets) | 1 | `2504.07952` |
| 代码片段 (Code Snippets) | 1 | `2504.07952` |
| 增强系统提示词 (Augmented System Prompts) | 1 | `2504.07952` |
| LearnGUI Dataset | 1 | `2504.13805` |
| Virtual Session Buffer | 1 | `2504.14603` |
| Named Pipes | 1 | `2504.14603` |
| Screen Snapshots | 1 | `2504.14603` |
| 图数据库 (Graph Database) | 1 | `2504.19413` |
| External Knowledge Database | 1 | `2505.15962` |
| Model Weights (Linguistic Only) | 1 | `2505.15962` |
| Knowledge Graph Nodes/Edges | 1 | `2505.16348` |
| Habitat 3.0 Simulator State | 1 | `2505.16348` |
| Continuous Embedding Vectors | 1 | `2505.17670` |
| VLM Internal Hidden States | 1 | `2505.17670` |
| Dense Vector Index | 1 | `2505.20231` |
| External Open Source Repositories | 1 | `2505.20286` |
| Internal Agent Context | 1 | `2505.20286` |
| 源代码仓库 (Source Code Repository) | 1 | `2505.22954` |
| 安全沙箱环境 (Safety Sandbox Environment) | 1 | `2505.22954` |
| Diffusion Latents | 1 | `2506.03141` |
| Camera Poses | 1 | `2506.03141` |
| Interaction Trajectories | 1 | `2506.07398` |
| Collaboration Experiences | 1 | `2506.07398` |
| Internal State Token (<IS>) | 1 | `2506.15841` |
| Text Interaction Sequence | 1 | `2506.15841` |
| Text Segments | 1 | `2507.02259` |
| LLM Base Model Parameters | 1 | `2507.02259` |
| Agent Execution Trajectories (智能体执行轨迹) | 1 | `2507.06229` |
| Lightweight API Interface (轻量级 API 接口) | 1 | `2507.06229` |
| 文本对话 | 1 | `2507.07957` |
| 文档文件 | 1 | `2507.07957` |
| 敏感凭证 | 1 | `2507.07957` |
| 时间戳事件日志 | 1 | `2507.07957` |
| MCP Server Tool List | 1 | `2507.21428` |
| Text Conversation History | 1 | `2507.22925` |
| User Profiles | 1 | `2507.22925` |
| Semantic Indexes | 1 | `2507.22925` |
| 预训练数据集 (WikiText-103, Web datasets) | 1 | `2508.01832` |
| 1B 参数 MLP 模块 | 1 | `2508.01832` |
| 基础 LLM 解码器 | 1 | `2508.01832` |
| Memory Database | 1 | `2508.03341` |
| Text Sequence | 1 | `2508.04664` |
| Tool Call Trajectory | 1 | `2508.04664` |
| 世界状态模型 (World State Model) | 1 | `2508.04700` |
| 策略模型权重 (Policy Model Weights) | 1 | `2508.04700` |
| 文本指南库 (Text Guide Repository) | 1 | `2508.04700` |
| Structured Memory Bank | 1 | `2508.04903` |
| 文本轨迹 (Text Trajectory) | 1 | `2508.06433` |
| 向量嵌入 (Vector Embeddings) | 1 | `2508.06433` |
| Structured Memory Templates | 1 | `2508.08997` |
| Agent-specific Output Logs | 1 | `2508.08997` |
| Long-term Memory Bank | 1 | `2508.09736` |
| Multimodal Input Stream | 1 | `2508.09736` |
| Module Weights | 1 | `2508.09874` |
| Domain-Specific Corpus | 1 | `2508.09874` |
| 长上下文 Token 序列 (Long Context Token Sequences) | 1 | `2508.10419` |
| 向量检索数据库 (Vector Retrieval Database) | 1 | `2508.10419` |
| Dense Vector | 1 | `2508.12630` |
| Dependency Parse Triples | 1 | `2508.12630` |
| Coreference Chains | 1 | `2508.12630` |
| Discourse Relation Labels | 1 | `2508.12630` |
| Text Queries | 1 | `2508.15253` |
| Retrieved Document Chunks | 1 | `2508.15253` |
| Embedding Space Representations | 1 | `2508.15253` |
| 对话文本 (Dialogue Text) | 1 | `2508.15294` |
| 向量化记忆片段 (Vectorized Memory Segments) | 1 | `2508.15294` |
| 冻结的大模型参数 (Frozen LLM Parameters) | 1 | `2508.16153` |
| 多工具交互日志 (Multi-tool Interaction Logs) | 1 | `2508.19005` |
| 七类工具接口 (Seven Tool Interfaces) | 1 | `2508.19005` |
| 校园模拟环境状态 (Campus Simulation Environment State) | 1 | `2508.19005` |
| 上下文工程提示词 (Context Engineering Prompts) | 1 | `2508.19005` |
| Perceptual Tokens | 1 | `2508.19236` |
| Cognitive Tokens | 1 | `2508.19236` |
| RGB Observation Frames | 1 | `2508.19236` |
| Key-Value Storage | 1 | `2508.19828` |
| AR 虚拟形象 (AR Virtual Avatar) | 1 | `2509.05298` |
| 多模态交互日志 (Multimodal Interaction Logs) | 1 | `2509.05298` |
| 云端/本地混合存储 (Cloud/Local Hybrid Storage) | 1 | `2509.05298` |
| 增强记忆库 (Enhanced Memory Bank) | 1 | `2509.10852` |
| 文本对话流 (Text Dialogue Flow) | 1 | `2509.11860` |
| 微调大语言模型 (Micro-tuned LLM) | 1 | `2509.11860` |
| Training Set Embeddings | 1 | `2509.12760` |
| High-dimensional Input Representations | 1 | `2509.12760` |
| Agent-Environment Interaction Trajectories | 1 | `2509.12810` |
| AgentFounder-30B Model | 1 | `2509.13310` |
| Agent Behavior Pre-training Data | 1 | `2509.13310` |
| Web-scale Text Chunks (网络规模文本块) | 1 | `2509.13312` |
| Cited Report Sections (引用报告章节) | 1 | `2509.13312` |
| 外部策略数据库 (External Strategy Database) | 1 | `2509.17459` |
| 结构化文本原则库 | 1 | `2509.17459` |
| Reasoning Trajectory Logs | 1 | `2509.22315` |
| External Knowledge Base Snippets | 1 | `2509.22315` |
| Intermediate Token Streams | 1 | `2509.22315` |
| Latent Tokens | 1 | `2509.24704` |
| LLM Internal State | 1 | `2509.24704` |
| LLM 基座模型 (LLM Base Model) | 1 | `2509.25140` |
| 多轮交互序列 (Multi-turn Interaction Sequence) | 1 | `2509.25911` |
| 问答评估对 (QA Evaluation Pair) | 1 | `2509.25911` |
| 持久化存储 (Persistent Storage) | 1 | `2509.25911` |
| Natural Language Compression Guidelines | 1 | `2510.00615` |
| Distilled Student Compressor Model | 1 | `2510.00615` |
| Transformer Parameters | 1 | `2510.02375` |
| Anchor Model Parameters | 1 | `2510.02375` |
| KV 缓存 (KV Cache) | 1 | `2510.04618` |
| Central Memory Database (中央记忆库) | 1 | `2510.04851` |
| Agent Context Window (代理上下文窗口) | 1 | `2510.04851` |
| LLM-generated Node Summaries | 1 | `2510.05520` |
| Task Prompts (任务 Prompt) | 1 | `2510.06664` |
| Tool Solutions (工具解决方案) | 1 | `2510.06664` |
| Quality Feedback Scores (质量反馈分数) | 1 | `2510.06664` |
| Capability Assessment Text (能力评估文本) | 1 | `2510.06664` |
| 交互历史数据 (Interaction History Data) | 1 | `2510.07925` |
| 用户偏好特征 (User Preference Features) | 1 | `2510.07925` |
| Input Token Sequence | 1 | `2510.08191` |
| API Context Window | 1 | `2510.08191` |
| Screenshot-Action Pairs (截图 - 动作对) | 1 | `2510.09038` |
| Text Context (文本上下文) | 1 | `2510.10666` |
| DOM/Accessibility Tree (DOM/可访问性树) | 1 | `2510.10666` |
| Webpage State (网页状态) | 1 | `2510.10666` |
| Token-based Context Window (基于 Token 的上下文窗口) | 1 | `2510.12635` |
| Model Policy Parameters (模型策略参数) | 1 | `2510.12635` |
| Interaction Logs (交互日志) | 1 | `2510.12635` |
| Non-structured Dialogue Text | 1 | `2510.13363` |
| Abstract Meaning Representation (AMR) | 1 | `2510.13363` |
| OWL Ontology | 1 | `2510.13363` |
| External Memory Storage | 1 | `2510.16392` |
| Graph Database | 1 | `2510.16392` |
| Compressed Topic Fragments | 1 | `2510.18866` |
| Dialogue Text Sequences | 1 | `2510.18866` |
| Topic Summaries | 1 | `2510.18866` |
| Multi-turn Interaction Trajectories | 1 | `2510.21618` |
| Tool API Descriptions | 1 | `2510.21618` |
| Task Instructions | 1 | `2510.21618` |
| Code Toolkits | 1 | `2510.23601` |
| Semantic Embeddings | 1 | `2510.23601` |
| 上下文 Token (Context Tokens) | 1 | `2510.24699` |
| Search Tool Response | 1 | `2511.02805` |
| Reasoning Model | 1 | `2511.03773` |
| Replay Buffer | 1 | `2511.03773` |
| LLM 智能体 (LLM Agent) | 1 | `2511.06449` |
| 经验库存储系统 (Experience Library Storage System) | 1 | `2511.06449` |
| 反思模块 (Reflection Module) | 1 | `2511.06449` |
| Textual Trajectories | 1 | `2511.10395` |
| Model Parameters | 1 | `2511.10395` |
| 连续潜在上下文 (Continuous Latent Contexts) | 1 | `2511.11007` |
| 潜在空间表示 (Latent Space Representations) | 1 | `2511.11007` |
| User Interaction Logs | 1 | `2511.13593` |
| LLM Agent Context Window | 1 | `2511.17208` |
| Embedding Vector Index | 1 | `2511.17208` |
| Text Session Trajectories | 1 | `2511.18423` |
| Token Embeddings | 1 | `2511.18423` |
| Vector Store | 1 | `2511.18423` |
| Firestore 对话历史 | 1 | `2512.01710` |
| S3 加密生物信息 | 1 | `2512.01710` |
| 时间戳事件存储 | 1 | `2512.01710` |
| 外部 API 数据 | 1 | `2512.01710` |
| 会话内缓冲区 | 1 | `2512.01710` |
| Text Summaries | 1 | `2512.02425` |
| Time Segments | 1 | `2512.02425` |
| Image Embeddings | 1 | `2512.03627` |
| Video Embeddings | 1 | `2512.03627` |
| Lightweight Neural Network Parameters | 1 | `2512.03627` |
| Small Language Model (SLM) | 1 | `2512.04763` |
| Small Vision-Language Model (SVLM) | 1 | `2512.04763` |
| LLM Agent Memory System | 1 | `2512.10696` |
| Structured Experience Records | 1 | `2512.10696` |
| Embedding Vectors | 1 | `2512.10696` |
| Structured Dialogue Logs | 1 | `2512.12686` |
| Knowledge Triples | 1 | `2512.12686` |
| Session IDs | 1 | `2512.12686` |
| 对话流 (Dialogue Stream) | 1 | `2512.12818` |
| 结构化记忆库 (Structured Memory Bank) | 1 | `2512.12818` |
| LLM 上下文 (LLM Context) | 1 | `2512.13564` |
| 神经网络参数 (Neural Parameters) | 1 | `2512.13564` |
| 向量存储 (Vector Storage) | 1 | `2512.13564` |
| Source Index Anchored EDU Nodes | 1 | `2512.14244` |
| Compressed Token Sequence | 1 | `2512.14244` |
| Offline Browser Sandbox (离线浏览器沙盒) | 1 | `2512.18202` |
| Synthetic User Behavior Streams (合成用户行为流) | 1 | `2512.18202` |
| 交互轨迹 (Interaction Trajectories) | 1 | `2512.18746` |
| 蒸馏经验 (Distilled Experience) | 1 | `2512.18746` |
| 可复用工具 (Reusable Tools) | 1 | `2512.18746` |
| Text Interaction Trajectories | 1 | `2601.01885` |
| Token-based Context | 1 | `2601.01885` |
| Graph Edges | 1 | `2601.03236` |
| Event Nodes | 1 | `2601.04726` |
| Logical Edges | 1 | `2601.04726` |

---

## 八、记忆功能定位

共 **325** 个记忆功能概念，按功能维度分组。

### Episodic Memory (9)

| 概念名称 | 来源论文数 | 来源论文 |
|---------|-----------|---------|
| Episodic Memory (Interaction History) | 10 | `2407.04363`, `2412.01857`, `2505.16348`, `2508.03341`, `2508.09736` (+5) |
| 情景记忆 (Episodic Memory) | 6 | `2303.11366`, `2407.06567`, `2507.07957`, `2508.16153`, `2509.10852` (+1) |
| Local Episodic Memory (Text Chunks) | 1 | `2404.16130` |
| Episodic Memory Graph | 1 | `2406.10996` |
| Episodic Simulation | 1 | `2412.01857` |
| Episodic Demonstration Memory | 1 | `2504.13805` |
| 情景记忆片段 (Episodic Memory Segment) | 1 | `2508.15294` |
| 情景事件记忆 | 1 | `2512.01710` |
| 情节痕迹 (Episodic Trace) | 1 | `2601.02163` |

### Experiential Memory (8)

| 概念名称 | 来源论文数 | 来源论文 |
|---------|-----------|---------|
| 经验记忆 (Experiential Memory) | 4 | `2508.04700`, `2509.10852`, `2509.25140`, `2512.13564` |
| Cross-Domain Experience (跨域经验) | 1 | `2507.06229` |
| Experiential Knowledge | 1 | `2510.08191` |
| Early Experience (早期经验) | 1 | `2510.08558` |
| 结构化经验 (Structured Experience) | 1 | `2511.06449` |
| 成功/失败轨迹经验 (Success/Failure Trajectory Experience) | 1 | `2511.06449` |
| 智能体经验 (Agent Experience) | 1 | `2512.12818` |
| 经验知识 (Experiential Knowledge) | 1 | `2512.18746` |

### Factual Memory (5)

| 概念名称 | 来源论文数 | 来源论文 |
|---------|-----------|---------|
| 事实记忆 (Factual Memory) | 2 | `2509.10852`, `2512.13564` |
| 结构化事实备忘录 (Structured Fact Memos) | 1 | `2308.08239` |
| 个性化事实知识 (Personalized Factual Knowledge) | 1 | `2405.19686` |
| Externalized Factual Memory | 1 | `2505.15962` |
| 世界事实 (World Facts) | 1 | `2512.12818` |

### Long-Term Memory (16)

| 概念名称 | 来源论文数 | 来源论文 |
|---------|-----------|---------|
| Long-Term Memory (Light3/LTM) | 4 | `2310.03052`, `2502.00592`, `2510.18866`, `2601.01885` |
| 长期记忆 (Long-term Memory) | 3 | `2207.07115`, `2407.01178`, `2504.19413` |
| Long-term Memory (LTM) | 3 | `2304.13343`, `2305.13304`, `2512.03627` |
| Long-term Reflection Memory | 1 | `2308.02151` |
| 神经生物学启发的长期记忆 | 1 | `2405.14831` |
| 时间敏感长期记忆 (Time-Sensitive Long-term Memory) | 1 | `2406.00057` |
| Long-Term Dialogue Memory | 1 | `2406.06124` |
| Long-term Task Goal Storage | 1 | `2410.08164` |
| Life-long Interaction Memory | 1 | `2412.13103` |
| 神经长期记忆 (Neural Long-Term Memory) | 1 | `2501.00663` |
| Long-term Agent Memory | 1 | `2501.13956` |
| 长期交互记忆 (Long-term Interaction Memory) | 1 | `2509.05298` |
| Long-tail Knowledge Memory | 1 | `2510.02375` |
| Long-Term Conversational Memory | 1 | `2511.17208` |
| 长期用户记忆 | 1 | `2512.01710` |
| LongTermMemory | 0 | - |

### Other Memory Type (233)

| 概念名称 | 来源论文数 | 来源论文 |
|---------|-----------|---------|
| Agentic Memory | 3 | `2508.12630`, `2512.12686`, `2601.01885` |
| Summarized Memory (Daily/Global) | 2 | `2305.10250`, `2310.02172` |
| User Profile Memory (Hierarchical KG) | 2 | `2305.10250`, `2505.16348` |
| 持久记忆 (Persistent Memory) | 2 | `2501.00663`, `2510.07925` |
| Hierarchical Memory (Local & Global) | 2 | `2502.04395`, `2507.22925` |
| Query Memory | 2 | `2503.05193`, `2506.07398` |
| 核心记忆 (Core Memory) | 2 | `2507.07957`, `2509.25911` |
| 推理记忆 (Reasoning Memory) | 2 | `2509.10852`, `2509.25140` |
| Text Memory (文本记忆 - 基线对比) | 2 | `2510.09038`, `2512.04763` |
| Event-Centric Memory (EMem) | 2 | `2511.17208`, `2601.04726` |
| Visual Memory | 2 | `2512.02425`, `2512.04763` |
| Editable Knowledge State | 1 | `2104.08164` |
| External Tool Knowledge | 1 | `2302.04761` |
| Self-Supervised Tool Decision State | 1 | `2302.04761` |
| 言语强化记忆 (Verbal Reinforcement Memory) | 1 | `2303.11366` |
| Observation Memory | 1 | `2304.03442` |
| 医疗指令数据 (Medical Instruction Data) | 1 | `2304.06975` |
| 知识图谱实例 (Knowledge Graph Instances) | 1 | `2304.06975` |
| Self-Controlled Memory | 1 | `2304.13343` |
| Raw Dialogue Memory | 1 | `2305.10250` |
| 通用读写记忆 (General Read-Write Memory) | 1 | `2305.14322` |
| 外部记忆模块 (External Memory Module) | 1 | `2305.14322` |
| 记忆槽 (Memory Slots) | 1 | `2307.06945` |
| 压缩上下文表示 (Compressed Context Representation) | 1 | `2307.06945` |
| 工具指令记忆 (Tool Instruction Memory) | 1 | `2307.16789` |
| 执行轨迹记忆 (Execution Trace Memory) | 1 | `2307.16789` |
| SOP-Encoded Knowledge | 1 | `2308.00352` |
| Role-Specific Context | 1 | `2308.00352` |
| 自用备忘录 (Self-use Memos) | 1 | `2308.08239` |
| Static Character Profile Memory | 1 | `2308.09597` |
| Retrievable Script Memory | 1 | `2308.09597` |
| Dynamic Dialogue History Memory | 1 | `2308.09597` |
| Recursive Summary Memory | 1 | `2308.15022` |
| Generated Dialogue Memory | 1 | `2308.15022` |
| Experience Stream | 1 | `2310.02172` |
| Key Memory | 1 | `2310.02172` |
| Virtual Context (Main Context) | 1 | `2310.08560` |
| External Memory (Archival/Recall Storage) | 1 | `2310.08560` |
| Repair State Memory | 1 | `2403.17134` |
| Tool Feedback Memory | 1 | `2403.17134` |
| Code Context Memory | 1 | `2403.17134` |
| Domain-specific Memory Pool | 1 | `2404.09982` |
| Global Memory Pool | 1 | `2404.09982` |
| Candidate Memory | 1 | `2404.09982` |
| 海马体索引记忆 | 1 | `2405.14831` |
| Completeness-Oriented Tool Memory | 1 | `2405.16089` |
| 用户交互反馈记忆 (User Interaction Feedback Memory) | 1 | `2405.19686` |
| 上下文敏感记忆 (Context-Sensitive Memory) | 1 | `2406.00057` |
| Hierarchical Aggregated Memory | 1 | `2406.06124` |
| Timeline Memory | 1 | `2406.10996` |
| 中期记忆 (Medium-term Memory) | 1 | `2407.01178` |
| 概念化投资信念 (Conceptual Investment Beliefs) | 1 | `2407.06567` |
| 主动记忆 (Active Memory) | 1 | `2409.19401` |
| 被动记忆 (Passive Memory) | 1 | `2409.19401` |
| 记忆类型 (Memory Type) | 1 | `2409.19401` |
| 记忆子类 (Memory Subclass) | 1 | `2409.19401` |
| Parameterized Fact Memory | 1 | `2410.02355` |
| Static Human-Centric Documentation | 1 | `2410.08197` |
| Dynamic LLM-Adapted Documentation | 1 | `2410.08197` |
| Interaction Experience Memory | 1 | `2410.08197` |
| Surprising Information Memory | 1 | `2410.12859` |
| Dynamic Tree Memory | 1 | `2410.14052` |
| Hierarchical Schema Memory | 1 | `2410.14052` |
| Online Incremental Memory | 1 | `2410.14052` |
| Individual Agent Context Memory | 1 | `2411.11581` |
| Global Environment State Memory | 1 | `2411.11581` |
| Visually-aligned Auxiliary Text Memory | 1 | `2411.13093` |
| Real Memory | 1 | `2412.01857` |
| Imagined Memory | 1 | `2412.01857` |
| Dynamic User Persona | 1 | `2412.13103` |
| Session History Memory | 1 | `2412.13103` |
| 持久场景记忆 (Persistent Scene Memory) | 1 | `2501.00358` |
| 多模态具身记忆 (Multimodal Embodied Memory) | 1 | `2501.00358` |
| Bi-temporal Memory | 1 | `2501.13956` |
| Pre-trained Multimodal Knowledge | 1 | `2502.04395` |
| Explicit Auxiliary Memory | 1 | `2502.06049` |
| Context Representation Memory | 1 | `2502.06049` |
| 交互历史记忆 (Interaction History Memory) | 1 | `2502.13172` |
| 敏感查询记忆 (Sensitive Query Memory) | 1 | `2502.13172` |
| 全局记忆 (Global Memory) | 1 | `2502.14254` |
| 自我中心记忆 (Ego-centric Memory) | 1 | `2502.14254` |
| 全局到自我对齐记忆 (Global-to-Ego Aligned Memory) | 1 | `2502.14254` |
| Associative Memory | 1 | `2502.14802` |
| Fact Memory | 1 | `2502.14802` |
| Contextual Memory | 1 | `2502.14802` |
| 可逆记忆 (Reversible Memory) | 1 | `2502.15957` |
| 虚拟记忆 (Virtual Memory) | 1 | `2502.15957` |
| 交互轨迹记忆 (Interaction Trajectory Memory) | 1 | `2503.09263` |
| 状态快照记忆 (State Snapshot Memory) | 1 | `2503.09263` |
| 成功/失败案例记忆 (Success/Failure Case Memory) | 1 | `2503.09263` |
| Text-based Skills (Declarative Memory) | 1 | `2504.06821` |
| Executable API Memory | 1 | `2504.07079` |
| 自适应记忆 (Adaptive Memory) | 1 | `2504.07952` |
| 动态作弊表记忆 (Dynamic Cheatsheet Memory) | 1 | `2504.07952` |
| 策略记忆 (Strategy Memory) | 1 | `2504.07952` |
| Execution Trace Memory | 1 | `2504.14603` |
| 图基于记忆 (Graph-based Memory) | 1 | `2504.19413` |
| 向量基于记忆 (Vector-based Memory) | 1 | `2504.19413` |
| Limited Memory | 1 | `2505.15962` |
| Internal Linguistic Memory | 1 | `2505.15962` |
| General Continuous Memory (CoMEM) | 1 | `2505.17670` |
| External Multimodal Knowledge Memory | 1 | `2505.17670` |
| Intent-Driven Memory | 1 | `2505.20231` |
| Multi-Session Task Memory | 1 | `2505.20231` |
| Dynamic Capability Memory (MCPs) | 1 | `2505.20286` |
| Task Context Memory | 1 | `2505.20286` |
| 进化档案库 (Evolutionary Archive) | 1 | `2505.22954` |
| 代理版本树 (Agent Version Tree) | 1 | `2505.22954` |
| Context-as-Memory | 1 | `2506.03141` |
| Geometric-Indexed Memory | 1 | `2506.03141` |
| Insight Memory | 1 | `2506.07398` |
| Interaction Memory | 1 | `2506.07398` |
| Constant Memory | 1 | `2506.15841` |
| Compressed Internal State | 1 | `2506.15841` |
| RL-Managed Memory | 1 | `2507.02259` |
| Segmented Context Memory | 1 | `2507.02259` |
| Planning Seeds (规划种子) | 1 | `2507.06229` |
| Feedback Diagnosis (反馈诊断) | 1 | `2507.06229` |
| 资源记忆 (Resource Memory) | 1 | `2507.07957` |
| 知识保险库 (Knowledge Vault) | 1 | `2507.07957` |
| Autonomous Memory | 1 | `2507.21428` |
| Workflow Memory | 1 | `2507.21428` |
| Domain Memory | 1 | `2507.22925` |
| Category Memory | 1 | `2507.22925` |
| Trace Memory | 1 | `2507.22925` |
| Episode Memory | 1 | `2507.22925` |
| Passive Input Context | 1 | `2508.04664` |
| 知识记忆 (Knowledge Memory) | 1 | `2508.04700` |
| Role-Aware Context Memory | 1 | `2508.04903` |
| 原始轨迹记忆 (Raw Trajectory) | 1 | `2508.06433` |
| 抽象脚本记忆 (Abstract Script) | 1 | `2508.06433` |
| Intrinsic Memory | 1 | `2508.08997` |
| Heterogeneous Agent Memory | 1 | `2508.08997` |
| Fine-grained Memory | 1 | `2508.09736` |
| High-level Abstract Memory | 1 | `2508.09736` |
| Pretrained Plug-and-Play Memory | 1 | `2508.09874` |
| 状态化记忆 (Stateful Memory) | 1 | `2508.10419` |
| Retrieved Context (External Memory) | 1 | `2508.15253` |
| 关键词记忆片段 (Keyword Memory Segment) | 1 | `2508.15294` |
| 认知视角记忆片段 (Cognitive Perspective Memory Segment) | 1 | `2508.15294` |
| 神经案例记忆 (Neural Case Memory) | 1 | `2508.16153` |
| 个人经历记忆 (Personal Experience Memory) | 1 | `2508.19005` |
| 领域知识记忆 (Domain Knowledge Memory) | 1 | `2508.19005` |
| 常识推理记忆 (Common Sense Reasoning Memory) | 1 | `2508.19005` |
| Perceptual Memory | 1 | `2508.19236` |
| Cognitive Memory | 1 | `2508.19236` |
| Perceptual-Cognitive Memory | 1 | `2508.19236` |
| External Structured Memory | 1 | `2508.19828` |
| LLM Context Memory | 1 | `2508.19828` |
| 渐进式压缩记忆 (Progressive Compressed Memory) | 1 | `2509.05298` |
| 情感上下文记忆 (Emotional Context Memory) | 1 | `2509.05298` |
| 原始记忆 (Raw Memory) | 1 | `2509.10852` |
| 主观记忆 (Subjective Memory) | 1 | `2509.10852` |
| 叙事记忆 (Narrative Memory) | 1 | `2509.11860` |
| 人物记忆 (Character Memory) | 1 | `2509.11860` |
| Similarity Signal | 1 | `2509.12760` |
| Distance Signal | 1 | `2509.12760` |
| Magnitude Signal | 1 | `2509.12760` |
| High-level Planning Memory | 1 | `2509.12810` |
| Low-level Execution Memory | 1 | `2509.12810` |
| Agent Behavior Trajectories (智能体行为轨迹) | 1 | `2509.13310` |
| Tool Invocation Sequences (工具调用序列) | 1 | `2509.13310` |
| Multi-step Reasoning Chains (多步推理链) | 1 | `2509.13310` |
| Evidence Memory (证据记忆) | 1 | `2509.13312` |
| Dynamic Outline Memory (动态大纲记忆) | 1 | `2509.13312` |
| 合成策略记忆 (Synthetic Strategy Memory) | 1 | `2509.17459` |
| System 1 Intuitive Memory | 1 | `2509.22315` |
| System 2 Deliberative Memory | 1 | `2509.22315` |
| Generative Latent Memory | 1 | `2509.24704` |
| Planning Memory | 1 | `2509.24704` |
| Interaction History Memory | 1 | `2510.00615` |
| Environment Observation Memory | 1 | `2510.00615` |
| Common Knowledge Memory | 1 | `2510.02375` |
| 进化上下文 (Evolving Context) | 1 | `2510.04618` |
| 静态提示 (Static Prompt) | 1 | `2510.04618` |
| 结构化剧本 (Structured Playbook) | 1 | `2510.04618` |
| Orchestrator Memory (编排器记忆) | 1 | `2510.04851` |
| Task Agent Memory (任务代理记忆) | 1 | `2510.04851` |
| Constructivist Agentic Memory (CAM) | 1 | `2510.05520` |
| Hierarchical Schemata Memory | 1 | `2510.05520` |
| Tool Capability Memory (工具能力记忆) | 1 | `2510.06664` |
| Structured Capability Memory (结构化能力记忆) | 1 | `2510.06664` |
| Learnable Memory (可学习记忆) | 1 | `2510.06664` |
| 动态用户画像 (Dynamic User Profiles) | 1 | `2510.07925` |
| Token Prior | 1 | `2510.08191` |
| Reward-Free Interaction Memory (无奖励交互记忆) | 1 | `2510.08558` |
| Continuous Memory (连续记忆) | 1 | `2510.09038` |
| Multimodal Trajectory Memory (多模态轨迹记忆) | 1 | `2510.09038` |
| Explicit Memory (显式记忆) | 1 | `2510.10666` |
| Conclusion Memory (结论记忆) | 1 | `2510.10666` |
| Reasoning Chain Memory (推理链记忆) | 1 | `2510.10666` |
| Curated Memory (策展记忆) | 1 | `2510.12635` |
| Task-Integrated Memory (任务整合记忆) | 1 | `2510.12635` |
| Dynamic Structured Memory (DSM) | 1 | `2510.13363` |
| L0 Microscopic Evidence Memory | 1 | `2510.16392` |
| L1 Mesoscopic Knowledge Memory | 1 | `2510.16392` |
| L2 Macroscopic Profile Memory | 1 | `2510.16392` |
| Scenario Memory | 1 | `2510.21618` |
| Tool Memory | 1 | `2510.21618` |
| Task Trajectory Memory | 1 | `2510.23601` |
| 折叠记忆 (Folded Memory) | 1 | `2510.24699` |
| Compact Memory | 1 | `2511.02805` |
| Full Interaction History | 1 | `2511.02805` |
| Synthetic Experience | 1 | `2511.03773` |
| Abstract State | 1 | `2511.03773` |
| Reasoning-based Feedback | 1 | `2511.03773` |
| Self-Evolving Experience Memory | 1 | `2511.10395` |
| Synthetic Task Memory | 1 | `2511.10395` |
| Active User Profile | 1 | `2511.13593` |
| Interaction Event Record | 1 | `2511.13593` |
| Offline Lightweight Memory | 1 | `2511.18423` |
| Online Deep Research Memory | 1 | `2511.18423` |
| Just-In-Time Compiled Context | 1 | `2511.18423` |
| 对话记忆 | 1 | `2512.01710` |
| Core Memory | 1 | `2512.03627` |
| Experience-Driven Memory | 1 | `2512.10696` |
| Structured Experience Memory | 1 | `2512.10696` |
| 合成实体摘要 (Entity Summaries) | 1 | `2512.12818` |
| 演化信念 (Evolving Beliefs) | 1 | `2512.12818` |
| 令牌级记忆 (Token-level Memory) | 1 | `2512.13564` |
| 潜在级记忆 (Latent Memory) | 1 | `2512.13564` |
| EDU-based Context Memory | 1 | `2512.14244` |
| Structured Discourse Memory | 1 | `2512.14244` |
| Self-Model (自我模型) | 1 | `2512.18202` |
| Creed (不可变信条) | 1 | `2512.18202` |
| Capability List (能力清单) | 1 | `2512.18202` |
| 记忆架构 (Memory Architecture) | 1 | `2512.18746` |
| 元进化记忆系统 (Meta-Evolutionary Memory System) | 1 | `2512.18746` |
| Utility-Enhanced Memory | 1 | `2601.03192` |
| Temporal Memory | 1 | `2601.03236` |
| Causal Memory | 1 | `2601.03236` |
| Entity Memory | 1 | `2601.03236` |
| Flat Memory | 1 | `2601.04726` |

### Parametric Memory (7)

| 概念名称 | 来源论文数 | 来源论文 |
|---------|-----------|---------|
| Parametric Memory (参数化记忆) | 3 | `2508.01832`, `2510.02375`, `2512.03627` |
| Parametric Factual Knowledge | 1 | `2104.08164` |
| 参数化记忆 (Parametric Memory) | 1 | `2410.03439` |
| Non-Parametric Continual Learning | 1 | `2502.14802` |
| Parametric Knowledge (Internal Memory) | 1 | `2508.15253` |
| 非参数化策略记忆 (Non-parametric Strategy Memory) | 1 | `2509.17459` |
| 参数级记忆 (Parametric Memory) | 1 | `2512.13564` |

### Procedural Memory (9)

| 概念名称 | 来源论文数 | 来源论文 |
|---------|-----------|---------|
| 程序记忆 (Procedural Memory) | 2 | `2407.06567`, `2507.07957` |
| Programmatic Skills (Procedural Memory) | 1 | `2504.06821` |
| Procedural Skill Memory | 1 | `2504.07079` |
| 程序性记忆 (Procedural Memory) | 1 | `2508.06433` |
| 技能模式记忆 (Skill Pattern Memory) | 1 | `2508.19005` |
| Procedural Memory | 1 | `2509.24704` |
| Modular Procedural Memory (模块化过程记忆) | 1 | `2510.04851` |
| Procedural Tool Memory (MCP Box) | 1 | `2510.23601` |
| Dynamic Procedural Memory | 1 | `2512.10696` |

### Reflection Memory (2)

| 概念名称 | 来源论文数 | 来源论文 |
|---------|-----------|---------|
| Reflection Memory | 2 | `2304.03442`, `2509.22315` |
| 反思经验 (Reflection Experience) | 1 | `2511.06449` |

### Retrieval Memory (4)

| 概念名称 | 来源论文数 | 来源论文 |
|---------|-----------|---------|
| 生成式检索记忆 (Generative Retrieval Memory) | 1 | `2410.03439` |
| MLP Memory (检索器预训练记忆) | 1 | `2508.01832` |
| Retriever-Pretrained Memory (检索器预训练记忆) | 1 | `2508.01832` |
| Implicit Retrieval Memory | 1 | `2508.09874` |

### Semantic Memory (13)

| 概念名称 | 来源论文数 | 来源论文 |
|---------|-----------|---------|
| Semantic Memory (Knowledge Graph) | 9 | `2407.04363`, `2503.05193`, `2505.16348`, `2508.03341`, `2508.09736` (+4) |
| 语义记忆 (Semantic Memory) | 2 | `2507.07957`, `2509.25911` |
| API 语义记忆 (API Semantic Memory) | 1 | `2307.16789` |
| Global Semantic Memory (Community Summaries) | 1 | `2404.16130` |
| Semantic-Graph Hybrid Memory | 1 | `2405.16089` |
| Implicit Semantic Memory | 1 | `2410.02355` |
| Modality-specific Semantic Memory (OCR/ASR/DET) | 1 | `2411.13093` |
| Semantic Action Memory | 1 | `2504.13805` |
| Semantic Knowledge Memory | 1 | `2504.14603` |
| Semantic Anchored Memory | 1 | `2508.12630` |
| 语义记忆片段 (Semantic Memory Segment) | 1 | `2508.15294` |
| 长期语义巩固记忆 (Long-term Semantic Consolidation Memory) | 1 | `2511.11007` |
| 语义场景 (Semantic Scene) | 1 | `2601.02163` |

### Sensory Memory (4)

| 概念名称 | 来源论文数 | 来源论文 |
|---------|-----------|---------|
| 感官记忆 (Sensory Memory) | 1 | `2207.07115` |
| Sensory Memory (Light1) | 1 | `2510.18866` |
| 感官情境记忆 | 1 | `2512.01710` |
| SensoryMemory | 0 | - |

### Short-Term Memory (8)

| 概念名称 | 来源论文数 | 来源论文 |
|---------|-----------|---------|
| Short-Term Memory (Light2/STM) | 5 | `2310.03052`, `2410.12859`, `2502.00592`, `2510.18866`, `2601.01885` |
| Short-term Memory (STM) | 2 | `2305.13304`, `2512.03627` |
| Short-term Trajectory Memory | 1 | `2308.02151` |
| 短期记忆 (Short-term Memory) | 1 | `2407.01178` |
| Short-term Operation History | 1 | `2410.08164` |
| 短期注意力记忆 (Short-Term Attention Memory) | 1 | `2501.00663` |
| Short-Term Tool Memory | 1 | `2507.21428` |
| 短期感知保留记忆 (Short-term Perception Retention Memory) | 1 | `2511.11007` |

### Working Memory (7)

| 概念名称 | 来源论文数 | 来源论文 |
|---------|-----------|---------|
| Working Memory (工作记忆) | 5 | `2310.03052`, `2508.19236`, `2509.24704`, `2510.12635`, `2510.21618` |
| 工作记忆 (Working Memory) | 3 | `2207.07115`, `2407.06567`, `2512.13564` |
| Active Working Memory | 1 | `2508.04664` |
| 动态工作记忆 (Dynamic Working Memory) | 1 | `2508.10419` |
| 动态上下文工作区 (Dynamic Context Workspace) | 1 | `2510.24699` |
| 短期工作记忆 | 1 | `2512.01710` |
| ShortTermMemory / WorkingMemory | 0 | - |

---

## 九、概念关系网络

### 9.1 is-a 关系

共 **244** 条 is-a 关系，描述概念的实例化与分类。

| 源概念 | 目标概念 | 描述 |
|-------|---------|------|
| KnowledgeEditor | Model Editing Method | KnowledgeEditor is a specific instantiation of model editing without meta-learning pre-training |
| 感官记忆 | 记忆存储类型 | 基于 GRU 隐藏状态的短期瞬态记忆 |
| 工作记忆 | 记忆存储类型 | 存储最近帧高分辨率特征的缓存记忆 |
| 长期记忆 | 记忆存储类型 | 存储压缩原型的持久化记忆 |
| Toolformer | Tool-Enhanced Language Model | Toolformer is a specific instance of a language model augmented with tool usage capabilities. |
| API Call | Token Generation Step | Invoking a tool is treated ontologically as generating a specific sequence of tokens. |
| 言语强化学习 (Verbal RL) | 强化学习范式 (Reinforcement Learning Paradigm) | 通过文本反馈而非数值奖励或权重更新进行优化 |
| Reflection | Memory | Reflections are abstracted higher-order memories derived from raw observations |
| HuaTuo 模型 | 中文医疗大语言模型 | HuaTuo 是专门针对中文医疗领域微调的垂直大模型 |
| SCM Framework | Memory Framework | SCM is a specific framework designed for enhancing LLM memory capabilities |
| Daily Summary | Summarized Memory | Daily summary is a specific type of summarized memory generated from raw dialogue |
| Global Summary | Summarized Memory | Global summary is a high-level abstraction of long-term interaction history |
| Long-term Memory | Memory Type | Stores historical content via vector database for long-range coherence |
| Short-term Memory | Memory Type | Stores recent step summaries for immediate context |
| RET-LLM 记忆 | 外部记忆 | RET-LLM 定义了一种不修改模型内部参数的独立外部记忆类型 |
| 知识三元组 | 知识表示形式 | 基于戴维森语义理论将知识解构为可操作的三元组形式 |
| 记忆槽 | 上下文紧凑表示 | 记忆槽是原始长文本的紧凑向量表示形式，替代原始令牌序列 |
| ICAE | 上下文压缩方法 | ICAE 是一种基于自编码器架构的上下文压缩方法 |
| ToolLLaMA | 指令微调大型语言模型 | ToolLLaMA 是基于 LLaMA 进行工具使用指令微调后的模型实例 |
| DFSDT | 推理算法 | DFSDT 是一种基于深度优先搜索的决策树推理算法 |
| Role Agent | Collaborative Agent | Specific agents (PM, Architect, Engineer) are instances of collaborative agents within the framework. |
| Retrospective Model | Trainable LLM | The retrospective model is defined as a lightweight, trainable LLM (e.g., LongChat-7b) |
| Actor Model | Frozen LLM | The actor model is defined as a frozen, black-box LLM (e.g., GPT-3) |
| 自用备忘录 | 内部记忆机制 | 由模型内部管理而非依赖外部插件的记忆形式 |
| Retrievable Script Memory | Long-term Memory | Script segments serve as externalized long-term knowledge for the character. |
| Dynamic Dialogue History Memory | Short-term Memory | Conversation history functions as temporary short-term context. |
| Recursive Summary Memory | Long-Term Dialogue Memory | Defines a specific implementation of long-term memory via recursive text generation. |
| Lyfe Agents | Generative Agents | Lyfe Agents are a specialized subtype of Generative Agents optimized for resource efficiency |
| Engram | Memory Carrier | Engram is defined as the minimal unit of memory containing content and lifecycle. |
| LLM Core | Operating System Processor | LLM is conceptualized as the CPU kernel managing processes. |
| Main Context | Virtual Memory (RAM) | The limited context window acts as volatile high-speed memory. |
| RepairAgent | Autonomous LLM Agent | RepairAgent is a specialized instantiation of an autonomous agent designed specifically for program repair tasks |
| Domain-specific Memory Pool | Memory Pool | A specialized memory pool restricted to agents within the same domain for optimized sharing |
| Graph RAG | Retrieval-Augmented Generation | Graph RAG is a specialized form of RAG utilizing graph structures. |
| Community Summary | Global Index Unit | Community summaries serve as the fundamental units for global indexing. |
| HippoRAG | 检索增强生成系统 | HippoRAG 是一种专门用于长程推理和知识整合的 RAG 框架 |
| COLT | Tool Retrieval Framework | COLT is a specialized framework for completeness-oriented tool retrieval |
| 知识图谱调优 (KGT) | 参数高效个性化方法 (Parameter-Efficient Personalization) | KGT 被归类为一种无需全量参数更新即可实现模型个性化的方法 |
| 时间敏感长期记忆 | 长期记忆 | 时间敏感长期记忆是长期记忆的一种特殊形式，强调对时间元数据的精确处理能力 |
| Hierarchical Aggregate Tree | Memory Structure | HAT defines a specific tree-based structural form for organizing long-term memory |
| Timeline Memory | Structured Memory | Timeline memory is a specific form of structured memory that organizes events chronologically and causally. |
| 短期记忆 | 显式记忆 | 短期记忆是显式记忆的一种类型，用于处理即时上下文信息 |
| 中期记忆 | 显式记忆 | 中期记忆是显式记忆的一种类型，用于处理会话级信息 |
| 长期记忆 | 显式记忆 | 长期记忆是显式记忆的一种类型，用于处理持久化知识 |
| Episodic Memory | Memory Type | Specific memory type for tracking agent trajectory and specific events |
| Semantic Memory | Memory Type | Specific memory type for storing general knowledge and facts |
| 概念性言语强化 (Conceptual Verbal Reinforcement) | 学习机制 (Learning Mechanism) | 一种替代梯度下降的基于文本的 LLM 智能体优化方法 |
| 可编辑记忆图 (EMG) | 记忆结构 | EMG 是一种专门用于管理动态记忆的特殊图谱结构 |
| AlphaEdit | Knowledge Editing Method | AlphaEdit is a specific instantiation of knowledge editing using null-space constraints |
| Null-Space Constraint | Parameter Update Constraint | Null-space constraint is a type of update restriction to ensure orthogonality |
| 工具检索 (Tool Retrieval) | 文本生成 (Text Generation) | 将传统的检索过程重新定义为模型内部的序列生成任务。 |
| 虚拟令牌 (Virtual Token) | 工具表示 (Tool Representation) | 每个独立的工具被表示为词汇表中的唯一特殊令牌。 |
| Agent S | GUI Interaction Agent | Agent S is instantiated as a specific type of graphical user interface interaction agent. |
| Visual Encoder | Perception Module | The visual encoder functions as a component within the perception layer. |
| Dynamic LLM-Adapted Documentation | Tool Knowledge Memory | Documentation serves as external memory optimized for LLM retrieval and cognition |
| ILM-TR | RAG Mechanism | ILM-TR is a specialized retrieval-augmented generation mechanism with inner loop feedback. |
| STM | Memory Type | Short-Term Memory is a specific type of memory used for intermediate reasoning states. |
| LLM Agent | Social Agent | LLM-driven entities function as social agents within the simulation |
| OASIS | Social Media Simulator | OASIS is a specific instance of a general social media simulation framework |
| Auxiliary Text | External Memory | Auxiliary text generated from video modalities serves as external memory for the LVLM. |
| Imagined Node | Memory Node | Imagined nodes are a specific type of memory node representing unvisited areas generated by simulation |
| Real Node | Memory Node | Real nodes are memory nodes representing visited or current observations |
| Dynamic User Persona | Memory Type | The user persona is conceptualized as a specific type of long-term memory that evolves over time. |
| Embodied VideoAgent | 多模态代理架构 | 该代理是一种结合视觉与具身感知的多模态系统 |
| 持久场景记忆 | 动态记忆结构 | 一种支持随时间更新和查询的记忆形式 |
| Titans | 序列模型 (Sequence Model) | Titans 是一种支持测试时记忆更新的新型序列建模架构 |
| 神经长期记忆 | 记忆模块 (Memory Module) | 一种在推理阶段通过梯度更新权重的特定记忆模块 |
| Temporal Knowledge Graph | Knowledge Graph | Extends standard KG with time validity attributes for edges |
| Zep Memory Layer | Agent Memory Infrastructure | Specialized infrastructure for managing LLM agent long-term memory |
| Short-Term Memory (STM) | Memory Type | STM is a volatile memory type stored on GPU for active processing |
| Long-Term Memory (LTM) | Memory Type | LTM is a persistent memory type stored on CPU for long-term retention |
| Time Series Image | Visual Representation | Time series data transformed into image format serves as a visual representation. |
| Structured Prompt | Textual Representation | Generated statistics and trends serve as textual representation. |
| LM2 | Large Memory Model | LM2 is instantiated as a specific type of Large Memory Model architecture |
| LM2 | Enhanced Transformer Architecture | LM2 extends the standard Decoder-only Transformer with memory capabilities |
| MEXTRA | 黑盒提示词攻击 (Black-box Prompt Attack) | MEXTRA 被定义为一种针对记忆模块的特定黑盒攻击方法 |
| 记忆模块 (Memory Module) | LLM 代理组件 (LLM Agent Component) | 记忆模块是 LLM 代理架构中用于存储历史交互的核心组成部分 |
| Mem2Ego | VLM 增强框架 (VLM Augmentation Framework) | Mem2Ego 是一种专门用于具身导航的视觉语言模型增强架构 |
| 全局到自我对齐记忆 | 增强记忆机制 (Augmented Memory Mechanism) | 一种将全局上下文转化为适配局部视角提示的记忆形式 |
| HippoRAG 2 | Non-Parametric Continual Learning System | HippoRAG 2 is instantiated as a system for non-parametric continual learning in LLMs. |
| Passage Node | Memory Carrier | Passage nodes serve as carriers for contextual information within the memory structure. |
| 虚拟记忆令牌 | 记忆载体 | 虚拟令牌作为记忆信息的物理承载形式，嵌入输入序列中 |
| Query Memory | Memory Module | Query Memory is a specialized type of memory module designed for storing query descriptions. |
| MemQ | KGQA Framework | MemQ is a specific framework instance for Knowledge Graph Question Answering. |
| 交互式回退机制 | 容错机制 | 交互式回退是面向 UI 自动化的一种具体容错实现方式 |
| 决策代理 | 多智能体 | 决策代理是 COLA 框架中多智能体协作的具体实例 |
| Programmatic Skill | Agent Memory Entry | Programmatic skills are a specific type of storable memory entry for agents. |
| Skill API | Procedural Knowledge | Skills encapsulated as code are a form of procedural knowledge memory. |
| SkillWeaver | Self-Improving Agent Framework | The proposed framework is a specific instance of self-improving agent architectures. |
| 动态作弊表 | 测试时学习机制 | 动态作弊表是一种无需微调的测试时学习实现形式 |
| 策略片段 | 记忆载体 | 策略片段是记忆库中存储的基本信息单元 |
| LearnAct | Mobile GUI Agent | LearnAct is a specific implementation of a mobile GUI agent utilizing few-shot demonstration learning. |
| LearnGUI | Demonstration Benchmark | LearnGUI is a benchmark dataset specifically designed for evaluating demonstration-based learning in mobile GUIs. |
| AppAgent | AgentOS Component | AppAgent is a specialized execution component within the AgentOS runtime. |
| HostAgent | Control Plane | HostAgent functions as the central control and scheduling unit. |
| 图基于记忆 | 长期记忆 | 图基于记忆是长期记忆的一种增强型结构化实现形式 |
| Limited Memory Language Model (LmLm) | Language Model | LmLm is a specialized type of language model with decoupled memory architecture. |
| User Profile Memory | Structured Memory | User profile memory is implemented as a structured hierarchical knowledge graph rather than unstructured text |
| CoMEM | Memory Mechanism | CoMEM is a specific type of external memory mechanism designed for Vision-Language Models |
| Intent-Driven Memory | Long-term Memory | Intent-Driven Memory is a specialized form of long-term memory focused on task goals. |
| Alita | Generalist Agent | Alita is instantiated as a Generalist Agent capable of scalable reasoning. |
| Task-related MCP | External Capability | Model Context Protocols function as structured external capabilities stored in memory. |
| 达尔文哥德尔机 | 自我改进代理系统 | DGM 是一种具体的自我改进代理系统实现，结合了进化论与哥德尔机理论 |
| 实证验证 | 有益性证明方法 | 用实证测试替代理论证明来确认修改的有益性，是哥德尔机的实践变体 |
| Historical Context | Memory | Historical generated frames are explicitly treated as long-term memory for consistency |
| Insight Graph | Memory Structure | Represents high-level abstract knowledge storage within the hierarchy |
| Interaction Graph | Memory Structure | Represents fine-grained collaboration trajectory storage within the hierarchy |
| Compressed Internal State | Memory Representation | The internal state serves as a compressed, constant-size form of memory representation. |
| MemAgent | Memory Agent System | MemAgent is a specific implementation of a memory agent designed for long-context LLMs |
| Overwrite Strategy | Memory Operation | Overwrite is a specific type of operation defined to manage memory capacity and prevent infinite growth |
| Agent KB | Universal Memory Infrastructure | Agent KB is defined as a universal infrastructure enabling memory sharing across heterogeneous agent frameworks. |
| Planning Seeds | Cross-Domain Experience | Planning seeds are a specific subtype of cross-domain experience used for workflow guidance. |
| 核心记忆 | LLM 智能体记忆类型 | 核心记忆是一种高优先级持久化记忆类型，存储人设与基本事实 |
| 情景记忆 | LLM 智能体记忆类型 | 情景记忆是一种时间戳事件日志型记忆 |
| 语义记忆 | LLM 智能体记忆类型 | 语义记忆是一种抽象知识与关系型记忆 |
| 程序记忆 | LLM 智能体记忆类型 | 程序记忆是一种目标导向流程型记忆 |
| Autonomous Mode | Memory Management Mode | Agent fully controls memory operations |
| Workflow Mode | Memory Management Mode | System deterministically controls memory operations |
| Hybrid Mode | Memory Management Mode | System removes tools, Agent searches tools |
| Episode Layer | Concrete Memory Content | Stores specific dialogue content and user profiles |
| Trace Layer | Meta-Memory | Records interaction frequency and memory weights |
| MLP Memory | Parametric Memory | MLP Memory 是一种参数化记忆形式，将检索行为内化到模型参数中 |
| MLP Memory | Memory Enhancement Module | MLP Memory 是大型语言模型的知识增强模块 |
| Episodic Memory | Agent Memory | Stores detailed interaction details and context |
| Semantic Memory | Agent Memory | Stores distilled knowledge and abstracted facts |
| Active Context Management | Cognitive Agency Mechanism | ACM is defined as a specific implementation of cognitive agency in LLMs. |
| 专家模型 | 策略模型 | 专家模型是单软件优化后的策略模型实例 |
| 通才模型 | 策略模型 | 通才模型是泛化后的策略模型实例 |
| Optimal Context Routing Problem | 0/1 Knapsack Problem | The paper formalizes the context routing optimization as a combinatorial knapsack problem. |
| 抽象脚本 | 程序性记忆 | 抽象脚本是程序性记忆的一种高层泛化形式 |
| 原始轨迹 | 程序性记忆 | 原始轨迹是程序性记忆的具体执行记录形式 |
| Memory Decoder | Memory Module | The proposed component functions as a specialized memory unit for LLMs |
| Memory Decoder | Transformer Decoder | Implemented using a small Transformer decoder architecture |
| ComoRAG | 状态化 RAG 框架 | ComoRAG 是一种支持状态化推理的检索增强生成框架 |
| 动态记忆工作区 | 记忆结构 | 动态记忆工作区是存储推理中间状态与证据的记忆结构 |
| Semantic Anchored Memory | Agentic Memory | Semantic Anchored Memory is a specialized type of Agentic Memory grounded in linguistic structures. |
| Conflict-Aware Soft Prompting | Prompt Tuning Method | CARE is defined as a specific type of soft prompting technique designed for conflict resolution |
| M-MDP | 马尔可夫决策过程 (MDP) | M-MDP 是引入记忆增强机制的专用马尔可夫决策过程 |
| 自演进智能代理 | 智能代理 | 自演进代理是具有终身学习能力的特殊智能代理类型 |
| 经验驱动终身学习框架 | 终身学习框架 | ELL 框架是基于经验驱动的特定终身学习框架 |
| StuLife 基准 | 智能代理评估基准 | StuLife 是专门用于评估自演进代理的特定基准 |
| Perceptual-Cognitive Memory | Temporal Memory Mechanism | A specialized memory mechanism for VLA models handling temporal dependencies |
| Memory Management Agent | LLM Agent | Specialized agent responsible for executing memory operations |
| Answer Agent | LLM Agent | Specialized agent responsible for reasoning based on filtered memory |
| Livia 系统 | 情感感知 AR 伴侣 | Livia 被定义为一种特定类型的增强现实情感陪伴系统 |
| TBC/DIMF | 记忆压缩算法 | 两种核心算法属于记忆压缩技术范畴 |
| 推理记忆 | 情景记忆 | 推理记忆是经过预存储推理增强后的高级情景记忆形式 |
| 事实记忆 | 结构化记忆片段 | 事实记忆是结构化记忆片段的一种具体分类类型 |
| 叙事记忆 | 长期记忆 | 叙事记忆是专注于情节发展的长期记忆类型 |
| 人物记忆 | 长期记忆 | 人物记忆是专注于用户画像与属性的长期记忆类型 |
| SDM Activation | Activation Function | SDM is a novel activation function designed to replace Softmax for uncertainty modeling |
| High-level Planning Memory | Memory Component | High-level memory is a specific type of memory component focused on planning insights. |
| Low-level Execution Memory | Memory Component | Low-level memory is a specific type of memory component focused on execution details. |
| AgentFounder-30B | Deep Research Agent | AgentFounder-30B 是深度研究智能体的具体实现 |
| Agentic CPT | Continual Pre-training Method | 智能体持续预训练是持续预训练方法的智能体专用变体 |
| Planner Agent | Research Agent | 规划者智能体是研究智能体的一种，负责动态规划 |
| Writer Agent | Research Agent | 写作者智能体是研究智能体的一种，负责分层写作 |
| Open-Ended Deep Research | Knowledge Work Task | 开放式深度研究是知识工作任务的一种特定形式 |
| 合成策略记忆 | 非参数记忆 | 记忆存储于模型参数之外的外部介质中，而非权重内 |
| System 1 | Fast Thinking Memory | System 1 represents the fast, intuitive memory access mode |
| System 2 | Slow Thinking Memory | System 2 represents the slow, deliberative memory construction mode |
| Generative Latent Memory | Memory Paradigm | A new memory paradigm that internalizes memory as latent tokens rather than external retrieval |
| Planning Memory | Generative Latent Memory | An evolved functional form of generative latent memory |
| 推理记忆 | 智能体记忆 | 推理记忆是智能体记忆的一种特殊类型，存储可泛化的推理策略而非原始轨迹 |
| 经验池 | 临时记忆存储 | 经验池是用于暂存生成经验的临时记忆存储结构 |
| 记忆构建策略 | 强化学习策略 | 将记忆管理决策建模为可优化的 RL 策略而非固定规则 |
| Compressed Context | Reduced Memory Representation | Compressed context is defined as a token-reduced semantic version of the original memory |
| Student Compressor | Lightweight Memory Processor | The distilled model functions as an efficient unit for processing memory inputs |
| Hierarchical Memory Bank | Parametric Memory | The memory bank is a specific implementation of parametric memory storing knowledge as weights |
| 进化上下文 | 上下文记忆 | 一种随时间动态演化的上下文记忆形式 |
| 条目化子弹点 | 记忆结构 | 用于存储记忆单元的具体结构化格式 |
| Orchestrator Memory | Procedural Memory | 编排器记忆是过程记忆的一种特定类型，用于规划 |
| Task Agent Memory | Procedural Memory | 任务代理记忆是过程记忆的一种特定类型，用于执行 |
| CAM | Agentic Memory | CAM is a specific instantiation of agentic memory grounded in constructivist theory |
| Schemata | Memory Structure | Schemata represents the hierarchical organizational structure of memory |
| Tool Capability Memory | Learnable Memory | 工具能力记忆是一种可学习记忆类型，支持动态演进 |
| Structured Capability Memory | Tool Capability Memory | 结构化能力记忆是工具能力记忆的具体实现形式 |
| 持久记忆 | 长期交互机制 | 持久记忆是实现长期交互的一种具体记忆类型 |
| 动态用户画像 | 个性化记忆载体 | 用户画像是承载个性化信息的动态记忆形式 |
| Training-Free GRPO | Policy Optimization Method | A variant of GRPO that operates without parameter updates |
| Token Prior | Soft Constraint | Guides model behavior through input modulation rather than weight changes |
| Early Experience | Learning Paradigm | Defines a new paradigm bridging imitation learning and reinforcement learning |
| Multimodal Trajectory | Memory Carrier | Multimodal trajectories serve as the raw carrier for memory storage |
| BrowserAgent | Web Agent | BrowserAgent 是一种基于原生浏览器交互的网页智能体 |
| Explicit Memory | Memory Mechanism | 显式记忆是一种支持长推理链的记忆机制 |
| Conclusion Tag | Memory Structure | 结论标签是一种结构化的记忆存储形式 |
| Memory Action | Learnable Policy Action | 记忆动作被定义为可学习的策略动作，而非固定规则 |
| Working Memory | MDP State | 工作记忆被建模为马尔可夫决策过程中的状态表示 |
| Dynamic Structured Memory | Memory Maintenance Module | DSM is a specific implementation of a memory maintenance module using structured graphs |
| Reasoning Tree | Response Generation Component | RT acts as the reasoning engine within the response generation phase |
| L1 Mesoscopic Knowledge Memory | Memory Structure | L1 is a specific type of memory structure represented as a dynamic knowledge graph |
| Renormalization Operators | Memory Operations | Renormalization operators are specific operations driving memory evolution across scales |
| LightMem | Memory-Augmented Generation System | LightMem is instantiated as a lightweight memory-augmented generation system. |
| Sensory Memory | Memory Layer | Sensory Memory is defined as the first stage memory layer processing raw input. |
| DeepAgent | General Reasoning Agent | DeepAgent is instantiated as a general reasoning agent capable of handling scalable toolsets. |
| ToolPO | Reinforcement Learning Strategy | ToolPO is defined as a specific RL strategy for tool call advantage attribution. |
| Abstract MCP | Reusable Tool | Abstracted MCPs are generalized tools capable of cross-task reuse. |
| Specialized Agent | Self-Evolving Generative Agent | The specialized agent is a refined instance of the self-evolving framework. |
| 细粒度浓缩 | 折叠操作 | 一种保留关键细节的特定折叠类型 |
| 深度整合 | 折叠操作 | 一种抽象多步子任务的特定折叠类型 |
| MemSearcher | Search Agent | MemSearcher is a specific type of search agent optimized for memory management. |
| Compact Memory | Memory | Compact Memory is a specialized form of memory retaining only necessary information. |
| Synthetic Experience | Training Data | Synthesized trajectories are treated as valid training data for RL agents |
| 结构化经验 | 经验类型 | 结构化经验是一种可检索、可继承的经验类型 |
| 反思经验 | 经验类型 | 反思经验是对成功/失败轨迹的自然语言总结 |
| Self-Evolving Agent System | Reinforcement Learning Agent System | AgentEvolver is defined as a specialized RL agent system capable of autonomous evolution without heavy human annotation. |
| 短期感知保留记忆 | 记忆类型 | 定义用于细粒度感知保留的特定记忆类型 |
| VisMem 框架 | 记忆架构 | 定义整体系统架构 |
| User Profile Layer | Memory Component | Stores static and dynamic user attributes for personalization |
| Event Record Layer | Memory Component | Stores thematic interaction context for consistency |
| EMem-G | EMem | EMem-G is a graph-enhanced variant of the base EMem framework designed for complex reasoning tasks |
| GAM Framework | Agentic Memory System | GAM is a specific implementation of a general agentic memory system. |
| Concise Snapshot | Offline Lightweight Memory | Snapshots are a form of offline memory. |
| 对话记忆 | 记忆模块 | 五层记忆分类体系中的基础交互记录类型 |
| 长期用户记忆 | 记忆模块 | 存储加密用户生物特征与偏好的持久化类型 |
| 短期工作记忆 | 记忆模块 | 会话内基于 Token 缓冲区的临时记忆类型 |
| Visual Memory | Memory Type | Stores raw scene detail information to prevent text abstraction loss |
| Long-term Memory (LTM) | Memory Type | LTM is a specific type of memory for structured experience storage |
| Short-term Memory (STM) | Memory Type | STM is a specific type of memory for recent context capture |
| Multimodal Knowledge Graph (MMKG) | Memory Structure | MMKG is the structural form of Long-term Memory |
| MemLoRA | On-Device Memory System | MemLoRA is defined as a specialized memory system designed for edge device deployment. |
| Dynamic Procedural Memory | Memory System | A specialized memory system for agent experience management |
| Keypoint-level Experience | Experience Structure | Fine-grained experience representation at key point level |
| Utility-based Deletion | Memory Operation | Operation for removing low-utility experiences |
| Session Summary | Episodic Memory | Session summaries represent specific event-based episodic memory. |
| Knowledge Triple | Semantic Memory | Extracted triples represent general fact-based semantic memory. |
| 演化信念 | 记忆类型 | 演化信念是四逻辑网络中定义的一种特定记忆内容类型 |
| 保留 | 记忆操作 | 保留是管控信息添加到记忆库的核心操作之一 |
| 令牌级记忆 | 记忆形式 | 令牌级记忆是记忆形式的一种，存储于上下文窗口 |
| 事实记忆 | 记忆功能 | 事实记忆是记忆功能的一种，用于知识检索 |
| 记忆形成 | 记忆动态 | 记忆形成是记忆动态生命周期中的一个阶段 |
| Elementary Discourse Unit | Atomic Context Unit | EDU is defined as the minimal semantic unit for context memory representation |
| System 3 | Meta-Cognitive Layer | System 3 is defined as the executive meta-cognitive core beyond System 1/2. |
| Persistent Agent | Artificial Life | Persistent agents with identity continuity are categorized as a form of Artificial Life. |
| 元进化记忆系统 | 代理记忆系统 | MemEvolve 是一种支持自我进化的代理记忆系统 |
| 经验知识 | 记忆内容 | 经验知识是记忆系统中可进化的内容类型 |
| 记忆架构 | 系统组件 | 记忆架构是记忆系统的结构化组件集合 |
| Agentic Memory | Memory Management System | Defines memory management as an integrated system specifically for agents |
| MemCells | 原子记忆单元 | MemCells 是捕捉情节痕迹和原子事实的基本单元 |
| MemScenes | 主题化语义结构 | MemScenes 是组织 MemCells 形成的主题化知识结构 |
| MemRL Memory | Episodic Memory | MemRL memory is a specific type of episodic memory enhanced with utility values for decision making |
| Intent-Experience-Utility Triplet | Memory Structure | The triplet is the specific structured representation used for memory storage in MemRL |
| Causal Memory | Memory Type | Memory type representing logical implications and dependencies |
| Event-Centric Memory | Agent Memory Mechanism | A specialized memory type organizing experience as discrete events rather than continuous text |

### 9.2 part-of 关系

共 **258** 条 part-of 关系，描述概念的组成结构。

| 源概念 | 目标概念 | 描述 |
|-------|---------|------|
| Weight Update | Edited Model State | The update vector is part of the new model configuration |
| 记忆原型 | 长期记忆 | 长期记忆由经过压缩和增强的原型集合组成 |
| API Response | Generation Context | The result returned by the tool becomes part of the input context for subsequent generation. |
| 自我反思 (Self-Reflection) | Reflexion 框架 (Reflexion Framework) | 核心组件，负责从失败轨迹中生成改进建议 |
| Memory Stream | Generative Agent Architecture | The memory stream serves as the central repository within the agent architecture |
| SUS 指标 | 医疗模型评估体系 | 安全性、可用性、流畅度是评估医疗模型的核心组成部分 |
| Memory Controller | SCM Framework | Controller is a core component responsible for dynamic decision making |
| Memory Stream | SCM Framework | Stream is the storage component within the framework |
| LLM-based Agent | SCM Framework | Agent is the main processing unit within the framework |
| MemoryBank | LLM System | MemoryBank acts as an external enhancement module for the LLM system |
| Memory Strength | Memory Update Mechanism | Memory strength is a core parameter within the dynamic update mechanism |
| Short-term Memory | Generation Context | Short-term memory is integrated into the prompt context |
| Long-term Memory | Generation Context | Retrieved long-term memory is integrated into the prompt context |
| 控制器 (Controller) | RET-LLM 架构 | 负责拦截 LLM 指令并执行记忆操作的核心组件 |
| 记忆模块 (Memory) | RET-LLM 架构 | 负责存储和检索三元组的功能模块 |
| 记忆槽 | 解码器输入序列 | 记忆槽替代原始文本作为解码器 Transformer 层的输入部分 |
| LoRA 适配器 | 编码器架构 | LoRA 是编码器中用于学习从文本到记忆槽压缩映射的可训练组件 |
| API 调用 | 解决方案路径 | 单次 API 调用是完成复杂任务解决方案路径的组成单元 |
| ToolBench | ToolLLM 框架 | ToolBench 数据集是 ToolLLM 框架数据构建阶段的核心产物 |
| SOP | Prompt Sequence | Standard Operating Procedures are encoded as parts of the prompt sequence. |
| Short-term Memory | Memory Module | Short-term memory storing current trajectory is a component of the central Memory Module |
| Reflection | Prompt Input | Generated reflections are inserted as part of the input prompt for the Actor |
| 备忘录撰写 | 三阶段记忆循环 | 将对话历史总结为备忘录的初始阶段 |
| 备忘录检索 | 三阶段记忆循环 | 根据查询匹配相关证据的中间阶段 |
| System Prompt | Context Construction | System prompts are a component of the input context construction process. |
| Memory Update Module | Dual-Role Architecture | The memory update process is a distinct component within the overall system architecture. |
| Summarize-and-Forget Mechanism | Memory System | The mechanism is a core component managing the lifecycle of agent memories |
| Option-Action Framework | Decision System | The framework structures the low-cost decision-making process |
| Working Memory | Memoria Architecture | WM serves as the input buffer and retrieval cue within the hierarchy. |
| Short-Term Memory | Memoria Architecture | STM acts as an intermediate layer between WM and LTM. |
| Long-Term Memory | Memoria Architecture | LTM stores infinite capacity memory as a graph structure. |
| FIFO Message Queue | Main Context | The queue is a component within the primary context window. |
| Queue Manager | System Layer | The manager module resides in the system control layer. |
| Retriever Layer | INMS Framework | Component responsible for memory retrieval and continuous updates within the system |
| Entity/Relation | Graph Index | Entities and relations constitute the nodes and edges of the graph index. |
| Community | Graph Structure | Communities are modular substructures within the overall graph. |
| 知识图谱 | 离线索引阶段 | 知识图谱在离线阶段构建并作为核心存储组件 |
| Collaborative Learning Stage | COLT Framework | The collaborative learning stage is a key component of the two-stage COLT architecture |
| 事实知识三元组 | 外部知识图谱 | 三元组是构成个性化知识图谱的基本单元 |
| 链式表操作 | 元数据检索模块 | 链式表操作是元数据检索模块的核心实现机制，用于过滤表格行 |
| Leaf Node | Hierarchical Aggregate Tree | Raw dialogue fragments are stored as leaf nodes within the tree |
| Root Node | Hierarchical Aggregate Tree | Global summary is stored as the root node of the tree |
| TeaBag Dataset | TeaFarm Evaluation | TeaBag is the specific dataset constructed for use within the TeaFarm counterfactual evaluation pipeline. |
| 记忆存储池 | 显式记忆模块 | 记忆存储池是显式记忆模块的核心组成部分 |
| 记忆检索器 | 显式记忆模块 | 记忆检索器是显式记忆模块的功能组件 |
| 显式记忆模块 | 语言模型架构 | 显式记忆模块可插拔集成到现有 LLM 架构中 |
| Knowledge Graph | AriGraph Memory Core | The core data structure constituting the memory module |
| Triple | Knowledge Graph | Basic unit composing the graph structure |
| 分析师智能体组 (Analyst Agents) | 智能体层 (Agent Layer) | 处理特定多模态数据流的专业智能体 |
| 风控组件 (Risk Control Component) | 控制层 (Control Layer) | 监控 CVaR 并触发反思机制 |
| 记忆类型层 (MTL) | 可编辑记忆图 (EMG) | MTL 是 EMG 架构中的顶层分层结构 |
| 记忆子类层 (MSL) | 可编辑记忆图 (EMG) | MSL 是 EMG 架构中的中间分层结构 |
| Projection Matrix | AlphaEdit Update Process | Projection matrix is a core component calculated during the update process |
| 虚拟令牌 (Virtual Token) | 扩展词表 (Extended Vocabulary) | 工具对应的虚拟令牌作为模型扩展词表的一部分存在。 |
| Action Executor | Agent Framework | The execution module is a constituent part of the overall agentic framework. |
| Documentation Rewriting | DRAFT Framework | Core phase responsible for updating memory content based on learned experience |
| Summary Tree | Retriever Module | The summary tree constitutes the core indexing structure of the retriever. |
| Inner Loop Query | ILM-TR Architecture | The inner loop query mechanism is a core component of the ILM-TR system. |
| Recommendation System | OASIS Framework | RecSys is a core module within the OASIS architecture |
| Action Space | Agent Interaction Model | 21 defined actions constitute the interaction capabilities |
| Retrieved Context | Final Input Context | Retrieved auxiliary text is concatenated with video frames to form the final input. |
| Hybrid Memory Map | Real Node | The hybrid memory map is composed of real nodes representing observed space |
| Hybrid Memory Map | Imagined Node | The hybrid memory map is composed of imagined nodes representing unobserved space |
| Demographics/Preferences | Learnable Persona Dictionary | Specific user attributes form the entries within the structured persona dictionary. |
| 深度/姿态数据 | 具身传感器输入 | 传感器数据的具体模态组成 |
| VLM 记忆更新器 | Embodied VideoAgent 架构 | 更新模块是整体代理架构的组成部分 |
| 神经长期记忆 | Titans 架构 | 神经长期记忆是 Titans 架构的核心组件之一 |
| 持久记忆 | Titans 架构 | 持久记忆作为静态参数组件存在于架构中 |
| Episode | Raw Data Ingestion | Episodes serve as the fundamental input units for memory construction |
| Graphiti | Zep Architecture | Graphiti is the core engine component within the Zep system |
| Long-Term Memory (LTM) | M+ Architecture | LTM is a core component of the M+ scalable memory architecture |
| Co-trained Retriever | M+ Architecture | Retriever is a module within M+ for accessing LTM |
| Retrieval-Augmented Learner (RAL) | Time-VLM Architecture | RAL is a core component responsible for temporal dependency capture. |
| Visual-Augmented Learner (VAL) | Time-VLM Architecture | VAL is a core component responsible for visual pattern extraction. |
| Text-Augmented Learner (TAL) | Time-VLM Architecture | TAL is a core component responsible for semantic text extraction. |
| Memory Bank | LM2 Architecture | The independent memory bank is a core component of the LM2 system |
| Gating Mechanisms | Memory Update Process | Input, Output, and Forget gates constitute the memory update logic |
| 查询 - 解决方案对 (Query-Solution Pair) | 记忆内容 (Memory Content) | 用户交互对构成了记忆模块存储的基本数据单元 |
| 自适应检索机制 | Mem2Ego 架构 | 负责从全局记忆中提取任务相关线索的核心组件 |
| 全局记忆模块 | Mem2Ego 架构 | 存储环境语义或拓扑信息的基础组件 |
| Phrase Nodes | Hybrid Knowledge Graph | Phrase nodes constitute the semantic entity layer of the hybrid graph. |
| Passage Nodes | Hybrid Knowledge Graph | Passage nodes constitute the contextual layer of the hybrid graph. |
| 层次化压缩 | R3Mem 框架 | 层次化压缩是框架的核心处理模块，负责从文档级到实体级的信息编码 |
| Query Memory | MemQ Architecture | Query Memory is a core component within the MemQ system architecture. |
| Rule Decomposition | Memory Construction Process | Rule-based decomposition is a sub-process involved in constructing the memory content. |
| 决策代理池 | COLA 框架 | 代理池是框架的核心组成部分，支持插件化扩展 |
| 记忆单元 | 决策代理 | 每个决策代理配备独立的记忆单元以实现自进化 |
| Verification Module | ASI Framework | The verification module is a core component of the Agent Skill Induction framework. |
| Skill Library | SkillWeaver Architecture | The library is a core component storing synthesized skills within the framework. |
| Skill Synthesis | Self-Improvement Loop | Synthesis is a phase within the iterative exploration-synthesis-optimization cycle. |
| 记忆检索模块 | 动态作弊表架构 | 检索模块是动态作弊表系统的核心组件之一 |
| 策展片段 | 动态记忆库 | 经过筛选的片段构成了动态记忆库的内容 |
| DemoParser | LearnAct Framework | DemoParser is the offline knowledge extraction module within the LearnAct architecture. |
| KnowSeeker | LearnAct Framework | KnowSeeker is the online retrieval module responsible for fetching relevant demonstrations. |
| ActExecutor | LearnAct Framework | ActExecutor is the decision-making module that executes tasks using retrieved knowledge. |
| Puppeteer | Execution Layer | Puppeteer orchestrates GUI and API actions within the execution layer. |
| PiP Session | Isolation Environment | Picture-in-Picture session constitutes the isolated execution environment. |
| 记忆巩固 | 记忆写入流程 | 记忆巩固是记忆写入流程中的核心子步骤，负责合并与更新信息 |
| External Knowledge Database | LmLm System | The external database functions as an integral component of the overall LmLm architecture. |
| Element | Knowledge Type | Specific knowledge elements belong to specific knowledge types within the user profile hierarchy |
| Compressed Vectors | Memory Structure | Compressed continuous vectors form the fundamental structural unit of the memory |
| Missing-Slot Guided Filtering | Two-Stage Memory Selection | Filtering is the second stage of the MemGuide selection process. |
| Self-Evolution Component | Alita Agent | The self-evolution mechanism is an integral part of the Alita agent architecture. |
| 开放式进化机制 | 达尔文哥德尔机 | 开放式进化是 DGM 的核心运行机制，负责探索搜索空间 |
| 代理档案库 | 达尔文哥德尔机架构 | 档案库是存储历史有效代理版本的组件，支持多样性保持 |
| Retrieved Key Context | Global Context | Selected frames via retrieval are a subset of the full history context |
| Insight Graph | G-Memory Architecture | One of the three core tiers constituting the hierarchical memory system |
| Interaction Trajectories | Interaction Graph | Raw data content stored and organized within the interaction layer |
| State Consolidation | Reasoning Process | Memory consolidation is treated as an integral part of the reasoning process rather than a separate module. |
| External Memory Module | MemAgent Architecture | The external memory module is a core component within the MemAgent system architecture |
| Text Segments | Long-Context Input | Long context inputs are decomposed into text segments for processing |
| Disagreement Gate | Hybrid Retrieval Engine | The disagreement gate is a functional component within the retrieval process designed to filter interfering knowledge. |
| 元记忆管理器 | 三层代理架构 | 元记忆管理器是三层代理工作流的第一层，负责分析输入并路由 |
| 专用记忆管理器 | 三层代理架构 | 六个专用记忆管理器并行更新各自负责的记忆组件 |
| 对话代理 | 三层代理架构 | 对话代理负责自然语言交互和主动检索执行 |
| Tool Context | LLM Input Context | Tools occupy a portion of the context window |
| Memory Management Module | LLM Agent Architecture | Module manages tool lifecycle within agent |
| Domain Layer | H-MEM Architecture | Top-level macro topic division |
| Category Layer | H-MEM Architecture | Second-level topic classification |
| Trace Layer | H-MEM Architecture | Third-level weight and frequency recording |
| Episode Layer | H-MEM Architecture | Bottom-level specific content storage |
| MLP 记忆模块 | LLM 推理架构 | MLP 记忆模块通过概率插值集成到基础 LLM 解码器中 |
| 概率插值机制 | 记忆集成机制 | 概率插值是连接 MLP 输出与 LLM 输出的核心集成方式 |
| Boundary Detection | Input Processing | Identifies semantic shifts to segment memory |
| Prediction-Calibration | Memory Evolution | Updates knowledge base based on prediction error |
| Reversible Tool | Sculptor Framework | Six reversible tools constitute the core management suite of the architecture. |
| 世界状态模型 | SEAgent 架构 | WSM 是自进化架构中的核心评估组件 |
| 软件指南记忆 | 课程生成器 | 指南记忆是课程生成器维护的核心知识储备 |
| Structured Memory Bank | Multi-Agent LLM System | The memory bank is a core component of the proposed multi-agent architecture. |
| 记忆构建模块 | Memp 框架 | 构建模块是 Memp 框架的核心组成部分 |
| 记忆检索模块 | Memp 框架 | 检索模块是 Memp 框架的核心组成部分 |
| 记忆更新模块 | Memp 框架 | 更新模块是 Memp 框架的核心组成部分 |
| Structured Memory Template | Context Construction | Templates form the high-priority part of the input context |
| Memorization Process | M3-Agent Architecture | Parallel process responsible for perception and memory updating |
| Control Process | M3-Agent Architecture | Parallel process responsible for instruction interpretation and task execution |
| Memory Decoder | Inference Pipeline | Inserted between input and main LLM during inference without modifying main weights |
| 探索性探针生成 | 核心推理引擎 | 探索性探针生成是核心推理引擎的关键组件 |
| 知识巩固 | 迭代推理循环 | 知识巩固是迭代推理循环中的关键步骤 |
| Dependency Parse Triples | Structured Memory Entry | Dependency triples constitute the syntactic component of a structured memory entry. |
| Coreference Chains | Structured Memory Entry | Coreference chains constitute the entity linking component of a structured memory entry. |
| Context Assessor | CARE Framework | The assessor module is a core component within the proposed CARE architecture |
| 记忆重写机制 | 记忆更新过程 | 记忆重写是记忆库根据环境反馈进行更新的核心组成部分 |
| 经验探索模块 | ELL 框架 | 经验探索是 ELL 框架的四层架构之一 |
| 长期记忆系统 | ELL 框架 | 长期记忆系统是 ELL 框架的核心组成部分 |
| 技能学习引擎 | ELL 框架 | 技能学习引擎是 ELL 框架的能力提升模块 |
| 知识内化机制 | ELL 框架 | 知识内化机制是 ELL 框架的最终转化模块 |
| PCMB | MemoryVLA Architecture | The core memory storage component within the MemoryVLA framework |
| Perceptual Tokens | Working Memory | Fine-grained visual details stored in short-term working memory |
| Memory Operations | Memory Management Process | Operations constitute the actionable steps of management |
| External Memory | Memory-R1 Architecture | Core component serving as shared state for dual agents |
| 记忆管理代理 | 模块化 AI 系统 | 记忆模块是四大核心 AI 代理之一 |
| 情感分析模块 | 模块化 AI 系统 | 情感分析是系统核心功能组件 |
| 预存储推理 | 离线记忆构建阶段 | 预存储推理是离线记忆构建阶段的核心处理操作 |
| 记忆检索 | 在线推理生成阶段 | 记忆检索是在线推理生成阶段获取上下文的关键步骤 |
| 叙事总结分支 (NSB) | MOOM 框架 | 叙事总结分支是 MOOM 双分支架构的核心组成部分 |
| 竞争 - 抑制遗忘机制 | MOOM 框架 | 遗忘机制是 MOOM 记忆维护模块的关键组件 |
| Similarity Signal | SDM Signal Decomposition | Similarity is one of the three core components of the SDM framework |
| Distance Signal | SDM Signal Decomposition | Distance is one of the three core components of the SDM framework |
| Magnitude Signal | SDM Signal Decomposition | Magnitude is one of the three core components of the SDM framework |
| High-level Planning Memory | Hierarchical Memory Architecture | High-level memory is a constituent part of the hierarchical architecture. |
| Low-level Execution Memory | Hierarchical Memory Architecture | Low-level memory is a constituent part of the hierarchical architecture. |
| Agentic CPT | Agent Training Pipeline | 智能体持续预训练是智能体训练管道的核心阶段 |
| SFT/RL | Post-training Stage | SFT 和 RL 是后训练阶段的对齐方法 |
| Evidence Chunk | Evidence Memory Bank | 证据块是证据记忆库的组成部分 |
| Outline Section | Dynamic Outline | 大纲章节是动态大纲的组成部分 |
| When/Should/Rather/Because 子句 | 原则 (Principle) | 四个子句共同构成一个完整的结构化策略原则单元 |
| Planning Agent | System 2 Memory Process | Planning is a component of the deep reasoning memory construction |
| Reflection Agent | Memory Control Mechanism | Reflection agent controls the switch between memory types |
| Memory Trigger | MemGen Architecture | Component that monitors reasoning state to decide memory access |
| Memory Weaver | MemGen Architecture | Component that constructs latent token sequences based on current state |
| ReasoningBank | 智能体自我进化框架 | ReasoningBank 是智能体自我进化框架的核心记忆组件 |
| MaTTS | ReasoningBank 架构 | 记忆感知测试时缩放模块是 ReasoningBank 架构的关键组成部分 |
| 核心记忆 | 混合记忆系统 | 核心记忆是混合记忆系统的长期稳定事实组件 |
| 情景记忆 | 混合记忆系统 | 情景记忆是混合记忆系统的交互历史片段组件 |
| 语义记忆 | 混合记忆系统 | 语义记忆是混合记忆系统的抽象知识组件 |
| Compression Guidelines | Offline Optimization Phase | Guidelines are generated and iteratively optimized within the offline training stage |
| Contrastive Feedback | Guideline Update Mechanism | Feedback derived from success/failure pairs drives the iteration of compression instructions |
| Feed-Forward Memory Blocks | Hierarchical Memory Bank | Small memory blocks constitute the larger hierarchical bank structure |
| Curator (策展者) | ACE 框架 | 负责整合更新到上下文的代理组件 |
| 洞察 (Insight) | 上下文条目 | 提取并存储在条目中的知识单元 |
| Memory Units | Task Trajectories | 记忆单元是任务轨迹分解后的组成部分 |
| LEGOMem Framework | Multi-agent LLM Systems | LEGOMem 是多智能体 LLM 系统的增强组件 |
| Low-level Unit | High-level Abstraction | Low-level units can be part of multiple high-level abstractions simultaneously (Many-to-Many mapping) |
| Memory Induction | Training Phase | 记忆诱导是记忆构建阶段的核心模块 |
| RAG Retrieval | Inference Phase | 检索增强是任务求解阶段的关键组件 |
| Retrieve-Refine Mechanism | Memory Update | 检索 - 精炼机制是记忆更新的核心流程 |
| 多源检索模块 | LLM 代理控制单元 | 检索模块是代理控制单元的核心组成部分 |
| 自验证模块 | 系统架构 | 自验证机制是整体系统架构的功能组件 |
| Semantic Advantage | Rollout Group Analysis | Derived from comparing semantic quality within a group of rollouts |
| Future State | Early Experience | Future states generated by agent actions serve as the core supervisory component of early experience |
| Memory Encoder | Memory System | The Q-Former based encoder is a core component of the memory system |
| Data Flywheel | Overall Framework | The auto-scaling data flywheel is part of the overall system architecture |
| Memory Module | BrowserAgent Architecture | 记忆模块是 BrowserAgent 三层架构的组成部分 |
| Playwright Engine | Native Browser Interaction Layer | Playwright 引擎是原生浏览器交互层的核心组件 |
| Ray Parallel Layer | BrowserAgent Architecture | Ray 并行编排层是架构的中间层组件 |
| Prune&Write Primitives | MemAct Framework | 记忆原语是 MemAct 框架的核心组成部分 |
| Memory Actions | Agent Action Space | 记忆动作与任务动作共同构成智能体的动作空间 |
| OWL Knowledge Graph | Dynamic Structured Memory | The OWL KG serves as the internal data structure for DSM |
| Beam Search | Reasoning Tree | Beam search is the algorithm used to traverse the Reasoning Tree |
| Abstract Concept Nodes | Dynamic Knowledge Graph | Abstract concept nodes are components within the L1 knowledge graph |
| L0 Microscopic Evidence Memory | Three-layer Memory State Space | L0 is the foundational layer of the three-layer memory architecture |
| STM Buffer | Short-Term Memory | The buffer is a component within the Short-Term Memory module for temporary storage. |
| Topic Segmentation | Sensory Memory Processing | Topic segmentation is a sub-process within the Sensory Memory layer. |
| Memory Module | DeepAgent Architecture | The memory module is a core component within the DeepAgent architecture managing historical interactions. |
| Tool Discovery | Reasoning Engine | Tool discovery is a functional sub-module within the reasoning engine. |
| Task Analyzer | Inference Phase | Task analysis is a sub-module within the inference workflow. |
| 折叠操作 | 主动上下文管理 | 管理框架中的核心机制 |
| Memory Update Module | MemSearcher Workflow | The memory update mechanism is a core component of the MemSearcher architecture. |
| Experience Model | DreamGym Framework | Core component responsible for distilling environment dynamics and generating transitions |
| 经验条目 | 结构化经验库 | 经验条目是经验库的基本组成单元 |
| 反思模块 | FLEX 架构 | 反思模块是 FLEX 进化闭环的核心组件 |
| 经验库 | FLEX 进化闭环 | 经验库是 FLEX 架构中存储和演化知识的核心部分 |
| Self-Questioning Mechanism | Self-Evolution Mechanism | Self-Questioning is one of the three core collaborative mechanisms driving self-evolution. |
| Experience Manager | AgentEvolver Architecture | Experience Manager is a core module responsible for memory retrieval and storage within the system. |
| 短期记忆模块 | VisMem 框架 | 双模块系统的核心组件之一 |
| 长期记忆模块 | VisMem 框架 | 双模块系统的核心组件之一 |
| User Profile Layer | O-Mem System | Core layer responsible for user characterization |
| Event Record Layer | O-Mem System | Core layer responsible for context management |
| Arguments | Enriched EDU | Semantic arguments are components that enrich the basic discourse unit with structured information |
| Memorizer | Offline Stage | The Memorizer module constitutes the offline processing phase. |
| Researcher | Online Stage | The Researcher module constitutes the online inference phase. |
| 记忆模块 | MMAG 框架 | 五个记忆模块共同构成混合记忆增强生成框架的核心 |
| 中央记忆控制器 | MMAG 框架 | 负责统一编排与协调所有记忆模块的组件 |
| 存储后端 | 记忆模块 | 每个记忆模块对应特定的持久化存储载体 |
| Adaptive Retrieval Agent | WorldMM Architecture | Core component responsible for dynamic memory source selection |
| Memory Construction Module | WorldMM Architecture | Pre-processing stage transforming video into memory stores |
| Short-term Memory (STM) | MemVerse Framework | STM is one of the three core components of the framework |
| Long-term Memory (LTM) | MemVerse Framework | LTM is one of the three core components of the framework |
| Parametric Memory | MemVerse Framework | Parametric Memory is one of the three core components of the framework |
| Episodic Memory | Long-term Memory (LTM) | Episodic Memory is a sub-component within the LTM Knowledge Graph |
| Semantic Memory | Long-term Memory (LTM) | Semantic Memory is a sub-component within the LTM Knowledge Graph |
| Expert Adapters | MemLoRA Architecture | Extraction, Update, and Generation adapters are modular components constituting the MemLoRA system. |
| Experience Acquisition | Dynamic Procedural Memory Framework | First phase of the three-stage cycle |
| Experience Reuse | Dynamic Procedural Memory Framework | Second phase of the three-stage cycle |
| Experience Refinement | Dynamic Procedural Memory Framework | Third phase of the three-stage cycle |
| Weighted Knowledge Graph | Memoria Framework | The KG is a core component of the dual-component memory architecture. |
| Dynamic Session Summary | Memoria Framework | The Summary module is a core component of the dual-component memory architecture. |
| 反思层 | HINDSIGHT 架构 | 反思层是架构中负责基于记忆推理和更新的关键组件 |
| 四逻辑网络 | 结构化记忆库 | 四个逻辑网络共同组成了结构化记忆库的核心存储结构 |
| 记忆形式 | 代理记忆系统 | 记忆形式是代理记忆系统三维分类体系的一个维度 |
| 记忆功能 | 代理记忆系统 | 记忆功能是代理记忆系统三维分类体系的一个维度 |
| 记忆动态 | 代理记忆系统 | 记忆动态是代理记忆系统三维分类体系的一个维度 |
| EDU Node | Structural Relationship Tree | Individual EDUs constitute the nodes within the hierarchical discourse tree |
| System 1/2/3 | Sophia Framework | The three cognitive systems constitute the core architecture of Sophia. |
| 编码模块 | 模块化记忆空间 | 编码模块是模块化记忆空间的组成部分 |
| 存储模块 | 模块化记忆空间 | 存储模块是模块化记忆空间的组成部分 |
| 检索模块 | 模块化记忆空间 | 检索模块是模块化记忆空间的组成部分 |
| 管理模块 | 模块化记忆空间 | 管理模块是模块化记忆空间的组成部分 |
| 元进化控制器 | MemEvolve 框架 | 元进化控制器是 MemEvolve 框架的核心组件 |
| Long-Term Memory (LTM) | Agentic Memory | LTM serves as the persistent component of the unified memory system |
| Short-Term Memory (STM) | Agentic Memory | STM serves as the working context component of the unified memory system |
| MemCells | MemScenes | 在语义巩固阶段，MemCells 被组织并归属于 MemScenes |
| Q-value | Intent-Experience-Utility Triplet | Q-value represents the utility component within the memory triplet |
| Dual-stage Retrieval | Memory Operation | Retrieval process consists of semantic gating and value ranking phases |
| Fast Path | Dual-stream Update Mechanism | Handles immediate indexing for low-latency ingestion |
| Multi-Graph Core | MAGMA Architecture | Stores orthogonal memory representations within the system |
| Event Nodes | Event Graph | Events serve as the fundamental units constituting the graph structure |
| Logical Edges | Event Graph | Relations serve as connections defining the graph topology |

### 9.3 related-to 关系

共 **242** 条 related-to 关系，描述概念的语义关联。

| 源概念 | 目标概念 | 描述 |
|-------|---------|------|
| Editing Locality | Catastrophic Forgetting | Locality constraint mitigates catastrophic forgetting during editing |
| 工作记忆 | 长期记忆 | 通过记忆巩固机制将工作记忆中的特征转入长期记忆 |
| 各向异性读取 | 三重记忆系统 | 解码器通过该操作从三个记忆库中聚合信息 |
| Tool Usage Frequency | Task Performance | The frequency and accuracy of tool calls are directly related to downstream task success. |
| 情景记忆 (Episodic Memory) | 策略优化 (Policy Optimization) | 记忆内容通过上下文引导未来动作选择，无需更新模型权重 |
| Memory Retrieval | Action Planning | Retrieved memories provide the contextual basis for generating action plans |
| CMeKG | 指令微调数据集 | 知识图谱是构建高质量医疗指令数据的基础来源 |
| Memory Controller | Memory Stream | Controller dynamically decides when and how to access or update the Stream |
| Memory Retention | Time Interval | Retention rate is exponentially related to time via Ebbinghaus curve |
| Retrieval Event | Memory Strength | Retrieval events trigger reinforcement and increase memory strength |
| Plan | Content Generation | The plan guides the generation of the current paragraph |
| Memory Mechanism | Text Coherence | Memory mechanisms directly influence the coherence of long text |
| LLM | Memory-API | LLM 通过自主生成 API 调用指令与记忆模块进行透明交互 |
| 三元组 | LSH 索引 | 三元组的向量表示存储于 LSH 索引中以支持语义相似性检索 |
| 记忆槽 | 原始上下文 | 通过自编码重建损失建立语义等价关联 |
| 编码器 | 解码器 | 通过记忆槽进行解耦连接，解码器主体参数保持固定 |
| 用户指令 | API 序列 | 用户自然语言指令与执行该任务所需的 API 调用序列存在语义映射关系 |
| ToolEval | 模型性能 | ToolEval 评估器与模型的工具使用性能存在验证关系 |
| Structured Output | Solution Coherence | Generating structured documents is related to improved solution coherence. |
| Environment Reward | Policy Gradient | Environment rewards provide the gradient signal for optimizing the Retrospective Model |
| 备忘录一致性 | 事实一致性 | 备忘录机制的使用直接提升长对话中的事实一致性表现 |
| Fine-tuning | Character Style Internalization | Fine-tuning operation is correlated with internalizing character speaking styles. |
| Retrieval Mechanism | Context Consistency | Retrieval mechanism is essential for maintaining background knowledge consistency. |
| Recursive Summarizing | Error Accumulation Risk | The recursive nature of the method is inherently related to the potential for hallucination and error propagation. |
| Resource-Rational Principle | Cost Reduction | Applying resource rationality directly correlates with reduced computational costs |
| Asynchronous Self-Monitoring | Behavioral Consistency | Monitoring processes ensure agent actions remain consistent with long-term goals |
| Hebbian Learning | Lifecycle Management | Hebbian principles dictate that retrieval extends memory lifecycle. |
| STM | LTM Retrieval | STM contents act as cues to trigger DFS search in LTM. |
| Context Usage | Paging Trigger | High context utilization triggers memory paging operations. |
| Function Call | Memory Operation | Function calls are the mechanism for executing memory read/write. |
| Bug Fix | Test Case | A valid fix is ontologically defined by its ability to pass the associated test cases |
| Memory Capacity | Agent Performance | Non-linear relationship where performance peaks at an optimal capacity and declines thereafter |
| Graph Modularity | Data Partitioning | Graph modularity is utilized to drive effective data partitioning for summarization. |
| Context Window Size | Generation Quality | Context window size (e.g., 8k) is correlated with optimal generation quality. |
| 海马体索引理论 | 架构设计 | 生物学记忆理论直接指导了系统的存储与索引分离设计 |
| Tool | Tool | Tools are related through implicit collaboration patterns captured in the graph |
| Query | Scene | Queries are contextually related to specific usage scenes |
| 人类反馈 | 知识图谱更新 | 用户反馈直接驱动记忆结构（图谱）的演化与更新 |
| 会话 ID | 时间戳 | 会话 ID 与时间戳共同构成结构化记忆的核心元数据，用于会话割裂与定位 |
| Memory Agent Traversal | Markov Decision Process | The navigation process through memory is formalized as an MDP |
| Memory Node | Memory Node | Nodes in the memory graph are connected via causal (Cause, React) or temporal relations. |
| 记忆 - 注意力融合 | 注意力机制 | 记忆向量通过融合机制与注意力输出整合 |
| 记忆检索准确率 | 下游任务性能 | 记忆检索质量直接影响语言模型的任务表现 |
| 记忆容量 | 推理延迟 | 记忆容量增加会带来计算开销的权衡 |
| AriGraph | LLM Agent | Memory architecture supporting agent decision making and planning |
| Environment Observation | Information Extraction | Input source for generating memory triples |
| CVaR 阈值 (CVaR Threshold) | 自我反思触发器 (Self-Reflection Trigger) | 风险阈值违规启动记忆更新和策略修订 |
| 投资信念 (Investment Belief) | Prompt 更新 (Prompt Update) | 概念化信念被编码进 Prompt 以指导未来决策 |
| 强化学习代理 (RL Agent) | 检索路径 | RL 代理动态优化图谱上记忆路径的选择策略 |
| Parameter Update | Locality Preservation | The direction of parameter update directly affects the preservation of unrelated knowledge |
| 原子索引 (Atomic Indexing) | 幻觉抑制 (Hallucination Reduction) | 采用原子索引方式与降低工具调用幻觉率强相关。 |
| Visual Feedback | Task Success Rate | The presence of visual feedback is positively correlated with task completion success. |
| Normalized Action Space | Cross-OS Compatibility | Standardized coordinates facilitate compatibility across different operating systems. |
| Interaction Feedback | Documentation Quality | Feedback signals directly correlate with memory refinement effectiveness and accuracy |
| Surprising Information | Retrieval Accuracy | Extracting surprising information is positively correlated with improved retrieval accuracy in long contexts. |
| Agent Scale | Group Dynamics Strength | Larger agent populations correlate with stronger group dynamics |
| Agent Scale | Opinion Diversity | Larger populations lead to more diverse opinion expression |
| User Query | Auxiliary Text | Connected via semantic similarity measured by Contriever embeddings. |
| Episodic Simulation | Episodic Memory | Simulation is used to augment memory for planning in unseen environments |
| Persona Update Operation | Dialogue Turn | The memory update operation is triggered conditionally based on the accumulation of dialogue turns. |
| 动作/活动检测 | 记忆更新触发 | 感知到的变化触发记忆库的写入操作 |
| LLM 代理核心 | 持久场景记忆库 | 代理通过查询记忆进行推理和规划 |
| 权重衰减 (Weight Decay) | 遗忘机制 (Forgetting Mechanism) | 权重衰减在 Titans 中被重新解释为管理记忆容量的遗忘机制 |
| 输入梯度大小 (Input Gradient Magnitude) | 记忆强度 (Memory Strength) | 惊喜度（梯度大小）决定了记忆更新的强度 |
| Event Time | Transaction Time | Dual timelines define fact validity and system knowledge state |
| New Fact | Old Fact | Connected via invalidation logic when contradictions occur |
| Short-Term Memory (STM) | Long-Term Memory (LTM) | STM content is migrated to LTM upon replacement based on age |
| Co-trained Retriever | Long-Term Memory (LTM) | Retriever queries LTM to fetch relevant context for generation |
| Time Series Data | Visual Modality | Time series data is mapped to visual modality via FFT and interpolation. |
| Time Series Data | Text Modality | Time series data is mapped to text modality via statistical feature generation. |
| Input Tokens | Memory Bank | Connected via Cross-Attention mechanism for bidirectional information exchange |
| Long-Context Reasoning | Explicit Memory | Explicit memory is posited as a primary solution for long-context reasoning challenges |
| 检索机制 (Retrieval Mechanism) | 隐私泄露风险 (Privacy Leakage Risk) | 不同的检索机制（如编辑距离 vs 余弦相似度）直接影响隐私泄露的严重程度 |
| 全局记忆 | 自我中心观测 | 通过动态对齐融合，弥补单一视角的局限性 |
| 任务指令 | 检索线索 | 任务指令驱动自适应检索过程以获取相关记忆 |
| Query | Triple | Queries are mapped to triples via Query-to-Triple matching for seed node identification. |
| Passage Nodes | Phrase Nodes | Passage nodes are connected to phrase nodes via synonym detection to preserve context. |
| 记忆保留 | 正向压缩 | 正向压缩过程直接服务于记忆保留目标，通过压缩上下文保留关键信息 |
| 记忆检索 | 反向重建 | 反向重建过程验证检索能力，确保压缩信息可被还原 |
| Tool Invocation | Knowledge Reasoning | Tool invocation is theoretically decoupled from knowledge reasoning to reduce hallucination. |
| Query Description | SPARQL Query | Query descriptions serve as natural language semantic representations of formal SPARQL queries. |
| 任务调度器 | 决策代理池 | 调度器根据任务语义动态选择代理池中的最优代理 |
| 回退机制 | Windows UI 环境 | 回退机制直接作用于环境状态进行快照恢复 |
| Action Trajectory | Programmatic Skill | Action trajectories serve as the raw data source for inducing programmatic skills. |
| Skill API | Web DOM Elements | Skills are semantically matched and bound to specific webpage structures. |
| Weak Agent | Strong Agent Skills | Skills synthesized by strong agents can be transferred to enhance weak agents. |
| 自适应记忆 | 推理准确率 | 自适应记忆的积累与推理任务准确率的提升正相关 |
| 测试时学习 | 黑盒大语言模型 | 测试时学习技术适用于无法修改参数的黑盒模型 |
| Demonstration Quality | Task Success Rate | High-quality structured demonstrations are positively correlated with higher task success rates. |
| Semantic Retrieval | Cross-App Generalization | Semantic retrieval mechanisms enable knowledge transfer to unseen applications. |
| UIA Metadata | Visual Annotations | UIA semantic data is fused with visual annotations for hybrid control detection. |
| 动态显著信息提取 | 记忆巩固 | 提取的结果作为巩固模块的输入，两者协作完成记忆转化 |
| Factual Knowledge | External Database | Factual knowledge is explicitly mapped to and stored in the external database rather than weights. |
| Language Ability | Model Weights | General linguistic capabilities remain encoded within the internal model weights. |
| Memory Utilization | Personalization Performance | Effective memory utilization directly impacts the personalization capability and success rate of embodied agents |
| VLM Hidden States | Memory Carriers | Internal hidden states are utilized as the primary carrier for encoding memory information |
| Intent Hypothesis | Missing Slot Identification | Intent hypothesis generation guides the identification of information gaps. |
| Minimal Predefinition | Scalable Reasoning | Reducing predefinition is positively related to the scalability of agent reasoning. |
| 代码修改 | 安全沙箱 | 代码修改必须在安全沙箱中进行以控制潜在风险 |
| 代理版本 | 基准测试性能 | 每个代理版本都关联具体的基准测试通过率作为进化依据 |
| Camera FOV | Memory Relevance | Geometric field-of-view overlap determines the relevance value of memory frames |
| G-Memory | Organizational Memory Theory | Theoretical foundation inspiring the architecture design and evolution mechanism |
| Query Graph | Insight Graph | Connected via bi-directional traversal to enable abstract-to-concrete retrieval |
| Memory Consolidation | Reinforcement Learning | RL drives the optimization of memory consolidation to synergize with reasoning. |
| Reinforcement Learning | Memory Management | RL is utilized to optimize the policy for memory updates and retention |
| Multi-Conv Generation | Training Data | Independent-context multi-conversation generation is related to the data strategy for RL training |
| Heterogeneous Agent Frameworks | Structured Knowledge Base | Frameworks contribute trajectories to the KB and retrieve knowledge from it to enhance reasoning. |
| 认知科学记忆分类理论 | 六模块记忆组件设计 | 基于人类记忆分类理论 (核心、情景、语义、程序记忆) 设计记忆系统 |
| 记忆巩固机制 | 多跳推理能力提升 | 记忆巩固显著降低推理负担，多跳推理超基线 24 分 |
| 主动检索机制 | 无需用户显式指令 | 根据当前上下文自动生成检索主题，实现被动到主动的转变 |
| Model Reasoning Capability | Management Mode Selection | Stronger models support autonomous mode |
| Tool Removal Rate | Context Overflow Risk | Higher removal rate reduces overflow risk |
| User Feedback | Dynamic Weight Adjustment | Feedback (approve/reject) directly modifies memory weights |
| Ebbinghaus Forgetting Curve | Memory Lifecycle | Theoretical basis for memory decay without reinforcement |
| Index Routing | Retrieval Efficiency | Layer-by-layer routing reduces full-scan computation |
| MLP Memory | kNN-LM | MLP Memory 在训练阶段模仿 kNN 检索器的行为分布 |
| MLP Memory | RAG | MLP Memory 是 RAG 的参数化替代方案，解决其高延迟问题 |
| MLP Memory | Fine-tuning (LoRA) | MLP Memory 避免微调导致的灾难性遗忘问题 |
| Episodic Memory | Semantic Memory | Episodic memory is distilled into semantic memory |
| Prediction Error | Knowledge Update | Drives active learning and memory refinement |
| Context Compression | Attention Dilution Mitigation | Compressing context is directly related to reducing attention interference. |
| 经验记忆 | 奖励信号 | 经验轨迹通过 WSM 评估转化为细粒度奖励信号 |
| 课程生成器 | 任务难度 | 生成器根据记忆反馈动态调整任务难度 |
| Role Awareness | Context Routing Decision | Agent roles directly influence the importance scoring for context selection. |
| 记忆更新 | 任务执行反馈 | 记忆更新机制依赖于任务成功或错误的反馈信号 |
| 强模型记忆 | 弱模型代理 | 强模型生成的记忆可迁移并赋能弱模型代理 |
| Agent Memory | Agent Role Goal | Memory content is dynamically aligned with specific agent objectives |
| Entity | Multimodal Information | Information is organized around entities to ensure logical consistency |
| Memory Decoder | Domain Adaptation | Serves as an efficient solution for domain-specific knowledge injection |
| 记忆缺口 | 探索性查询 | 探索性查询基于当前记忆缺口生成以发现新证据 |
| 新证据 | 记忆更新 | 新证据被整合入记忆池以更新全局心理模型 |
| Linguistic Structures | Persistent Conversational Context | Explicit linguistic structures are leveraged to maintain persistence in conversational context. |
| Retrieved Context | Parametric Knowledge | These two memory sources exhibit a potential conflict relationship requiring resolution |
| 记忆检索 | 策略决策 | 检索到的案例直接指导智能体的动作选择与策略生成 |
| 记忆管理能力 | 代理性能瓶颈 | 完美上下文实验证明记忆管理是当前代理的核心瓶颈 |
| 上下文工程设计 | 模型改进 | 上下文工程与模型改进对代理性能同等重要 |
| 遗忘度量指标 | 终身学习评估 | FGT 等指标用于量化代理的终身学习能力 |
| Memory Consolidation | Memory Capacity Control | Consolidation strategy directly manages memory bank size to prevent explosion |
| Reinforcement Learning | Memory Management Strategy | RL optimizes the decision-making policy for memory lifecycle |
| 情感状态 | 行为编排 | 虚拟形象的动作由实时情感状态驱动 |
| 记忆压缩 | 存储效率 | 压缩算法直接关联长期运行的存储成本优化 |
| 原始记忆 | 推理记忆 | 推理记忆基于原始记忆通过五种演化模式推导生成 |
| 用户查询 | 检索记忆 | 用户查询用于触发对相关原始记忆与推理记忆的检索 |
| 时间衰减 | 遗忘机制 | 时间衰减是遗忘机制中降低记忆权重的因素 |
| 检索强化 | 遗忘机制 | 检索强化是遗忘机制中提升记忆权重的对抗因素 |
| SDM Activation | Uncertainty Quantification | SDM is explicitly designed to enhance uncertainty quantification and selective classification |
| H2R Mechanism | Knowledge Distillation | H2R mechanism is used to distill hierarchical knowledge from interactions. |
| High-level Planning Memory | Sub-goals | High-level memory stores insights related to task sub-goals. |
| Low-level Execution Memory | Action Sequences | Low-level memory stores specific action sequences and execution details. |
| Agent Behaviors | Tool Invocation | 智能体行为与工具调用能力密切相关 |
| Foundation Model | Agent Capabilities | 基座模型质量直接影响智能体能力上限 |
| Dynamic Outline | Evidence Memory Bank | 动态大纲通过引用链接与证据记忆库相关联 |
| Planner Agent | Writer Agent | 规划者与写作者通过协作机制相关联 |
| 当前对话状态 | 检索到的原则 | 当前语境通过相似度匹配触发相关的历史策略原则 |
| Uncertainty Assessment | System 2 Activation | High uncertainty triggers the transition to System 2 memory |
| Token Consumption | Reasoning Depth | Memory depth is correlated with computational cost |
| Latent Token Sequence | Reasoning Process | Tightly interwoven cycle where memory augments reasoning |
| Generative Latent Memory | Self-Evolving Agents | Enables agents to evolve cognitive capabilities without explicit supervision |
| 经验蒸馏 | 记忆质量提升 | 经验蒸馏操作直接关联记忆质量的优化 |
| 测试时缩放 | 经验多样性生成 | 测试时缩放机制用于生成多样化经验以优化记忆合成 |
| 奖励信号 | 下游问答准确率 | RL 奖励直接基于下游任务的问答准确率反馈 |
| 代理控制器 | 记忆操作工具集 | 代理通过选择工具来执行具体的记忆操作 |
| Utility Maximization | Compression Maximization | Sequential optimization relationship where task utility is prioritized before context compression |
| Anchor Model | Common Knowledge | The anchor model is primarily responsible for storing common knowledge and reasoning capabilities |
| Memory Bank | Long-tail Knowledge | The memory bank is specialized for storing infrequent long-tail facts |
| 执行信号 | 反射过程 | 驱动反射代理进行分析的反馈信号 |
| Delta 更新 | 上下文坍塌预防 | 避免全量重写导致信息丢失的机制 |
| Orchestrator Memory | Task Decomposition | 编排器记忆与任务分解有效性强相关 |
| Task Agent Memory | Tool Execution Accuracy | 任务代理记忆与工具执行准确率强相关 |
| Assimilation | Node Replication | Assimilation operation is technically implemented via node replication to capture polysemy |
| Accommodation | Incremental Clustering | Accommodation operation is technically implemented via incremental label propagation for structure adjustment |
| Tool Capability Memory | Multimodal Agent Decision Making | 工具能力记忆与多模态代理决策过程密切相关 |
| Experience Collection | Memory Evolution | 交互经验收集驱动记忆的动态演进 |
| Tool Performance Variability | Memory Update Necessity | 工具性能波动性决定了记忆更新的必要性 |
| 持久记忆 | 个性化响应 | 持久记忆的存在直接关联到响应的个性化程度 |
| 用户画像 | 自适应性 | 用户画像的演化关联到系统的自适应能力 |
| Experiential Knowledge | Model Behavior Guidance | Distilled knowledge directly influences inference-time decisions |
| Self-Reflection | Policy Improvement | Reflection on early experience drives policy grounding and reasoning improvement |
| Memory Scale | Task Accuracy | Memory scale shows a logarithmic linear relationship with task accuracy |
| Continuous Memory | Retrieval Augmented Generation | Continuous memory is utilized within a RAG framework for agent inference |
| Explicit Memory | Long Reasoning Chains | 显式记忆机制与长推理链信息保留问题相关 |
| Native Browser Interaction | Human-Inspired Actions | 原生浏览器交互与人类启发的浏览动作相关 |
| Scroll Operation | Deep Content Access | 滚动操作与网页深度内容获取相关 |
| Context Curation | Task Performance | 上下文策展与任务性能通过强化学习联合优化 |
| Memory Compression | Inference Efficiency | 记忆压缩直接影响推理延迟和 Token 消耗 |
| Dynamic Structured Memory | Reasoning Tree | Symbiotically indispensable relationship where DSM provides facts and RT provides logic |
| Renormalization Group Theory | Memory Evolution Mechanism | Physics RG theory inspires the principle of memory scale transformation |
| Stability-Plasticity Dilemma | Fast-Slow Variable Separation | Fast-slow separation is the proposed solution to the stability-plasticity conflict |
| Soft Update | Information Integrity | Soft update mechanism is related to preserving global information integrity by avoiding overwriting. |
| Offline Update | Latency Reduction | Offline update strategy is related to reducing test-time inference latency. |
| Memory Folding | Error Accumulation Reduction | The memory folding mechanism is directly related to mitigating error accumulation in long-horizon tasks. |
| ToolPO | Tool Call Stability | The ToolPO strategy is correlated with improved stability and accuracy in tool usage. |
| Evolution Phase | Inference Phase | The evolution phase generates tools used by the inference phase. |
| MCP Retrieval | Task Analysis | Retrieval depends on the semantic embedding generated by task analysis. |
| 回顾性巩固 (人类认知) | 主动折叠 | 启发技术机制的人类认知过程 |
| Memory Management | End-to-End Reinforcement Learning | Memory management policies are optimized jointly with reasoning via RL. |
| Experience Synthesis | Real Environment Interaction | Substitutes expensive real interactions with reasoning-based synthesis to reduce cost |
| 经验继承 | 智能体进化 | 经验继承机制支持新智能体从旧经验中获益实现进化 |
| 经验检索 | 智能体决策 | 经验检索增强智能体在环境交互中的决策能力 |
| 经验增长 | 性能提升 | 经验库规模增长与智能体性能提升存在缩放律关系 |
| Environment Profile | Task Generation | Environment Profile guides the LLM to generate feasible synthetic tasks during the Self-Questioning phase. |
| 视觉输入 | 短期记忆 | 视觉输入进入短期记忆以保留感知细节 |
| 语义一致性 | 长期记忆 | 长期记忆负责确保生成过程中的语义一致性 |
| Active User Profiling | Personalization | Enables dynamic adaptation to user changes |
| Hierarchical Retrieval | Efficiency-Performance Balance | Achieves Pareto optimality in latency and accuracy |
| Neo-Davidsonian Semantics | Event-Centric Representation | Provides the theoretical foundation for structuring memory events and their semantic relations |
| Concise Snapshot | Page Store | Snapshots guide retrieval from the detailed page store. |
| Model Size | Research Module Performance | Research module effectiveness is sensitive to model scale. |
| 五层记忆分类 | 认知心理学记忆分类 | 技术组件设计直接映射自心理学理论模型 |
| 冲突解决策略 | 动态记忆注入 | 策略决定哪些记忆内容被优先注入到提示词中 |
| 异步记忆更新 | 系统延迟优化 | 操作机制直接关联到不增加对话延迟的工程目标 |
| User Query | Memory Source Selection | Query content dictates the choice of memory type and temporal granularity |
| Visual Memory | Text Summaries | Complementary relationship ensuring visual details are not lost in text abstraction |
| Parametric Memory | Long-term Memory (LTM) | Connected via Knowledge Distillation for internalization |
| Short-term Memory (STM) | Central Memory Orchestrator | STM feeds into the Orchestrator for management |
| Retrieval Augmentation | Parametric Memory | Retrieval enhances Parametric Memory output |
| Local Memory Bank | Small Language Model | The memory bank stores externalized knowledge accessed by the SLM through adapters. |
| Utility Monitoring | Experience Deletion | Monitors retrieval frequency and utility to trigger deletion |
| Scenario-aware Retrieval | Experience Reuse | Enables context-aware experience retrieval |
| Failure Reflection | Experience Acquisition | Allows learning from failed trajectories |
| Time-Decay Weight | Knowledge Triple | Weights determine the priority and relevance of triples during retrieval. |
| User Input | Triple Extraction | Triples are extracted exclusively from user inputs to ensure accuracy. |
| 记忆 | 推理基底 | 记忆被视为推理的结构化一级基底而非外部检索层 |
| 信念 | 经验 | 信念网络基于经验网络的内容进行演化和更新 |
| 事实记忆 | 参数级记忆 | 事实记忆功能通常与参数级记忆形式强相关 |
| 工作记忆 | 令牌级记忆 | 工作记忆功能通常依赖于令牌级记忆形式实现 |
| 经验记忆 | 潜在级记忆 | 经验记忆功能常通过潜在空间向量进行编码 |
| User Query | Selected Sub-Tree | The query guides the ranking and selection of relevant EDU sub-trees for compression |
| Episodic Memory | Reasoning Efficiency | Access to episodic memory significantly reduces redundant reasoning steps. |
| System 3 | Identity Consistency | Meta-cognitive monitoring ensures narrative coherence and identity consistency. |
| 交互轨迹 | 经验知识 | 交互轨迹是经验知识的来源载体 |
| 记忆架构 | 任务上下文 | 记忆架构需随任务上下文进行元适应 |
| 经验知识 | 记忆架构 | 经验知识与记忆架构进行联合进化 |
| Memory Operations | Reinforcement Learning | Memory operation selection is optimized through RL reward signals |
| Memory Quality | Task Success Rate | Improvements in memory quality directly correlate with higher task success rates |
| MemScenes | 用户画像 (User Profiles) | MemScenes 用于更新和维持长期一致的用户模型 |
| 对话流 (Dialogue Streams) | MemCells | 原始对话流被转化为 MemCells 进行存储 |
| Memory Q-value | Environment Reward | Q-values are iteratively updated based on feedback from environment rewards |
| Frozen LLM | External Memory | The frozen model relies on external memory for knowledge evolution without parameter updates |
| Query Intent | Traversal Weights | Dynamic adjustment of graph edge weights based on user intent |
| Node ID | Cross-Graph Mapping | Ensures consistency across different orthogonal graphs |
| Event Nodes | Event Nodes | Connected via explicit causal or temporal logical relations |

---

## 十、验证公理

### 10.1 理论公理 (Theoretical)

共 **313** 条理论公理。

- Minimal Perturbation Principle: The optimal edit minimizes weight change distance
  — 来源: `2104.08164`
- 阿特金森 - 希夫林人类记忆模型可有效映射为视频对象分割的特征存储架构
  — 来源: `2207.07115`
- 显存消耗与分割精度可通过多重存储机制实现解耦
  — 来源: `2207.07115`
- Language models can learn to use tools via self-supervision without extensive human annotation.
  — 来源: `2302.04761`
- Integrating tool usage into the generation process does not necessarily degrade core language modeling capabilities.
  — 来源: `2302.04761`
- 语言反馈可以替代梯度更新来实现 LLM 代理的策略优化
  — 来源: `2303.11366`
- 对失败轨迹的自我反思能够增强少样本学习复杂任务的能力
  — 来源: `2303.11366`
- Natural language is a sufficient medium for representing agent experience and state
  — 来源: `2304.03442`
- Believable human behavior simulation requires the integration of memory, planning, and reflection
  — 来源: `2304.03442`
- 知识图谱注入可显著提升大模型的领域专业性
  — 来源: `2304.06975`
- 医疗场景下安全性与可用性存在权衡关系 (Trade-off)
  — 来源: `2304.06975`
- LLMs lose key historical information when processing ultra-long inputs due to fixed length limits
  — 来源: `2304.13343`
- Active memory control mechanisms outperform passive retrieval for maintaining long-term context
  — 来源: `2304.13343`
- Memory retention rate decays exponentially over time following R=e^{-t/S}
  — 来源: `2305.10250`
- Memory strength increases upon successful retrieval simulating human review mechanism
  — 来源: `2305.10250`
- LLM computational states can be externalized and managed as natural language
  — 来源: `2305.13304`
- RNN recurrent mechanisms can be simulated via prompt engineering without model training
  — 来源: `2305.13304`
- 基于戴维森语义理论，知识可被解构为可操作的三元组以实现显式存储
  — 来源: `2305.14322`
- 记忆外置化是解决 LLM 知识固化与时效性更新问题的有效路径
  — 来源: `2305.14322`
- 文本信息冗余公理：长上下文包含冗余信息，可压缩至更短序列而不丢失核心语义
  — 来源: `2307.06945`
- 记忆解耦公理：上下文表示可与任务执行模型解耦，通过中间记忆槽交互
  — 来源: `2307.06945`
- 大规模真实世界 API 的指令微调可显著提升开源模型的工具使用能力
  — 来源: `2307.16789`
- 引入搜索算法可扩展大语言模型在工具调用空间中的推理能力
  — 来源: `2307.16789`
- 利用强模型生成数据蒸馏至弱模型可有效迁移工具学习知识
  — 来源: `2307.16789`
- Embedding SOPs in prompts constrains LLM generation to standard workflows, reducing hallucination.
  — 来源: `2308.00352`
- Meta-programming allows agents to manage their own behavioral procedures.
  — 来源: `2308.00352`
- Decoupling execution (Actor) and optimization (Retrospective) reduces training costs while maintaining performance.
  — 来源: `2308.02151`
- Gradient signals from environment rewards can effectively optimize reflection prompts without updating the Actor.
  — 来源: `2308.02151`
- 内部记忆管理减少对外部检索系统的依赖
  — 来源: `2308.08239`
- 结构化总结在有限上下文窗口内比原始上下文更好地保留事实
  — 来源: `2308.08239`
- Combining RAG and SFT yields higher character consistency than using either alone.
  — 来源: `2308.09597`
- External memory retrieval complements internal parameter knowledge for role consistency.
  — 来源: `2308.09597`
- Memory management can be formulated as a sequence generation task utilizing LLM in-context learning capabilities.
  — 来源: `2308.15022`
- Automatically generated memory summaries can be more fluent and model-compatible than human-annotated gold memory.
  — 来源: `2308.15022`
- Resource-Rational Agent Design: High-cost processes (LLM) should only be invoked when necessary for complex reasoning
  — 来源: `2310.02172`
- Memory Priority Axiom: Low-priority memories should be summarized or forgotten to maintain system efficiency
  — 来源: `2310.02172`
- Memory retrieval extends the lifecycle of an Engram.
  — 来源: `2310.03052`
- Unretrieved memory lifecycle decays over time leading to forgetting.
  — 来源: `2310.03052`
- Information importance is dynamic and evaluated via retrieval frequency rather than static position.
  — 来源: `2310.03052`
- Fixed context window limits act as hardware RAM constraints requiring virtual memory management.
  — 来源: `2310.08560`
- External storage integration provides an illusion of infinite context for LLMs.
  — 来源: `2310.08560`
- Autonomous planning surpasses fixed feedback loops in flexibility for complex repair tasks
  — 来源: `2403.17134`
- FSM guidance constrains agent actions to valid repair phases reducing hallucination and invalid states
  — 来源: `2403.17134`
- Memory sharing enables knowledge evolution and reduces isolation across LLM agents
  — 来源: `2404.09982`
- Retriever accuracy must evolve dynamically alongside memory distribution changes
  — 来源: `2404.09982`
- Graph modularity enables effective data partitioning for hierarchical summarization.
  — 来源: `2404.16130`
- Structured graph indices facilitate global reasoning beyond vector similarity.
  — 来源: `2404.16130`
- 索引与存储的分离能显著增强系统的知识整合能力
  — 来源: `2405.14831`
- 图谱结构支持单次检索完成多跳推理任务
  — 来源: `2405.14831`
- Retrieval completeness requires capturing tool collaboration information beyond semantic similarity
  — 来源: `2405.16089`
- Graph structures effectively model implicit tool dependencies for diverse retrieval
  — 来源: `2405.16089`
- 模型个性化可以通过优化外部知识表示而非内部权重来实现
  — 来源: `2405.19686`
- 冻结模型参数同时更新外部记忆可确保可解释性并降低计算成本
  — 来源: `2405.19686`
- 单纯依赖语义向量检索无法有效处理基于时间元数据的查询
  — 来源: `2406.00057`
- 混合检索架构在时间敏感性和消歧能力上优于单一检索模态
  — 来源: `2406.00057`
- Memory retrieval navigation can be formalized as a Markov Decision Process (MDP)
  — 来源: `2406.06124`
- Hierarchical aggregation preserves information density better than flat summarization
  — 来源: `2406.06124`
- Memory consistency is enhanced by preserving the causal-temporal evolution of events rather than isolated snippets.
  — 来源: `2406.10996`
- Optimal memory linking connects only recent relevant nodes to balance cost and performance.
  — 来源: `2406.10996`
- 显式记忆与语言生成可解耦：记忆存储与语言生成是两个独立但可协同的过程
  — 来源: `2407.01178`
- 三层记忆结构假说：不同时间尺度的信息需要分层记忆机制进行有效管理
  — 来源: `2407.01178`
- 记忆 - 注意力互补性：显式记忆可弥补注意力机制在长上下文场景下的信息丢失问题
  — 来源: `2407.01178`
- Dual memory system (Semantic + Episodic) can be unified into a Knowledge Graph structure
  — 来源: `2407.04363`
- Structured memory supports logical reasoning and planning better than unstructured retrieval
  — 来源: `2407.04363`
- 金融交易任务可形式化为无限视野部分可观测马尔可夫决策过程 (POMDP)
  — 来源: `2407.06567`
- 言语强化无需参数权重更新即可优化 LLM 策略
  — 来源: `2407.06567`
- 个性化智能体记忆必须同时具备可编辑性（更新/删除）和可选择性（精准检索）
  — 来源: `2409.19401`
- 相较于静态向量索引，图谱结构为动态记忆数据提供更优的语义关联能力
  — 来源: `2409.19401`
- Updates orthogonal to unrelated knowledge representations preserve original model behavior
  — 来源: `2410.02355`
- Null-space projection ensures zero interference with specified knowledge subspace
  — 来源: `2410.02355`
- 统一生成范式公理：工具检索与调用可统一为单一序列生成过程，无需外部检索器。
  — 来源: `2410.03439`
- 参数存储可行性公理：大规模工具知识（47k+ APIs）可通过微调有效存储于 LLM 参数中。
  — 来源: `2410.03439`
- Perception-Planning-Action loop is necessary for complex GUI task automation.
  — 来源: `2410.08164`
- Modular openness in agent design enhances generalization across different model backends.
  — 来源: `2410.08164`
- Documentation is a mutable memory component adaptable to learner cognition rather than static reference.
  — 来源: `2410.08197`
- Self-driven interaction generates sufficient signal for autonomous memory optimization without human intervention.
  — 来源: `2410.08197`
- Iterative retrieval with memory feedback converges to accurate answers.
  — 来源: `2410.12859`
- Surprising information extraction reduces noise in long-context retrieval.
  — 来源: `2410.12859`
- Online Top-Down (OTD) clustering inherits Moseley-Wang revenue function approximation guarantees.
  — 来源: `2410.14052`
- Well-separated data assumption ensures theoretical clustering quality bounds.
  — 来源: `2410.14052`
- Scale Axiom: Larger agent populations induce emergent group dynamics not visible in small-scale simulations
  — 来源: `2411.11581`
- Generality Axiom: A universal framework can reduce reconstruction costs across different social scenarios
  — 来源: `2411.11581`
- Retrieval augmentation mitigates context window limitations in long video comprehension.
  — 来源: `2411.13093`
- External tool-based text extraction compensates for LVLM visual perception weaknesses.
  — 来源: `2411.13093`
- Integrating episodic simulation with episodic memory improves generalization in unseen environments
  — 来源: `2412.01857`
- Dynamic weighting between real and imagined information optimizes navigation decisions over time
  — 来源: `2412.01857`
- Personalization is a dynamic state evolving with interaction rather than a static parameter set.
  — 来源: `2412.13103`
- Effective life-long memory requires balancing information retention with update stability to avoid catastrophic forgetting.
  — 来源: `2412.13103`
- 动态场景理解需要融合视觉与本体感知数据以维持记忆一致性
  — 来源: `2501.00358`
- 基于事件的记忆更新优于连续帧处理以平衡效率与准确性
  — 来源: `2501.00358`
- Titans 架构具备超越 TC0 复杂度类的理论表达性
  — 来源: `2501.00663`
- 测试时权重优化机制使得模型能够理论上支持无限上下文窗口建模
  — 来源: `2501.00663`
- Bi-temporal Fact Representation: Every fact possesses both an event time (when it happened) and a transaction time (when the system recorded it).
  — 来源: `2501.13956`
- s invalid_at timestamp is automatically set to the new edge
  — 来源: `2501.13956`
- Decoupling memory capacity from VRAM via CPU offloading enables scalable long-context modeling without quadratic growth
  — 来源: `2502.00592`
- Direct storage of latent memory vectors is superior to KV Cache for long-term information retention
  — 来源: `2502.00592`
- Multimodal fusion compensates for information loss inherent in unimodal time series.
  — 来源: `2502.04395`
- Self-generated modalities preserve domain distribution without requiring external data.
  — 来源: `2502.04395`
- Explicit memory mechanisms enhance long-range dependency capture in Transformers without disrupting original information flow
  — 来源: `2502.06049`
- Controlled memory updates via gating preserve general task performance while improving specialized reasoning capabilities
  — 来源: `2502.06049`
- 记忆容量与泄露绝对数量呈正相关 (Memory capacity is positively correlated with leakage volume)
  — 来源: `2502.13172`
- 基于格式的检索比语义检索更易受提示词操纵 (Format-based retrieval is more vulnerable to prompt manipulation than semantic retrieval)
  — 来源: `2502.13172`
- 基于语言的全局记忆会丢失几何信息，阻碍复杂环境下的空间推理
  — 来源: `2502.14254`
- 纯自我视角观测面临部分可观测决策问题，易导致次优决策
  — 来源: `2502.14254`
- 全局上下文与局部感知的动态对齐能显著增强长程任务的空间推理能力
  — 来源: `2502.14254`
- Hippocampal-Neocortical Complementarity maps to Offline Indexing and Online Retrieval stages.
  — 来源: `2502.14802`
- Non-parametric memory storage prevents catastrophic forgetting in continual learning scenarios.
  — 来源: `2502.14802`
- 双射变换保证信息无损 (Bijective transformation ensures lossless information)
  — 来源: `2502.15957`
- 循环一致性确保保留与检索对齐 (Cycle consistency aligns retention and retrieval)
  — 来源: `2502.15957`
- s core knowledge reasoning process.", 
  — 来源: `2503.05193`
- 动态调度优于静态架构以适应操作系统级任务的异构性
  — 来源: `2503.09263`
- 多智能体协作能突破单一模型在复杂 UI 场景下的能力瓶颈
  — 来源: `2503.09263`
- Executability implies Verifiability: Programmatic representations allow for automatic correctness validation unlike text.
  — 来源: `2504.06821`
- Composability enables Generalization: Modular programmatic skills can be combined to solve complex, unseen tasks.
  — 来源: `2504.06821`
- Experience abstracted as executable code APIs enhances robustness and reusability compared to text-based memory.
  — 来源: `2504.07079`
- Self-improvement in web agents requires a closed loop of exploration, synthesis, and optimization.
  — 来源: `2504.07079`
- LLM 推理无状态缺陷可通过外部记忆机制弥补
  — 来源: `2504.07952`
- 无需梯度更新即可在测试时实现知识积累
  — 来源: `2504.07952`
- 记忆策展优于全量存储以避免上下文爆炸
  — 来源: `2504.07952`
- Demonstration knowledge can be transferred across unseen applications via semantic retrieval.
  — 来源: `2504.13805`
- Structured semantic descriptions enhance the retrievability and usability of demonstration knowledge.
  — 来源: `2504.13805`
- System-level integration enhances automation robustness compared to application-layer scripts.
  — 来源: `2504.14603`
- AgentOS abstraction enables non-intrusive desktop automation as a system primitive.
  — 来源: `2504.14603`
- 结构化持久记忆对长程对话连贯性具有关键作用
  — 来源: `2504.19413`
- 记忆系统应模拟人类的提取与巩固机制以实现高效管理
  — 来源: `2504.19413`
- Factual memory and language ability are theoretically decouplable within transformer architectures.
  — 来源: `2505.15962`
- Learning to query external knowledge is more parameter-efficient than memorizing facts internally.
  — 来源: `2505.15962`
- Increasing context length alone cannot solve personalization problems in embodied agents
  — 来源: `2505.16348`
- Structured memory architecture is required for multi-source memory integration to avoid common sense preference bias
  — 来源: `2505.16348`
- VLM internal hidden states can function as universal memory carriers without requiring architectural modification
  — 来源: `2505.17670`
- Continuous embedding representation preserves core semantic information more efficiently than discrete tokens under high compression
  — 来源: `2505.17670`
- Memory retrieval effectiveness is determined by intent alignment and information gaps rather than semantic similarity alone.
  — 来源: `2505.20231`
- Cross-session task tracking requires structured memory units linking intents to slot facts.
  — 来源: `2505.20231`
- Simplicity is the ultimate sophistication: Minimal Predefinition combined with Maximal Self-Evolution optimizes agent performance.
  — 来源: `2505.20286`
- 实证有益性公理：无需理论证明全局最优，仅需实证验证局部改进即可纳入进化
  — 来源: `2505.22954`
- 开放式探索公理：并行多路径探索优于单一优化路径以避免局部最优
  — 来源: `2505.22954`
- Accessing global context with relevant extraction enables memory-aware generation without 3D reconstruction
  — 来源: `2506.03141`
- Context-as-Memory paradigm avoids information compression loss inherent in latent compression methods
  — 来源: `2506.03141`
- Multi-agent systems require hierarchical memory structures to enable effective self-evolution
  — 来源: `2506.07398`
- Effective memory retrieval necessitates bi-directional traversal between abstract insights and concrete interactions
  — 来源: `2506.07398`
- Memory as Reasoning Paradigm: Memory consolidation is viewed as part of the reasoning process.
  — 来源: `2506.15841`
- Constant Memory Constraint: Efficient long-horizon processing can be achieved with constant memory footprint.
  — 来源: `2506.15841`
- Agent-based workflow enables linear complexity for infinite context processing
  — 来源: `2507.02259`
- RL optimization can effectively balance memory retention versus forgetting in long sequences
  — 来源: `2507.02259`
- Cross-framework collective intelligence can be achieved through a shared memory infrastructure without model re-training.
  — 来源: `2507.06229`
- Experience sharing effectively avoids repeated errors by leveraging cross-domain knowledge.
  — 来源: `2507.06229`
- LLM 智能体记忆系统应基于认知科学的人类记忆分类理论进行模块化设计
  — 来源: `2507.07957`
- 记忆系统应支持抽象推理而非仅长上下文存储
  — 来源: `2507.07957`
- 多代理协同工作流可提升记忆管理效率与可扩展性
  — 来源: `2507.07957`
- 记忆自动路由机制可实现输入内容到相应记忆组件的精准映射
  — 来源: `2507.07957`
- Tool count must remain within API limit (e.g., 128) to prevent failure
  — 来源: `2507.21428`
- Small models lack reliability for autonomous tool context management
  — 来源: `2507.21428`
- Hierarchical semantic abstraction improves retrieval efficiency compared to flat structures
  — 来源: `2507.22925`
- Memory retention follows a forgetting curve modulated by user feedback reinforcement
  — 来源: `2507.22925`
- 检索模式可以通过参数化方式学习并内化到模型中
  — 来源: `2508.01832`
- 参数化记忆可以替代非参数检索实现高效知识访问
  — 来源: `2508.01832`
- 检索收益可以转化为完全参数化形式而无需外部文档访问
  — 来源: `2508.01832`
- Event Segmentation Theory: Memory boundaries align with semantic shifts in interaction
  — 来源: `2508.03341`
- Free Energy Principle: Memory evolution minimizes prediction error between expected and observed states
  — 来源: `2508.03341`
- Explicit interference removal alleviates attention dilution in long contexts.
  — 来源: `2508.04664`
- Reversible operations ensure information integrity during memory management.
  — 来源: `2508.04664`
- 自主经验学习可替代人工标注实现代理进化
  — 来源: `2508.04700`
- 细粒度状态评估能解决强化学习奖励稀疏问题
  — 来源: `2508.04700`
- Context Routing Problem is NP-hard
  — 来源: `2508.04903`
- Greedy Strategy satisfies optimality conditions under monotonic memory relevance
  — 来源: `2508.04903`
- 代理程序性记忆可在无需微调模型参数的情况下进行动态外部管理
  — 来源: `2508.06433`
- 高质量的经验记忆可作为跨模型知识蒸馏的有效媒介
  — 来源: `2508.06433`
- Memory heterogeneity is required for role specialization in multi-agent systems
  — 来源: `2508.08997`
- Intrinsic memory updates maintain better role consistency than external abstraction
  — 来源: `2508.08997`
- Agent long-term memory should mimic human cognitive classification (Episodic/Semantic) to handle long-term dependencies
  — 来源: `2508.09736`
- Entity-centric organization supports logical consistency in reasoning better than vector-only retrieval
  — 来源: `2508.09736`
- Retrieval behavior can be internalized into parametric memory without external database search
  — 来源: `2508.09874`
- Domain knowledge can be decoupled from base model parameters to enable component reusability
  — 来源: `2508.09874`
- 长叙事推理需通过状态化记忆捕捉全局逻辑与动态实体关系
  — 来源: `2508.10419`
- 推理是证据获取与知识巩固的迭代过程，而非一次性操作
  — 来源: `2508.10419`
- Memory consistency in long-range dialogue requires grounding in explicit linguistic structures.
  — 来源: `2508.12630`
- Neuro-symbolic hybrid retrieval outperforms pure vector retrieval for context persistence.
  — 来源: `2508.12630`
- External retrieved context can contradict internal parametric knowledge, leading to performance degradation
  — 来源: `2508.15253`
- Soft prompts can effectively modulate model attention between conflicting knowledge sources without fine-tuning
  — 来源: `2508.15253`
- 编码特异性原则：检索效果取决于编码与检索条件的一致性
  — 来源: `2508.15294`
- 加工层次理论：深层加工（如语义记忆）有助于提升记忆保持
  — 来源: `2508.15294`
- 多重记忆系统理论：不同记忆类型（情景/语义）服务于不同功能
  — 来源: `2508.15294`
- 记忆检索可替代梯度反向传播进行策略优化
  — 来源: `2508.16153`
- 无需更新底层模型参数即可实现智能体的持续自适应学习
  — 来源: `2508.16153`
- 自演进代理四大核心原则：经验探索→长期记忆→技能学习→知识内化形成完整闭环
  — 来源: `2508.19005`
- 人类认知发展规律可映射到智能代理架构设计，四层递进设计符合认知发展
  — 来源: `2508.19005`
- 长期记忆系统需支持时间步加权检索以防止灾难性遗忘
  — 来源: `2508.19005`
- 技能内化需策略性选择时机，避免过早固化导致能力僵化
  — 来源: `2508.19005`
- Human memory mechanisms (Working + Hippocampus) inspire effective robotic memory design
  — 来源: `2508.19236`
- Separating perceptual details from semantic cognition improves information integrity in long-horizon tasks
  — 来源: `2508.19236`
- Learned memory management policies outperform static heuristic rules
  — 来源: `2508.19828`
- A minimal set of memory operations is sufficient for dynamic control
  — 来源: `2508.19828`
- 模块化代理架构能够实现比单体模型更个性化的情感支持
  — 来源: `2509.05298`
- 渐进式记忆压缩可在保留关键上下文的同时解决长期交互存储瓶颈
  — 来源: `2509.05298`
- AR 具身交互能显著增强用户与虚拟伴侣的情感纽带
  — 来源: `2509.05298`
- 基于图式理论的记忆同化与顺应机制：记忆通过扩展、积累等模式动态演化
  — 来源: `2509.10852`
- 推理负担转移公理：将复杂推理前置到记忆存储阶段可显著降低生成阶段的计算负载
  — 来源: `2509.10852`
- 记忆保留应由时间衰减与检索强化的平衡决定（基于认知科学竞争 - 抑制理论）
  — 来源: `2509.11860`
- 情节信息与人物信息需通过独立路径处理以优化连贯性与准确性（基于文学叙事理论）
  — 来源: `2509.11860`
- Prediction uncertainty can be effectively decomposed into similarity, distribution distance, and decision boundary magnitude
  — 来源: `2509.12760`
- Training distribution awareness is necessary for robust OOD detection
  — 来源: `2509.12760`
- Fine-grained knowledge transfer reduces irrelevant information interference compared to coarse-grained units.
  — 来源: `2509.12810`
- Hierarchical structure aligns with human cognitive habits for planning and execution.
  — 来源: `2509.12810`
- 通用基座模型缺乏鲁棒的智能体基础，导致后训练阶段存在优化张力
  — 来源: `2509.13310`
- 解耦行为学习与对齐（先构建智能体基座，再后训练）可提升智能体性能上限
  — 来源: `2509.13310`
- Planning-Execution Separation Axiom: 分离规划与执行能显著减少长文本生成中的幻觉
  — 来源: `2509.13312`
- Dynamic Adaptation Axiom: 自适应规划比静态规划更能有效整合网络规模证据
  — 来源: `2509.13312`
- 隐性参数知识可无需训练显性化为外部结构化记忆
  — 来源: `2509.17459`
- 对比式成败原则 (成功 vs 失败) 可有效缓解模型固有偏好偏差
  — 来源: `2509.17459`
- Dual-Process Cognitive Theory Operationalization in LLMs
  — 来源: `2509.22315`
- Selective Computational Expenditure Principle
  — 来源: `2509.22315`
- Memory and reasoning should be tightly interwoven rather than separated into distinct modules
  — 来源: `2509.24704`
- 记忆驱动的经验缩放是智能体能力扩展的新维度
  — 来源: `2509.25140`
- 泛化推理策略存储优于原始轨迹存储用于智能体学习
  — 来源: `2509.25140`
- 记忆质量与测试时计算投入存在协同优化关系
  — 来源: `2509.25140`
- 记忆构建过程可以通过强化学习进行端到端优化，而非依赖手工规则
  — 来源: `2509.25911`
- 混合记忆结构比单一结构更能有效支持长上下文任务
  — 来源: `2509.25911`
- Natural Language Optimization Axiom: Optimizing compression policies in natural language space bypasses discrete token gradient constraints
  — 来源: `2510.00615`
- Dual-Objective Priority Axiom: Task utility must be maximized before context compression is enforced to prevent information loss
  — 来源: `2510.00615`
- Knowledge and reasoning capabilities can be decoupled at the parameter level within neural networks
  — 来源: `2510.02375`
- Long-tail knowledge can be stored externally in parameters without retraining the main anchor model
  — 来源: `2510.02375`
- 全量重写会导致上下文坍塌 (Context Collapse)
  — 来源: `2510.04618`
- 优化过程倾向于产生简洁性偏差 (Brevity Bias)
  — 来源: `2510.04618`
- 增量更新比全量重写更能保留知识多样性
  — 来源: `2510.04618`
- Role-specific memory allocation optimizes multi-agent system performance (角色特定的记忆分配优化多智能体系统性能)
  — 来源: `2510.04851`
- Procedural memory can compensate for model capacity limitations in workflows (过程记忆可弥补工作流中模型能力的不足)
  — 来源: `2510.04851`
- Memory structures must support Many-to-Many mappings to effectively capture information polysemy
  — 来源: `2510.05520`
- Memory evolution in LLMs should follow Constructivist principles (Assimilation and Accommodation) for adaptability
  — 来源: `2510.05520`
- 工具能力具有可学习性与演进性，而非静态固定属性
  — 来源: `2510.06664`
- 结构化记忆比原始示例存储更高效且抗噪声
  — 来源: `2510.06664`
- 经验诱导可将原始交互转化为紧凑的能力认知
  — 来源: `2510.06664`
- 检索 - 精炼机制可防止灾难性遗忘并修正过时信息
  — 来源: `2510.06664`
- 统一的个性化定义可推导出具体的技术需求（如记忆与画像）
  — 来源: `2510.07925`
- 集成持久记忆与用户画像是实现自适应 LLM 代理的必要条件
  — 来源: `2510.07925`
- Output distribution adjustment can be achieved via input priors without parameter updates
  — 来源: `2510.08191`
- Relative semantic advantage is a sufficient signal for policy optimization in low-data regimes
  — 来源: `2510.08191`
- Future states contain sufficient information for policy grounding without explicit rewards
  — 来源: `2510.08558`
- Agent-generated data can scale without expert annotation or environment rewards
  — 来源: `2510.08558`
- Continuous embedding space storage preserves multimodal experience better than text prompts for GUI tasks
  — 来源: `2510.09038`
- Memory scale follows a logarithmic linear growth law in relation to agent performance
  — 来源: `2510.09038`
- 原生浏览器交互范式无需重型外部工具即可实现有效网页智能体
  — 来源: `2510.10666`
- 显式记忆机制可有效防止长推理链中的信息丢失问题
  — 来源: `2510.10666`
- 人类启发的原子操作集（含滚动）可减少对静态摘要的依赖
  — 来源: `2510.10666`
- 记忆管理可作为核心推理能力被端到端学习
  — 来源: `2510.12635`
- 上下文管理可建模为 MDP 中的可学习动作而非固定规则
  — 来源: `2510.12635`
- 小模型通过记忆动作优化可超越大模型被动保留策略的性能
  — 来源: `2510.12635`
- Separation of memory maintenance and response generation enhances dialogue consistency
  — 来源: `2510.13363`
- The synergy between structured memory and explicit reasoning is necessary for small models to approximate large model performance
  — 来源: `2510.13363`
- Macroscopic Invariance Constraint: Long-term user profiles converge to fixed points beyond factual stability
  — 来源: `2510.16392`
- Phase Transition Dynamics: Profile updates exhibit non-linear characteristics triggered by evidence thresholds
  — 来源: `2510.16392`
- Information Density Maximization: Memory organization prioritizes density over raw capacity
  — 来源: `2510.16392`
- Decoupling online inference from memory update processes reduces test-time latency.
  — 来源: `2510.18866`
- Three-stage memory structure (Sensory-STM-LTM) aligns with cognitive efficiency principles for LLMs.
  — 来源: `2510.18866`
- End-to-end reasoning enables autonomous global task completion beyond predefined workflows.
  — 来源: `2510.21618`
- Memory folding mitigates error accumulation in long-horizon interactions by compressing history into structured forms.
  — 来源: `2510.21618`
- Tool accumulation via abstraction converts general capabilities into domain expertise.
  — 来源: `2510.23601`
- Procedural memory reusability reduces inference cost and improves accuracy.
  — 来源: `2510.23601`
- 上下文应被视为动态认知工作区而非被动日志
  — 来源: `2510.24699`
- 长程任务需要在上下文全面性与简洁性之间进行权衡
  — 来源: `2510.24699`
- Joint optimization of reasoning and memory management via RL yields better efficiency than fixed rules.
  — 来源: `2511.02805`
- Context length can be stabilized without sacrificing task accuracy through iterative memory compaction.
  — 来源: `2511.02805`
- Environment dynamics can be distilled into a reasoning-based experience model
  — 来源: `2511.03773`
- Synthetic experiences can effectively substitute real rollouts for RL training without significant performance loss
  — 来源: `2511.03773`
- 向前学习范式无需梯度更新即可实现智能体持续进化
  — 来源: `2511.06449`
- 经验增长遵循缩放律 (Experience Scaling Law)，经验积累与性能提升呈正相关
  — 来源: `2511.06449`
- 无梯度学习可避免传统微调的灾难性遗忘问题
  — 来源: `2511.06449`
- LLM reasoning capabilities can be directly converted into RL training signals to reduce reliance on sparse rewards.
  — 来源: `2511.10395`
- Combining self-generated tasks with historical experience reuse significantly improves sample efficiency in agent training.
  — 来源: `2511.10395`
- VLM 在自回归解码过程中倾向于优先积累文本上下文而忽视初始视觉证据
  — 来源: `2511.11007`
- 人类认知记忆理论（短期视觉主导 + 长期语义主导）可映射到神经网络潜在空间
  — 来源: `2511.11007`
- Memory systems should prioritize active user features over semantic grouping for long-horizon consistency
  — 来源: `2511.13593`
- Hierarchical retrieval achieves Pareto optimality between efficiency and performance
  — 来源: `2511.13593`
- Lossless event storage preserves fine-grained details better than lossy summarization or compression methods
  — 来源: `2511.17208`
- Reasoning-time effort (inference compute) can compensate for storage simplicity to achieve high accuracy
  — 来源: `2511.17208`
- Memory system performance is an optimization function of context size and task accuracy.
  — 来源: `2511.18423`
- Just-In-Time Compilation principles can be applied to dynamic context construction in agents.
  — 来源: `2511.18423`
- 认知心理学记忆模型可有效映射为 LLM 记忆技术组件以提升交互连续性
  — 来源: `2512.01710`
- 存储与检索接口分离能提升记忆系统的模块化与扩展性
  — 来源: `2512.01710`
- Dynamic multimodal memory enhances long video reasoning capability beyond text-only summaries
  — 来源: `2512.02425`
- Adaptive retrieval based on information sufficiency optimizes context window usage compared to fixed strategies
  — 来源: `2512.02425`
- Scalable memory mechanisms are more critical than model scale for continuous learning
  — 来源: `2512.03627`
- Dual-path memory (Intuition + Deliberation) mimics human cognitive complementarity
  — 来源: `2512.03627`
- Retrieval enhancement and parameter internalization can evolve synchronously
  — 来源: `2512.03627`
- Memory capabilities can be distilled from large models into lightweight adapters without full model fine-tuning.
  — 来源: `2512.04763`
- Modular memory operations (extract, update, generate) optimize resource usage on constrained devices.
  — 来源: `2512.04763`
- Memory quality outweighs quantity in agent evolution
  — 来源: `2512.10696`
- Dynamic refinement prevents experience pollution
  — 来源: `2512.10696`
- Keypoint-level distillation enables better knowledge transfer than trajectory-level
  — 来源: `2512.10696`
- Small model with high-quality memory can outperform large model without memory
  — 来源: `2512.10696`
- Memory relevance decays exponentially over time, requiring time-aware weighting mechanisms.
  — 来源: `2512.12686`
- Separating episodic (summary) and semantic (graph) memory improves scalability and interpretability.
  — 来源: `2512.12686`
- 记忆应作为结构化推理的一级基底 (Structured First-Class Substrate)
  — 来源: `2512.12818`
- 必须严格区分观察内容 (事实) 与推断内容 (信念) 以维持一致性
  — 来源: `2512.12818`
- 记忆应被视为代理智能设计中的一等原始概念 (First-class Primitive)
  — 来源: `2512.13564`
- 统一的分类学有助于解决领域碎片化和术语混淆问题
  — 来源: `2512.13564`
- 记忆系统的多样性无法仅通过长/短期记忆二分法捕捉
  — 来源: `2512.13564`
- Structure-then-Select preserves semantic fidelity better than token-level deletion
  — 来源: `2512.14244`
- Explicit structural representation reduces hallucination compared to implicit encoding
  — 来源: `2512.14244`
- Meta-cognition (System 3) is necessary for active goal generation and self-supervision in agents.
  — 来源: `2512.18202`
- Identity continuity and autobiographical memory are prerequisites for agents to exhibit Artificial Life characteristics.
  — 来源: `2512.18202`
- 记忆架构应随任务上下文动态调整以实现元适应
  — 来源: `2512.18746`
- 联合进化经验知识与记忆架构优于单一维度进化
  — 来源: `2512.18746`
- 代理记忆系统可通过元进化范式实现自我优化
  — 来源: `2512.18746`
- Memory management can be formally modeled as a Markov Decision Process (MDP)
  — 来源: `2601.01885`
- Unified optimization of LTM and STM yields superior performance compared to separate heuristic management
  — 来源: `2601.01885`
- 计算记忆印迹生命周期理论 (Computational Engram Lifecycle)
  — 来源: `2601.02163`
- 碎片化情节体验可转化为连贯稳定的知识结构
  — 来源: `2601.02163`
- Convergence of memory updates is proved under the Generalized Expectation Maximization (GEM) framework
  — 来源: `2601.03192`
- Variance of the utility updates is theoretically bounded
  — 来源: `2601.03192`
- Memory Orthogonality Principle: Semantic, Temporal, Causal, and Entity information should be decoupled to reduce information entanglement.
  — 来源: `2601.03236`
- Dual-Stream Efficiency Principle: Separating immediate ingestion from asynchronous consolidation optimizes both latency and memory quality.
  — 来源: `2601.03236`
- Memory organization should follow Event Segmentation Theory for better cognitive alignment
  — 来源: `2601.04726`
- Explicit logical relations are superior to semantic similarity for long-horizon reasoning
  — 来源: `2601.04726`

### 10.2 验证公理 (Validation)

共 **312** 条验证公理。

- Paraphrase Invariance: Edited knowledge must generalize to semantically equivalent queries
  — 来源: `2104.08164`
- Success Criterion: Post-edit model must output target answer for input query
  — 来源: `2104.08164`
- 长期记忆大小有界则推理速度不随视频长度增加而下降
  — 来源: `2207.07115`
- 记忆巩固机制能在压缩存储的同时保持长时序下的特征判别力
  — 来源: `2207.07115`
- Zero-shot performance improvement on math and QA tasks validates the efficacy of self-supervised tool learning.
  — 来源: `2302.04761`
- Stable perplexity (PPL) on standard text validates the absence of catastrophic forgetting.
  — 来源: `2302.04761`
- Reflexion 在 AlfWorld 和 HumanEval 等任务上的成功率显著优于 ReAct 和 CoT 基线
  — 来源: `2303.11366`
- 性能提升效果依赖于基座模型的自我评估与反思能力阈值
  — 来源: `2303.11366`
- Ablation of reflection components leads to a measurable decrease in behavioral believability
  — 来源: `2304.03442`
- Multi-agent coordination emerges from individual agents accessing shared environmental memory
  — 来源: `2304.03442`
- 医学专家人工评估是验证医疗模型安全性的必要公理
  — 来源: `2304.06975`
- SUS 评分优于基线模型证明领域适配成功
  — 来源: `2304.06975`
- SCM achieves better retrieval recall than competitive baselines in long-dialogue tasks
  — 来源: `2304.13343`
- SCM generates more informative responses without requiring model fine-tuning
  — 来源: `2304.13343`
- Hierarchical summarization improves retrieval accuracy compared to raw storage
  — 来源: `2305.10250`
- Dynamic forgetting mechanism reduces retrieval noise compared to static storage
  — 来源: `2305.10250`
- Ablation of memory components significantly reduces text coherence
  — 来源: `2305.13304`
- Generation quality scales with the capability of the base LLM model
  — 来源: `2305.13304`
- 引入通用读写记忆能显著提升模型在知识密集型和时效性任务上的准确性
  — 来源: `2305.14322`
- 无需重新训练模型参数即可通过外部记忆实现知识更新与纠错
  — 来源: `2305.14322`
- 性能保持公理：4 倍压缩率下，困惑度变化小于 0.5，任务准确率相当或更优
  — 来源: `2307.06945`
- 效率增益公理：引入记忆槽可显著降低注意力计算复杂度，提升推理速度 2-3.5 倍
  — 来源: `2307.06945`
- API 执行状态码可用于自动验证任务完成的成功率
  — 来源: `2307.16789`
- 分布外数据集 (APIBench) 上的表现可用于验证模型的零样本泛化能力
  — 来源: `2307.16789`
- Assembly line collaboration yields higher coherence than chat-based interaction.
  — 来源: `2308.00352`
- Role specialization improves task completion accuracy in complex software engineering tasks.
  — 来源: `2308.00352`
- Retrospective model optimization yields higher success rates than static reflection baselines (e.g., Reflexion).
  — 来源: `2308.02151`
- Minimal parameter tuning (0.53M) is sufficient for significant agent improvement on complex tasks.
  — 来源: `2308.02151`
- GPT4 评估结果与人类一致性判断具有相关性
  — 来源: `2308.08239`
- 带备忘录的 2k 上下文在一致性指标上优于不带备忘录的更大上下文
  — 来源: `2308.08239`
- Embedding similarity between generated response and character script correlates with perceived character consistency.
  — 来源: `2308.09597`
- Cosine similarity of embeddings serves as a proxy for character consistency evaluation.
  — 来源: `2308.09597`
- One-shot prompting significantly improves memory prediction accuracy (Mem_F1) compared to zero-shot settings.
  — 来源: `2308.15022`
- Recursive summary memory outperforms full context input in terms of consistency and recall in later dialogue sessions.
  — 来源: `2308.15022`
- Cost Efficiency Axiom: The proposed architecture reduces computational cost by 10-100x compared to baseline Generative Agents
  — 来源: `2310.02172`
- Real-time Interaction Axiom: Reduced latency enables seamless multi-agent collaboration in 3D environments
  — 来源: `2310.02172`
- The model reproduces human psychological effects like Primacy and Recency.
  — 来源: `2310.03052`
- Retrieved memory average age increases with training steps, proving effective LTM usage.
  — 来源: `2310.03052`
- 70% context usage threshold triggers a warning state.
  — 来源: `2310.08560`
- 100% context usage threshold triggers an automatic eviction/refresh cycle.
  — 来源: `2310.08560`
- Agent fixes unique bugs compared to prior techniques (39 unique fixes on Defects4J)
  — 来源: `2403.17134`
- Token cost is a measurable constraint for autonomy (avg 270k tokens/bug)
  — 来源: `2403.17134`
- Domain-specific memory sharing yields higher performance than global sharing
  — 来源: `2404.09982`
- Excessive memory capacity leads to performance degradation due to noise or retrieval difficulty
  — 来源: `2404.09982`
- Comprehensiveness and Diversity are superior metrics for evaluating global sensemaking tasks.
  — 来源: `2404.16130`
- Higher-level community summaries significantly reduce token consumption (up to 97%) while maintaining understanding.
  — 来源: `2404.16130`
- 基于图谱的 PPR 检索在准确率上可媲美迭代检索且成本更低
  — 来源: `2405.14831`
- 结构化记忆优于孤立段落编码在处理跨文档知识时的表现
  — 来源: `2405.14831`
- Lightweight models augmented with collaborative learning outperform large standalone models
  — 来源: `2405.16089`
- Dual-view graph structures yield superior retrieval diversity compared to single-view baselines
  — 来源: `2405.16089`
- KGT 在个性化性能上达到或优于传统微调方法
  — 来源: `2405.19686`
- KGT 在个性化过程中显著降低延迟和 GPU 显存消耗
  — 来源: `2405.19686`
- F2 分数（侧重召回）是评估记忆检索完整性的关键指标
  — 来源: `2406.00057`
- 注入前 2-4 句对话上下文对解决模糊查询至关重要
  — 来源: `2406.00057`
- Conditioned traversal outperforms heuristic search (BFS/DFS) in retrieval relevance
  — 来源: `2406.06124`
- HAT retrieval yields higher BLEU scores than full context injection
  — 来源: `2406.06124`
- Counterfactual question answering accuracy correlates with the truthfulness of retrieved memory.
  — 来源: `2406.10996`
- TeaFarm pipeline metrics validate the reduction of memory hallucination in dialogue agents.
  — 来源: `2406.10996`
- 长文本理解任务性能提升可验证显式记忆机制的有效性
  — 来源: `2407.01178`
- 困惑度 (PPL) 降低可作为记忆增强效果的量化指标
  — 来源: `2407.01178`
- 记忆检索准确率与下游任务性能呈正相关
  — 来源: `2407.01178`
- AriGraph outperforms Full History and RAG baselines in complex text game success rates
  — 来源: `2407.04363`
- Dynamic graph update is crucial for adapting to environment changes and maintaining consistency
  — 来源: `2407.04363`
- 记忆衰减机制在时间敏感的金融数据环境中提升检索相关性
  — 来源: `2407.06567`
- 集成反思的显式风控模块显著降低最大回撤
  — 来源: `2407.06567`
- EMG-RAG 方法在 ROUGE-1 指标上较基线 RAG 方法提升约 10%
  — 来源: `2409.19401`
- 在连续 4 周的记忆编辑场景下，系统性能保持稳定 (93%-97%)
  — 来源: `2409.19401`
- Locality metric increase correlates with effective null-space constraint
  — 来源: `2410.02355`
- Edit Success metric confirms target knowledge integration without degradation
  — 来源: `2410.02355`
- 零幻觉约束公理：对有效工具令牌空间应用约束束搜索可保证 0% 的工具幻觉率。
  — 来源: `2410.03439`
- 原子效率原则公理：在智能体任务中，原子索引的端到端任务成功率优于语义索引。
  — 来源: `2410.03439`
- Removing visual feedback reduces task success rate by approximately 30%.
  — 来源: `2410.08164`
- Cross-operating system performance variance remains below 5% indicating high pan-platform generalization.
  — 来源: `2410.08164`
- Optimized memory (documentation) significantly improves tool invocation success rates.
  — 来源: `2410.08197`
- Optimized memory exhibits generalization capabilities across different LLM architectures.
  — 来源: `2410.08197`
- Performance remains robust up to 500k tokens context length.
  — 来源: `2410.12859`
- Convergence is achievable via Longest Common Subsequence (LCS) stability check.
  — 来源: `2410.12859`
- Depth-adaptive threshold mechanism ensures hierarchy tightness and separation.
  — 来源: `2410.14052`
- Parent node aggregation update improves long-range retrieval recall.
  — 来源: `2410.14052`
- Phenomenon Reproduction: Successful simulation of polarization and herd effects validates model fidelity
  — 来源: `2411.11581`
- Cross-Platform Adaptability: Successful deployment on X and Reddit scenarios validates framework flexibility
  — 来源: `2411.11581`
- Performance improvement on Video-MME validates the effectiveness of visual-text alignment.
  — 来源: `2411.13093`
- Token efficiency metrics validate the cost-effectiveness of the retrieval mechanism.
  — 来源: `2411.13093`
- Hybrid memory systems achieve higher SPL than reality-only systems in unseen VLN tasks
  — 来源: `2412.01857`
- Memory pruning based on feature similarity maintains efficiency without significant performance loss
  — 来源: `2412.01857`
- An optimal update frequency exists (k=3 dialogue turns) that maximizes user satisfaction while minimizing computational cost.
  — 来源: `2412.13103`
- Inference-based memory updates can achieve performance close to Golden Persona ground truth without model fine-tuning.
  — 来源: `2412.13103`
- 在 Ego4D-VQ3D 和 EnvQA 上的性能提升验证了具身传感器对记忆构建的必要性
  — 来源: `2501.00358`
- 消融实验证明无传感器输入会导致动态理解能力下降
  — 来源: `2501.00358`
- 移除权重衰减会导致长序列任务性能显著下降
  — 来源: `2501.00663`
- 在超过 2M token 的上下文窗口中，Titans 性能优于 Transformer 和 Mamba
  — 来源: `2501.00663`
- Efficiency Gain Axiom: TKG retrieval reduces context tokens by approximately 98% (115k to 1.6k) compared to full-context baselines.
  — 来源: `2501.13956`
- Performance Gain Axiom: TKG improves accuracy by 15-18% on long-context tasks compared to full-context and MemGPT baselines.
  — 来源: `2501.13956`
- Jointly trained retrievers significantly outperform attention-score-based retrieval for long-term memory access
  — 来源: `2502.00592`
- Three-stage training strategy (Short->Long->LTM) is necessary for stable convergence of hybrid memory systems
  — 来源: `2502.00592`
- Few-shot performance correlates positively with multimodal feature richness.
  — 来源: `2502.04395`
- Visual modality contributes more significantly to periodic pattern capture than text modality.
  — 来源: `2502.04395`
- Memory-augmented models demonstrate superior performance on long-context benchmarks (BABILong) compared to standard baselines
  — 来源: `2502.06049`
- Integration of memory modules does not degrade performance on general knowledge benchmarks (MMLU)
  — 来源: `2502.06049`
- 提取数量 (EN) 和完全提取率 (CER) 可有效量化隐私风险 (EN and CER effectively quantify privacy risk)
  — 来源: `2502.13172`
- 检索深度 (k 值) 增加会加剧记忆泄露 (Increasing retrieval depth k exacerbates memory leakage)
  — 来源: `2502.13172`
- Mem2Ego 在物体导航任务上的成功率和路径效率优于现有 SOTA 方法
  — 来源: `2502.14254`
- 移除全局记忆或自适应检索模块会导致导航性能显著下降
  — 来源: `2502.14254`
- 该方法在仿真环境中有效改善了长程导航中的迷失问题
  — 来源: `2502.14254`
- Hybrid graph structure improves multi-hop reasoning without degrading fact memory performance.
  — 来源: `2502.14802`
- Token consumption is inversely proportional to retrieval efficiency in structured RAG systems.
  — 来源: `2502.14802`
- 困惑度降低验证保留能力 (Perplexity reduction validates retention capability)
  — 来源: `2502.15957`
- F1 提升验证检索能力 (F1 improvement validates retrieval capability)
  — 来源: `2502.15957`
- MemQ achieves State-of-the-Art performance on WebQSP and CWQ benchmarks.
  — 来源: `2503.05193`
- Decoupling tool invocation from reasoning improves interpretability and accuracy in KGQA tasks.
  — 来源: `2503.05193`
- 交互式回退显著降低错误修复成本，无需全流程重执行
  — 来源: `2503.09263`
- 在无 Web API 集成条件下，多智能体框架可达 SOTA 性能
  — 来源: `2503.09263`
- Verified Skills reduce Hallucination: Skills passing execution tests yield higher task success rates than unverified text prompts.
  — 来源: `2504.06821`
- Online Induction mitigates Distribution Shift: Dynamically induced skills adapt better to test-time environments than offline trained policies.
  — 来源: `2504.06821`
- Skill transfer from strong to weak agents significantly improves task success rates (up to 54.3%).
  — 来源: `2504.07079`
- Reusable skills reduce exploration costs and improve generalization in unknown web environments.
  — 来源: `2504.07079`
- 跨查询记忆积累能显著降低重复错误率
  — 来源: `2504.07952`
- 动态记忆机制在复杂推理任务中比静态检索更有效
  — 来源: `2504.07952`
- 策略复用比单纯增加指令更能提升性能
  — 来源: `2504.07952`
- Small models (7B) with retrieval augmentation can match the performance of large models (GPT-4o) without it.
  — 来源: `2504.13805`
- Removing retrieval or parsing modules significantly degrades agent performance (proven via ablation studies).
  — 来源: `2504.13805`
- Hybrid detection (UIA+Vision) reduces failure rates compared to single-modality detection.
  — 来源: `2504.14603`
- GUI+API hybrid mode reduces task steps significantly compared to pure GUI interaction.
  — 来源: `2504.14603`
- Mem0 相比全上下文方法可降低 91% 延迟及 90% 成本
  — 来源: `2504.19413`
- 图记忆结构相比基础版能进一步提升 2% 的准确率
  — 来源: `2504.19413`
- Deleting database entries achieves perfect machine unlearning without requiring model fine-tuning.
  — 来源: `2505.15962`
- Shielding retrieved values during loss calculation effectively prevents internal memorization of facts.
  — 来源: `2505.15962`
- Increasing retrieved memory quantity leads to performance degradation due to information overload
  — 来源: `2505.16348`
- Human baseline 100% completion proves the task is solvable and the bottleneck lies in agent memory mechanisms
  — 来源: `2505.16348`
- Continuous memory maintains performance stability under increased retrieval count compared to discrete token RAG
  — 来源: `2505.17670`
- Memory vectors encoded by VLM possess cross-modal semantic generalization capability transferable to LLMs
  — 来源: `2505.17670`
- Intent alignment improves retrieval recall by 7.7% compared to standard RAG.
  — 来源: `2505.20231`
- Slot-guided filtering reduces dialogue turns by up to 47% while maintaining 99% task success rate.
  — 来源: `2505.20231`
- A minimalist architecture with self-evolution achieves superior pass@1 scores on GAIA compared to complex pre-defined systems.
  — 来源: `2505.20286`
- 沙箱隔离公理：所有自我修改代码必须在隔离环境中执行
  — 来源: `2505.22954`
- 人工监督公理：关键进化节点需保留人工干预或停止机制
  — 来源: `2505.22954`
- 20-frame context window optimizes the performance-speed trade-off for interactive generation
  — 来源: `2506.03141`
- PSNR and LPIPS metrics effectively quantify memory capability in video generation tasks
  — 来源: `2506.03141`
- Hierarchical memory architecture improves embodied action success rates without modifying underlying MAS frameworks
  — 来源: `2506.07398`
- Absorbing new collaboration trajectories promotes progressive system evolution and measurable performance gain
  — 来源: `2506.07398`
- RL Training Superiority: RL training outperforms SFT in long-horizon tasks beyond 6 steps.
  — 来源: `2506.15841`
- Efficiency-Performance Tradeoff: A 7B model with MEM1 can outperform a 14B model with full context while using less compute.
  — 来源: `2506.15841`
- Performance loss remains under 5% even at 3.5M context length
  — 来源: `2507.02259`
- 95%+ accuracy is achievable on 512K RULER benchmark with MemAgent
  — 来源: `2507.02259`
- Hybrid retrieval mechanisms significantly improve agent performance compared to baseline frameworks (e.g., +18.7pp in pass@3).
  — 来源: `2507.06229`
- Automatically generated experiences are comparable in quality to human-curated ones for agent enhancement.
  — 来源: `2507.06229`
- 记忆压缩与巩固是核心优势，显式存储巩固后事件解决多跳推理信息分散问题
  — 来源: `2507.07957`
- 存储效率数量级优化 (减少 99.9%) 适合长期运行与可穿戴设备场景
  — 来源: `2507.07957`
- 分层记忆存储有效支持时间推理能力
  — 来源: `2507.07957`
- 无需重训练模型即可兼容闭源 LLM(GPT-4、Gemini 等)
  — 来源: `2507.07957`
- Hybrid mode achieves >90% removal rate with high task completion on reasoning models
  — 来源: `2507.21428`
- System prompt must include dynamic tool count variable for effective removal
  — 来源: `2507.21428`
- Index routing retrieval outperforms full similarity search in latency and precision
  — 来源: `2507.22925`
- Dynamic weight regulation significantly improves long-term dialogue coherence
  — 来源: `2507.22925`
- MLP Memory 在 5 个 QA 基准上相对提升 12.3% 准确率
  — 来源: `2508.01832`
- MLP Memory 推理速度比 RAG 快 2.5 倍 (TTFT/TPS 指标)
  — 来源: `2508.01832`
- MLP Memory 在 HaluEval 上减少幻觉高达 10 个点
  — 来源: `2508.01832`
- MLP Memory 在 9 个通用 NLP 任务上绝对提升 5.2 分
  — 来源: `2508.01832`
- Structured memory reduces token usage by approximately 96% compared to full context
  — 来源: `2508.03341`
- Prediction-Calibration mechanism yields higher accuracy than passive knowledge extraction
  — 来源: `2508.03341`
- ACM improves accuracy on information-sparse tasks compared to passive context.
  — 来源: `2508.04664`
- Internal context optimization can outperform external retrieval for specific long-context tasks.
  — 来源: `2508.04664`
- OSWorld 基准成功率提升验证了自进化有效性
  — 来源: `2508.04700`
- 专家到通才策略优于直接通才训练
  — 来源: `2508.04700`
- Token reduction of 25-47% maintains or improves F1 score
  — 来源: `2508.04903`
- 3 Iterations yield optimal efficiency-accuracy balance
  — 来源: `2508.04903`
- 引入纠错更新机制的记忆库能显著提升后续任务的成功率
  — 来源: `2508.06433`
- 程序性记忆的复用能有效减少任务执行的平均步骤与 Token 消耗
  — 来源: `2508.06433`
- Intrinsic memory mechanisms reduce output variance in execution tasks
  — 来源: `2508.08997`
- Structured templates improve reliability in planning tasks compared to generic memory
  — 来源: `2508.08997`
- Reinforcement learning trained memory mechanisms improve accuracy in long-video QA tasks compared to prompt engineering baselines
  — 来源: `2508.09736`
- Perplexity reduction on domain corpora validates memory effectiveness and knowledge injection
  — 来源: `2508.09874`
- Cross-model performance consistency validates the plug-and-play capability across different model sizes
  — 来源: `2508.09874`
- 迭代推理在 200K+ tokens 场景下优于单步检索（相对增益最高 11%）
  — 来源: `2508.10419`
- 移除记忆工作区会导致长文本全局理解性能显著下降
  — 来源: `2508.10419`
- Hybrid retrieval yields higher Fact Recall (FR) than pure vector retrieval in long-dialogue tasks.
  — 来源: `2508.12630`
- Coreference chains are critical for maintaining Discourse Coherence (DC).
  — 来源: `2508.12630`
- CARE improves QA and Fact Verification accuracy by an average of 5.0% in conflict scenarios
  — 来源: `2508.15253`
- Removal of the Context Assessor component results in significant performance decline
  — 来源: `2508.15253`
- 高质量记忆内容生成可显著降低系统响应延迟
  — 来源: `2508.15294`
- 检索与生成单元分离设计能优化匹配精度与生成效果
  — 来源: `2508.15294`
- 无需微调的智能体在 GAIA 基准上可达到最先进水平 (87.88% Pass@3)
  — 来源: `2508.16153`
- 记忆机制能显著提升分布外 (OOD) 任务的泛化能力 (4.7% 至 9.6%)
  — 来源: `2508.16153`
- 完美上下文下任务可解性公理：若提供地面真值信息，SOTA 模型成功率可达 98.18%
  — 来源: `2508.19005`
- 记忆瓶颈定位公理：当前代理瓶颈在于记忆管理而非任务理解能力
  — 来源: `2508.19005`
- 模型规模非充分条件公理：模型规模从 8B 至 235B 提升不直接解决长期记忆问题
  — 来源: `2508.19005`
- 评估维度扩展公理：传统任务完成率不足以评估终身学习能力，需引入遗忘度量、迁移指标
  — 来源: `2508.19005`
- Dual-stream memory achieves higher success rates than single-stream alternatives
  — 来源: `2508.19236`
- Token merging consolidation outperforms FIFO strategies in retaining relevant history
  — 来源: `2508.19236`
- High data efficiency (152 QA pairs) achieves SOTA performance
  — 来源: `2508.19828`
- Dual-agent collaboration improves reasoning accuracy over single-agent baselines
  — 来源: `2508.19828`
- 系统使用能显著降低用户的孤独感量表评分
  — 来源: `2509.05298`
- 记忆压缩算法能在降低存储占用的同时保持对话连贯性
  — 来源: `2509.05298`
- 多模态融合比单模态输入具有更高的情感识别准确率
  — 来源: `2509.05298`
- 小模型配合预存储推理可超越大模型基线：14B 模型+PREMem 性能优于 72B 基线
  — 来源: `2509.10852`
- 低 Token 预算下性能稳健公理：在上下文受限情况下，预存储推理方法优于传统检索增强方法
  — 来源: `2509.10852`
- 有限容量配合主动遗忘机制在超长对话中的精度优于无限记忆累积
  — 来源: `2509.11860`
- 双分支架构在记忆提取准确率及问答精度上显著优于单分支方法
  — 来源: `2509.11860`
- SDM demonstrates higher robustness than Softmax under covariate shift conditions
  — 来源: `2509.12760`
- SDM supports more reliable selective classification decisions compared to existing calibration methods
  — 来源: `2509.12760`
- Separate retrieval of high and low-level memories improves generalization and decision performance over single coarse-grained retrieval.
  — 来源: `2509.12810`
- Decoupling planning and execution knowledge enhances multi-task learning efficiency.
  — 来源: `2509.12810`
- Agentic CPT 方法在多个基准测试（BrowseComp、HLE 等）上优于现有开源领先模型
  — 来源: `2509.13310`
- 30B 参数规模的智能体基座模型在性能与成本间取得较好平衡
  — 来源: `2509.13310`
- Dynamic Outline Superiority: 动态大纲机制在 RACE 得分上显著优于静态大纲
  — 来源: `2509.13312`
- Dual-Agent Accuracy: 双智能体架构在引用准确率 (FACT) 上优于单体生成范式
  — 来源: `2509.13312`
- 无训练记忆检索在任务成功率上可优于微调基线方法
  — 来源: `2509.17459`
- 结构化对比记忆能显著提升策略多样性 (熵) 并避免策略坍塌
  — 来源: `2509.17459`
- High Confidence System 1 Output reduces System 2 Load
  — 来源: `2509.22315`
- System 2 Activation significantly improves Hard Task Accuracy
  — 来源: `2509.22315`
- Generative Latent Memory outperforms external retrieval memory systems on task success rates
  — 来源: `2509.24704`
- Self-evolving memory functions emerge spontaneously through interaction without labeled data
  — 来源: `2509.24704`
- 配备 ReasoningBank 的智能体在 Web 浏览和软件工程基准上优于现有记忆机制
  — 来源: `2509.25140`
- MaTTS 机制对记忆质量提升具有必要性
  — 来源: `2509.25140`
- 智能体可通过历史经验实现自我进化能力
  — 来源: `2509.25140`
- 在短序列 (30k tokens) 上训练的策略可以泛化至长序列 (400k+ tokens) 推理
  — 来源: `2509.25911`
- 基于 RL 的记忆管理在问答准确率上显著优于基于规则的记忆系统基线
  — 来源: `2509.25911`
- Cost-Accuracy Pareto Axiom: Significant token reduction (26-54%) can be achieved without degrading task accuracy
  — 来源: `2510.00615`
- Small Model Enhancement Axiom: Compression mechanisms disproportionately benefit smaller models in long-horizon tasks by reducing context overload
  — 来源: `2510.00615`
- A 160M model augmented with 18M memory parameters performs comparably to a dense model with 2x parameters
  — 来源: `2510.02375`
- Long-tail knowledge accuracy improves significantly (e.g., 17% to 83%) with hierarchical memory augmentation
  — 来源: `2510.02375`
- ACE 框架在降低 80% 以上 Token 成本的同时保持或提升准确率
  — 来源: `2510.04618`
- 增量更新机制有效防止了长程任务中的知识丢失
  — 来源: `2510.04618`
- Orchestrator memory significantly improves planning accuracy (编排器记忆显著提升规划准确性)
  — 来源: `2510.04851`
- Small models with LEGOMem approximate large model performance (配备 LEGOMem 的小模型可接近大模型性能)
  — 来源: `2510.04851`
- Online incremental update mechanisms are significantly more efficient than offline reconstruction for dynamic long-context tasks
  — 来源: `2510.05520`
- Hierarchical memory structures with flexibility outperform rigid or unstructured memory in complex reasoning tasks
  — 来源: `2510.05520`
- ToolMem 在文本场景降低 MAE 14.8%，图像场景降低 28.7%
  — 来源: `2510.06664`
- 工具选择准确率提升 24%，Pearson 相关系数提升 76.7%
  — 来源: `2510.06664`
- 弱模型场景下记忆机制增益显著优于强模型场景
  — 来源: `2510.06664`
- 检索粒度 k=12 时信息量与噪声达到最优平衡
  — 来源: `2510.06664`
- 检索准确率与响应正确性共同验证记忆系统的有效性
  — 来源: `2510.07925`
- 用户反馈与 BertScore 指标可量化评估感知个性化水平
  — 来源: `2510.07925`
- Performance on AIME benchmarks improves with token prior injection compared to baseline
  — 来源: `2510.08191`
- Cost efficiency is higher than fine-tuning small models for specific domains
  — 来源: `2510.08191`
- Consistent effectiveness improvement across eight diverse environments
  — 来源: `2510.08558`
- Enhanced out-of-domain generalization capability compared to baselines
  — 来源: `2510.08558`
- A 7B open-source model equipped with this memory system can match the performance of top closed-source models like GPT-4o
  — 来源: `2510.09038`
- Peak performance is achieved with only 1500 fine-tuning samples, indicating high data efficiency
  — 来源: `2510.09038`
- 5.3K 训练样本配合 7B 模型可实现多跳 QA 任务的 SOTA 性能
  — 来源: `2510.10666`
- 增加交互步数预算（6 步→30 步）可显著提升任务完成率
  — 来源: `2510.10666`
- 双重评估机制（EM+LLM-judge）比单一指标更能反映真实性能
  — 来源: `2510.10666`
- RL 优化相比 SFT 在多目标任务上准确率提升 10.6% (48.5%→59.1%)
  — 来源: `2510.12635`
- 记忆动作使 14B 模型准确率超越 235B 模型 (59.1% vs 53.1%)
  — 来源: `2510.12635`
- 主动上下文管理可减少 51% 上下文长度和 40% 推理延迟
  — 来源: `2510.12635`
- NLI-based metrics (CS/DER) are valid proxies for quantifying dialogue consistency
  — 来源: `2510.13363`
- Asynchronous memory updates can mitigate the latency overhead of structured reasoning
  — 来源: `2510.13363`
- Memory Evolution Mechanism is more important than Storage Capacity for performance
  — 来源: `2510.16392`
- Multi-scale Organization achieves near Full-Context performance within limited context windows
  — 来源: `2510.16392`
- Threshold Mechanism effectively filters noise while maintaining adaptability
  — 来源: `2510.16392`
- Soft update retains global information better than hard update in long-dialogue scenarios.
  — 来源: `2510.18866`
- Pre-compression combined with topic segmentation reduces token consumption without significant accuracy loss.
  — 来源: `2510.18866`
- Superior performance on 8 diverse benchmarks validates the effectiveness of the end-to-end framework.
  — 来源: `2510.21618`
- Ablation studies confirm that removing Memory Folding or ToolPO significantly degrades performance.
  — 来源: `2510.21618`
- Three evolution iterations yield the optimal balance between performance and redundancy.
  — 来源: `2510.23601`
- A similarity threshold of 0.7 optimizes tool retrieval precision.
  — 来源: `2510.23601`
- 30B 参数的 AgentFold 模型在 BrowseComp 上性能超越 671B 基线模型
  — 来源: `2510.24699`
- 100 轮交互后的上下文可被压缩至约 7k tokens
  — 来源: `2510.24699`
- A 3B model with MemSearcher can outperform a 7B baseline on search tasks.
  — 来源: `2511.02805`
- Efficiency gains (compute/memory) are achievable simultaneously with accuracy improvements.
  — 来源: `2511.02805`
- Performance on WebArena improves >30% using synthetic experience compared to baselines
  — 来源: `2511.03773`
- Policies trained on pure synthetic experience can successfully transfer to real environments (Sim-to-Real)
  — 来源: `2511.03773`
- 经验可跨智能体继承并显著提升新智能体性能
  — 来源: `2511.06449`
- 无梯度向前学习在数学、化学、生物多领域验证有效
  — 来源: `2511.06449`
- 单智能体持续进化成本可控制在 100 美元以下
  — 来源: `2511.06449`
- Removing any of the three mechanisms (Questioning, Navigating, Attributing) leads to significant performance degradation in ablation studies.
  — 来源: `2511.10395`
- Optimal process-result reward weight (alpha) lies between 0.10 and 0.20 for stable convergence.
  — 来源: `2511.10395`
- 潜在空间记忆增强使 VLM 在视觉理解、推理、生成任务上平均性能提升 11.0%
  — 来源: `2511.11007`
- O-Mem achieves 51.67% accuracy on LoCoMo, outperforming LangMem
  — 来源: `2511.13593`
- O-Mem achieves 62.99% accuracy on PERSONAMEM, outperforming A-Mem
  — 来源: `2511.13593`
- System performance remains stable across retrieval quantity hyperparameters within the 20-40 range
  — 来源: `2511.17208`
- LLM filtering module is the critical determinant for multi-hop reasoning accuracy
  — 来源: `2511.17208`
- Research module effectiveness requires a model size threshold (e.g., >7B parameters).
  — 来源: `2511.18423`
- Memory module remains robust even with smaller model capacities.
  — 来源: `2511.18423`
- 异步记忆更新机制可在不增加对话延迟前提下实现记忆增强
  — 来源: `2512.01710`
- 基于 Token 的修剪机制能有效防止上下文溢出并维持系统性能
  — 来源: `2512.01710`
- 结构化记忆增强在真实应用中能显著提升用户留存率与对话时长
  — 来源: `2512.01710`
- WorldMM achieves an average 8.4% performance improvement over SOTA on five long-video QA benchmarks
  — 来源: `2512.02425`
- Retrieving fewer relevant memories reduces input tokens while maintaining or improving accuracy
  — 来源: `2512.02425`
- Memory mechanism effectiveness is independent of full model retraining
  — 来源: `2512.03627`
- Sliding window cache avoids frequent long-term storage updates while maintaining context
  — 来源: `2512.03627`
- Lightweight fine-tuning with external memory improves performance without massive compute
  — 来源: `2512.03627`
- SLMs with MemLoRA adapters achieve performance comparable to models 10x larger on memory benchmarks.
  — 来源: `2512.04763`
- Visual memory integration significantly outperforms title-based methods in multimodal tasks.
  — 来源: `2512.04763`
- Dynamic version outperforms fixed version across all settings
  — 来源: `2512.10696`
- Retrieval count K=5 is optimal balance point
  — 来源: `2512.10696`
- Selective addition (success-only) outperforms full addition
  — 来源: `2512.10696`
- 32B summary model brings significant gains over 8B
  — 来源: `2512.10696`
- Structured knowledge triples significantly reduce token consumption compared to raw context retrieval.
  — 来源: `2512.12686`
- Time-aware weighting mechanisms effectively resolve information conflicts and improve update accuracy.
  — 来源: `2512.12686`
- 结构化记忆优化对长程任务的贡献优于单纯扩大模型规模
  — 来源: `2512.12818`
- 四逻辑网络架构能显著提升长程记忆基准得分并超越全上下文大模型
  — 来源: `2512.12818`
- 现有基准与开源框架可映射至形式 - 功能 - 动态三维体系进行验证
  — 来源: `2512.13564`
- 任务类型（事实/经验/工作）决定记忆形式的选择以优化成本
  — 来源: `2512.13564`
- 记忆系统的评估需覆盖形式、功能与动态三个维度
  — 来源: `2512.13564`
- High EDU structure prediction accuracy correlates with improved downstream task performance
  — 来源: `2512.14244`
- Explicit anchoring ensures traceability and reduces information loss during compression
  — 来源: `2512.14244`
- Memory retrieval reuse reduces repetitive reasoning steps by approximately 80%.
  — 来源: `2512.18202`
- The presence of System 3 increases complex task success rate by approximately 40%.
  — 来源: `2512.18202`
- 元进化框架在多个基准测试中性能提升显著（最高 17.06%）
  — 来源: `2512.18746`
- 跨任务与跨模型泛化能力验证了方法的有效性
  — 来源: `2512.18746`
- 仅进化知识或仅进化架构的效果均不如联合进化
  — 来源: `2512.18746`
- End-to-end RL strategy learning outperforms static heuristic-based memory rules
  — 来源: `2601.01885`
- Step-wise GRPO effectively solves long-term credit assignment in memory-intensive tasks
  — 来源: `2601.01885`
- 在 LoCoMo 和 Long-MemEval 基准上性能显著优于 SOTA 方法
  — 来源: `2601.02163`
- 结构化检索相比全量上下文输入能减少计算开销
  — 来源: `2601.02163`
- Memory Q-value prediction positively correlates with actual task success rate
  — 来源: `2601.03192`
- Forgetting rate is bounded below 0.05 under continuous learning scenarios
  — 来源: `2601.03192`
- LLM-as-a-Judge Correlation: Semantic scores from LLM judges correlate better with reasoning quality than traditional F1 in long-context tasks.
  — 来源: `2601.03236`
- Latency-Accuracy Compatibility: Structural decoupling allows low latency (1.47s) and high accuracy (0.700 Judge Score) to coexist.
  — 来源: `2601.03236`
- Event Graph structure improves retrieval and reasoning performance compared to flat memory
  — 来源: `2601.04726`
- CompassMem framework demonstrates consistency across multiple backbone models
  — 来源: `2601.04726`

---

## 十一、未来发展方向

### 短期 (2025-2026)

- 统一记忆检索接口标准，减少工程实现碎片化
- 建立记忆质量评估基准，量化新鲜度/一致性/置信度
- 完善隐私保护机制，特别是检索增强场景下的防御策略
- 扩展多模态记忆载体支持（视觉/音频/触觉）

### 中期 (2027-2028)

- 实现记忆的自动化反思与信念更新循环
- 建立跨 Agent 记忆共享协议
- 开发记忆演化可观测工具链
- 标准化记忆-决策因果链路分析

### 长期 (2029+)

- 探索记忆的自组织结构与涌现智能
- 建立 Agent Memory 形式化验证体系
- 实现记忆的跨模态迁移与泛化
- 定义 Agent Memory 伦理与安全框架

---

## 十二、概念索引

共 **1411** 个唯一概念，按字母序排列。

| 概念名 | 类别 | 论文数 | 权重 |
|-------|------|--------|------|
| 1B 参数 MLP 模块 | carrier | 1 | 1 |
| 64x64 Time Series Image | structure | 1 | 1 |
| 8-Vector Compressed Sequence | structure | 1 | 1 |
| <conclusion> Tag Structure (结论标签结构) | structure | 1 | 1 |
| Abstract Meaning Representation (AMR) | carrier | 1 | 1 |
| Abstract State | type | 1 | 1 |
| Abstract-to-OS Action Mapping | operation | 1 | 1 |
| Abstracted MCP Repository | structure | 1 | 1 |
| Action-Future State Pairs (动作 - 未来状态对) | structure | 1 | 1 |
| Action Trajectory Buffer | structure | 1 | 1 |
| Active Feature Extraction | operation | 1 | 1 |
| Active User Profile | type | 1 | 1 |
| Active Working Memory | type | 1 | 1 |
| Adapter 权重 (Adapter Weights) | carrier | 1 | 1 |
| Adaptive Graph Traversal | operation | 1 | 1 |
| Adaptive Retrieval | operation | 1 | 1 |
| Adaptive Task Generation | operation | 1 | 1 |
| ADD | operation | 1 | 1 |
| Add | operation | 1 | 1 |
| Adversarial Soft Prompting | operation | 1 | 1 |
| Age-tagged Memory Pool | structure | 1 | 1 |
| Agent Behavior Pre-training Data | carrier | 1 | 1 |
| Agent Behavior Trajectories (智能体行为轨迹) | type | 1 | 1 |
| Agent Context Window (代理上下文窗口) | carrier | 1 | 1 |
| Agent-Environment Interaction Trajectories | carrier | 1 | 1 |
| Agent Execution Trajectories (智能体执行轨迹) | carrier | 1 | 1 |
| Agent Foundation Model Architecture (智能体基座模型架构) | structure | 1 | 1 |
| Agent Interaction Logs (智能体交互日志) | carrier | 2 | 2 |
| Agent KB Infrastructure (Agent KB 基础设施) | structure | 1 | 1 |
| Agent-specific Output Logs | carrier | 1 | 1 |
| Agent Workflow Pipeline | structure | 1 | 1 |
| AgentFounder-30B Model | carrier | 1 | 1 |
| Agentic Continual Pre-training (智能体持续预训练) | operation | 1 | 1 |
| Agentic Memory | type | 3 | 3 |
| Anchor Model Parameters | carrier | 1 | 1 |
| API Context Window | carrier | 1 | 1 |
| API Documentation Text | carrier | 1 | 1 |
| API-Embedded Text Sequence | structure | 1 | 1 |
| API Function Definitions | carrier | 1 | 1 |
| API 生成清洗 (API Generation & Cleaning) | operation | 1 | 1 |
| API 语义记忆 (API Semantic Memory) | type | 1 | 1 |
| API 调用 (API Invocation) | operation | 1 | 1 |
| API 调用拦截 (API Call Interception) | operation | 1 | 1 |
| AR 虚拟形象 (AR Virtual Avatar) | carrier | 1 | 1 |
| Associative Memory | type | 1 | 1 |
| Asynchronous Self-Monitoring | operation | 1 | 1 |
| Asynchronous Update | operation | 1 | 1 |
| Attribute-Context Dual Layer | structure | 1 | 1 |
| Auto-scaling Collection (自动扩展收集) | operation | 1 | 1 |
| Autonomous API Invocation | operation | 1 | 1 |
| Autonomous MCP Generation | operation | 1 | 1 |
| Autonomous Memory | type | 1 | 1 |
| Autonomous Retrieval | operation | 1 | 1 |
| Beam Search Path Planning | operation | 1 | 1 |
| Behavior Logs | carrier | 1 | 1 |
| Bi-directional Memory Traversal | operation | 1 | 1 |
| Bi-temporal Memory | type | 1 | 1 |
| Boundary Detection | operation | 1 | 1 |
| Budget Allocation | operation | 1 | 1 |
| Buffer-Triggered Summarization | operation | 1 | 1 |
| Camera Poses | carrier | 1 | 1 |
| Camera Trajectory Map | structure | 1 | 1 |
| Candidate Memory | type | 1 | 1 |
| Capability Assessment Text (能力评估文本) | carrier | 1 | 1 |
| Capability List (能力清单) | type | 1 | 1 |
| Capability Refinement | operation | 1 | 1 |
| Capability Reuse | operation | 1 | 1 |
| Category Memory | type | 1 | 1 |
| Causal Memory | type | 1 | 1 |
| Causal-Temporal Graph | structure | 1 | 1 |
| CDF-based Estimation | operation | 1 | 1 |
| Central Memory Database (中央记忆库) | carrier | 1 | 1 |
| Central Memory Orchestrator | structure | 1 | 1 |
| Cited Report Sections (引用报告章节) | carrier | 1 | 1 |
| Co-trained Retrieval | operation | 1 | 1 |
| Coarse-graining | operation | 1 | 1 |
| Code Context Memory | type | 1 | 1 |
| Code Toolkits | carrier | 1 | 1 |
| Cognitive Memory | type | 1 | 1 |
| Cognitive Tokens | carrier | 1 | 1 |
| Collaboration Experiences | carrier | 1 | 1 |
| Collaborative Graph Learning | operation | 1 | 1 |
| Common Knowledge Memory | type | 1 | 1 |
| Community Reports (Text Summaries) | carrier | 1 | 1 |
| Compact Memory | type | 1 | 1 |
| Completeness-Oriented Tool Memory | type | 1 | 1 |
| Composite Reward Signal | structure | 1 | 1 |
| Compressed Context Sequence | structure | 1 | 1 |
| Compressed Internal State | type | 1 | 1 |
| Compressed Textual Summary | structure | 1 | 1 |
| Compressed Token Sequence | carrier | 1 | 1 |
| Compressed Topic Fragments | carrier | 1 | 1 |
| Concise Session Snapshot | structure | 1 | 1 |
| Conclusion Memory (结论记忆) | type | 1 | 1 |
| Conditioned Tree Traversal | operation | 1 | 1 |
| Confidence Assessment Log | structure | 1 | 1 |
| Conflict Assessment | operation | 1 | 1 |
| Conflict Resolution | operation | 2 | 2 |
| Consensus-driven Termination | operation | 1 | 1 |
| Constant Memory | type | 1 | 1 |
| Constraint-based Editing | operation | 1 | 1 |
| Constructivist Accommodation (Incremental Clustering) | operation | 1 | 1 |
| Constructivist Agentic Memory (CAM) | type | 1 | 1 |
| Constructivist Assimilation (Node Replication) | operation | 1 | 1 |
| Context-as-Memory | type | 1 | 1 |
| Context-aware Persona Retrieval | operation | 1 | 1 |
| Context-aware Refinement | operation | 1 | 1 |
| Context Buffer (上下文缓冲区) | structure | 1 | 1 |
| Context Compilation | operation | 1 | 1 |
| Context Compression | operation | 1 | 1 |
| Context Count Check | operation | 1 | 1 |
| Context Curation (上下文策展) | operation | 1 | 1 |
| Context-dependent Memory Block Fetching | operation | 1 | 1 |
| Context-Embedded Memory (上下文嵌入记忆) | structure | 1 | 1 |
| Context Folding | operation | 1 | 1 |
| Context Fragmentation | operation | 1 | 1 |
| Context Injection | operation | 1 | 1 |
| Context Integration | operation | 1 | 1 |
| Context Memory Embeddings | structure | 1 | 1 |
| Context Paging | operation | 1 | 1 |
| Context Pruning | operation | 1 | 1 |
| Context Recovery | operation | 1 | 1 |
| Context Representation Memory | type | 1 | 1 |
| Context Routing | operation | 1 | 1 |
| Context Search | operation | 1 | 1 |
| Context State (Vision + Plan) | structure | 1 | 1 |
| Context Summarization/Compression | operation | 1 | 1 |
| Context Update | operation | 1 | 1 |
| Context Window Tokens | carrier | 1 | 1 |
| Contextual Memory | type | 1 | 1 |
| Continuous Embedding Vectors | carrier | 1 | 1 |
| Continuous Memory (连续记忆) | type | 1 | 1 |
| Continuous Vector Compression | operation | 1 | 1 |
| Contrastive Feedback Optimization | operation | 1 | 1 |
| Contrastive Trajectory Pair | structure | 1 | 1 |
| Control Token Sequence | structure | 1 | 1 |
| Convergence Judgment | operation | 1 | 1 |
| Core Memory | type | 1 | 1 |
| Coreference Chains | carrier | 1 | 1 |
| CPU RAM | carrier | 1 | 1 |
| Creed (不可变信条) | type | 1 | 1 |
| Cross-Attention Read | operation | 1 | 1 |
| Cross-Attention Retrieval | operation | 1 | 1 |
| Cross-Domain Experience (跨域经验) | type | 1 | 1 |
| Cross-Modal Attention Fusion | operation | 1 | 1 |
| Curated Memory (策展记忆) | type | 1 | 1 |
| Database-driven Unlearning | operation | 1 | 1 |
| Decoupled Query Representation | structure | 1 | 1 |
| DELETE | operation | 1 | 1 |
| Delete | operation | 1 | 1 |
| Demonstration Parsing | operation | 1 | 1 |
| Dense Embeddings | carrier | 1 | 1 |
| Dense Matching | operation | 1 | 1 |
| Dense Vector | carrier | 1 | 1 |
| Dense Vector Index | carrier | 1 | 1 |
| Dependency Parse Triples | carrier | 1 | 1 |
| Depth-Adaptive Threshold Node | structure | 1 | 1 |
| DFS Retrieval | operation | 1 | 1 |
| Dialogue Logs | carrier | 1 | 1 |
| Dialogue Text Sequences | carrier | 1 | 1 |
| Dialogue/Document Records | carrier | 1 | 1 |
| Diffusion Latents | carrier | 1 | 1 |
| Directed Weighted Graph | structure | 1 | 1 |
| Disagreement Gating (分歧门控) | operation | 1 | 1 |
| Discourse Relation Labels | carrier | 1 | 1 |
| Distance Signal | type | 1 | 1 |
| Distilled Knowledge Statements | structure | 1 | 1 |
| Distilled Student Compressor Model | carrier | 1 | 1 |
| Diversity-Promoting Exploration | operation | 1 | 1 |
| DOM/Accessibility Tree (DOM/可访问性树) | carrier | 1 | 1 |
| Domain Memory | type | 1 | 1 |
| Domain-Specific Corpus | carrier | 1 | 1 |
| Domain-specific Memory Pool | type | 1 | 1 |
| Dual-layer Memory Storage | structure | 1 | 1 |
| Dual-stage Retrieval | operation | 1 | 1 |
| Dual-Strategy Retrieval (Threshold/Top-k) | operation | 1 | 1 |
| Dual-stream Memory Structure | structure | 1 | 1 |
| Dual-view Bipartite Graph | structure | 1 | 1 |
| Dynamic Capability Memory (MCPs) | type | 1 | 1 |
| Dynamic Community Structure | structure | 1 | 1 |
| Dynamic Context State | structure | 1 | 1 |
| Dynamic Dialogue History Memory | type | 1 | 1 |
| Dynamic Knowledge Graph | structure | 1 | 1 |
| Dynamic Knowledge Update | operation | 1 | 1 |
| Dynamic LLM-Adapted Documentation | type | 1 | 1 |
| Dynamic Memory Evolution | operation | 1 | 1 |
| Dynamic Memory Expansion | operation | 1 | 1 |
| Dynamic Memory Scheduling | operation | 1 | 1 |
| Dynamic Node Update | operation | 1 | 1 |
| Dynamic Outline Memory (动态大纲记忆) | type | 1 | 1 |
| Dynamic Procedural Memory | type | 1 | 1 |
| Dynamic Prompt Context Buffer | structure | 1 | 1 |
| Dynamic Query Generation | operation | 1 | 1 |
| Dynamic Session Summary | structure | 1 | 1 |
| Dynamic Social Network Graph | structure | 1 | 1 |
| Dynamic Structured Memory (DSM) | type | 1 | 1 |
| Dynamic Tool Pool | structure | 1 | 1 |
| Dynamic Tree Memory | type | 1 | 1 |
| Dynamic User Persona | type | 1 | 1 |
| Dynamic Weight Adjustment | operation | 1 | 1 |
| Dynamic Weight Fusion | operation | 1 | 1 |
| Early Experience (早期经验) | type | 1 | 1 |
| Editable Knowledge State | type | 1 | 1 |
| EDU-based Context Memory | type | 1 | 1 |
| EDU Decomposition | operation | 1 | 1 |
| Elementary Discourse Unit (EDU) Tree | structure | 1 | 1 |
| Embedding Space Representations | carrier | 1 | 1 |
| Embedding Vector Index | carrier | 1 | 1 |
| Embedding Vectors | carrier | 1 | 1 |
| Empirical CDF Partition | structure | 1 | 1 |
| Engram | structure | 1 | 1 |
| Engram Unit | carrier | 1 | 1 |
| Enhanced Prompt with Retrieved Context | structure | 1 | 1 |
| Enriched EDU (Elementary Discourse Unit) | structure | 1 | 1 |
| Entity-centric Memory Bank | structure | 1 | 1 |
| Entity Memory | type | 1 | 1 |
| Entity-Relation-Entity Triple | structure | 1 | 1 |
| Entity Resolution | operation | 1 | 1 |
| Environment Observation Memory | type | 1 | 1 |
| Environment Profile | structure | 1 | 1 |
| Environment Reward Signals | carrier | 1 | 1 |
| Episode Data Unit | carrier | 1 | 1 |
| Episode Memory | type | 1 | 1 |
| Episodic Demonstration Memory | type | 1 | 1 |
| Episodic Memory (Interaction History) | type | 10 | 10 |
| Episodic Memory Graph | type | 1 | 1 |
| Episodic Simulation | type | 1 | 1 |
| Event-Centric Memory (EMem) | type | 2 | 2 |
| Event Graph | structure | 1 | 1 |
| Event Nodes | carrier | 1 | 1 |
| Evidence Acquisition (证据获取) | operation | 1 | 1 |
| Evidence Memory (证据记忆) | type | 1 | 1 |
| Evidence Memory Bank (证据记忆库) | structure | 1 | 1 |
| Executable API Memory | type | 1 | 1 |
| Executable Code Snippets | carrier | 1 | 1 |
| Execute (21 Action Types) | operation | 1 | 1 |
| Execution Logs | carrier | 1 | 1 |
| Execution Trace Memory | type | 1 | 1 |
| Experience Distillation | operation | 1 | 1 |
| Experience-Driven Memory | type | 1 | 1 |
| Experience-Induced Memory Entries (经验诱导记忆条目) | structure | 1 | 1 |
| Experience Model | structure | 1 | 1 |
| Experience Rewriting | operation | 1 | 1 |
| Experience Stream | type | 1 | 1 |
| Experience Synthesis | operation | 1 | 1 |
| Experiential Knowledge | type | 1 | 1 |
| Expert Adapters | structure | 1 | 1 |
| Explicit Auxiliary Memory | type | 1 | 1 |
| Explicit Memory (显式记忆) | type | 1 | 1 |
| Explicit Query Description | structure | 1 | 1 |
| Exponential Time-Decay Weighting | operation | 1 | 1 |
| External API Endpoints | carrier | 1 | 1 |
| External Knowledge Base Snippets | carrier | 1 | 1 |
| External Knowledge Database | carrier | 1 | 1 |
| External Memory (Archival/Recall Storage) | type | 1 | 1 |
| External Memory Module | carrier | 2 | 2 |
| External Memory Storage | carrier | 1 | 1 |
| External Multimodal Knowledge Memory | type | 1 | 1 |
| External Open Source Repositories | carrier | 1 | 1 |
| External Persona Database (Key-Value) | carrier | 1 | 1 |
| External Structured Memory | type | 1 | 1 |
| External Tool Knowledge | type | 1 | 1 |
| External Vector Database | carrier | 3 | 3 |
| Externalized Factual Memory | type | 1 | 1 |
| Extracted Text Chunks | carrier | 1 | 1 |
| Fact Memory | type | 1 | 1 |
| Failure-aware Reflection | operation | 1 | 1 |
| FAISS Vector Index (FAISS 向量索引) | carrier | 2 | 2 |
| FAISS Vector Index for Video Semantics | structure | 1 | 1 |
| Fast Path Ingestion | operation | 1 | 1 |
| Fast-Slow Variable Separation | operation | 1 | 1 |
| Feed-Forward Memory Blocks | structure | 1 | 1 |
| Feedback Correction | operation | 1 | 1 |
| Feedback Diagnosis (反馈诊断) | type | 1 | 1 |
| Feedback-Driven Analysis | operation | 1 | 1 |
| Feedback-Driven Update | operation | 1 | 1 |
| Feedback-Integrated Documentation | structure | 1 | 1 |
| FIFO Message Queue | structure | 1 | 1 |
| File-based State Persistence (基于文件的状态持久化) | structure | 1 | 1 |
| Filter | operation | 1 | 1 |
| Fine-grained Memory | type | 1 | 1 |
| Fine-tuned Parameter Space | structure | 1 | 1 |
| Finite State Machine (FSM) Flow | structure | 1 | 1 |
| Firestore 对话历史 | carrier | 1 | 1 |
| Fixed-length Continuous Embedding (固定长度连续嵌入) | structure | 1 | 1 |
| Flat Memory | type | 1 | 1 |
| Folded Memory Representation | structure | 1 | 1 |
| Folded Tree Node Set | structure | 1 | 1 |
| Folded Tree Retrieval | operation | 1 | 1 |
| Forget Operation | operation | 1 | 1 |
| Forgetting Curve Decay | operation | 1 | 1 |
| Forward/Backward Learning Integration (前后向学习整合) | operation | 1 | 1 |
| Four-Layer Semantic Architecture | structure | 1 | 1 |
| FOV Overlap Retrieval | operation | 1 | 1 |
| Frozen VLM Encoder | carrier | 1 | 1 |
| Full Interaction History | type | 1 | 1 |
| Function Calling | operation | 1 | 1 |
| Future State Collection (未来状态收集) | operation | 1 | 1 |
| Gated Dynamic Weighting | operation | 1 | 1 |
| Gated Fusion | operation | 1 | 1 |
| Gated Memory Unit | structure | 1 | 1 |
| Gated Write/Update | operation | 1 | 1 |
| General Continuous Memory (CoMEM) | type | 1 | 1 |
| Generate-Reset-Inject Cycle | operation | 1 | 1 |
| Generated Dialogue Memory | type | 1 | 1 |
| Generative Latent Memory | type | 1 | 1 |
| Geometric-Indexed Memory | type | 1 | 1 |
| Global Environment State Memory | type | 1 | 1 |
| Global Memory Pool | type | 1 | 1 |
| Global Semantic Memory (Community Summaries) | type | 1 | 1 |
| GPU VRAM | carrier | 1 | 1 |
| Graph Database | carrier | 1 | 1 |
| Graph Edges | carrier | 1 | 1 |
| Graph Neural Network Nodes | carrier | 1 | 1 |
| Graph Nodes (Memory Snippets) | carrier | 4 | 4 |
| Graph Update & Fusion | operation | 1 | 1 |
| Graph/Chart Representation | structure | 1 | 1 |
| Graphiti Engine | carrier | 1 | 1 |
| GRU 隐藏状态 | structure | 1 | 1 |
| Guideline-Guided Compression | operation | 1 | 1 |
| Habitat 3.0 Simulator State | carrier | 1 | 1 |
| Hebbian Strengthening | operation | 1 | 1 |
| Heterogeneous Agent Memory | type | 1 | 1 |
| Heterogeneous Memory Graph | structure | 1 | 1 |
| Hidden State Activations | carrier | 1 | 1 |
| Hierarchical Aggregate Tree (HAT) | structure | 1 | 1 |
| Hierarchical Aggregated Memory | type | 1 | 1 |
| Hierarchical Community Tree | structure | 1 | 1 |
| Hierarchical Hindsight Reflection (H2R) | operation | 1 | 1 |
| Hierarchical Memory (Local & Global) | type | 2 | 2 |
| Hierarchical Memory Architecture | structure | 2 | 2 |
| Hierarchical Memory Bank | structure | 1 | 1 |
| Hierarchical Memory Graph | structure | 1 | 1 |
| Hierarchical Memory Storage | structure | 1 | 1 |
| Hierarchical Memory System | structure | 1 | 1 |
| Hierarchical Retrieval | operation | 2 | 2 |
| Hierarchical Schema Memory | type | 1 | 1 |
| Hierarchical Schemata Memory | type | 1 | 1 |
| High-dimensional Input Representations | carrier | 1 | 1 |
| High-level Abstract Memory | type | 1 | 1 |
| High-level Planning Memory | type | 1 | 1 |
| Historical Session Buffer | structure | 1 | 1 |
| HTML/Markdown Logs (结构化日志) | structure | 1 | 1 |
| Hybrid Index Architecture | structure | 1 | 1 |
| Hybrid Knowledge Graph | structure | 1 | 1 |
| Hybrid Memory Map | structure | 1 | 1 |
| Hybrid Replay Buffer | structure | 1 | 1 |
| Hybrid Retrieval (混合检索) | operation | 2 | 2 |
| Hybrid Search & Rerank | operation | 1 | 1 |
| Hybrid Storage Layer (SQLite + ChromaDB) | structure | 1 | 1 |
| Hyper-network Parameters | carrier | 1 | 1 |
| Hyper-network Weight Generator | structure | 1 | 1 |
| Image Embeddings | carrier | 1 | 1 |
| Imagination Tree | structure | 1 | 1 |
| Imagined Memory | type | 1 | 1 |
| Implicit Retrieval Memory | type | 1 | 1 |
| Implicit Semantic Memory | type | 1 | 1 |
| Implicit World Model Representations (隐式世界模型表示) | structure | 1 | 1 |
| Implicit World Modeling (隐式世界建模) | operation | 1 | 1 |
| Importance Scoring | operation | 2 | 2 |
| In-Context Memory Integration | operation | 1 | 1 |
| Incremental Event Segmentation | operation | 1 | 1 |
| Incremental Memory Update | operation | 1 | 1 |
| Incremental Summary Update | operation | 1 | 1 |
| Independent Memory Bank | structure | 1 | 1 |
| Independent Small Transformer Decoder | structure | 1 | 1 |
| Index Routing Mechanism | structure | 1 | 1 |
| Index Routing Retrieval | operation | 1 | 1 |
| Individual Agent Context Memory | type | 1 | 1 |
| Inference-based Persona Update | operation | 1 | 1 |
| Inline Memory Action (原地记忆动作执行) | operation | 1 | 1 |
| Inner Loop Query | operation | 1 | 1 |
| Input Token Sequence | carrier | 1 | 1 |
| Insight Graph | structure | 1 | 1 |
| Insight Memory | type | 1 | 1 |
| Instruction-based Prompting | operation | 1 | 1 |
| Intent-Aligned Retrieval | operation | 1 | 1 |
| Intent-Aware Routing | operation | 1 | 1 |
| Intent-Driven Memory | type | 1 | 1 |
| Intent-Experience-Utility Triplet | structure | 1 | 1 |
| Interaction Compression | operation | 1 | 1 |
| Interaction Event Record | type | 1 | 1 |
| Interaction Experience Memory | type | 1 | 1 |
| Interaction Feedback Signals | carrier | 1 | 1 |
| Interaction Graph | structure | 1 | 1 |
| Interaction History Memory | type | 1 | 1 |
| Interaction Logs (交互日志) | carrier | 1 | 1 |
| Interaction Memory | type | 1 | 1 |
| Interaction Record Sequence (交互记录序列) | structure | 1 | 1 |
| Interaction Trajectories | carrier | 1 | 1 |
| Interaction Trajectory Log | structure | 1 | 1 |
| Intermediate Conclusion Storage (中间结论存储) | structure | 1 | 1 |
| Intermediate Layer Embedding Slot | structure | 1 | 1 |
| Intermediate Token Streams | carrier | 1 | 1 |
| Intermediate Validation | operation | 1 | 1 |
| Internal Agent Context | carrier | 1 | 1 |
| Internal Linguistic Memory | type | 1 | 1 |
| Internal Model Weights | carrier | 1 | 1 |
| Internal State Token (<IS>) | carrier | 1 | 1 |
| Interpolation Integration Layer | structure | 1 | 1 |
| Intrinsic Memory | type | 1 | 1 |
| Intrinsic Memory Update | operation | 1 | 1 |
| Iterative Documentation Rewriting | operation | 1 | 1 |
| Iterative Memory Loop | structure | 1 | 1 |
| Iterative Pre-compression | operation | 1 | 1 |
| Iterative Retrieval Stop | operation | 1 | 1 |
| Just-In-Time Compiled Context | type | 1 | 1 |
| Key Conclusion Extraction (关键结论提取) | operation | 1 | 1 |
| Key Memory | type | 1 | 1 |
| Key-Value Storage | carrier | 1 | 1 |
| Keypoint-level Experience Structure | structure | 1 | 1 |
| Knowledge Distillation | operation | 1 | 1 |
| Knowledge Distillation Transfer | operation | 1 | 1 |
| Knowledge Fusion | operation | 1 | 1 |
| Knowledge Graph Nodes/Edges | carrier | 1 | 1 |
| Knowledge Graph Triples | carrier | 1 | 1 |
| Knowledge Graph World Model | structure | 1 | 1 |
| Knowledge Retrieval | operation | 1 | 1 |
| Knowledge Source Biasing | operation | 1 | 1 |
| Knowledge Triples | carrier | 1 | 1 |
| Knowledge Triplets (Entity-Relation-Value) | structure | 1 | 1 |
| KV 缓存 (KV Cache) | carrier | 1 | 1 |
| L0 Microscopic Evidence Memory | type | 1 | 1 |
| L1 Mesoscopic Knowledge Memory | type | 1 | 1 |
| L2 Macroscopic Profile Memory | type | 1 | 1 |
| Latent Dimension Concatenation | operation | 1 | 1 |
| Latent Space Memory Vectors | structure | 1 | 1 |
| Latent Token Sequence | structure | 1 | 1 |
| Latent Tokens | carrier | 1 | 1 |
| Learnable Memory (可学习记忆) | type | 1 | 1 |
| Learnable Persona Dictionary | structure | 1 | 1 |
| LearnGUI Dataset | carrier | 1 | 1 |
| Leiden Community Detection | operation | 1 | 1 |
| LFU 淘汰 (LFU Eviction) | operation | 1 | 1 |
| Life-long Interaction Memory | type | 1 | 1 |
| Lifecycle Management | operation | 1 | 1 |
| Lightweight API Interface (轻量级 API 接口) | carrier | 1 | 1 |
| Lightweight Neural Network Parameters | carrier | 1 | 1 |
| Limited Memory | type | 1 | 1 |
| Linearized Event Timeline | structure | 1 | 1 |
| Linked Outline Structure (链接式大纲结构) | structure | 1 | 1 |
| LLaMA-7B 模型权重 (LLaMA-7B Weights) | carrier | 1 | 1 |
| LLM Agent Context Window | carrier | 1 | 1 |
| LLM Agent Memory System | carrier | 1 | 1 |
| LLM Base Model Parameters | carrier | 1 | 1 |
| LLM Context Memory | type | 1 | 1 |
| LLM Context Window (大模型上下文窗口) | carrier | 11 | 11 |
| LLM-driven Entity-Relation Extraction | operation | 1 | 1 |
| LLM-generated Node Summaries | carrier | 1 | 1 |
| LLM Generated Summaries | carrier | 1 | 1 |
| LLM Internal State | carrier | 1 | 1 |
| LLM Prompt Context Window | carrier | 1 | 1 |
| LLM Token Context | carrier | 1 | 1 |
| LLM Token Context Window | carrier | 1 | 1 |
| LLM 上下文 (LLM Context) | carrier | 1 | 1 |
| LLM 上下文窗口 (LLM Context Window) | carrier | 4 | 4 |
| LLM 基座模型 (LLM Base Model) | carrier | 1 | 1 |
| LLM 嵌入空间向量 (LLM Embedding Space Vectors) | carrier | 1 | 1 |
| LLM 智能体 (LLM Agent) | carrier | 1 | 1 |
| Local Episodic Memory (Text Chunks) | type | 1 | 1 |
| Local Memory Bank | structure | 1 | 1 |
| Local Weight Update | operation | 1 | 1 |
| Logic Map | structure | 1 | 1 |
| Logical Edges | carrier | 1 | 1 |
| Logical Relation Linking | operation | 1 | 1 |
| Long-tail Knowledge Memory | type | 1 | 1 |
| Long-term Agent Memory | type | 1 | 1 |
| Long-Term Conversational Memory | type | 1 | 1 |
| Long-Term Dialogue Memory | type | 1 | 1 |
| Long-Term Memory (Light3/LTM) | type | 4 | 4 |
| Long-term Memory (LTM) | type | 3 | 3 |
| Long-term Memory Bank | carrier | 1 | 1 |
| Long-term Reflection Memory | type | 1 | 1 |
| Long-term Task Goal Storage | type | 1 | 1 |
| LongTermMemory | type | 0 | 1 |
| LoRA 适配器参数 (LoRA Adapter Parameters) | carrier | 1 | 1 |
| Loss Masking on Retrieved Values | operation | 1 | 1 |
| Low-level Execution Memory | type | 1 | 1 |
| LSH 向量索引表 (LSH Vector Index Table) | structure | 1 | 1 |
| LyfeGame 3D Environment | carrier | 1 | 1 |
| Magnitude Signal | type | 1 | 1 |
| Map-Reduce Answer Generation | operation | 1 | 1 |
| Masked Trajectory | structure | 1 | 1 |
| MCP Abstraction (Parameterization) | operation | 1 | 1 |
| MCP Server Tool List | carrier | 1 | 1 |
| MEM_READ (记忆读取) | operation | 1 | 1 |
| MEM_WRITE (记忆写入) | operation | 1 | 1 |
| MemCells (记忆细胞) | carrier | 1 | 2 |
| Memorization | operation | 1 | 1 |
| Memory Acquisition (ReAct Triples) | operation | 1 | 1 |
| Memory Allocation (记忆分配) | operation | 1 | 1 |
| Memory Augmentation | operation | 1 | 1 |
| Memory Bank | structure | 1 | 1 |
| Memory Compression (记忆压缩) | operation | 1 | 1 |
| Memory Consolidation (Summarization) | operation | 3 | 3 |
| Memory Construction | operation | 1 | 1 |
| Memory Control Decision | operation | 1 | 1 |
| Memory Database | carrier | 1 | 1 |
| Memory Decay (Forgetting) | operation | 1 | 1 |
| Memory Decomposition (记忆分解) | operation | 1 | 1 |
| Memory Eviction | operation | 1 | 1 |
| Memory Extraction | operation | 1 | 1 |
| Memory Folding | operation | 1 | 1 |
| Memory Fusion | operation | 1 | 1 |
| Memory Generation | operation | 1 | 1 |
| Memory Induction (记忆诱导) | operation | 1 | 1 |
| Memory Migration (STM to LTM) | operation | 1 | 1 |
| Memory Module | carrier | 1 | 1 |
| Memory Pool | structure | 1 | 1 |
| Memory Pruning | operation | 1 | 1 |
| Memory Recording (记忆记录) | operation | 1 | 1 |
| Memory Reinforcement (Retrieval) | operation | 1 | 1 |
| Memory Retrieval (Embedding Query) | operation | 3 | 3 |
| Memory Retrieval & Reuse (记忆检索复用) | operation | 1 | 1 |
| Memory Scoring and Filtering | operation | 1 | 1 |
| Memory Sharing | operation | 1 | 1 |
| Memory Stream | structure | 3 | 3 |
| Memory Strength Parameter | structure | 1 | 1 |
| Memory Triggering | operation | 1 | 1 |
| Memory Units (记忆单元) | structure | 1 | 1 |
| Memory Update | operation | 3 | 3 |
| Memory Vectors | carrier | 1 | 1 |
| Memory Weaving | operation | 1 | 1 |
| MemScenes (记忆场景) | carrier | 1 | 2 |
| MemTree | structure | 1 | 1 |
| Minimalist Single-Core Architecture | structure | 1 | 1 |
| Missing-Slot Guided Filtering | operation | 1 | 1 |
| MLP Memory (检索器预训练记忆) | type | 1 | 1 |
| MLP Weight Matrices | carrier | 1 | 1 |
| MLP 记忆模块 (MLP Memory Module) | structure | 1 | 1 |
| Modality-specific Semantic Memory (OCR/ASR/DET) | type | 1 | 1 |
| Model Parameters | carrier | 1 | 1 |
| Model Policy Parameters (模型策略参数) | carrier | 1 | 1 |
| Model Weights (Linguistic Only) | carrier | 1 | 1 |
| Modular Code Repository | structure | 1 | 1 |
| Modular Procedural Memory (模块化过程记忆) | type | 1 | 1 |
| Module Weights | carrier | 1 | 1 |
| Multi-agent Reasoning Trace | structure | 1 | 1 |
| Multi-context Group Structure | structure | 1 | 1 |
| Multi-parent Memory Nodes | structure | 1 | 1 |
| Multi-scale Effective Theory Structure | structure | 1 | 1 |
| Multi-Session Task Memory | type | 1 | 1 |
| Multi-step Reasoning Chains (多步推理链) | type | 1 | 1 |
| Multi-temporal Granularity Index | structure | 1 | 1 |
| Multi-turn Interaction Trajectories | carrier | 1 | 1 |
| Multi-turn Reasoning | operation | 1 | 1 |
| Multimodal Input Stream | carrier | 1 | 1 |
| Multimodal Knowledge Graph (MMKG) | structure | 1 | 1 |
| Multimodal Trajectory Memory (多模态轨迹记忆) | type | 1 | 1 |
| Named Pipes | carrier | 1 | 1 |
| Natural Language Compression Guidelines | carrier | 1 | 1 |
| Natural Language Context | carrier | 1 | 1 |
| Natural Language Instructions | carrier | 2 | 2 |
| Natural Language Summary Buffer | structure | 1 | 1 |
| Natural Language Text | carrier | 2 | 2 |
| Neuro-symbolic Knowledge Extraction | operation | 1 | 1 |
| Nightly Self-Critique (夜间自评) | operation | 1 | 1 |
| Non-Parametric Continual Learning | type | 1 | 1 |
| Non-structured Dialogue Text | carrier | 1 | 1 |
| NOOP | operation | 1 | 1 |
| Normalized Action Space (0-1000 Coordinates) | structure | 1 | 1 |
| Null-Space Basis | structure | 1 | 1 |
| Null-Space Constrained Editing | operation | 1 | 1 |
| Observation Memory | type | 1 | 1 |
| Offline Browser Sandbox (离线浏览器沙盒) | carrier | 1 | 1 |
| Offline Event Extraction | operation | 1 | 1 |
| Offline Indexing | operation | 1 | 1 |
| Offline Lightweight Memory | type | 1 | 1 |
| Offline Parallel Update | operation | 1 | 1 |
| Offline Parallel Update Queue | structure | 1 | 1 |
| Online Deep Research Memory | type | 1 | 1 |
| Online Incremental Memory | type | 1 | 1 |
| Online Retrieval | operation | 1 | 1 |
| Online Top-Down Clustering Insertion | operation | 1 | 1 |
| Operation Logs | carrier | 1 | 1 |
| Optimized Context Window | structure | 1 | 1 |
| Option-Action Hierarchy | structure | 1 | 1 |
| Orchestrator Memory (编排器记忆) | type | 1 | 1 |
| Orthogonal Graph Representation | structure | 1 | 1 |
| Orthogonal Projection Matrix | structure | 1 | 1 |
| Orthogonal Projection Update | operation | 1 | 1 |
| Outline Optimization (大纲优化) | operation | 1 | 1 |
| Overwrite Strategy | operation | 1 | 1 |
| OWL Knowledge Graph | structure | 1 | 1 |
| OWL Ontology | carrier | 1 | 1 |
| Page-based Storage | structure | 1 | 1 |
| (Prompt, Answer) Pair | structure | 1 | 1 |
| Parallel Search | operation | 1 | 1 |
| Parameter-Free Model Integration | operation | 1 | 1 |
| Parameter Injection | operation | 1 | 1 |
| Parameterized Fact Memory | type | 1 | 1 |
| Parametric Factual Knowledge | type | 1 | 1 |
| Parametric Knowledge (Internal Memory) | type | 1 | 1 |
| Parametric Memory (参数化记忆) | type | 3 | 3 |
| Parent Node Aggregation Update | operation | 1 | 1 |
| Passive Input Context | type | 1 | 1 |
| Patch Embedding | structure | 1 | 1 |
| Perceive (Filter Content) | operation | 1 | 1 |
| Perceptual-Cognitive Memory | type | 1 | 1 |
| Perceptual-Cognitive Memory Bank (PCMB) | structure | 1 | 1 |
| Perceptual Memory | type | 1 | 1 |
| Perceptual Tokens | carrier | 1 | 1 |
| Personalized PageRank Propagation | operation | 2 | 2 |
| Perturbation Vector (Δθ) | structure | 1 | 1 |
| Phrase-Paragraph Dual Node Structure | structure | 1 | 1 |
| Plan Generation | operation | 1 | 1 |
| Planning Memory | type | 1 | 1 |
| Planning Seeds (规划种子) | type | 1 | 1 |
| PLM Embeddings | carrier | 1 | 1 |
| Plug-and-Play Injection | operation | 1 | 1 |
| Policy Gradient Update | operation | 1 | 1 |
| Post Information Flow Stream | structure | 1 | 1 |
| Post-training Alignment via SFT/RL (后训练对齐) | operation | 1 | 1 |
| Pre-trained Multimodal Knowledge | type | 1 | 1 |
| Prediction-Calibration | operation | 1 | 1 |
| Pretrained Plug-and-Play Memory | type | 1 | 1 |
| Prior Injection | operation | 1 | 1 |
| Priority-based Context Window | structure | 1 | 1 |
| Procedural Memory | type | 1 | 1 |
| Procedural Skill Memory | type | 1 | 1 |
| Procedural Tool Memory (MCP Box) | type | 1 | 1 |
| Proficiency Classification Schema (熟练度分类法) | structure | 1 | 1 |
| Profile Tags | carrier | 1 | 1 |
| Program Verification (Validation) | operation | 1 | 1 |
| Programmatic Skills (Procedural Memory) | type | 1 | 1 |
| Prompt Context Window | structure | 1 | 1 |
| Prompt Sequences | structure | 1 | 1 |
| Prompt Text | carrier | 1 | 1 |
| Prune (删除冗余上下文 ID) | operation | 1 | 1 |
| Prune&Write Memory Primitives (记忆原语结构) | structure | 1 | 1 |
| Prune-and-Grow Retrieval | operation | 1 | 1 |
| Python Async Scripts | carrier | 1 | 1 |
| Quality Feedback Scores (质量反馈分数) | carrier | 1 | 1 |
| Query Decomposition | operation | 1 | 1 |
| Query Decoupling | operation | 1 | 1 |
| Query Generation | operation | 1 | 1 |
| Query Graph | structure | 1 | 1 |
| Query Memory | type | 2 | 2 |
| Query Reconstruction | operation | 1 | 1 |
| Query-Relevant Sub-Tree | structure | 1 | 1 |
| Query-Scene-Tool Interaction Graph | structure | 1 | 1 |
| Query-to-Triple Mapping | structure | 1 | 1 |
| Queue Structure | structure | 1 | 1 |
| RAG-based Memory Retrieval (基于 RAG 的记忆检索) | operation | 1 | 1 |
| Raw Dialogue Memory | type | 1 | 1 |
| Read/Write Separation (Multi-LoRA) | operation | 1 | 1 |
| Real Memory | type | 1 | 1 |
| Reasoning Augmentation | operation | 1 | 1 |
| Reasoning-based Feedback | type | 1 | 1 |
| Reasoning Chain Memory (推理链记忆) | type | 1 | 1 |
| Reasoning Model | carrier | 1 | 1 |
| Reasoning Trajectory Logs | carrier | 1 | 1 |
| Reasoning Tree (RT) | structure | 1 | 1 |
| ReasoningBank 推理记忆库 | structure | 1 | 1 |
| Recall-oriented LLM Filtering | operation | 1 | 1 |
| Recognition Memory Filtering | operation | 1 | 1 |
| Recursive Imagination | operation | 1 | 1 |
| Recursive Memory Update | operation | 1 | 1 |
| Recursive Summary Aggregation | operation | 1 | 1 |
| Recursive Summary Memory | type | 1 | 1 |
| Reflection Generation | operation | 1 | 1 |
| Reflection Memory | type | 2 | 2 |
| Reflective Iteration | operation | 1 | 1 |
| Reflective Synthesis | operation | 1 | 1 |
| Relation-aware Linking | operation | 1 | 1 |
| Relevance Retrieval | operation | 1 | 1 |
| Renormalization Operators (R_K1, R_K2, R_K3) | operation | 1 | 1 |
| Repair State Memory | type | 1 | 1 |
| Replay Buffer | carrier | 1 | 1 |
| Replay Buffer for Offline RL | structure | 1 | 1 |
| Result Injection & Continuation | operation | 1 | 1 |
| Retrievable Script Memory | type | 1 | 1 |
| Retrieval | operation | 1 | 1 |
| Retrieval Augmentation | operation | 1 | 1 |
| Retrieve | operation | 1 | 1 |
| Retrieve-Refine Update (检索 - 精炼更新) | operation | 1 | 1 |
| Retrieved Context (External Memory) | type | 1 | 1 |
| Retrieved Document Chunks | carrier | 1 | 1 |
| Retriever Behavior Imitation | operation | 1 | 1 |
| Retriever Continuous Training | operation | 1 | 1 |
| Retriever-Pretrained Memory (检索器预训练记忆) | type | 1 | 1 |
| Reversible Context Segment | structure | 1 | 1 |
| Reward-Free Interaction Memory (无奖励交互记忆) | type | 1 | 1 |
| RGB-D Features | carrier | 1 | 1 |
| RGB Observation Frames | carrier | 1 | 1 |
| RL-Managed Memory | type | 1 | 1 |
| RL Policy Optimization | operation | 1 | 1 |
| Role-Aware Context Memory | type | 1 | 1 |
| Role-Specific Context | type | 1 | 1 |
| Rollout Group | structure | 1 | 1 |
| Rubric-based Scoring System | carrier | 1 | 1 |
| Rule-based Decomposed Statements | structure | 1 | 1 |
| Runtime Q-value Update | operation | 1 | 1 |
| S3 加密生物信息 | carrier | 1 | 1 |
| Scenario-aware Index | structure | 1 | 1 |
| Scenario-aware Retrieval | operation | 1 | 1 |
| Scenario Memory | type | 1 | 1 |
| Screen Screenshots | carrier | 1 | 1 |
| Screen Snapshots | carrier | 1 | 1 |
| Screenshot-Action Pairs (截图 - 动作对) | carrier | 1 | 1 |
| SDM Activation Module | structure | 1 | 1 |
| Search Tool Response | carrier | 1 | 1 |
| Segmented Context Memory | type | 1 | 1 |
| Segmented Ingestion | operation | 1 | 1 |
| Segmented Trajectory (轨迹分段) | structure | 1 | 1 |
| Self-Attributing | operation | 1 | 1 |
| Self-Augmentation Generation | operation | 1 | 1 |
| Self-Controlled Memory | type | 1 | 1 |
| Self-Evolutionary Curation | operation | 1 | 1 |
| Self-Evolving Experience Memory | type | 1 | 1 |
| Self-Generated Graph Index | structure | 1 | 1 |
| Self-Model (自我模型) | type | 1 | 1 |
| Self-Navigating | operation | 1 | 1 |
| Self-Questioning | operation | 1 | 1 |
| Self-Reflection (自我反思) | operation | 1 | 1 |
| Self-Supervised Tool Decision State | type | 1 | 1 |
| Semantic Action Memory | type | 1 | 1 |
| Semantic Advantage Distribution | structure | 1 | 1 |
| Semantic Advantage Extraction | operation | 1 | 1 |
| Semantic Anchored Memory | type | 1 | 1 |
| Semantic Anchoring | operation | 1 | 1 |
| Semantic Embedding Index | structure | 1 | 1 |
| Semantic Embedding Retrieval | operation | 1 | 1 |
| Semantic Embedding Vectors | carrier | 1 | 1 |
| Semantic Embeddings | carrier | 1 | 1 |
| Semantic Features | carrier | 1 | 1 |
| Semantic Gating | operation | 1 | 1 |
| Semantic-Graph Fusion Retrieval | operation | 1 | 1 |
| Semantic-Graph Hybrid Memory | type | 1 | 1 |
| Semantic Indexes | carrier | 1 | 1 |
| Semantic Knowledge Memory | type | 1 | 1 |
| Semantic Memory (Knowledge Graph) | type | 9 | 9 |
| Semantic Retrieval (语义检索) | operation | 3 | 3 |
| Semantic Similarity Retrieval | operation | 1 | 1 |
| Sensory Memory (Light1) | type | 1 | 1 |
| SensoryMemory | type | 0 | 1 |
| Separate Retrieval | operation | 1 | 1 |
| Session-based Memory State | structure | 1 | 1 |
| Session History Memory | type | 1 | 1 |
| Session IDs | carrier | 1 | 1 |
| Session Lifecycle Management | operation | 1 | 1 |
| Shared Environment State | carrier | 1 | 1 |
| Shared State Space | structure | 1 | 1 |
| Shared Vector Database | carrier | 1 | 1 |
| Short-Term Memory (Light2/STM) | type | 5 | 5 |
| Short-term Memory (STM) | type | 2 | 2 |
| Short-term Operation History | type | 1 | 1 |
| Short-Term Tool Memory | type | 1 | 1 |
| Short-term Trajectory Memory | type | 1 | 1 |
| ShortTermMemory / WorkingMemory | type | 0 | 1 |
| Signal Fusion | operation | 1 | 1 |
| Sim-to-Real Transfer | operation | 1 | 1 |
| Similarity-based Retrieval (基于相似度的检索) | operation | 2 | 2 |
| Similarity Signal | type | 1 | 1 |
| Simulated Platform Database | carrier | 1 | 1 |
| Skill Distillation | operation | 1 | 1 |
| Skill Honing | operation | 1 | 1 |
| Skill Induction (Encoding) | operation | 1 | 1 |
| Skill Library | structure | 1 | 1 |
| Skill Proposal | operation | 1 | 1 |
| Skill Reuse (Retrieval & Execution) | operation | 1 | 1 |
| Skill Synthesis | operation | 1 | 1 |
| Sliding Window Caching | operation | 1 | 1 |
| Slow Path Consolidation | operation | 1 | 1 |
| Small Language Model (SLM) | carrier | 1 | 1 |
| Small Vision-Language Model (SVLM) | carrier | 1 | 1 |
| Soft Prompt Vectors | structure | 1 | 1 |
| Soft Update (Incremental Add) | operation | 1 | 1 |
| SOP-Encoded Knowledge | type | 1 | 1 |
| SOP Encoding | operation | 1 | 1 |
| Source Code Repository | carrier | 1 | 1 |
| Source Index Anchored EDU Nodes | carrier | 1 | 1 |
| Special API Tokens (<API>) | carrier | 1 | 1 |
| Special Query Tokens | structure | 1 | 1 |
| Speculative Execution | operation | 1 | 1 |
| State Consolidation | operation | 1 | 1 |
| State Summarization | operation | 1 | 1 |
| State Synchronization | operation | 1 | 1 |
| State Transition | operation | 1 | 1 |
| Static Character Profile Memory | type | 1 | 1 |
| Static Human-Centric Documentation | type | 1 | 1 |
| STM Buffer | structure | 1 | 1 |
| STM Storage Area | structure | 1 | 1 |
| STM Update | operation | 1 | 1 |
| Structured Artifacts (PRD, Code) | structure | 1 | 1 |
| Structured Capability Memory (结构化能力记忆) | type | 1 | 1 |
| Structured Contextual Memory | structure | 1 | 1 |
| Structured Dialogue Logs | carrier | 1 | 1 |
| Structured Discourse Memory | type | 1 | 1 |
| Structured Experience Memory | type | 1 | 1 |
| Structured Experience Records | carrier | 1 | 1 |
| Structured Knowledge Base (结构化知识库) | structure | 1 | 1 |
| Structured Memory | structure | 2 | 2 |
| Structured Memory Bank | carrier | 1 | 1 |
| Structured Memory Entries | structure | 1 | 1 |
| Structured Memory Entry | structure | 1 | 1 |
| Structured Memory Storage | structure | 1 | 1 |
| Structured Memory Templates | carrier | 1 | 1 |
| Structured Narrative Tuples | structure | 1 | 1 |
| Structured Navigation Retrieval | operation | 1 | 1 |
| Structured QA Memory Unit (Intent + Slots) | structure | 1 | 1 |
| Structured Semantic Description | structure | 1 | 1 |
| Structured Text Prompt | structure | 1 | 1 |
| Structured Triplet (z, e, Q) | structure | 1 | 1 |
| Sub-question Sub-answer Sequence | structure | 1 | 1 |
| Sub-Tree Ranking | operation | 1 | 1 |
| Subgraph Retrieval | operation | 1 | 1 |
| Summarize-and-Forget | operation | 1 | 1 |
| Summarized Memory (Daily/Global) | type | 2 | 2 |
| Summary | operation | 1 | 1 |
| Summary-Leaf Node Structure | structure | 1 | 1 |
| Summary Nodes | carrier | 1 | 1 |
| Summary Tree | structure | 1 | 1 |
| Supervised Fine-tuning (SFT) | operation | 1 | 1 |
| Supervised Weight Updating | operation | 1 | 1 |
| Surprising Information Memory | type | 1 | 1 |
| SUS 评估体系 (Safety-Usability-Smoothness Framework) | structure | 1 | 1 |
| Synthetic Experience | type | 1 | 1 |
| Synthetic Task Memory | type | 1 | 1 |
| Synthetic User Behavior Streams (合成用户行为流) | carrier | 1 | 1 |
| System 1 Intuitive Memory | type | 1 | 1 |
| System 2 Deliberative Memory | type | 1 | 1 |
| System Logs | carrier | 1 | 1 |
| Targeted Retrieval (针对性检索) | operation | 1 | 1 |
| Task Agent Memory (任务代理记忆) | type | 1 | 1 |
| Task Context Memory | type | 1 | 1 |
| Task Execution Logs | carrier | 2 | 2 |
| Task Instructions | carrier | 1 | 1 |
| Task-Integrated Memory (任务整合记忆) | type | 1 | 1 |
| Task Prompts (任务 Prompt) | carrier | 1 | 1 |
| Task-related MCP Graph | structure | 1 | 1 |
| Task Trajectories (任务轨迹) | structure | 1 | 1 |
| Task Trajectory Memory | type | 1 | 1 |
| Temporal Invalidation | operation | 1 | 1 |
| Temporal Knowledge Graph | structure | 1 | 1 |
| Temporal Memory | type | 1 | 1 |
| Text-based Skills (Declarative Memory) | type | 1 | 1 |
| Text Chunks | carrier | 1 | 1 |
| Text Context (文本上下文) | carrier | 1 | 1 |
| Text Conversation History | carrier | 1 | 1 |
| Text Conversation Streams | carrier | 1 | 1 |
| Text Embedding | carrier | 1 | 1 |
| Text Embedding Vectors | carrier | 1 | 1 |
| Text Embeddings | carrier | 3 | 3 |
| Text Interaction Logs | carrier | 1 | 1 |
| Text Interaction Sequence | carrier | 1 | 1 |
| Text Interaction Trajectories | carrier | 1 | 1 |
| Text Memory (文本记忆 - 基线对比) | type | 2 | 2 |
| Text Memory Stream | carrier | 1 | 1 |
| Text Passages | carrier | 1 | 1 |
| Text Prompts | carrier | 1 | 1 |
| Text Queries | carrier | 1 | 1 |
| Text Scene Graph | structure | 1 | 1 |
| Text Segments | carrier | 1 | 1 |
| Text Sequence | carrier | 1 | 1 |
| Text Sequences | carrier | 1 | 1 |
| Text Session Trajectories | carrier | 1 | 1 |
| Text Summaries | carrier | 1 | 1 |
| Text Tokens | carrier | 1 | 1 |
| Textual Trajectories | carrier | 1 | 1 |
| Textual Tree Nodes | carrier | 1 | 1 |
| Three-layer Hierarchical Structure (User->Type->Element) | structure | 1 | 1 |
| Three-layer Memory State Space | structure | 1 | 1 |
| Three-layer Memory System | structure | 1 | 1 |
| Three-tier Graph Hierarchy | structure | 1 | 1 |
| Threshold-triggered Evolution | operation | 1 | 1 |
| Time Segments | carrier | 1 | 1 |
| Time Series Vector | carrier | 1 | 1 |
| Time-Varying Directed Multi-Graph | structure | 1 | 1 |
| Timeline Memory | type | 1 | 1 |
| Titans 架构变体 (MAC/MAG/MAL) | structure | 1 | 1 |
| Token-based Context | carrier | 1 | 1 |
| Token-based Context Window (基于 Token 的上下文窗口) | carrier | 1 | 1 |
| Token Embeddings | carrier | 1 | 1 |
| Token Merging | operation | 1 | 1 |
| Token Prior | type | 1 | 1 |
| Token Representations | carrier | 1 | 1 |
| Token Sequence Context | structure | 1 | 1 |
| Token 嵌入序列 (Token Embedding Sequences) | carrier | 1 | 1 |
| Token/Character Sequence | carrier | 1 | 1 |
| Tool API Descriptions | carrier | 1 | 1 |
| Tool-Augmented Context Window | structure | 1 | 1 |
| Tool-based Memory Interface | structure | 1 | 1 |
| Tool Call Trajectory | carrier | 1 | 1 |
| Tool Capability Memory (工具能力记忆) | type | 1 | 1 |
| Tool Context Window | structure | 1 | 1 |
| Tool Feedback Memory | type | 1 | 1 |
| Tool Invocation | operation | 1 | 1 |
| Tool Invocation Sequences (工具调用序列) | type | 1 | 1 |
| Tool Memory | type | 1 | 1 |
| Tool Remove | operation | 1 | 1 |
| Tool Retrieval | operation | 1 | 1 |
| Tool Search | operation | 1 | 1 |
| Tool Solutions (工具解决方案) | carrier | 1 | 1 |
| Tool Usage Filtering | operation | 1 | 1 |
| ToolBench 数据集 (ToolBench Dataset) | carrier | 1 | 1 |
| ToolLLaMA 模型参数 (ToolLLaMA Model Parameters) | carrier | 1 | 1 |
| Topic-Aware Segmentation | operation | 1 | 1 |
| Topic Summaries | carrier | 1 | 1 |
| Topic-Summary-Turn Structure | structure | 1 | 1 |
| Topological Map | structure | 1 | 1 |
| Topological Map Nodes | carrier | 1 | 1 |
| Trace Memory | type | 1 | 1 |
| Training Set Embeddings | carrier | 1 | 1 |
| Trajectory Aggregation (轨迹聚合) | operation | 1 | 1 |
| Trajectory Analysis | operation | 1 | 1 |
| Trajectory Assimilation | operation | 1 | 1 |
| Trajectory Compression (轨迹压缩) | operation | 1 | 1 |
| Trajectory-level Advantage Propagation | operation | 1 | 1 |
| Trajectory Reflection | operation | 1 | 1 |
| Transformer Model Parameters | carrier | 1 | 1 |
| Transformer Parameters | carrier | 1 | 1 |
| Tree-to-Text Linearization | operation | 1 | 1 |
| Trial-and-Error Execution Logs | structure | 1 | 1 |
| Triple Extraction | operation | 1 | 1 |
| Two-stage Training Pipeline (两阶段训练管道) | structure | 1 | 1 |
| Two-Step Alignment | operation | 1 | 1 |
| UI 元素树 (UI Element Tree) | carrier | 1 | 1 |
| UIA Semantic Tree | structure | 1 | 1 |
| Uncertainty-based Retrieval | operation | 1 | 1 |
| Untangle Retrieval | operation | 1 | 1 |
| Update (State/Network) | operation | 2 | 2 |
| UPDATE | operation | 1 | 1 |
| User-Input Triple Extraction | operation | 1 | 1 |
| User Interaction Logs | carrier | 1 | 1 |
| User Profile Memory (Hierarchical KG) | type | 2 | 2 |
| User Profiles | carrier | 1 | 1 |
| Utility-based Deletion | operation | 1 | 1 |
| Utility-Enhanced Memory | type | 1 | 1 |
| Vector Database (向量数据库) | carrier | 4 | 4 |
| Vector Database Memory Store (向量库记忆存储) | structure | 1 | 1 |
| Vector Database Storage | structure | 1 | 1 |
| Vector Embedding Space | carrier | 1 | 1 |
| Vector Embeddings | carrier | 10 | 10 |
| Vector Index (FAISS) | structure | 2 | 2 |
| Vector Space Index | structure | 1 | 1 |
| Vector Store | carrier | 1 | 1 |
| Vector-Text Dual Storage | structure | 1 | 1 |
| Vectorized Knowledge Index | structure | 1 | 1 |
| Verified Skill Library | structure | 1 | 1 |
| Video Embeddings | carrier | 1 | 1 |
| Video Frames | carrier | 2 | 2 |
| Video Latent Sequence | structure | 1 | 1 |
| Virtual Context (Main Context) | type | 1 | 1 |
| Virtual Session Buffer | carrier | 1 | 1 |
| Visual Embedding | carrier | 1 | 1 |
| Visual Grounding Map | structure | 1 | 1 |
| Visual Memory | type | 2 | 2 |
| Visually-aligned Auxiliary Text Memory | type | 1 | 1 |
| VLM Hidden State Extraction | operation | 1 | 1 |
| VLM Internal Hidden States | carrier | 1 | 1 |
| VLM 触发式记忆更新 (VLM-Triggered Memory Update) | operation | 1 | 1 |
| Web Interaction Traces | carrier | 1 | 1 |
| Web-scale Text Chunks (网络规模文本块) | carrier | 1 | 1 |
| Webpage State (网页状态) | carrier | 1 | 1 |
| Weighted Fusion Ranking | operation | 1 | 1 |
| Weighted Knowledge Graph | structure | 1 | 1 |
| Workflow Memory | type | 1 | 1 |
| Working Memory (工作记忆) | type | 5 | 5 |
| Write (写入总结内容) | operation | 1 | 1 |
| YAML Format | structure | 1 | 1 |
| 七类工具接口 (Seven Tool Interfaces) | carrier | 1 | 1 |
| 三层代理工作流 (元管理器 + 专用管理器 + 对话代理) | structure | 1 | 1 |
| 三层分层图谱结构 (MTL/MSL/MGL) | structure | 1 | 1 |
| 三阶段记忆循环 (Three-Stage Memory Loop) | structure | 1 | 1 |
| 上下文 Token (Context Tokens) | carrier | 1 | 1 |
| 上下文修剪 (Context Pruning) | operation | 1 | 1 |
| 上下文工程提示词 (Context Engineering Prompts) | carrier | 1 | 1 |
| 上下文敏感记忆 (Context-Sensitive Memory) | type | 1 | 1 |
| 上下文数据库 (ContextDB) | structure | 1 | 1 |
| 上下文检索与更新 (Context Retrieval & Update) | operation | 1 | 1 |
| 上下文窗口 (Context Window) | carrier | 2 | 2 |
| 上下文编码压缩 (Context Encoding/Compression) | operation | 1 | 1 |
| 上下文记忆单元 (Context Memory Unit) | structure | 1 | 1 |
| 世界事实 (World Facts) | type | 1 | 1 |
| 世界状态模型 (World State Model) | carrier | 1 | 1 |
| 个人经历记忆 (Personal Experience Memory) | type | 1 | 1 |
| 个性化 PageRank 检索 | operation | 1 | 1 |
| 个性化事实知识 (Personalized Factual Knowledge) | type | 1 | 1 |
| 中国医学知识图谱 (CMeKG) | carrier | 1 | 1 |
| 中央记忆控制器 | structure | 1 | 1 |
| 中期记忆 (Medium-term Memory) | type | 1 | 1 |
| 主动折叠 (Proactive Folding) | operation | 1 | 1 |
| 主动检索 (Active Retrieval) | operation | 1 | 1 |
| 主动记忆 (Active Memory) | type | 1 | 1 |
| 主观记忆 (Subjective Memory) | type | 1 | 1 |
| 事实知识三元组 (Factual Knowledge Triples) | structure | 1 | 1 |
| 事实记忆 (Factual Memory) | type | 2 | 2 |
| 云端/本地混合存储 (Cloud/Local Hybrid Storage) | carrier | 1 | 1 |
| 交互历史数据 (Interaction History Data) | carrier | 1 | 1 |
| 交互历史记忆 (Interaction History Memory) | type | 1 | 1 |
| 交互轨迹 (Interaction Trajectories) | carrier | 1 | 1 |
| 交互轨迹记忆 (Interaction Trajectory Memory) | type | 1 | 1 |
| 人物记忆 (Character Memory) | type | 1 | 1 |
| 代理版本树 (Agent Version Tree) | type | 1 | 1 |
| 代理能力描述表 (Agent Capability Description Table) | structure | 1 | 1 |
| 代码库状态快照 (Codebase State Snapshot) | structure | 1 | 1 |
| 代码片段 (Code Snippets) | carrier | 1 | 1 |
| 令牌级记忆 (Token-level Memory) | type | 1 | 1 |
| 任务相关线索片段 (Task-relevant Clue Fragments) | structure | 1 | 1 |
| 任务试错轨迹 (Task Trial Trajectories) | carrier | 1 | 1 |
| 会话内缓冲区 | carrier | 1 | 1 |
| 保留 (Retain) | operation | 1 | 1 |
| 信封加密存储 | structure | 1 | 1 |
| 信息分流 (Information Shunting) | operation | 1 | 1 |
| 元进化 (Meta-Evolution) | operation | 1 | 1 |
| 元进化记忆系统 (Meta-Evolutionary Memory System) | type | 1 | 1 |
| 元适应 (Meta-Adaptation) | operation | 1 | 1 |
| 全局 - 自我对齐融合 (Global-to-Ego Alignment Fusion) | operation | 1 | 1 |
| 全局到自我对齐记忆 (Global-to-Ego Aligned Memory) | type | 1 | 1 |
| 全局记忆 (Global Memory) | type | 1 | 1 |
| 全局记忆池 (Global Memory Pool) | structure | 1 | 1 |
| 六模块记忆组件架构 | structure | 1 | 1 |
| 关键词记忆片段 (Keyword Memory Segment) | type | 1 | 1 |
| 具身传感器数据 (深度/姿态) (Embodied Sensor Data: Depth/Pose) | carrier | 1 | 1 |
| 冲突解决策略 | operation | 1 | 1 |
| 决策树搜索 (Decision Tree Search) | operation | 1 | 1 |
| 冻结的大模型参数 (Frozen LLM Parameters) | carrier | 1 | 1 |
| 分层交互系统 (Layered Interaction System) | structure | 1 | 1 |
| 删除 (Deletion) | operation | 1 | 1 |
| 动态上下文工作区 (Dynamic Context Workspace) | type | 1 | 1 |
| 动态上下文注入 (Dynamic Context Injection) | operation | 1 | 1 |
| 动态作弊表记忆 (Dynamic Cheatsheet Memory) | type | 1 | 1 |
| 动态工作记忆 (Dynamic Working Memory) | type | 1 | 1 |
| 动态显著信息提取 (Dynamic Significant Information Extraction) | operation | 1 | 1 |
| 动态更新 (Dynamic Update) | operation | 2 | 2 |
| 动态演化更新 (Dynamic Evolution Update) | operation | 1 | 1 |
| 动态用户画像 (Dynamic User Profiles) | type | 1 | 1 |
| 动态记忆库 (Dynamic Memory Bank) | structure | 1 | 1 |
| 动态记忆注入 | operation | 1 | 1 |
| 动态重要性记忆过滤 (DIMF) | operation | 1 | 1 |
| 医疗指令数据 (Medical Instruction Data) | type | 1 | 1 |
| 单元映射 (Unit Mapping) | operation | 1 | 1 |
| 历史交互日志 (Historical Interaction Log) | structure | 1 | 1 |
| 压缩上下文表示 (Compressed Context Representation) | type | 1 | 1 |
| 原始记忆 (Raw Memory) | type | 1 | 1 |
| 原始轨迹记忆 (Raw Trajectory) | type | 1 | 1 |
| 原子索引映射 (Atomic Index Mapping) | structure | 1 | 1 |
| 参数化知识内化 (Parametric Knowledge Internalization) | operation | 1 | 1 |
| 参数化记忆 (Parametric Memory) | type | 1 | 1 |
| 参数级记忆 (Parametric Memory) | type | 1 | 1 |
| 双单元存储 (Dual-Unit Storage) | operation | 1 | 1 |
| 双模块记忆框架 (Dual-module Memory Framework) | structure | 1 | 1 |
| 双阶段架构 (训练 - 推理分离架构) | structure | 1 | 1 |
| 反向重建 (Backward Reconstruction) | operation | 1 | 1 |
| 反思 (Reflect) | operation | 1 | 1 |
| 反思层 (Reflection Layer) | structure | 1 | 1 |
| 反思模块 (Reflection Module) | carrier | 1 | 1 |
| 反思生成 (Reflection Generation) | operation | 1 | 1 |
| 反思经验 (Reflection Experience) | type | 1 | 1 |
| 叙事记忆 (Narrative Memory) | type | 1 | 1 |
| 可复用工具 (Reusable Tools) | carrier | 1 | 1 |
| 可学习令牌序列 (Learnable Token Sequence) | structure | 1 | 1 |
| 可学习参数向量 (Learnable Parameter Vectors) | carrier | 1 | 1 |
| 可寻址向量数据库 (Addressable Vector Database) | carrier | 1 | 1 |
| 可微分记忆读写 (Differentiable Memory Read/Write) | operation | 1 | 1 |
| 可编辑记忆图 (Editable Memory Graph, EMG) | structure | 1 | 1 |
| 可逆 Transformer 架构 (Reversible Transformer Architecture) | structure | 1 | 1 |
| 可逆记忆 (Reversible Memory) | type | 1 | 1 |
| 各向异性读取 (Anisotropic Reading) | operation | 1 | 1 |
| 合成实体摘要 (Entity Summaries) | type | 1 | 1 |
| 合成策略记忆 (Synthetic Strategy Memory) | type | 1 | 1 |
| 向量化记忆片段 (Vectorized Memory Segments) | carrier | 1 | 1 |
| 向量基于记忆 (Vector-based Memory) | type | 1 | 1 |
| 向量存储 (Vector Storage) | carrier | 1 | 1 |
| 向量嵌入 (Vector Embeddings) | carrier | 1 | 1 |
| 向量或图结构数据库 (Vector/Graph Database) | carrier | 1 | 1 |
| 向量数据库 (Vector Database) | carrier | 9 | 9 |
| 向量检索匹配 (Vector Retrieval Matching) | operation | 1 | 1 |
| 向量检索数据库 (Vector Retrieval Database) | carrier | 1 | 1 |
| 向量索引 (Vector Index) | structure | 1 | 1 |
| 四逻辑网络 (Four Logical Networks) | structure | 1 | 1 |
| 回忆 (Recall) | operation | 1 | 1 |
| 固定长度连续向量 (Fixed-length Continuous Vectors) | structure | 1 | 1 |
| 图基于记忆 (Graph-based Memory) | type | 1 | 1 |
| 图式 (Schema) | structure | 1 | 1 |
| 图式演化 (Schema Evolution) | operation | 1 | 1 |
| 图数据库 (Graph Database) | carrier | 1 | 1 |
| 图谱节点与边 | carrier | 1 | 1 |
| 基于 Prompt 的策略存储 (Prompt-based Strategy Storage) | structure | 1 | 1 |
| 基于 Token 的修剪机制 | structure | 1 | 1 |
| 基于关键特征平均相似度的检索 (AveFact Retrieval) | operation | 1 | 1 |
| 基于内容的记忆检索 (Content-based Memory Retrieval) | operation | 1 | 1 |
| 基于反馈的知识提取 (Knowledge Extraction from Feedback) | operation | 1 | 1 |
| 基于备忘录的响应生成 (Memo-Augmented Response) | operation | 1 | 1 |
| 基于嵌入的检索 (Embedding-based Retrieval) | operation | 1 | 1 |
| 基于相关性的检索 (Relevance-based Retrieval) | operation | 1 | 1 |
| 基于编辑距离的索引 (Edit-Distance Based Index) | structure | 1 | 1 |
| 基于记忆的解码生成 (Memory-based Decoding) | operation | 1 | 1 |
| 基础 LLM 解码器 | carrier | 1 | 1 |
| 增强系统提示词 (Augmented System Prompts) | carrier | 1 | 1 |
| 增强记忆库 (Enhanced Memory Bank) | carrier | 1 | 1 |
| 增量 Delta 更新 (Incremental Delta Update) | operation | 1 | 1 |
| 备忘录存储 (Memo Store) | structure | 1 | 1 |
| 备忘录撰写 (Memo Writing) | operation | 1 | 1 |
| 备忘录检索 (Memo Retrieval) | operation | 1 | 1 |
| 外部 API 数据 | carrier | 1 | 1 |
| 外部 API 服务器 (External API Servers) | carrier | 1 | 1 |
| 外部向量数据库 (External Vector Database) | structure | 1 | 1 |
| 外部图数据库 (External Graph Database) | carrier | 1 | 1 |
| 外部知识图谱 (External Knowledge Graph) | structure | 1 | 1 |
| 外部策略数据库 (External Strategy Database) | carrier | 1 | 1 |
| 外部记忆库 (External Memory Bank) | carrier | 2 | 2 |
| 外部记忆数据库 (External Memory Database) | carrier | 1 | 1 |
| 外部记忆模块 (External Memory Module) | type | 1 | 1 |
| 多尺度历史轨迹 (Multi-scale History Trajectory) | structure | 1 | 1 |
| 多工具交互日志 (Multi-tool Interaction Logs) | carrier | 1 | 1 |
| 多模态交互日志 (Multimodal Interaction Logs) | carrier | 1 | 1 |
| 多模态具身记忆 (Multimodal Embodied Memory) | type | 1 | 1 |
| 多模态金融数据 (文本/音频/表格) | carrier | 1 | 1 |
| 多源检索 (Multi-source Retrieval) | operation | 1 | 1 |
| 多源检索模块 (Multi-source Retrieval Module) | structure | 1 | 1 |
| 多记忆片段系统 (Multi-Memory Segment System, MMS) | structure | 1 | 1 |
| 多轮交互序列 (Multi-turn Interaction Sequence) | carrier | 1 | 1 |
| 大模型参数 (LLM Parameters) | carrier | 1 | 1 |
| 存储模块 (Store Module) | structure | 1 | 1 |
| 安全沙箱环境 (Safety Sandbox Environment) | carrier | 1 | 1 |
| 实体关系图谱 (Entity-Relation Graph) | structure | 1 | 1 |
| 实证验证 (Empirical Verification) | operation | 1 | 1 |
| 对比原则结构 (When/Should/Rather/Because) | structure | 1 | 1 |
| 对话历史 (Dialogue History) | carrier | 2 | 2 |
| 对话文本 (Dialogue Text) | carrier | 1 | 1 |
| 对话流 (Dialogue Stream) | carrier | 1 | 1 |
| 对话记忆 | type | 1 | 1 |
| 层次化压缩结构 (Hierarchical Compression Structure) | structure | 1 | 1 |
| 层级化故事线 (Hierarchical Storylines) | structure | 1 | 1 |
| 层级化记忆管理 (Hierarchical Memory Management) | structure | 1 | 1 |
| 层级总结 (Hierarchical Summarization) | operation | 1 | 1 |
| 屏幕截图 (Screen Screenshots) | carrier | 2 | 2 |
| 工作记忆 (Working Memory) | type | 3 | 3 |
| 工具指令记忆 (Tool Instruction Memory) | type | 1 | 1 |
| 工具记忆化 (Tool Memorization) | operation | 1 | 1 |
| 工具辅助记忆查询 (Tool-Assisted Memory Query) | operation | 1 | 1 |
| 常识推理记忆 (Common Sense Reasoning Memory) | type | 1 | 1 |
| 平均向量表示 (Average Vector Representation) | carrier | 1 | 1 |
| 并行更新 (Parallel Update) | operation | 1 | 1 |
| 异步记忆更新 | operation | 1 | 1 |
| 强化学习路径选择 (RL-guided Path Selection) | operation | 1 | 1 |
| 循环一致性优化 (Cycle Consistency Optimization) | operation | 1 | 1 |
| 微调大语言模型 (Micro-tuned LLM) | carrier | 1 | 1 |
| 性能评估记录 (Performance Evaluation Record) | structure | 1 | 1 |
| 情感上下文记忆 (Emotional Context Memory) | type | 1 | 1 |
| 情景事件记忆 | type | 1 | 1 |
| 情景记忆 (Episodic Memory) | type | 6 | 6 |
| 情景记忆库 (Episodic Memory Bank) | structure | 1 | 1 |
| 情景记忆片段 (Episodic Memory Segment) | type | 1 | 1 |
| 情节痕迹 (Episodic Trace) | type | 1 | 1 |
| 情节痕迹形成 (Episodic Trace Formation) | operation | 1 | 1 |
| 惊喜度驱动编码 (Surprise-Driven Encoding) | operation | 1 | 1 |
| 感官情境记忆 | type | 1 | 1 |
| 感官记忆 (Sensory Memory) | type | 1 | 1 |
| 成功/失败案例记忆 (Success/Failure Case Memory) | type | 1 | 1 |
| 成功/失败轨迹经验 (Success/Failure Trajectory Experience) | type | 1 | 1 |
| 执行轨迹记忆 (Execution Trace Memory) | type | 1 | 1 |
| 扩展特殊令牌 (Extended Special Tokens) | carrier | 1 | 1 |
| 技能抽象提取 (Skill Abstraction Extraction) | operation | 1 | 1 |
| 技能模式记忆 (Skill Pattern Memory) | type | 1 | 1 |
| 折叠记忆 (Folded Memory) | type | 1 | 1 |
| 抽象脚本记忆 (Abstract Script) | type | 1 | 1 |
| 持久化世界状态 (Persistent World State) | structure | 1 | 1 |
| 持久化存储 (Persistent Storage) | carrier | 1 | 1 |
| 持久场景记忆 (Persistent Scene Memory) | type | 1 | 1 |
| 持久记忆 (Persistent Memory) | type | 2 | 2 |
| 指令微调 (Instruction Tuning) | operation | 1 | 1 |
| 指令微调后的 LLM 参数 (Instruction-Tuned LLM Parameters) | carrier | 1 | 1 |
| 探索性探针生成 (Exploratory Probing Generation) | operation | 1 | 1 |
| 推理 - 动作 - 观察三元组 (Reasoning-Action-Observation Triplet) | structure | 1 | 1 |
| 推理困境检测 (Reasoning Dilemma Detection) | operation | 1 | 1 |
| 推理期无缝调用 (Inference-time Invocation) | operation | 1 | 1 |
| 推理记忆 (Reasoning Memory) | type | 2 | 2 |
| 提示检索 (Hint Retrieval) | operation | 1 | 1 |
| 插入 (Insertion) | operation | 1 | 1 |
| 操作动作序列 (Action Sequences) | carrier | 1 | 1 |
| 敏感信息分级访问控制 | operation | 1 | 1 |
| 敏感凭证 | carrier | 1 | 1 |
| 敏感查询记忆 (Sensitive Query Memory) | type | 1 | 1 |
| 文本 Prompt | carrier | 1 | 1 |
| 文本备忘录字符串 (Textual Memo Strings) | carrier | 1 | 1 |
| 文本对话 | carrier | 1 | 1 |
| 文本对话流 (Text Dialogue Flow) | carrier | 1 | 1 |
| 文本序列 (Text Sequence) | carrier | 1 | 1 |
| 文本指南库 (Text Guide Repository) | carrier | 1 | 1 |
| 文本段落 | carrier | 1 | 1 |
| 文本策略片段 (Text Strategy Snippets) | carrier | 1 | 1 |
| 文本轨迹 (Text Trajectory) | carrier | 1 | 1 |
| 文档文件 | carrier | 1 | 1 |
| 新皮层式存储 | structure | 1 | 1 |
| 无反向传播图谱优化 (Graph Optimization without Back-propagation) | operation | 1 | 1 |
| 时空语义系统 (Spatio-Temporal Semantic System) | structure | 1 | 1 |
| 时间二进制压缩 (TBC) | operation | 1 | 1 |
| 时间实体感知记忆层 (Temporal Entity-Aware Memory Layer) | structure | 1 | 1 |
| 时间戳事件存储 | carrier | 1 | 1 |
| 时间戳事件日志 | carrier | 1 | 1 |
| 时间敏感长期记忆 (Time-Sensitive Long-term Memory) | type | 1 | 1 |
| 时间衰减 (Time-based Decay) | operation | 1 | 1 |
| 显存缓冲区 | carrier | 1 | 1 |
| 智能体经验 (Agent Experience) | type | 1 | 1 |
| 替换 (Replacement) | operation | 1 | 1 |
| 本地手机端存储 | carrier | 1 | 1 |
| 权重衰减遗忘机制 (Weight Decay Forgetting) | operation | 1 | 1 |
| 条目化子弹点 (Itemized Bullet Entries) | structure | 1 | 1 |
| 架构优化 (Architecture Optimization) | operation | 1 | 1 |
| 查询分类路由 (Query Classification Routing) | operation | 1 | 1 |
| 校园模拟环境状态 (Campus Simulation Environment State) | carrier | 1 | 1 |
| 核心记忆 (Core Memory) | type | 2 | 2 |
| 档案库采样 (Archive Sampling) | operation | 1 | 1 |
| 检索器行为模仿 (Retriever Behavior Imitation) | operation | 1 | 1 |
| 检索增强推理 (Retrieval-Augmented Inference) | operation | 1 | 1 |
| 检索增强记忆存储 (Retrieval-Augmented Memory Store) | structure | 1 | 1 |
| 检索操纵 (Retrieval Manipulation) | operation | 1 | 1 |
| 检索模块 (Retrieve Module) | structure | 1 | 1 |
| 检索记忆单元 (Retrieval Memory Unit) | structure | 1 | 1 |
| 概念化投资信念 (Conceptual Investment Beliefs) | type | 1 | 1 |
| 概率插值机制 (Probability Interpolation Mechanism) | structure | 1 | 1 |
| 概率插值集成 (Probability Interpolation Integration) | operation | 1 | 1 |
| 模块化 AI 代理架构 (Modular AI Agent Architecture) | structure | 1 | 1 |
| 模块化记忆服务 | structure | 1 | 1 |
| 模块化记忆空间 (Modular Memory Space) | structure | 1 | 1 |
| 模型权重 (Model Weights) | structure | 1 | 1 |
| 正向压缩 (Forward Compression) | operation | 1 | 1 |
| 洞察提取 (Insight Extraction) | operation | 1 | 1 |
| 测试时可更新权重矩阵 (Test-Time Updatable Weight Matrix) | structure | 1 | 1 |
| 测试时梯度下降更新 (Test-Time Gradient Descent) | operation | 1 | 1 |
| 海马体式索引 | structure | 1 | 1 |
| 海马体索引记忆 | type | 1 | 1 |
| 深度优先搜索决策树 (DFSDT) | structure | 1 | 1 |
| 深度整合 (Deep Consolidation) | operation | 1 | 1 |
| 混合存储策略 (端云结合) | structure | 1 | 1 |
| 混合检索 (Hybrid Retrieval) | operation | 1 | 1 |
| 混合记忆架构 (Hybrid Memory Architecture) | structure | 2 | 2 |
| 渐进式压缩记忆 (Progressive Compressed Memory) | type | 1 | 1 |
| 源代码仓库 (Source Code Repository) | carrier | 1 | 1 |
| 滑动窗口上下文 (Sliding Window Context) | structure | 1 | 1 |
| 演化信念 (Evolving Beliefs) | type | 1 | 1 |
| 潜在空间向量 (Latent Space Vectors) | structure | 1 | 1 |
| 潜在空间表示 (Latent Space Representations) | carrier | 1 | 1 |
| 潜在级记忆 (Latent Memory) | type | 1 | 1 |
| 潜在视觉记忆模块 (Latent Vision Memory Module) | structure | 1 | 1 |
| 版本化经验库 (Versioned Experience Library) | structure | 1 | 1 |
| 状态化记忆 (Stateful Memory) | type | 1 | 1 |
| 状态回滚 (State Rollback) | operation | 1 | 1 |
| 状态快照记忆 (State Snapshot Memory) | type | 1 | 1 |
| 生成式检索记忆 (Generative Retrieval Memory) | type | 1 | 1 |
| 用户交互反馈记忆 (User Interaction Feedback Memory) | type | 1 | 1 |
| 用户偏好特征 (User Preference Features) | carrier | 1 | 1 |
| 画像模块 (Profile Module) | structure | 1 | 1 |
| 知识三元组 (Knowledge Triplets ⟨参数 1, 关系，参数 2⟩) | structure | 1 | 1 |
| 知识保险库 (Knowledge Vault) | type | 1 | 1 |
| 知识内化转换 (Knowledge Internalization Transformation) | operation | 1 | 1 |
| 知识图谱实例 (Knowledge Graph Instances) | type | 1 | 1 |
| 知识图谱记忆结构 | structure | 1 | 1 |
| 知识巩固与整合 (Knowledge Consolidation & Integration) | operation | 1 | 1 |
| 知识蒸馏 (Knowledge Distillation) | operation | 1 | 1 |
| 知识记忆 (Knowledge Memory) | type | 1 | 1 |
| 知识采样 (Knowledge Sampling) | operation | 1 | 1 |
| 短期工作记忆 | type | 1 | 1 |
| 短期感知保留记忆 (Short-term Perception Retention Memory) | type | 1 | 1 |
| 短期注意力记忆 (Short-Term Attention Memory) | type | 1 | 1 |
| 短期记忆 (Short-term Memory) | type | 1 | 1 |
| 神经 API 检索索引 (Neural API Retrieval Index) | structure | 1 | 1 |
| 神经案例记忆 (Neural Case Memory) | type | 1 | 1 |
| 神经生物学启发的长期记忆 | type | 1 | 1 |
| 神经网络参数 (Neural Parameters) | carrier | 1 | 1 |
| 神经长期记忆 (Neural Long-Term Memory) | type | 1 | 1 |
| 离线索引构建 | operation | 1 | 1 |
| 离线自博弈生成 (Offline Self-Play Generation) | operation | 1 | 1 |
| 程序化构建 (Proceduralization) | operation | 1 | 1 |
| 程序性记忆 (Procedural Memory) | type | 1 | 1 |
| 程序记忆 (Procedural Memory) | type | 2 | 2 |
| 竞争 - 抑制遗忘 (Competitive-Inhibitory Forgetting) | operation | 1 | 1 |
| 第一人称视频流 (Egocentric Video Streams) | carrier | 1 | 1 |
| 策展片段集合 (Curated Snippet Collection) | structure | 1 | 1 |
| 策略模型权重 (Policy Model Weights) | carrier | 1 | 1 |
| 策略记忆 (Strategy Memory) | type | 1 | 1 |
| 管理模块 (Manage Module) | structure | 1 | 1 |
| 纠错更新 (Correction Update/Reflexion) | operation | 1 | 1 |
| 约束生成 (Constrained Generation) | operation | 1 | 1 |
| 细粒度浓缩 (Granular Condensation) | operation | 1 | 1 |
| 细粒度评估 (Fine-grained Evaluation) | operation | 1 | 1 |
| 经验反思 (Experience Reflection) | operation | 1 | 1 |
| 经验存储 (Experience Storage) | operation | 1 | 1 |
| 经验库存储系统 (Experience Library Storage System) | carrier | 1 | 1 |
| 经验库演化 (Experience Library Evolution) | operation | 1 | 1 |
| 经验探索检索 (Experience Exploration Retrieval) | operation | 1 | 1 |
| 经验条目 (Experience Entries) | structure | 1 | 1 |
| 经验检索增强 (Experience Retrieval Augmentation) | operation | 1 | 1 |
| 经验池 (Experience Pool) | structure | 1 | 1 |
| 经验知识 (Experiential Knowledge) | type | 1 | 1 |
| 经验继承 (Experience Inheritance) | operation | 1 | 1 |
| 经验蒸馏 (Experience Distillation) | operation | 1 | 1 |
| 经验记忆 (Experiential Memory) | type | 4 | 4 |
| 经验轨迹记录 (Experience Trajectory Records) | structure | 1 | 1 |
| 结构化事实备忘录 (Structured Fact Memos) | type | 1 | 1 |
| 结构化任务序列 (Structured Task Sequences) | structure | 1 | 1 |
| 结构化剧本 (Structured Playbook) | type | 1 | 1 |
| 结构化图谱节点 (实体/关系) | carrier | 1 | 1 |
| 结构化对话日志表 (Structured Conversation Log Table) | structure | 1 | 1 |
| 结构化推理基底 (Structured First-Class Substrate) | structure | 1 | 1 |
| 结构化文本三元组 (Structured Text Triplets) | carrier | 1 | 1 |
| 结构化文本原则 (Structured Text Principles) | structure | 1 | 1 |
| 结构化文本原则库 | carrier | 1 | 1 |
| 结构化经验 (Structured Experience) | type | 1 | 1 |
| 结构化经验库 (Structured Experience Library) | structure | 1 | 1 |
| 结构化表格 (Structured Table) | carrier | 1 | 1 |
| 结构化记忆库 (Structured Memory Bank) | carrier | 1 | 1 |
| 结构化记忆片段 (Structured Memory Fragments) | structure | 1 | 1 |
| 编码模块 (Encode Module) | structure | 1 | 1 |
| 联合进化 (Joint Evolution) | operation | 1 | 1 |
| 能力匹配 (Capability Matching) | operation | 1 | 1 |
| 自主生成 (Autonomous Generation) | operation | 1 | 1 |
| 自动化标注 (Automated Annotation) | operation | 1 | 1 |
| 自我中心记忆 (Ego-centric Memory) | type | 1 | 1 |
| 自我代码修改 (Self-Code Modification) | operation | 1 | 1 |
| 自我提示库 (Self-Hint Repository) | structure | 1 | 1 |
| 自我策展 (Self-Curation) | operation | 1 | 1 |
| 自然语言文本 (Natural Language Text) | carrier | 1 | 1 |
| 自用备忘录 (Self-use Memos) | type | 1 | 1 |
| 自适应检索 (Adaptive Retrieval) | operation | 1 | 1 |
| 自适应记忆 (Adaptive Memory) | type | 1 | 1 |
| 自验证 (Self-Validation) | operation | 1 | 1 |
| 蒸馏经验 (Distilled Experience) | carrier | 1 | 1 |
| 虚拟令牌词表 (Virtual Token Vocabulary) | structure | 1 | 1 |
| 虚拟记忆 (Virtual Memory) | type | 1 | 1 |
| 虚拟记忆令牌 (Virtual Memory Tokens) | carrier | 1 | 1 |
| 融合视频与传感器的记忆库 (Video-Sensor Fused Memory Bank) | structure | 1 | 1 |
| 被动记忆 (Passive Memory) | type | 1 | 1 |
| 视觉语言模型 (Vision-Language Model) | carrier | 1 | 1 |
| 视频帧特征图 | carrier | 1 | 1 |
| 解决方案路径 (Solution Path) | structure | 1 | 1 |
| 言语强化 Prompt 更新 (Prompt Update via Verbal Reinforcement) | operation | 1 | 1 |
| 言语强化记忆 (Verbal Reinforcement Memory) | type | 1 | 1 |
| 认知视角记忆片段 (Cognitive Perspective Memory Segment) | type | 1 | 1 |
| 记忆 - 注意力融合模块 (Memory-Attention Fusion Module) | structure | 1 | 1 |
| 记忆写入 (Memory Write) | operation | 1 | 1 |
| 记忆原型 (Prototypes) | structure | 1 | 1 |
| 记忆向量表示 (Memory Vector Representation) | carrier | 1 | 1 |
| 记忆图层 (Memory Graph Layer, MGL) | structure | 1 | 1 |
| 记忆图谱 (Memory Graph) | structure | 1 | 1 |
| 记忆块 (Memory Block) | structure | 1 | 1 |
| 记忆增强 (Potentiation) | operation | 1 | 1 |
| 记忆增强马尔可夫决策过程 (M-MDP) | structure | 1 | 1 |
| 记忆子类 (Memory Subclass) | type | 1 | 1 |
| 记忆存储池 (Memory Storage Pool) | structure | 1 | 1 |
| 记忆巩固 (Memory Consolidation) | operation | 3 | 3 |
| 记忆库 (Memory Bank) | structure | 1 | 1 |
| 记忆形成 (Memory Formation) | operation | 1 | 1 |
| 记忆提取 (Memory Extraction) | operation | 1 | 1 |
| 记忆提取攻击 (Memory Extraction Attack) | operation | 1 | 1 |
| 记忆整合 (Memory Integration) | operation | 1 | 1 |
| 记忆更新 (Memory Update) | operation | 1 | 1 |
| 记忆更新策略 (Memory Update Strategy) | operation | 1 | 1 |
| 记忆构建策略 (Memory Construction Strategy) | operation | 1 | 1 |
| 记忆架构 (Memory Architecture) | type | 1 | 1 |
| 记忆检索 (Memory Retrieval) | operation | 4 | 4 |
| 记忆检索器 (Memory Retriever) | structure | 1 | 1 |
| 记忆槽 (Memory Slots) | type | 1 | 1 |
| 记忆槽缓存复用 (Memory Slot Caching/Reuse) | operation | 1 | 1 |
| 记忆淘汰机制 (Memory Elimination Mechanism) | operation | 1 | 1 |
| 记忆演化 (Memory Evolution) | operation | 1 | 1 |
| 记忆片段构建 (Memory Segment Construction) | operation | 1 | 1 |
| 记忆类型 (Memory Type) | type | 1 | 1 |
| 记忆编码与压缩 (Memory Encoding & Compression) | operation | 1 | 1 |
| 记忆编码器 (Memory Encoder) | structure | 1 | 1 |
| 记忆自动路由 (Memory Auto-Routing) | operation | 1 | 1 |
| 记忆自进化 (Memory Self-Evolution) | operation | 1 | 1 |
| 记忆解码器 (Memory Decoder) | structure | 1 | 1 |
| 记忆读取 (Memory Read) | operation | 1 | 1 |
| 记忆距离加权评分 (Memory Distance Weighted Scoring) | operation | 1 | 1 |
| 记忆遗忘 (Memory Forgetting) | operation | 1 | 1 |
| 记忆重写 (Memory Rewrite) | operation | 1 | 1 |
| 语义/拓扑地图 (Semantic/Topological Map) | structure | 1 | 1 |
| 语义去重 (Semantic Deduplication) | operation | 1 | 1 |
| 语义场景 (Semantic Scene) | type | 1 | 1 |
| 语义巩固 (Semantic Consolidation) | operation | 1 | 1 |
| 语义检索 (Semantic Retrieval) | operation | 2 | 2 |
| 语义记忆 (Semantic Memory) | type | 2 | 2 |
| 语义记忆片段 (Semantic Memory Segment) | type | 1 | 1 |
| 语境重解释 (Contextual Re-interpretation) | operation | 1 | 1 |
| 资源记忆 (Resource Memory) | type | 1 | 1 |
| 跨交互读写 (Cross-interaction Read/Write) | operation | 1 | 1 |
| 跨会话聚类 (Cross-session Clustering) | operation | 1 | 1 |
| 跨段落知识整合 | operation | 1 | 1 |
| 轨迹存储 (Trajectory Storage) | operation | 1 | 1 |
| 轨迹序列 (Trajectory Sequence) | structure | 1 | 1 |
| 软件指南书 (Software Guidebook) | structure | 1 | 1 |
| 进化上下文 (Evolving Context) | type | 1 | 1 |
| 进化档案库 (Evolutionary Archive) | type | 1 | 1 |
| 连续潜在上下文 (Continuous Latent Contexts) | carrier | 1 | 1 |
| 连贯上下文 (Coherent Context) | structure | 1 | 1 |
| 选择性遗忘 | operation | 1 | 1 |
| 通用读写记忆 (General Read-Write Memory) | type | 1 | 1 |
| 重构式回忆 (Reconstructed Recall) | operation | 1 | 1 |
| 链式表过滤 (Chain-of-Tables Filtering) | operation | 1 | 1 |
| 键值对记忆库 (Key-Value Memory Bank) | structure | 1 | 1 |
| 键值融合 (Key-Value Fusion) | operation | 1 | 1 |
| 长上下文 Token 序列 (Long Context Token Sequences) | carrier | 1 | 1 |
| 长期交互记忆 (Long-term Interaction Memory) | type | 1 | 1 |
| 长期用户记忆 | type | 1 | 1 |
| 长期记忆 (Long-term Memory) | type | 3 | 3 |
| 长期记忆数据库 (Long-term Memory Database) | structure | 1 | 1 |
| 长期语义巩固记忆 (Long-term Semantic Consolidation Memory) | type | 1 | 1 |
| 问答对结构 (QA Pairs Structure) | structure | 1 | 1 |
| 问答评估对 (QA Evaluation Pair) | carrier | 1 | 1 |
| 静态提示 (Static Prompt) | type | 1 | 1 |
| 非参数化策略记忆 (Non-parametric Strategy Memory) | type | 1 | 1 |
| 非结构化文本记忆 | carrier | 1 | 1 |
| 预存储推理 (Pre-Storage Reasoning) | operation | 1 | 1 |
| 预训练数据集 (WikiText-103, Web datasets) | carrier | 1 | 1 |
| 领域知识记忆 (Domain Knowledge Memory) | type | 1 | 1 |
| 风险触发式自我反思 (Risk-triggered Self-Reflection) | operation | 1 | 1 |
| 高分辨率键值对 (Key/Value) | structure | 1 | 1 |

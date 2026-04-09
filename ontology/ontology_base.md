---
based_on_version: '2.49'
created_at: 2026-03-30
current_version: '2.50'
description: Agent Memory 领域本体论创世版本
papers_covered: 146
title: Agent Memory 领域本体论
updated_at: '2026-04-09T15:16:46.541156'
---




























































































# Agent Memory 领域本体论

## 版本信息
**版本**: 创世版本 v1.0
**初始化时间**: 2026-03-30
**覆盖论文总数**: 54 篇

---

## 核心公理体系

### 记忆存在公理
- **持久性**: 记忆必须能够跨时间保持信息完整性
- **可访问性**: 记忆必须支持高效的检索和更新操作
- **一致性**: 记忆内容必须保持逻辑一致性和事实准确性

### 记忆操作公理
- **形成公理**: 记忆形成必须基于有意义的经验单元（事件、对话、观察）
- **演化公理**: 记忆必须支持结构化演进（巩固、遗忘、整合）
- **检索公理**: 记忆检索必须支持目标导向的主动搜索

### 认知交互公理
- **感知绑定**: 记忆必须与感知系统紧密集成
- **推理支撑**: 记忆必须为推理提供必要且充分的上下文
- **行动指导**: 记忆必须能够指导智能体的行为决策

### 本体论公理

#### 公理 1: 直接操作优于抽象
```
∀ agent ∈ WebAgent:
  DirectOperation(agent, RawWebPage) > AbstractOperation(agent, StaticText)
```
**解释**: 直接操作原始网页的智能体优于转换为静态文本的智能体

#### 公理 2: 显式记忆优于隐式记忆
```
∀ agent ∈ ToolAgent:
  ExplicitMemory(agent, ToolCapability) > ImplicitMemory(agent, ParameterUpdate)
```
**解释**: 显式工具能力记忆优于隐式参数更新

#### 公理 3: 效率与性能可兼得
```
∀ method ∈ EfficiencyOptimization:
  ReduceMemory(method) ∧ MaintainPerformance(method)
```
**解释**: 效率优化方法可同时减少内存使用和保持性能

#### 公理 4: 小模型可超越大模型
```
∀ small_model ∈ SmallLM, task ∈ LongHorizonTask:
  EnhancedBy(small_model, EfficiencyMethod) > Baseline(small_model)
```
**解释**: 小模型通过效率优化方法可超越基线大模型

---

## 概念关系网络

### 形式维度网络 (Forms)
- **Token-level Memory**: 显式离散存储
  - *子类型*: Event Graph, Multi-Graph, Structural Tree, Experience Pool, Modular Design Space, Dynamic Experience Pool, Expert Adapters
- **Parametric Memory**: 隐式权重存储
  - *子类型*: Fine-tuning, Adapter-based, Memory Adapters, Meta-Evolution Architecture
- **Latent Memory**: 隐藏状态存储
  - *子类型*: Hidden States, Attention Patterns, Visual Features, Visual Memory Corpus, SVLM Features

### 功能维度网络 (Functions)
- **Factual Memory**: 知识存储与检索
  - *应用场景*: 长文档QA、知识问答
  - *技术特征*: 结构化表示、精确检索
- **Experiential Memory**: 技能学习与进化
  - *应用场景*: 自主代理、强化学习
  - *技术特征*: 效用驱动、自适应更新
- **Working Memory**: 上下文管理与推理
  - *应用场景*: 多跳推理、复杂任务规划
  - *技术特征*: 主动搜索、动态维护

### 动态维度网络 (Dynamics)
- **Formation**: 记忆提取与构建
  - *机制*: 事件分割、EDU分解、经验抽象
  - *质量指标*: 忠实度、完整性、结构化程度
- **Evolution**: 记忆巩固与遗忘
  - *机制*: 语义巩固、效用更新、周期性重聚类
  - *质量指标*: 一致性、抗干扰性、演化稳定性
- **Retrieval**: 记忆访问与检索
  - *机制*: 策略引导遍历、两阶段检索、主动多路径搜索
  - *质量指标*: 相关性、效率、可解释性

---

## 跨维度整合网络

### 三维一体记忆模型
```
[Form] ←→ [Function] ←→ [Dynamics]
   ↑         ↑           ↑
结构化     目标导向     生命周期
表示       应用        管理
```

### 认知架构集成
- **感知层**: 原始输入 → 记忆形成
- **记忆层**: 结构化存储 ↔ 动态演化 ↔ 目标检索
- **推理层**: 记忆检索 → 上下文合成 → 决策生成
- **行动层**: 决策执行 → 经验反馈 → 记忆更新

---

## 记忆结构类型

### 基础记忆图结构
- **Event Graph** (CompassMem): 基于事件分割理论的图结构
- **Multi-Graph** (MAGMA): 四个正交关系图的解耦表示
- **Structural Relation Tree** (From Context to EDUs): EDU分解的树结构
- **Intent-Experience-Utility Triplet** (MemRL): 强化学习驱动的三元组
- **Heterogeneous Graph** (EMem): Sessions-EDUs-Arguments 三层异构图
- **4 Logical Networks** (Hindsight): World Facts, Agent Experiences, Entity Summaries, Evolving Beliefs
- **Multi-Temporal Graphs** (WorldMM): 秒级/分钟级/小时级多粒度图
- **Weighted Knowledge Graph** (Memoria): 指数衰减加权的知识图谱 (α=0.02)

### 网页智能体架构
- **人类启发式浏览器动作** (Human-Inspired Browser Actions): 滚动/点击/打字等直接操作原始网页的动作
- **端到端深度推理** (End-to-End Deep Reasoning): 单一连贯推理过程中执行自主思考、工具发现和行动执行
- **主动上下文折叠** (Proactive Context Folding): 将上下文视为动态认知工作空间，学习执行折叠操作
- **动态结构化记忆** (Dynamic Structured Memory): 增量构建 OWL 合规知识图谱，维护对话一致性
- **建设性记忆观** (Constructivist Memory View): 结构化图式 + 灵活同化 + 动态顺应

### 工具使用与学习
- **工具能力记忆** (Tool Capability Memory): 从过去交互中学习工具优缺点，结构化存储
- **群相对语义优势** (Group Relative Semantic Advantage): 替代数值优势，迭代蒸馏经验知识
- **重正化群启发记忆** (Renormalization Group-Inspired Memory): 层次化粗粒化 + 阈值更新 + 重缩放
- **三阶段人脑记忆** (Three-Stage Human Memory): 感官记忆 + 主题感知 STM + 睡眠时 LTM 更新
- **早期经验学习** (Early Experience Learning): 智能体自身行动生成的交互数据，未来状态作为监督信号

### 小模型增强
- **无训练策略优化** (Training-Free Policy Optimization): 无需参数更新，语义优势替代数值优势
- **梯度无关压缩** (Gradient-Free Compression): 无需参数更新，直接适用于 API 模型
- **令牌先验** (Token Prior): 经验知识作为令牌先验，推理时集成指导模型行为

---

### 新增概念 (自动提取)
- **Hyper-network Weight Generator**: 待完善描述 `[Source: 待补充]`
- **Transformer Model Parameters**: 待完善描述 `[Source: 待补充]`
- **Editable Knowledge State**: 待完善描述 `[Source: 待补充]`
- **Local Weight Update**: 待完善描述 `[Source: 待补充]`
- **Perturbation Vector (Δθ)**: 待完善描述 `[Source: 待补充]`
- **Parametric Factual Knowledge**: 待完善描述 `[Source: 待补充]`
- **Constraint-based Editing**: 待完善描述 `[Source: 待补充]`
- **Hyper-network Parameters**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Parametric Factual Knowledge**: 待完善描述 `[Source: 待补充]`
- **Editable Knowledge State**: 待完善描述 `[Source: 待补充]`
- **Hyper-network Weight Generator**: 待完善描述 `[Source: 待补充]`
- **Perturbation Vector (Δθ)**: 待完善描述 `[Source: 待补充]`
- **Constraint-based Editing**: 待完善描述 `[Source: 待补充]`
- **Local Weight Update**: 待完善描述 `[Source: 待补充]`
- **Transformer Model Parameters**: 待完善描述 `[Source: 待补充]`
- **Hyper-network Parameters**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **感官记忆 (Sensory Memory)**: 待完善描述 `[Source: 待补充]`
- **工作记忆 (Working Memory)**: 待完善描述 `[Source: 待补充]`
- **长期记忆 (Long-term Memory)**: 待完善描述 `[Source: 待补充]`
- **GRU 隐藏状态**: 待完善描述 `[Source: 待补充]`
- **高分辨率键值对 (Key/Value)**: 待完善描述 `[Source: 待补充]`
- **记忆原型 (Prototypes)**: 待完善描述 `[Source: 待补充]`
- **记忆巩固 (Consolidation)**: 待完善描述 `[Source: 待补充]`
- **记忆增强 (Potentiation)**: 待完善描述 `[Source: 待补充]`
- **各向异性读取 (Anisotropic Reading)**: 待完善描述 `[Source: 待补充]`
- **LFU 淘汰 (LFU Eviction)**: 待完善描述 `[Source: 待补充]`
- **视频帧特征图**: 待完善描述 `[Source: 待补充]`
- **显存缓冲区**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **External Tool Knowledge**: 待完善描述 `[Source: 待补充]`
- **Self-Supervised Tool Decision State**: 待完善描述 `[Source: 待补充]`
- **API-Embedded Text Sequence**: 待完善描述 `[Source: 待补充]`
- **Tool-Augmented Context Window**: 待完善描述 `[Source: 待补充]`
- **Autonomous API Invocation**: 待完善描述 `[Source: 待补充]`
- **Result Injection & Continuation**: 待完善描述 `[Source: 待补充]`
- **Tool Usage Filtering**: 待完善描述 `[Source: 待补充]`
- **Special API Tokens (<API>)**: 待完善描述 `[Source: 待补充]`
- **External API Endpoints**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **情景记忆 (Episodic Memory)**: 待完善描述 `[Source: 待补充]`
- **言语强化记忆 (Verbal Reinforcement Memory)**: 待完善描述 `[Source: 待补充]`
- **滑动窗口上下文 (Sliding Window Context)**: 待完善描述 `[Source: 待补充]`
- **自我提示库 (Self-Hint Repository)**: 待完善描述 `[Source: 待补充]`
- **反思生成 (Reflection Generation)**: 待完善描述 `[Source: 待补充]`
- **轨迹存储 (Trajectory Storage)**: 待完善描述 `[Source: 待补充]`
- **提示检索 (Hint Retrieval)**: 待完善描述 `[Source: 待补充]`
- **自然语言文本 (Natural Language Text)**: 待完善描述 `[Source: 待补充]`
- **任务试错轨迹 (Task Trial Trajectories)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Observation Memory**: 待完善描述 `[Source: 待补充]`
- **Reflection Memory**: 待完善描述 `[Source: 待补充]`
- **Memory Stream**: 待完善描述 `[Source: 待补充]`
- **Relevance Retrieval**: 待完善描述 `[Source: 待补充]`
- **Reflective Synthesis**: 待完善描述 `[Source: 待补充]`
- **Importance Scoring**: 待完善描述 `[Source: 待补充]`
- **Natural Language Text**: 待完善描述 `[Source: 待补充]`
- **Vector Embeddings**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **医疗指令数据 (Medical Instruction Data)**: 待完善描述 `[Source: 待补充]`
- **知识图谱实例 (Knowledge Graph Instances)**: 待完善描述 `[Source: 待补充]`
- **SUS 评估体系 (Safety-Usability-Smoothness Framework)**: 待完善描述 `[Source: 待补充]`
- **问答对结构 (QA Pairs Structure)**: 待完善描述 `[Source: 待补充]`
- **知识采样 (Knowledge Sampling)**: 待完善描述 `[Source: 待补充]`
- **指令微调 (Instruction Tuning)**: 待完善描述 `[Source: 待补充]`
- **API 生成清洗 (API Generation & Cleaning)**: 待完善描述 `[Source: 待补充]`
- **LLaMA-7B 模型权重 (LLaMA-7B Weights)**: 待完善描述 `[Source: 待补充]`
- **中国医学知识图谱 (CMeKG)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Self-Controlled Memory**: 待完善描述 `[Source: 待补充]`
- **Long-term Memory**: 待完善描述 `[Source: 待补充]`
- **Memory Stream**: 待完善描述 `[Source: 待补充]`
- **Memory Update**: 待完善描述 `[Source: 待补充]`
- **Memory Retrieval**: 待完善描述 `[Source: 待补充]`
- **Memory Control Decision**: 待完善描述 `[Source: 待补充]`
- **Text Sequences**: 待完善描述 `[Source: 待补充]`
- **Dialogue/Document Records**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Raw Dialogue Memory**: 待完善描述 `[Source: 待补充]`
- **Summarized Memory (Daily/Global)**: 待完善描述 `[Source: 待补充]`
- **User Profile Memory**: 待完善描述 `[Source: 待补充]`
- **Hierarchical Memory Storage**: 待完善描述 `[Source: 待补充]`
- **Vector Index (FAISS)**: 待完善描述 `[Source: 待补充]`
- **Memory Strength Parameter**: 待完善描述 `[Source: 待补充]`
- **Memory Consolidation (Summarization)**: 待完善描述 `[Source: 待补充]`
- **Memory Decay (Forgetting)**: 待完善描述 `[Source: 待补充]`
- **Memory Reinforcement (Retrieval)**: 待完善描述 `[Source: 待补充]`
- **Text Embeddings**: 待完善描述 `[Source: 待补充]`
- **Dialogue Logs**: 待完善描述 `[Source: 待补充]`
- **Profile Tags**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Long-term Memory**: 待完善描述 `[Source: 待补充]`
- **Short-term Memory**: 待完善描述 `[Source: 待补充]`
- **Vector Database Storage**: 待完善描述 `[Source: 待补充]`
- **Natural Language Summary Buffer**: 待完善描述 `[Source: 待补充]`
- **Semantic Retrieval**: 待完善描述 `[Source: 待补充]`
- **State Summarization**: 待完善描述 `[Source: 待补充]`
- **Plan Generation**: 待完善描述 `[Source: 待补充]`
- **Natural Language Text**: 待完善描述 `[Source: 待补充]`
- **Vector Embeddings**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **通用读写记忆 (General Read-Write Memory)**: 待完善描述 `[Source: 待补充]`
- **外部记忆模块 (External Memory Module)**: 待完善描述 `[Source: 待补充]`
- **知识三元组 (Knowledge Triplets ⟨参数 1, 关系，参数 2⟩)**: 待完善描述 `[Source: 待补充]`
- **LSH 向量索引表 (LSH Vector Index Table)**: 待完善描述 `[Source: 待补充]`
- **MEM_WRITE (记忆写入)**: 待完善描述 `[Source: 待补充]`
- **MEM_READ (记忆读取)**: 待完善描述 `[Source: 待补充]`
- **API 调用拦截 (API Call Interception)**: 待完善描述 `[Source: 待补充]`
- **结构化文本三元组 (Structured Text Triplets)**: 待完善描述 `[Source: 待补充]`
- **平均向量表示 (Average Vector Representation)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **记忆槽 (Memory Slots)**: 待完善描述 `[Source: 待补充]`
- **压缩上下文表示 (Compressed Context Representation)**: 待完善描述 `[Source: 待补充]`
- **固定长度连续向量 (Fixed-length Continuous Vectors)**: 待完善描述 `[Source: 待补充]`
- **可学习令牌序列 (Learnable Token Sequence)**: 待完善描述 `[Source: 待补充]`
- **上下文编码压缩 (Context Encoding/Compression)**: 待完善描述 `[Source: 待补充]`
- **记忆槽缓存复用 (Memory Slot Caching/Reuse)**: 待完善描述 `[Source: 待补充]`
- **基于记忆的解码生成 (Memory-based Decoding)**: 待完善描述 `[Source: 待补充]`
- **LLM 嵌入空间向量 (LLM Embedding Space Vectors)**: 待完善描述 `[Source: 待补充]`
- **LoRA 适配器参数 (LoRA Adapter Parameters)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **工具指令记忆 (Tool Instruction Memory)**: 待完善描述 `[Source: 待补充]`
- **API 语义记忆 (API Semantic Memory)**: 待完善描述 `[Source: 待补充]`
- **执行轨迹记忆 (Execution Trace Memory)**: 待完善描述 `[Source: 待补充]`
- **深度优先搜索决策树 (DFSDT)**: 待完善描述 `[Source: 待补充]`
- **神经 API 检索索引 (Neural API Retrieval Index)**: 待完善描述 `[Source: 待补充]`
- **解决方案路径 (Solution Path)**: 待完善描述 `[Source: 待补充]`
- **API 调用 (API Invocation)**: 待完善描述 `[Source: 待补充]`
- **决策树搜索 (Decision Tree Search)**: 待完善描述 `[Source: 待补充]`
- **语义检索 (Semantic Retrieval)**: 待完善描述 `[Source: 待补充]`
- **自动化标注 (Automated Annotation)**: 待完善描述 `[Source: 待补充]`
- **ToolLLaMA 模型参数 (ToolLLaMA Model Parameters)**: 待完善描述 `[Source: 待补充]`
- **外部 API 服务器 (External API Servers)**: 待完善描述 `[Source: 待补充]`
- **ToolBench 数据集 (ToolBench Dataset)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **SOP-Encoded Knowledge**: 待完善描述 `[Source: 待补充]`
- **Role-Specific Context**: 待完善描述 `[Source: 待补充]`
- **Prompt Sequences**: 待完善描述 `[Source: 待补充]`
- **Structured Artifacts (PRD, Code)**: 待完善描述 `[Source: 待补充]`
- **SOP Encoding**: 待完善描述 `[Source: 待补充]`
- **Intermediate Validation**: 待完善描述 `[Source: 待补充]`
- **Feedback Correction**: 待完善描述 `[Source: 待补充]`
- **LLM Token Context**: 待完善描述 `[Source: 待补充]`
- **Shared Environment State**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Short-term Trajectory Memory**: 待完善描述 `[Source: 待补充]`
- **Long-term Reflection Memory**: 待完善描述 `[Source: 待补充]`
- **Replay Buffer for Offline RL**: 待完善描述 `[Source: 待补充]`
- **Prompt Context Window**: 待完善描述 `[Source: 待补充]`
- **Trajectory Analysis**: 待完善描述 `[Source: 待补充]`
- **Reflection Generation**: 待完善描述 `[Source: 待补充]`
- **Policy Gradient Update**: 待完善描述 `[Source: 待补充]`
- **Text Prompts**: 待完善描述 `[Source: 待补充]`
- **Environment Reward Signals**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **自用备忘录 (Self-use Memos)**: 待完善描述 `[Source: 待补充]`
- **结构化事实备忘录 (Structured Fact Memos)**: 待完善描述 `[Source: 待补充]`
- **备忘录存储 (Memo Store)**: 待完善描述 `[Source: 待补充]`
- **三阶段记忆循环 (Three-Stage Memory Loop)**: 待完善描述 `[Source: 待补充]`
- **备忘录撰写 (Memo Writing)**: 待完善描述 `[Source: 待补充]`
- **备忘录检索 (Memo Retrieval)**: 待完善描述 `[Source: 待补充]`
- **基于备忘录的响应生成 (Memo-Augmented Response)**: 待完善描述 `[Source: 待补充]`
- **指令微调后的 LLM 参数 (Instruction-Tuned LLM Parameters)**: 待完善描述 `[Source: 待补充]`
- **文本备忘录字符串 (Textual Memo Strings)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Static Character Profile Memory**: 待完善描述 `[Source: 待补充]`
- **Retrievable Script Memory**: 待完善描述 `[Source: 待补充]`
- **Dynamic Dialogue History Memory**: 待完善描述 `[Source: 待补充]`
- **Vector Space Index**: 待完善描述 `[Source: 待补充]`
- **Token Sequence Context**: 待完善描述 `[Source: 待补充]`
- **Fine-tuned Parameter Space**: 待完善描述 `[Source: 待补充]`
- **Semantic Embedding Retrieval**: 待完善描述 `[Source: 待补充]`
- **Instruction-based Prompting**: 待完善描述 `[Source: 待补充]`
- **Supervised Weight Updating**: 待完善描述 `[Source: 待补充]`
- **External Vector Database**: 待完善描述 `[Source: 待补充]`
- **Internal Model Weights**: 待完善描述 `[Source: 待补充]`
- **Context Window Tokens**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Recursive Summary Memory**: 待完善描述 `[Source: 待补充]`
- **Generated Dialogue Memory**: 待完善描述 `[Source: 待补充]`
- **Compressed Textual Summary**: 待完善描述 `[Source: 待补充]`
- **Session-based Memory State**: 待完善描述 `[Source: 待补充]`
- **Recursive Memory Update**: 待完善描述 `[Source: 待补充]`
- **In-Context Memory Integration**: 待完善描述 `[Source: 待补充]`
- **LLM Context Window**: 待完善描述 `[Source: 待补充]`
- **Prompt Text**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Summarized Memory**: 待完善描述 `[Source: 待补充]`
- **Experience Stream**: 待完善描述 `[Source: 待补充]`
- **Key Memory**: 待完善描述 `[Source: 待补充]`
- **Memory Stream**: 待完善描述 `[Source: 待补充]`
- **Option-Action Hierarchy**: 待完善描述 `[Source: 待补充]`
- **Summarize-and-Forget**: 待完善描述 `[Source: 待补充]`
- **Asynchronous Self-Monitoring**: 待完善描述 `[Source: 待补充]`
- **Retrieval**: 待完善描述 `[Source: 待补充]`
- **LyfeGame 3D Environment**: 待完善描述 `[Source: 待补充]`
- **Text Memory Stream**: 待完善描述 `[Source: 待补充]`
- **Behavior Logs**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Working Memory (WM)**: 待完善描述 `[Source: 待补充]`
- **Short-Term Memory (STM)**: 待完善描述 `[Source: 待补充]`
- **Long-Term Memory (LTM)**: 待完善描述 `[Source: 待补充]`
- **Engram**: 待完善描述 `[Source: 待补充]`
- **Directed Weighted Graph**: 待完善描述 `[Source: 待补充]`
- **Queue Structure**: 待完善描述 `[Source: 待补充]`
- **Lifecycle Management**: 待完善描述 `[Source: 待补充]`
- **DFS Retrieval**: 待完善描述 `[Source: 待补充]`
- **Hebbian Strengthening**: 待完善描述 `[Source: 待补充]`
- **Engram Unit**: 待完善描述 `[Source: 待补充]`
- **Token/Character Sequence**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Virtual Context (Main Context)**: 待完善描述 `[Source: 待补充]`
- **External Memory (Archival/Recall Storage)**: 待完善描述 `[Source: 待补充]`
- **Hierarchical Memory System**: 待完善描述 `[Source: 待补充]`
- **FIFO Message Queue**: 待完善描述 `[Source: 待补充]`
- **Vector Index**: 待完善描述 `[Source: 待补充]`
- **Context Paging**: 待完善描述 `[Source: 待补充]`
- **Memory Eviction**: 待完善描述 `[Source: 待补充]`
- **Autonomous Retrieval**: 待完善描述 `[Source: 待补充]`
- **Function Calling**: 待完善描述 `[Source: 待补充]`
- **Text Tokens**: 待完善描述 `[Source: 待补充]`
- **Vector Embeddings**: 待完善描述 `[Source: 待补充]`
- **System Logs**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Repair State Memory**: 待完善描述 `[Source: 待补充]`
- **Tool Feedback Memory**: 待完善描述 `[Source: 待补充]`
- **Code Context Memory**: 待完善描述 `[Source: 待补充]`
- **Finite State Machine (FSM) Flow**: 待完善描述 `[Source: 待补充]`
- **Dynamic Prompt Context Buffer**: 待完善描述 `[Source: 待补充]`
- **State Transition**: 待完善描述 `[Source: 待补充]`
- **Tool Invocation**: 待完善描述 `[Source: 待补充]`
- **Context Update**: 待完善描述 `[Source: 待补充]`
- **LLM Context Window**: 待完善描述 `[Source: 待补充]`
- **Execution Logs**: 待完善描述 `[Source: 待补充]`
- **Source Code Repository**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Domain-specific Memory Pool**: 待完善描述 `[Source: 待补充]`
- **Global Memory Pool**: 待完善描述 `[Source: 待补充]`
- **Candidate Memory**: 待完善描述 `[Source: 待补充]`
- **(Prompt, Answer) Pair**: 待完善描述 `[Source: 待补充]`
- **Enhanced Prompt with Retrieved Context**: 待完善描述 `[Source: 待补充]`
- **Retriever Continuous Training**: 待完善描述 `[Source: 待补充]`
- **Memory Scoring and Filtering**: 待完善描述 `[Source: 待补充]`
- **Memory Sharing**: 待完善描述 `[Source: 待补充]`
- **Shared Vector Database**: 待完善描述 `[Source: 待补充]`
- **Rubric-based Scoring System**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Global Semantic Memory (Community Summaries)**: 待完善描述 `[Source: 待补充]`
- **Local Episodic Memory (Text Chunks)**: 待完善描述 `[Source: 待补充]`
- **Self-Generated Graph Index**: 待完善描述 `[Source: 待补充]`
- **Hierarchical Community Tree**: 待完善描述 `[Source: 待补充]`
- **LLM-driven Entity-Relation Extraction**: 待完善描述 `[Source: 待补充]`
- **Leiden Community Detection**: 待完善描述 `[Source: 待补充]`
- **Map-Reduce Answer Generation**: 待完善描述 `[Source: 待补充]`
- **Graph Nodes (Entities)**: 待完善描述 `[Source: 待补充]`
- **Community Reports (Text Summaries)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **神经生物学启发的长期记忆**: 待完善描述 `[Source: 待补充]`
- **海马体索引记忆**: 待完善描述 `[Source: 待补充]`
- **知识图谱记忆结构**: 待完善描述 `[Source: 待补充]`
- **新皮层式存储**: 待完善描述 `[Source: 待补充]`
- **海马体式索引**: 待完善描述 `[Source: 待补充]`
- **离线索引构建**: 待完善描述 `[Source: 待补充]`
- **个性化 PageRank 检索**: 待完善描述 `[Source: 待补充]`
- **跨段落知识整合**: 待完善描述 `[Source: 待补充]`
- **文本段落**: 待完善描述 `[Source: 待补充]`
- **图谱节点与边**: 待完善描述 `[Source: 待补充]`
- **LLM 上下文窗口**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Completeness-Oriented Tool Memory**: 待完善描述 `[Source: 待补充]`
- **Semantic-Graph Hybrid Memory**: 待完善描述 `[Source: 待补充]`
- **Dual-view Bipartite Graph**: 待完善描述 `[Source: 待补充]`
- **Query-Scene-Tool Interaction Graph**: 待完善描述 `[Source: 待补充]`
- **Collaborative Graph Learning**: 待完善描述 `[Source: 待补充]`
- **Semantic-Graph Fusion Retrieval**: 待完善描述 `[Source: 待补充]`
- **PLM Embeddings**: 待完善描述 `[Source: 待补充]`
- **Graph Neural Network Nodes**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **个性化事实知识 (Personalized Factual Knowledge)**: 待完善描述 `[Source: 待补充]`
- **用户交互反馈记忆 (User Interaction Feedback Memory)**: 待完善描述 `[Source: 待补充]`
- **外部知识图谱 (External Knowledge Graph)**: 待完善描述 `[Source: 待补充]`
- **事实知识三元组 (Factual Knowledge Triples)**: 待完善描述 `[Source: 待补充]`
- **基于反馈的知识提取 (Knowledge Extraction from Feedback)**: 待完善描述 `[Source: 待补充]`
- **无反向传播图谱优化 (Graph Optimization without Back-propagation)**: 待完善描述 `[Source: 待补充]`
- **检索增强推理 (Retrieval-Augmented Inference)**: 待完善描述 `[Source: 待补充]`
- **外部图数据库 (External Graph Database)**: 待完善描述 `[Source: 待补充]`
- **LLM 上下文窗口 (LLM Context Window)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **时间敏感长期记忆 (Time-Sensitive Long-term Memory)**: 待完善描述 `[Source: 待补充]`
- **上下文敏感记忆 (Context-Sensitive Memory)**: 待完善描述 `[Source: 待补充]`
- **结构化对话日志表 (Structured Conversation Log Table)**: 待完善描述 `[Source: 待补充]`
- **混合记忆架构 (Hybrid Memory Architecture)**: 待完善描述 `[Source: 待补充]`
- **链式表过滤 (Chain-of-Tables Filtering)**: 待完善描述 `[Source: 待补充]`
- **查询分类路由 (Query Classification Routing)**: 待完善描述 `[Source: 待补充]`
- **向量数据库 (Vector Database)**: 待完善描述 `[Source: 待补充]`
- **结构化表格 (Structured Table)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Long-Term Dialogue Memory**: 待完善描述 `[Source: 待补充]`
- **Hierarchical Aggregated Memory**: 待完善描述 `[Source: 待补充]`
- **Hierarchical Aggregate Tree (HAT)**: 待完善描述 `[Source: 待补充]`
- **Summary-Leaf Node Structure**: 待完善描述 `[Source: 待补充]`
- **Recursive Summary Aggregation**: 待完善描述 `[Source: 待补充]`
- **Conditioned Tree Traversal**: 待完善描述 `[Source: 待补充]`
- **Dynamic Node Update**: 待完善描述 `[Source: 待补充]`
- **LLM Context Window**: 待完善描述 `[Source: 待补充]`
- **Textual Tree Nodes**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Timeline Memory**: 待完善描述 `[Source: 待补充]`
- **Episodic Memory Graph**: 待完善描述 `[Source: 待补充]`
- **Causal-Temporal Graph**: 待完善描述 `[Source: 待补充]`
- **Linearized Event Timeline**: 待完善描述 `[Source: 待补充]`
- **Relation-aware Linking**: 待完善描述 `[Source: 待补充]`
- **Untangle Retrieval**: 待完善描述 `[Source: 待补充]`
- **Context-aware Refinement**: 待完善描述 `[Source: 待补充]`
- **Graph Nodes (Memory Snippets)**: 待完善描述 `[Source: 待补充]`
- **Text Embedding Vectors**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **短期记忆 (Short-term Memory)**: 待完善描述 `[Source: 待补充]`
- **中期记忆 (Medium-term Memory)**: 待完善描述 `[Source: 待补充]`
- **长期记忆 (Long-term Memory)**: 待完善描述 `[Source: 待补充]`
- **记忆存储池 (Memory Storage Pool)**: 待完善描述 `[Source: 待补充]`
- **记忆编码器 (Memory Encoder)**: 待完善描述 `[Source: 待补充]`
- **记忆检索器 (Memory Retriever)**: 待完善描述 `[Source: 待补充]`
- **记忆解码器 (Memory Decoder)**: 待完善描述 `[Source: 待补充]`
- **记忆 - 注意力融合模块 (Memory-Attention Fusion Module)**: 待完善描述 `[Source: 待补充]`
- **记忆编码与压缩 (Memory Encoding & Compression)**: 待完善描述 `[Source: 待补充]`
- **基于内容的记忆检索 (Content-based Memory Retrieval)**: 待完善描述 `[Source: 待补充]`
- **记忆更新策略 (Memory Update Strategy)**: 待完善描述 `[Source: 待补充]`
- **记忆淘汰机制 (Memory Elimination Mechanism)**: 待完善描述 `[Source: 待补充]`
- **可微分记忆读写 (Differentiable Memory Read/Write)**: 待完善描述 `[Source: 待补充]`
- **文本序列 (Text Sequence)**: 待完善描述 `[Source: 待补充]`
- **记忆向量表示 (Memory Vector Representation)**: 待完善描述 `[Source: 待补充]`
- **可寻址向量数据库 (Addressable Vector Database)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Episodic Memory**: 待完善描述 `[Source: 待补充]`
- **Semantic Memory**: 待完善描述 `[Source: 待补充]`
- **Knowledge Graph World Model**: 待完善描述 `[Source: 待补充]`
- **Entity-Relation-Entity Triple**: 待完善描述 `[Source: 待补充]`
- **Triple Extraction**: 待完善描述 `[Source: 待补充]`
- **Graph Update & Fusion**: 待完善描述 `[Source: 待补充]`
- **Subgraph Retrieval**: 待完善描述 `[Source: 待补充]`
- **Text Interaction Logs**: 待完善描述 `[Source: 待补充]`
- **Natural Language Instructions**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **工作记忆 (Working Memory)**: 待完善描述 `[Source: 待补充]`
- **程序记忆 (Procedural Memory)**: 待完善描述 `[Source: 待补充]`
- **情景记忆 (Episodic Memory)**: 待完善描述 `[Source: 待补充]`
- **概念化投资信念 (Conceptual Investment Beliefs)**: 待完善描述 `[Source: 待补充]`
- **层级化记忆管理 (Hierarchical Memory Management)**: 待完善描述 `[Source: 待补充]`
- **基于 Prompt 的策略存储 (Prompt-based Strategy Storage)**: 待完善描述 `[Source: 待补充]`
- **基于相关性的检索 (Relevance-based Retrieval)**: 待完善描述 `[Source: 待补充]`
- **言语强化 Prompt 更新 (Prompt Update via Verbal Reinforcement)**: 待完善描述 `[Source: 待补充]`
- **时间衰减 (Time-based Decay)**: 待完善描述 `[Source: 待补充]`
- **风险触发式自我反思 (Risk-triggered Self-Reflection)**: 待完善描述 `[Source: 待补充]`
- **文本 Prompt**: 待完善描述 `[Source: 待补充]`
- **多模态金融数据 (文本/音频/表格)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **主动记忆 (Active Memory)**: 待完善描述 `[Source: 待补充]`
- **被动记忆 (Passive Memory)**: 待完善描述 `[Source: 待补充]`
- **记忆类型 (Memory Type)**: 待完善描述 `[Source: 待补充]`
- **记忆子类 (Memory Subclass)**: 待完善描述 `[Source: 待补充]`
- **可编辑记忆图 (Editable Memory Graph, EMG)**: 待完善描述 `[Source: 待补充]`
- **三层分层图谱结构 (MTL/MSL/MGL)**: 待完善描述 `[Source: 待补充]`
- **记忆图层 (Memory Graph Layer, MGL)**: 待完善描述 `[Source: 待补充]`
- **插入 (Insertion)**: 待完善描述 `[Source: 待补充]`
- **删除 (Deletion)**: 待完善描述 `[Source: 待补充]`
- **替换 (Replacement)**: 待完善描述 `[Source: 待补充]`
- **强化学习路径选择 (RL-guided Path Selection)**: 待完善描述 `[Source: 待补充]`
- **结构化图谱节点 (实体/关系)**: 待完善描述 `[Source: 待补充]`
- **非结构化文本记忆**: 待完善描述 `[Source: 待补充]`
- **本地手机端存储**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Parameterized Fact Memory**: 待完善描述 `[Source: 待补充]`
- **Implicit Semantic Memory**: 待完善描述 `[Source: 待补充]`
- **Null-Space Basis**: 待完善描述 `[Source: 待补充]`
- **Orthogonal Projection Matrix**: 待完善描述 `[Source: 待补充]`
- **Null-Space Constrained Editing**: 待完善描述 `[Source: 待补充]`
- **Orthogonal Projection Update**: 待完善描述 `[Source: 待补充]`
- **MLP Weight Matrices**: 待完善描述 `[Source: 待补充]`
- **Hidden State Activations**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **参数化记忆 (Parametric Memory)**: 待完善描述 `[Source: 待补充]`
- **生成式检索记忆 (Generative Retrieval Memory)**: 待完善描述 `[Source: 待补充]`
- **虚拟令牌词表 (Virtual Token Vocabulary)**: 待完善描述 `[Source: 待补充]`
- **原子索引映射 (Atomic Index Mapping)**: 待完善描述 `[Source: 待补充]`
- **工具记忆化 (Tool Memorization)**: 待完善描述 `[Source: 待补充]`
- **约束生成 (Constrained Generation)**: 待完善描述 `[Source: 待补充]`
- **大模型参数 (LLM Parameters)**: 待完善描述 `[Source: 待补充]`
- **扩展特殊令牌 (Extended Special Tokens)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Short-term Operation History**: 待完善描述 `[Source: 待补充]`
- **Long-term Task Goal Storage**: 待完善描述 `[Source: 待补充]`
- **Context State (Vision + Plan)**: 待完善描述 `[Source: 待补充]`
- **Normalized Action Space (0-1000 Coordinates)**: 待完善描述 `[Source: 待补充]`
- **Context Summarization/Compression**: 待完善描述 `[Source: 待补充]`
- **Abstract-to-OS Action Mapping**: 待完善描述 `[Source: 待补充]`
- **Screen Screenshots**: 待完善描述 `[Source: 待补充]`
- **Operation Logs**: 待完善描述 `[Source: 待补充]`
- **Natural Language Instructions**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Static Human-Centric Documentation**: 待完善描述 `[Source: 待补充]`
- **Dynamic LLM-Adapted Documentation**: 待完善描述 `[Source: 待补充]`
- **Interaction Experience Memory**: 待完善描述 `[Source: 待补充]`
- **Feedback-Integrated Documentation**: 待完善描述 `[Source: 待补充]`
- **Trial-and-Error Execution Logs**: 待完善描述 `[Source: 待补充]`
- **Diversity-Promoting Exploration**: 待完善描述 `[Source: 待补充]`
- **Feedback-Driven Analysis**: 待完善描述 `[Source: 待补充]`
- **Iterative Documentation Rewriting**: 待完善描述 `[Source: 待补充]`
- **API Documentation Text**: 待完善描述 `[Source: 待补充]`
- **Interaction Feedback Signals**: 待完善描述 `[Source: 待补充]`
- **Natural Language Context**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Short-Term Memory (STM)**: 待完善描述 `[Source: 待补充]`
- **Surprising Information Memory**: 待完善描述 `[Source: 待补充]`
- **Summary Tree**: 待完善描述 `[Source: 待补充]`
- **STM Storage Area**: 待完善描述 `[Source: 待补充]`
- **Inner Loop Query**: 待完善描述 `[Source: 待补充]`
- **Dynamic Query Generation**: 待完善描述 `[Source: 待补充]`
- **Convergence Judgment**: 待完善描述 `[Source: 待补充]`
- **STM Update**: 待完善描述 `[Source: 待补充]`
- **Text Chunks**: 待完善描述 `[Source: 待补充]`
- **Vector Embeddings**: 待完善描述 `[Source: 待补充]`
- **Summary Nodes**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Dynamic Tree Memory**: 待完善描述 `[Source: 待补充]`
- **Hierarchical Schema Memory**: 待完善描述 `[Source: 待补充]`
- **Online Incremental Memory**: 待完善描述 `[Source: 待补充]`
- **MemTree**: 待完善描述 `[Source: 待补充]`
- **Depth-Adaptive Threshold Node**: 待完善描述 `[Source: 待补充]`
- **Folded Tree Node Set**: 待完善描述 `[Source: 待补充]`
- **Online Top-Down Clustering Insertion**: 待完善描述 `[Source: 待补充]`
- **Parent Node Aggregation Update**: 待完善描述 `[Source: 待补充]`
- **Folded Tree Retrieval**: 待完善描述 `[Source: 待补充]`
- **Semantic Embedding Vectors**: 待完善描述 `[Source: 待补充]`
- **Text Conversation Streams**: 待完善描述 `[Source: 待补充]`
- **LLM Generated Summaries**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Individual Agent Context Memory**: 待完善描述 `[Source: 待补充]`
- **Global Environment State Memory**: 待完善描述 `[Source: 待补充]`
- **Dynamic Social Network Graph**: 待完善描述 `[Source: 待补充]`
- **Post Information Flow Stream**: 待完善描述 `[Source: 待补充]`
- **Perceive (Filter Content)**: 待完善描述 `[Source: 待补充]`
- **Execute (21 Action Types)**: 待完善描述 `[Source: 待补充]`
- **Update (State/Network)**: 待完善描述 `[Source: 待补充]`
- **LLM Token Context Window**: 待完善描述 `[Source: 待补充]`
- **Agent Interaction Logs**: 待完善描述 `[Source: 待补充]`
- **Simulated Platform Database**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Visually-aligned Auxiliary Text Memory**: 待完善描述 `[Source: 待补充]`
- **Modality-specific Semantic Memory (OCR/ASR/DET)**: 待完善描述 `[Source: 待补充]`
- **FAISS Vector Index for Video Semantics**: 待完善描述 `[Source: 待补充]`
- **Decoupled Query Representation**: 待完善描述 `[Source: 待补充]`
- **Query Decoupling**: 待完善描述 `[Source: 待补充]`
- **Semantic Retrieval**: 待完善描述 `[Source: 待补充]`
- **Context Integration**: 待完善描述 `[Source: 待补充]`
- **Extracted Text Chunks**: 待完善描述 `[Source: 待补充]`
- **Vector Embeddings**: 待完善描述 `[Source: 待补充]`
- **Video Frames**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Episodic Memory**: 待完善描述 `[Source: 待补充]`
- **Episodic Simulation**: 待完善描述 `[Source: 待补充]`
- **Real Memory**: 待完善描述 `[Source: 待补充]`
- **Imagined Memory**: 待完善描述 `[Source: 待补充]`
- **Hybrid Memory Map**: 待完善描述 `[Source: 待补充]`
- **Topological Map**: 待完善描述 `[Source: 待补充]`
- **Imagination Tree**: 待完善描述 `[Source: 待补充]`
- **Memory Pruning**: 待完善描述 `[Source: 待补充]`
- **Recursive Imagination**: 待完善描述 `[Source: 待补充]`
- **Dynamic Weight Fusion**: 待完善描述 `[Source: 待补充]`
- **Topological Map Nodes**: 待完善描述 `[Source: 待补充]`
- **RGB-D Features**: 待完善描述 `[Source: 待补充]`
- **Semantic Features**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Life-long Interaction Memory**: 待完善描述 `[Source: 待补充]`
- **Dynamic User Persona**: 待完善描述 `[Source: 待补充]`
- **Session History Memory**: 待完善描述 `[Source: 待补充]`
- **Learnable Persona Dictionary**: 待完善描述 `[Source: 待补充]`
- **Historical Session Buffer**: 待完善描述 `[Source: 待补充]`
- **Inference-based Persona Update**: 待完善描述 `[Source: 待补充]`
- **Context-aware Persona Retrieval**: 待完善描述 `[Source: 待补充]`
- **Session Lifecycle Management**: 待完善描述 `[Source: 待补充]`
- **External Persona Database (Key-Value)**: 待完善描述 `[Source: 待补充]`
- **LLM Prompt Context Window**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **持久场景记忆 (Persistent Scene Memory)**: 待完善描述 `[Source: 待补充]`
- **多模态具身记忆 (Multimodal Embodied Memory)**: 待完善描述 `[Source: 待补充]`
- **融合视频与传感器的记忆库 (Video-Sensor Fused Memory Bank)**: 待完善描述 `[Source: 待补充]`
- **VLM 触发式记忆更新 (VLM-Triggered Memory Update)**: 待完善描述 `[Source: 待补充]`
- **工具辅助记忆查询 (Tool-Assisted Memory Query)**: 待完善描述 `[Source: 待补充]`
- **第一人称视频流 (Egocentric Video Streams)**: 待完善描述 `[Source: 待补充]`
- **具身传感器数据 (深度/姿态) (Embodied Sensor Data: Depth/Pose)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **神经长期记忆 (Neural Long-Term Memory)**: 待完善描述 `[Source: 待补充]`
- **短期注意力记忆 (Short-Term Attention Memory)**: 待完善描述 `[Source: 待补充]`
- **持久记忆 (Persistent Memory)**: 待完善描述 `[Source: 待补充]`
- **Titans 架构变体 (MAC/MAG/MAL)**: 待完善描述 `[Source: 待补充]`
- **测试时可更新权重矩阵 (Test-Time Updatable Weight Matrix)**: 待完善描述 `[Source: 待补充]`
- **测试时梯度下降更新 (Test-Time Gradient Descent)**: 待完善描述 `[Source: 待补充]`
- **权重衰减遗忘机制 (Weight Decay Forgetting)**: 待完善描述 `[Source: 待补充]`
- **惊喜度驱动编码 (Surprise-Driven Encoding)**: 待完善描述 `[Source: 待补充]`
- **Token 嵌入序列 (Token Embedding Sequences)**: 待完善描述 `[Source: 待补充]`
- **可学习参数向量 (Learnable Parameter Vectors)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Long-term Agent Memory**: 待完善描述 `[Source: 待补充]`
- **Bi-temporal Memory**: 待完善描述 `[Source: 待补充]`
- **Temporal Knowledge Graph**: 待完善描述 `[Source: 待补充]`
- **Dynamic Community Structure**: 待完善描述 `[Source: 待补充]`
- **Temporal Invalidation**: 待完善描述 `[Source: 待补充]`
- **Hybrid Search & Rerank**: 待完善描述 `[Source: 待补充]`
- **Entity Resolution**: 待完善描述 `[Source: 待补充]`
- **Graphiti Engine**: 待完善描述 `[Source: 待补充]`
- **Episode Data Unit**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Short-Term Memory (STM)**: 待完善描述 `[Source: 待补充]`
- **Long-Term Memory (LTM)**: 待完善描述 `[Source: 待补充]`
- **Age-tagged Memory Pool**: 待完善描述 `[Source: 待补充]`
- **Latent Space Memory Vectors**: 待完善描述 `[Source: 待补充]`
- **Memory Migration (STM to LTM)**: 待完善描述 `[Source: 待补充]`
- **Co-trained Retrieval**: 待完善描述 `[Source: 待补充]`
- **Read/Write Separation (Multi-LoRA)**: 待完善描述 `[Source: 待补充]`
- **GPU VRAM**: 待完善描述 `[Source: 待补充]`
- **CPU RAM**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Hierarchical Memory (Local & Global)**: 待完善描述 `[Source: 待补充]`
- **Pre-trained Multimodal Knowledge**: 待完善描述 `[Source: 待补充]`
- **64x64 Time Series Image**: 待完善描述 `[Source: 待补充]`
- **Structured Text Prompt**: 待完善描述 `[Source: 待补充]`
- **Patch Embedding**: 待完善描述 `[Source: 待补充]`
- **Self-Augmentation Generation**: 待完善描述 `[Source: 待补充]`
- **Cross-Modal Attention Fusion**: 待完善描述 `[Source: 待补充]`
- **Gated Dynamic Weighting**: 待完善描述 `[Source: 待补充]`
- **Frozen VLM Encoder**: 待完善描述 `[Source: 待补充]`
- **Time Series Vector**: 待完善描述 `[Source: 待补充]`
- **Visual Embedding**: 待完善描述 `[Source: 待补充]`
- **Text Embedding**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Explicit Auxiliary Memory**: 待完善描述 `[Source: 待补充]`
- **Context Representation Memory**: 待完善描述 `[Source: 待补充]`
- **Independent Memory Bank**: 待完善描述 `[Source: 待补充]`
- **Gated Memory Unit**: 待完善描述 `[Source: 待补充]`
- **Cross-Attention Read**: 待完善描述 `[Source: 待补充]`
- **Gated Write/Update**: 待完善描述 `[Source: 待补充]`
- **Forget Operation**: 待完善描述 `[Source: 待补充]`
- **Memory Vectors**: 待完善描述 `[Source: 待补充]`
- **Token Representations**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **交互历史记忆 (Interaction History Memory)**: 待完善描述 `[Source: 待补充]`
- **敏感查询记忆 (Sensitive Query Memory)**: 待完善描述 `[Source: 待补充]`
- **检索增强记忆存储 (Retrieval-Augmented Memory Store)**: 待完善描述 `[Source: 待补充]`
- **基于编辑距离的索引 (Edit-Distance Based Index)**: 待完善描述 `[Source: 待补充]`
- **记忆提取攻击 (Memory Extraction Attack)**: 待完善描述 `[Source: 待补充]`
- **检索操纵 (Retrieval Manipulation)**: 待完善描述 `[Source: 待补充]`
- **LLM 上下文窗口 (LLM Context Window)**: 待完善描述 `[Source: 待补充]`
- **外部记忆数据库 (External Memory Database)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **全局记忆 (Global Memory)**: 待完善描述 `[Source: 待补充]`
- **自我中心记忆 (Ego-centric Memory)**: 待完善描述 `[Source: 待补充]`
- **全局到自我对齐记忆 (Global-to-Ego Aligned Memory)**: 待完善描述 `[Source: 待补充]`
- **语义/拓扑地图 (Semantic/Topological Map)**: 待完善描述 `[Source: 待补充]`
- **任务相关线索片段 (Task-relevant Clue Fragments)**: 待完善描述 `[Source: 待补充]`
- **自适应检索 (Adaptive Retrieval)**: 待完善描述 `[Source: 待补充]`
- **全局 - 自我对齐融合 (Global-to-Ego Alignment Fusion)**: 待完善描述 `[Source: 待补充]`
- **动态上下文注入 (Dynamic Context Injection)**: 待完善描述 `[Source: 待补充]`
- **视觉语言模型 (Vision-Language Model)**: 待完善描述 `[Source: 待补充]`
- **向量或图结构数据库 (Vector/Graph Database)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Non-Parametric Continual Learning**: 待完善描述 `[Source: 待补充]`
- **Associative Memory**: 待完善描述 `[Source: 待补充]`
- **Fact Memory**: 待完善描述 `[Source: 待补充]`
- **Contextual Memory**: 待完善描述 `[Source: 待补充]`
- **Hybrid Knowledge Graph**: 待完善描述 `[Source: 待补充]`
- **Phrase-Paragraph Dual Node Structure**: 待完善描述 `[Source: 待补充]`
- **Query-to-Triple Mapping**: 待完善描述 `[Source: 待补充]`
- **Offline Indexing**: 待完善描述 `[Source: 待补充]`
- **Online Retrieval**: 待完善描述 `[Source: 待补充]`
- **Personalized PageRank Propagation**: 待完善描述 `[Source: 待补充]`
- **Recognition Memory Filtering**: 待完善描述 `[Source: 待补充]`
- **Text Passages**: 待完善描述 `[Source: 待补充]`
- **Knowledge Graph Triples**: 待完善描述 `[Source: 待补充]`
- **Dense Embeddings**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **可逆记忆 (Reversible Memory)**: 待完善描述 `[Source: 待补充]`
- **虚拟记忆 (Virtual Memory)**: 待完善描述 `[Source: 待补充]`
- **层次化压缩结构 (Hierarchical Compression Structure)**: 待完善描述 `[Source: 待补充]`
- **可逆 Transformer 架构 (Reversible Transformer Architecture)**: 待完善描述 `[Source: 待补充]`
- **正向压缩 (Forward Compression)**: 待完善描述 `[Source: 待补充]`
- **反向重建 (Backward Reconstruction)**: 待完善描述 `[Source: 待补充]`
- **循环一致性优化 (Cycle Consistency Optimization)**: 待完善描述 `[Source: 待补充]`
- **虚拟记忆令牌 (Virtual Memory Tokens)**: 待完善描述 `[Source: 待补充]`
- **Adapter 权重 (Adapter Weights)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Query Memory**: 待完善描述 `[Source: 待补充]`
- **Semantic Memory**: 待完善描述 `[Source: 待补充]`
- **Explicit Query Description**: 待完善描述 `[Source: 待补充]`
- **Rule-based Decomposed Statements**: 待完善描述 `[Source: 待补充]`
- **Semantic Similarity Retrieval**: 待完善描述 `[Source: 待补充]`
- **Query Reconstruction**: 待完善描述 `[Source: 待补充]`
- **Memory Augmentation**: 待完善描述 `[Source: 待补充]`
- **Memory Module**: 待完善描述 `[Source: 待补充]`
- **LLM Context Window**: 待完善描述 `[Source: 待补充]`
- **Vector Embedding Space**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **交互轨迹记忆 (Interaction Trajectory Memory)**: 待完善描述 `[Source: 待补充]`
- **状态快照记忆 (State Snapshot Memory)**: 待完善描述 `[Source: 待补充]`
- **成功/失败案例记忆 (Success/Failure Case Memory)**: 待完善描述 `[Source: 待补充]`
- **代理能力描述表 (Agent Capability Description Table)**: 待完善描述 `[Source: 待补充]`
- **历史交互日志 (Historical Interaction Log)**: 待完善描述 `[Source: 待补充]`
- **状态回滚 (State Rollback)**: 待完善描述 `[Source: 待补充]`
- **能力匹配 (Capability Matching)**: 待完善描述 `[Source: 待补充]`
- **记忆自进化 (Memory Self-Evolution)**: 待完善描述 `[Source: 待补充]`
- **UI 元素树 (UI Element Tree)**: 待完善描述 `[Source: 待补充]`
- **屏幕截图 (Screen Screenshots)**: 待完善描述 `[Source: 待补充]`
- **操作动作序列 (Action Sequences)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Programmatic Skills (Procedural Memory)**: 待完善描述 `[Source: 待补充]`
- **Text-based Skills (Declarative Memory)**: 待完善描述 `[Source: 待补充]`
- **Verified Skill Library**: 待完善描述 `[Source: 待补充]`
- **Action Trajectory Buffer**: 待完善描述 `[Source: 待补充]`
- **Skill Induction (Encoding)**: 待完善描述 `[Source: 待补充]`
- **Program Verification (Validation)**: 待完善描述 `[Source: 待补充]`
- **Skill Reuse (Retrieval & Execution)**: 待完善描述 `[Source: 待补充]`
- **Executable Code Snippets**: 待完善描述 `[Source: 待补充]`
- **Web Interaction Traces**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Procedural Skill Memory**: 待完善描述 `[Source: 待补充]`
- **Executable API Memory**: 待完善描述 `[Source: 待补充]`
- **Skill Library**: 待完善描述 `[Source: 待补充]`
- **Modular Code Repository**: 待完善描述 `[Source: 待补充]`
- **Skill Proposal**: 待完善描述 `[Source: 待补充]`
- **Skill Synthesis**: 待完善描述 `[Source: 待补充]`
- **Skill Distillation**: 待完善描述 `[Source: 待补充]`
- **Skill Honing**: 待完善描述 `[Source: 待补充]`
- **Python Async Scripts**: 待完善描述 `[Source: 待补充]`
- **API Function Definitions**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **自适应记忆 (Adaptive Memory)**: 待完善描述 `[Source: 待补充]`
- **动态作弊表记忆 (Dynamic Cheatsheet Memory)**: 待完善描述 `[Source: 待补充]`
- **策略记忆 (Strategy Memory)**: 待完善描述 `[Source: 待补充]`
- **动态记忆库 (Dynamic Memory Bank)**: 待完善描述 `[Source: 待补充]`
- **策展片段集合 (Curated Snippet Collection)**: 待完善描述 `[Source: 待补充]`
- **自我策展 (Self-Curation)**: 待完善描述 `[Source: 待补充]`
- **语义检索 (Semantic Retrieval)**: 待完善描述 `[Source: 待补充]`
- **动态更新 (Dynamic Update)**: 待完善描述 `[Source: 待补充]`
- **洞察提取 (Insight Extraction)**: 待完善描述 `[Source: 待补充]`
- **文本策略片段 (Text Strategy Snippets)**: 待完善描述 `[Source: 待补充]`
- **代码片段 (Code Snippets)**: 待完善描述 `[Source: 待补充]`
- **增强系统提示词 (Augmented System Prompts)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Episodic Demonstration Memory**: 待完善描述 `[Source: 待补充]`
- **Semantic Action Memory**: 待完善描述 `[Source: 待补充]`
- **Vectorized Knowledge Index**: 待完善描述 `[Source: 待补充]`
- **Structured Semantic Description**: 待完善描述 `[Source: 待补充]`
- **Demonstration Parsing**: 待完善描述 `[Source: 待补充]`
- **Similarity-based Retrieval**: 待完善描述 `[Source: 待补充]`
- **Context Injection**: 待完善描述 `[Source: 待补充]`
- **LearnGUI Dataset**: 待完善描述 `[Source: 待补充]`
- **Vector Database**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Long-term Memory Context**: 待完善描述 `[Source: 待补充]`
- **Real-time State Tracking**: 待完善描述 `[Source: 待补充]`
- **System State Memory**: 待完善描述 `[Source: 待补充]`
- **Action Trajectory Log**: 待完善描述 `[Source: 待补充]`
- **Screen Snapshots**: 待完善描述 `[Source: 待补充]`
- **Accessibility API Data**: 待完善描述 `[Source: 待补充]`
- **UI Tree Structure**: 待完善描述 `[Source: 待补充]`
- **Context Retrieval for Planning**: 待完善描述 `[Source: 待补充]`
- **System Event Logs**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **短期记忆缓存 (Short-Term Memory Cache)**: 待完善描述 `[Source: 待补充]`
- **分层记忆架构 (Hierarchical Memory Architecture)**: 待完善描述 `[Source: 待补充]`
- **相关性排序 (Relevance Ranking)**: 待完善描述 `[Source: 待补充]`
- **向量数据库 (Vector Database)**: 待完善描述 `[Source: 待补充]`
- **可扩展记忆存储架构 (Scalable Memory Storage Architecture)**: 待完善描述 `[Source: 待补充]`
- **高速缓存 (High-Speed Cache)**: 待完善描述 `[Source: 待补充]`
- **长期记忆 (Long-Term Memory)**: 待完善描述 `[Source: 待补充]`
- **记忆编码 (Memory Encoding)**: 待完善描述 `[Source: 待补充]`
- **知识图谱 (Knowledge Graph)**: 待完善描述 `[Source: 待补充]`
- **记忆检索 (Memory Retrieval)**: 待完善描述 `[Source: 待补充]`
- **智能体交互历史 (Agent Interaction History)**: 待完善描述 `[Source: 待补充]`
- **记忆更新 (Memory Update)**: 待完善描述 `[Source: 待补充]`
- **语义记忆索引 (Semantic Memory Index)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Visual Grounding Map**: 待完善描述 `[Source: 待补充]`
- **Speculative Execution**: 待完善描述 `[Source: 待补充]`
- **Virtual Session Buffer**: 待完善描述 `[Source: 待补充]`
- **State Synchronization**: 待完善描述 `[Source: 待补充]`
- **Execution Trace Memory**: 待完善描述 `[Source: 待补充]`
- **Knowledge Retrieval**: 待完善描述 `[Source: 待补充]`
- **Screen Snapshots**: 待完善描述 `[Source: 待补充]`
- **Semantic Knowledge Memory**: 待完善描述 `[Source: 待补充]`
- **UIA Semantic Tree**: 待完善描述 `[Source: 待补充]`
- **Named Pipes**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **图基于记忆 (Graph-based Memory)**: 待完善描述 `[Source: 待补充]`
- **向量索引 (Vector Index)**: 待完善描述 `[Source: 待补充]`
- **实体关系图谱 (Entity-Relation Graph)**: 待完善描述 `[Source: 待补充]`
- **对话历史 (Dialogue History)**: 待完善描述 `[Source: 待补充]`
- **动态显著信息提取 (Dynamic Significant Information Extraction)**: 待完善描述 `[Source: 待补充]`
- **向量数据库 (Vector Database)**: 待完善描述 `[Source: 待补充]`
- **图数据库 (Graph Database)**: 待完善描述 `[Source: 待补充]`
- **长期记忆 (Long-Term Memory)**: 待完善描述 `[Source: 待补充]`
- **记忆检索 (Memory Retrieval)**: 待完善描述 `[Source: 待补充]`
- **向量基于记忆 (Vector-based Memory)**: 待完善描述 `[Source: 待补充]`
- **记忆巩固 (Memory Consolidation)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **External Knowledge Database**: 待完善描述 `[Source: 待补充]`
- **Query Generation**: 待完善描述 `[Source: 待补充]`
- **Loss Masking on Retrieved Values**: 待完善描述 `[Source: 待补充]`
- **Knowledge Triplets (Entity-Relation-Value)**: 待完善描述 `[Source: 待补充]`
- **Limited Memory**: 待完善描述 `[Source: 待补充]`
- **Database-driven Unlearning**: 待完善描述 `[Source: 待补充]`
- **Model Weights (Linguistic Only)**: 待完善描述 `[Source: 待补充]`
- **Externalized Factual Memory**: 待完善描述 `[Source: 待补充]`
- **Special Query Tokens**: 待完善描述 `[Source: 待补充]`
- **Internal Linguistic Memory**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Text Scene Graph**: 待完善描述 `[Source: 待补充]`
- **Memory Acquisition (ReAct Triples)**: 待完善描述 `[Source: 待补充]`
- **User Profile Memory (Hierarchical KG)**: 待完善描述 `[Source: 待补充]`
- **Knowledge Graph Nodes/Edges**: 待完善描述 `[Source: 待补充]`
- **LLM Context Window**: 待完善描述 `[Source: 待补充]`
- **Semantic Memory (Scene Graph)**: 待完善描述 `[Source: 待补充]`
- **Three-layer Hierarchical Structure (User->Type->Element)**: 待完善描述 `[Source: 待补充]`
- **Habitat 3.0 Simulator State**: 待完善描述 `[Source: 待补充]`
- **Memory Retrieval (Embedding Query)**: 待完善描述 `[Source: 待补充]`
- **Dynamic Knowledge Update**: 待完善描述 `[Source: 待补充]`
- **Episodic Memory (Interaction History)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Continuous Embedding Vectors**: 待完善描述 `[Source: 待补充]`
- **Plug-and-Play Injection**: 待完善描述 `[Source: 待补充]`
- **VLM Hidden State Extraction**: 待完善描述 `[Source: 待补充]`
- **Intermediate Layer Embedding Slot**: 待完善描述 `[Source: 待补充]`
- **Continuous Vector Compression**: 待完善描述 `[Source: 待补充]`
- **VLM Internal Hidden States**: 待完善描述 `[Source: 待补充]`
- **External Multimodal Knowledge Memory**: 待完善描述 `[Source: 待补充]`
- **General Continuous Memory (CoMEM)**: 待完善描述 `[Source: 待补充]`
- **8-Vector Compressed Sequence**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Multi-Session Task Memory**: 待完善描述 `[Source: 待补充]`
- **Missing-Slot Guided Filtering**: 待完善描述 `[Source: 待补充]`
- **Intent-Driven Memory**: 待完善描述 `[Source: 待补充]`
- **Dense Vector Index**: 待完善描述 `[Source: 待补充]`
- **Structured QA Memory Unit (Intent + Slots)**: 待完善描述 `[Source: 待补充]`
- **LLM Context Window**: 待完善描述 `[Source: 待补充]`
- **Memory Bank**: 待完善描述 `[Source: 待补充]`
- **Intent-Aligned Retrieval**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Capability Reuse**: 待完善描述 `[Source: 待补充]`
- **Task-related MCP Graph**: 待完善描述 `[Source: 待补充]`
- **Minimalist Single-Core Architecture**: 待完善描述 `[Source: 待补充]`
- **Task Context Memory**: 待完善描述 `[Source: 待补充]`
- **Capability Refinement**: 待完善描述 `[Source: 待补充]`
- **Internal Agent Context**: 待完善描述 `[Source: 待补充]`
- **Autonomous MCP Generation**: 待完善描述 `[Source: 待补充]`
- **Dynamic Capability Memory (MCPs)**: 待完善描述 `[Source: 待补充]`
- **External Open Source Repositories**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **进化档案库 (Evolutionary Archive)**: 待完善描述 `[Source: 待补充]`
- **自我代码修改 (Self-Code Modification)**: 待完善描述 `[Source: 待补充]`
- **性能评估记录 (Performance Evaluation Record)**: 待完善描述 `[Source: 待补充]`
- **源代码仓库 (Source Code Repository)**: 待完善描述 `[Source: 待补充]`
- **代理版本树 (Agent Version Tree)**: 待完善描述 `[Source: 待补充]`
- **安全沙箱环境 (Safety Sandbox Environment)**: 待完善描述 `[Source: 待补充]`
- **档案库采样 (Archive Sampling)**: 待完善描述 `[Source: 待补充]`
- **实证验证 (Empirical Verification)**: 待完善描述 `[Source: 待补充]`
- **代码库状态快照 (Codebase State Snapshot)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Video Latent Sequence**: 待完善描述 `[Source: 待补充]`
- **Geometric-Indexed Memory**: 待完善描述 `[Source: 待补充]`
- **Latent Dimension Concatenation**: 待完善描述 `[Source: 待补充]`
- **Diffusion Latents**: 待完善描述 `[Source: 待补充]`
- **Camera Trajectory Map**: 待完善描述 `[Source: 待补充]`
- **Context-as-Memory**: 待完善描述 `[Source: 待补充]`
- **Camera Poses**: 待完善描述 `[Source: 待补充]`
- **FOV Overlap Retrieval**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Three-tier Graph Hierarchy**: 待完善描述 `[Source: 待补充]`
- **Graph Nodes**: 待完善描述 `[Source: 待补充]`
- **Interaction Memory**: 待完善描述 `[Source: 待补充]`
- **Insight Memory**: 待完善描述 `[Source: 待补充]`
- **Insight Graph**: 待完善描述 `[Source: 待补充]`
- **Query Graph**: 待完善描述 `[Source: 待补充]`
- **Interaction Trajectories**: 待完善描述 `[Source: 待补充]`
- **Interaction Graph**: 待完善描述 `[Source: 待补充]`
- **Hierarchical Retrieval**: 待完善描述 `[Source: 待补充]`
- **Collaboration Experiences**: 待完善描述 `[Source: 待补充]`
- **Bi-directional Memory Traversal**: 待完善描述 `[Source: 待补充]`
- **Trajectory Assimilation**: 待完善描述 `[Source: 待补充]`
- **Query Memory**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Text Interaction Sequence**: 待完善描述 `[Source: 待补充]`
- **Constant Memory**: 待完善描述 `[Source: 待补充]`
- **Masked Trajectory**: 待完善描述 `[Source: 待补充]`
- **State Consolidation**: 待完善描述 `[Source: 待补充]`
- **Generate-Reset-Inject Cycle**: 待完善描述 `[Source: 待补充]`
- **Internal State Token (<IS>)**: 待完善描述 `[Source: 待补充]`
- **Control Token Sequence**: 待完善描述 `[Source: 待补充]`
- **Context Pruning**: 待完善描述 `[Source: 待补充]`
- **Compressed Internal State**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **RL Policy Optimization**: 待完善描述 `[Source: 待补充]`
- **Agent Workflow Pipeline**: 待完善描述 `[Source: 待补充]`
- **RL-Managed Memory**: 待完善描述 `[Source: 待补充]`
- **Segmented Ingestion**: 待完善描述 `[Source: 待补充]`
- **External Memory Module**: 待完善描述 `[Source: 待补充]`
- **LLM Base Model Parameters**: 待完善描述 `[Source: 待补充]`
- **Overwrite Strategy**: 待完善描述 `[Source: 待补充]`
- **Text Segments**: 待完善描述 `[Source: 待补充]`
- **Segmented Context Memory**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Feedback Diagnosis (反馈诊断)**: 待完善描述 `[Source: 待补充]`
- **Planning Seeds (规划种子)**: 待完善描述 `[Source: 待补充]`
- **Lightweight API Interface (轻量级 API 接口)**: 待完善描述 `[Source: 待补充]`
- **Agent Execution Trajectories (智能体执行轨迹)**: 待完善描述 `[Source: 待补充]`
- **Hybrid Retrieval (混合检索)**: 待完善描述 `[Source: 待补充]`
- **Structured Knowledge Base (结构化知识库)**: 待完善描述 `[Source: 待补充]`
- **Cross-Domain Experience (跨域经验)**: 待完善描述 `[Source: 待补充]`
- **Trajectory Aggregation (轨迹聚合)**: 待完善描述 `[Source: 待补充]`
- **Agent KB Infrastructure (Agent KB 基础设施)**: 待完善描述 `[Source: 待补充]`
- **Disagreement Gating (分歧门控)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **情景记忆 (Episodic Memory)**: 待完善描述 `[Source: 待补充]`
- **混合存储策略 (端云结合)**: 待完善描述 `[Source: 待补充]`
- **主动检索 (Active Retrieval)**: 待完善描述 `[Source: 待补充]`
- **核心记忆 (Core Memory)**: 待完善描述 `[Source: 待补充]`
- **记忆巩固 (Memory Consolidation)**: 待完善描述 `[Source: 待补充]`
- **三层代理工作流 (元管理器 + 专用管理器 + 对话代理)**: 待完善描述 `[Source: 待补充]`
- **屏幕截图**: 待完善描述 `[Source: 待补充]`
- **知识保险库 (Knowledge Vault)**: 待完善描述 `[Source: 待补充]`
- **资源记忆 (Resource Memory)**: 待完善描述 `[Source: 待补充]`
- **文本对话**: 待完善描述 `[Source: 待补充]`
- **敏感信息分级访问控制**: 待完善描述 `[Source: 待补充]`
- **程序记忆 (Procedural Memory)**: 待完善描述 `[Source: 待补充]`
- **并行更新 (Parallel Update)**: 待完善描述 `[Source: 待补充]`
- **文档文件**: 待完善描述 `[Source: 待补充]`
- **敏感凭证**: 待完善描述 `[Source: 待补充]`
- **语义记忆 (Semantic Memory)**: 待完善描述 `[Source: 待补充]`
- **记忆自动路由 (Memory Auto-Routing)**: 待完善描述 `[Source: 待补充]`
- **时间戳事件日志**: 待完善描述 `[Source: 待补充]`
- **六模块记忆组件架构**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **MCP Server Tool List**: 待完善描述 `[Source: 待补充]`
- **Tool Remove**: 待完善描述 `[Source: 待补充]`
- **Autonomous Memory**: 待完善描述 `[Source: 待补充]`
- **Tool Context Window**: 待完善描述 `[Source: 待补充]`
- **LLM Context Window**: 待完善描述 `[Source: 待补充]`
- **Tool Search**: 待完善描述 `[Source: 待补充]`
- **Workflow Memory**: 待完善描述 `[Source: 待补充]`
- **Short-Term Tool Memory**: 待完善描述 `[Source: 待补充]`
- **Dynamic Tool Pool**: 待完善描述 `[Source: 待补充]`
- **Context Count Check**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Dynamic Weight Adjustment**: 待完善描述 `[Source: 待补充]`
- **User Profiles**: 待完善描述 `[Source: 待补充]`
- **Text Conversation History**: 待完善描述 `[Source: 待补充]`
- **Semantic Indexes**: 待完善描述 `[Source: 待补充]`
- **Trace Memory**: 待完善描述 `[Source: 待补充]`
- **Feedback-Driven Update**: 待完善描述 `[Source: 待补充]`
- **Forgetting Curve Decay**: 待完善描述 `[Source: 待补充]`
- **Domain Memory**: 待完善描述 `[Source: 待补充]`
- **Episode Memory**: 待完善描述 `[Source: 待补充]`
- **Four-Layer Semantic Architecture**: 待完善描述 `[Source: 待补充]`
- **Index Routing Mechanism**: 待完善描述 `[Source: 待补充]`
- **Index Routing Retrieval**: 待完善描述 `[Source: 待补充]`
- **Vector-Text Dual Storage**: 待完善描述 `[Source: 待补充]`
- **Vector Embeddings**: 待完善描述 `[Source: 待补充]`
- **Category Memory**: 待完善描述 `[Source: 待补充]`
- **Hierarchical Memory (H-MEM)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **双阶段架构 (训练 - 推理分离架构)**: 待完善描述 `[Source: 待补充]`
- **检索器行为模仿 (Retriever Behavior Imitation)**: 待完善描述 `[Source: 待补充]`
- **参数化知识内化 (Parametric Knowledge Internalization)**: 待完善描述 `[Source: 待补充]`
- **MLP 记忆模块 (MLP Memory Module)**: 待完善描述 `[Source: 待补充]`
- **概率插值机制 (Probability Interpolation Mechanism)**: 待完善描述 `[Source: 待补充]`
- **Retriever-Pretrained Memory (检索器预训练记忆)**: 待完善描述 `[Source: 待补充]`
- **1B 参数 MLP 模块**: 待完善描述 `[Source: 待补充]`
- **基础 LLM 解码器**: 待完善描述 `[Source: 待补充]`
- **概率插值集成 (Probability Interpolation Integration)**: 待完善描述 `[Source: 待补充]`
- **Parametric Memory (参数化记忆)**: 待完善描述 `[Source: 待补充]`
- **MLP Memory (检索器预训练记忆)**: 待完善描述 `[Source: 待补充]`
- **预训练数据集 (WikiText-103, Web datasets)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Episodic Memory**: 待完善描述 `[Source: 待补充]`
- **Two-Step Alignment**: 待完善描述 `[Source: 待补充]`
- **Prediction-Calibration**: 待完善描述 `[Source: 待补充]`
- **Semantic Memory**: 待完善描述 `[Source: 待补充]`
- **Boundary Detection**: 待完善描述 `[Source: 待补充]`
- **Structured Narrative Tuples**: 待完善描述 `[Source: 待补充]`
- **Memory Database**: 待完善描述 `[Source: 待补充]`
- **Distilled Knowledge Statements**: 待完善描述 `[Source: 待补充]`
- **Vector Embeddings**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Context Search**: 待完善描述 `[Source: 待补充]`
- **Context Folding**: 待完善描述 `[Source: 待补充]`
- **Passive Input Context**: 待完善描述 `[Source: 待补充]`
- **Dynamic Context State**: 待完善描述 `[Source: 待补充]`
- **Context Compression**: 待完善描述 `[Source: 待补充]`
- **Active Working Memory**: 待完善描述 `[Source: 待补充]`
- **Reversible Context Segment**: 待完善描述 `[Source: 待补充]`
- **Context Fragmentation**: 待完善描述 `[Source: 待补充]`
- **Tool Call Trajectory**: 待完善描述 `[Source: 待补充]`
- **Text Sequence**: 待完善描述 `[Source: 待补充]`
- **Context Recovery**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **经验记忆 (Experience Memory)**: 待完善描述 `[Source: 待补充]`
- **软件指南书 (Software Guidebook)**: 待完善描述 `[Source: 待补充]`
- **细粒度评估 (Fine-grained Evaluation)**: 待完善描述 `[Source: 待补充]`
- **知识蒸馏 (Knowledge Distillation)**: 待完善描述 `[Source: 待补充]`
- **策略模型权重 (Policy Model Weights)**: 待完善描述 `[Source: 待补充]`
- **自主生成 (Autonomous Generation)**: 待完善描述 `[Source: 待补充]`
- **世界状态模型 (World State Model)**: 待完善描述 `[Source: 待补充]`
- **文本指南库 (Text Guide Repository)**: 待完善描述 `[Source: 待补充]`
- **知识记忆 (Knowledge Memory)**: 待完善描述 `[Source: 待补充]`
- **轨迹序列 (Trajectory Sequence)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Importance Scoring**: 待完善描述 `[Source: 待补充]`
- **Graph/Chart Representation**: 待完善描述 `[Source: 待补充]`
- **Structured Memory**: 待完善描述 `[Source: 待补充]`
- **LLM Context Window**: 待完善描述 `[Source: 待补充]`
- **Role-Aware Context Memory**: 待完善描述 `[Source: 待补充]`
- **YAML Format**: 待完善描述 `[Source: 待补充]`
- **Conflict Resolution**: 待完善描述 `[Source: 待补充]`
- **Budget Allocation**: 待完善描述 `[Source: 待补充]`
- **Context Routing**: 待完善描述 `[Source: 待补充]`
- **Structured Memory Bank**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **程序化构建 (Proceduralization)**: 待完善描述 `[Source: 待补充]`
- **纠错更新 (Correction Update/Reflexion)**: 待完善描述 `[Source: 待补充]`
- **原始轨迹记忆 (Raw Trajectory)**: 待完善描述 `[Source: 待补充]`
- **抽象脚本记忆 (Abstract Script)**: 待完善描述 `[Source: 待补充]`
- **程序性记忆 (Procedural Memory)**: 待完善描述 `[Source: 待补充]`
- **向量数据库 (Vector Database)**: 待完善描述 `[Source: 待补充]`
- **外部记忆库 (External Memory Bank)**: 待完善描述 `[Source: 待补充]`
- **向量嵌入 (Vector Embeddings)**: 待完善描述 `[Source: 待补充]`
- **文本轨迹 (Text Trajectory)**: 待完善描述 `[Source: 待补充]`
- **基于关键特征平均相似度的检索 (AveFact Retrieval)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Priority-based Context Window**: 待完善描述 `[Source: 待补充]`
- **Agent-specific Output Logs**: 待完善描述 `[Source: 待补充]`
- **Intrinsic Memory**: 待完善描述 `[Source: 待补充]`
- **Intrinsic Memory Update**: 待完善描述 `[Source: 待补充]`
- **Structured Contextual Memory**: 待完善描述 `[Source: 待补充]`
- **Consensus-driven Termination**: 待完善描述 `[Source: 待补充]`
- **Structured Memory Templates**: 待完善描述 `[Source: 待补充]`
- **Heterogeneous Agent Memory**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Episodic Memory**: 待完善描述 `[Source: 待补充]`
- **High-level Abstract Memory**: 待完善描述 `[Source: 待补充]`
- **Multi-turn Reasoning**: 待完善描述 `[Source: 待补充]`
- **Entity-centric Memory Bank**: 待完善描述 `[Source: 待补充]`
- **Memory Retrieval**: 待完善描述 `[Source: 待补充]`
- **Semantic Memory**: 待完善描述 `[Source: 待补充]`
- **Memorization**: 待完善描述 `[Source: 待补充]`
- **Fine-grained Memory**: 待完善描述 `[Source: 待补充]`
- **Multimodal Input Stream**: 待完善描述 `[Source: 待补充]`
- **Long-term Memory Bank**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Pretrained Plug-and-Play Memory**: 待完善描述 `[Source: 待补充]`
- **Independent Small Transformer Decoder**: 待完善描述 `[Source: 待补充]`
- **Implicit Retrieval Memory**: 待完善描述 `[Source: 待补充]`
- **Interpolation Integration Layer**: 待完善描述 `[Source: 待补充]`
- **Domain-Specific Corpus**: 待完善描述 `[Source: 待补充]`
- **Retriever Behavior Imitation**: 待完善描述 `[Source: 待补充]`
- **Parameter-Free Model Integration**: 待完善描述 `[Source: 待补充]`
- **Module Weights**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **全局记忆池 (Global Memory Pool)**: 待完善描述 `[Source: 待补充]`
- **向量检索数据库 (Vector Retrieval Database)**: 待完善描述 `[Source: 待补充]`
- **动态工作记忆 (Dynamic Working Memory)**: 待完善描述 `[Source: 待补充]`
- **长上下文 Token 序列 (Long Context Token Sequences)**: 待完善描述 `[Source: 待补充]`
- **知识巩固与整合 (Knowledge Consolidation & Integration)**: 待完善描述 `[Source: 待补充]`
- **状态化记忆 (Stateful Memory)**: 待完善描述 `[Source: 待补充]`
- **推理困境检测 (Reasoning Dilemma Detection)**: 待完善描述 `[Source: 待补充]`
- **连贯上下文 (Coherent Context)**: 待完善描述 `[Source: 待补充]`
- **探索性探针生成 (Exploratory Probing Generation)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Agentic Memory**: 待完善描述 `[Source: 待补充]`
- **Hybrid Retrieval**: 待完善描述 `[Source: 待补充]`
- **Discourse Relation Labels**: 待完善描述 `[Source: 待补充]`
- **Semantic Anchored Memory**: 待完善描述 `[Source: 待补充]`
- **Weighted Fusion Ranking**: 待完善描述 `[Source: 待补充]`
- **Dependency Parse Triples**: 待完善描述 `[Source: 待补充]`
- **Structured Memory Entry**: 待完善描述 `[Source: 待补充]`
- **Semantic Anchoring**: 待完善描述 `[Source: 待补充]`
- **Dense Vector**: 待完善描述 `[Source: 待补充]`
- **Hybrid Index Architecture**: 待完善描述 `[Source: 待补充]`
- **Coreference Chains**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Embedding Space Representations**: 待完善描述 `[Source: 待补充]`
- **Text Queries**: 待完善描述 `[Source: 待补充]`
- **Adversarial Soft Prompting**: 待完善描述 `[Source: 待补充]`
- **Retrieved Document Chunks**: 待完善描述 `[Source: 待补充]`
- **Soft Prompt Vectors**: 待完善描述 `[Source: 待补充]`
- **Conflict Assessment**: 待完善描述 `[Source: 待补充]`
- **Context Memory Embeddings**: 待完善描述 `[Source: 待补充]`
- **Retrieved Context (External Memory)**: 待完善描述 `[Source: 待补充]`
- **Parametric Knowledge (Internal Memory)**: 待完善描述 `[Source: 待补充]`
- **Knowledge Source Biasing**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **检索记忆单元 (Retrieval Memory Unit)**: 待完善描述 `[Source: 待补充]`
- **情景记忆片段 (Episodic Memory Segment)**: 待完善描述 `[Source: 待补充]`
- **多记忆片段系统 (Multi-Memory Segment System, MMS)**: 待完善描述 `[Source: 待补充]`
- **认知视角记忆片段 (Cognitive Perspective Memory Segment)**: 待完善描述 `[Source: 待补充]`
- **上下文记忆单元 (Context Memory Unit)**: 待完善描述 `[Source: 待补充]`
- **记忆片段构建 (Memory Segment Construction)**: 待完善描述 `[Source: 待补充]`
- **单元映射 (Unit Mapping)**: 待完善描述 `[Source: 待补充]`
- **语义记忆片段 (Semantic Memory Segment)**: 待完善描述 `[Source: 待补充]`
- **向量化记忆片段 (Vectorized Memory Segments)**: 待完善描述 `[Source: 待补充]`
- **双单元存储 (Dual-Unit Storage)**: 待完善描述 `[Source: 待补充]`
- **向量数据库 (Vector Database)**: 待完善描述 `[Source: 待补充]`
- **向量检索匹配 (Vector Retrieval Matching)**: 待完善描述 `[Source: 待补充]`
- **关键词记忆片段 (Keyword Memory Segment)**: 待完善描述 `[Source: 待补充]`
- **对话文本 (Dialogue Text)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **记忆增强马尔可夫决策过程 (M-MDP)**: 待完善描述 `[Source: 待补充]`
- **记忆重写 (Memory Rewrite)**: 待完善描述 `[Source: 待补充]`
- **情景记忆 (Episodic Memory)**: 待完善描述 `[Source: 待补充]`
- **冻结的大模型参数 (Frozen LLM Parameters)**: 待完善描述 `[Source: 待补充]`
- **神经案例记忆 (Neural Case Memory)**: 待完善描述 `[Source: 待补充]`
- **记忆检索 (Memory Retrieval)**: 待完善描述 `[Source: 待补充]`
- **经验存储 (Experience Storage)**: 待完善描述 `[Source: 待补充]`
- **外部记忆库 (External Memory Bank)**: 待完善描述 `[Source: 待补充]`
- **情景记忆库 (Episodic Memory Bank)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **时空语义系统 (Spatio-Temporal Semantic System)**: 待完善描述 `[Source: 待补充]`
- **个人经历记忆 (Personal Experience Memory)**: 待完善描述 `[Source: 待补充]`
- **校园模拟环境状态 (Campus Simulation Environment State)**: 待完善描述 `[Source: 待补充]`
- **七类工具接口 (Seven Tool Interfaces)**: 待完善描述 `[Source: 待补充]`
- **领域知识记忆 (Domain Knowledge Memory)**: 待完善描述 `[Source: 待补充]`
- **技能模式记忆 (Skill Pattern Memory)**: 待完善描述 `[Source: 待补充]`
- **技能抽象提取 (Skill Abstraction Extraction)**: 待完善描述 `[Source: 待补充]`
- **结构化任务序列 (Structured Task Sequences)**: 待完善描述 `[Source: 待补充]`
- **知识内化转换 (Knowledge Internalization Transformation)**: 待完善描述 `[Source: 待补充]`
- **上下文工程提示词 (Context Engineering Prompts)**: 待完善描述 `[Source: 待补充]`
- **经验轨迹记录 (Experience Trajectory Records)**: 待完善描述 `[Source: 待补充]`
- **常识推理记忆 (Common Sense Reasoning Memory)**: 待完善描述 `[Source: 待补充]`
- **经验探索检索 (Experience Exploration Retrieval)**: 待完善描述 `[Source: 待补充]`
- **多工具交互日志 (Multi-tool Interaction Logs)**: 待完善描述 `[Source: 待补充]`
- **记忆距离加权评分 (Memory Distance Weighted Scoring)**: 待完善描述 `[Source: 待补充]`
- **持久化世界状态 (Persistent World State)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Gated Fusion**: 待完善描述 `[Source: 待补充]`
- **Cognitive Memory**: 待完善描述 `[Source: 待补充]`
- **Cross-Attention Retrieval**: 待完善描述 `[Source: 待补充]`
- **Perceptual Memory**: 待完善描述 `[Source: 待补充]`
- **Perceptual-Cognitive Memory Bank (PCMB)**: 待完善描述 `[Source: 待补充]`
- **Token Merging**: 待完善描述 `[Source: 待补充]`
- **Cognitive Tokens**: 待完善描述 `[Source: 待补充]`
- **Memory Consolidation**: 待完善描述 `[Source: 待补充]`
- **Perceptual Tokens**: 待完善描述 `[Source: 待补充]`
- **Perceptual-Cognitive Memory**: 待完善描述 `[Source: 待补充]`
- **RGB Observation Frames**: 待完善描述 `[Source: 待补充]`
- **Working Memory**: 待完善描述 `[Source: 待补充]`
- **Dual-stream Memory Structure**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **UPDATE**: 待完善描述 `[Source: 待补充]`
- **Shared State Space**: 待完善描述 `[Source: 待补充]`
- **ADD**: 待完善描述 `[Source: 待补充]`
- **External Vector Database**: 待完善描述 `[Source: 待补充]`
- **NOOP**: 待完善描述 `[Source: 待补充]`
- **Key-Value Storage**: 待完善描述 `[Source: 待补充]`
- **DELETE**: 待完善描述 `[Source: 待补充]`
- **LLM Context Memory**: 待完善描述 `[Source: 待补充]`
- **External Structured Memory**: 待完善描述 `[Source: 待补充]`
- **Structured Memory Entries**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **动态重要性记忆过滤 (DIMF)**: 待完善描述 `[Source: 待补充]`
- **多模态交互日志 (Multimodal Interaction Logs)**: 待完善描述 `[Source: 待补充]`
- **长期记忆数据库 (Long-term Memory Database)**: 待完善描述 `[Source: 待补充]`
- **AR 虚拟形象 (AR Virtual Avatar)**: 待完善描述 `[Source: 待补充]`
- **渐进式压缩记忆 (Progressive Compressed Memory)**: 待完善描述 `[Source: 待补充]`
- **分层交互系统 (Layered Interaction System)**: 待完善描述 `[Source: 待补充]`
- **时间二进制压缩 (TBC)**: 待完善描述 `[Source: 待补充]`
- **模块化 AI 代理架构 (Modular AI Agent Architecture)**: 待完善描述 `[Source: 待补充]`
- **上下文检索与更新 (Context Retrieval & Update)**: 待完善描述 `[Source: 待补充]`
- **情感上下文记忆 (Emotional Context Memory)**: 待完善描述 `[Source: 待补充]`
- **云端/本地混合存储 (Cloud/Local Hybrid Storage)**: 待完善描述 `[Source: 待补充]`
- **长期交互记忆 (Long-term Interaction Memory)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **记忆图谱 (Memory Graph)**: 待完善描述 `[Source: 待补充]`
- **经验记忆 (Experience Memory)**: 待完善描述 `[Source: 待补充]`
- **主观记忆 (Subjective Memory)**: 待完善描述 `[Source: 待补充]`
- **结构化记忆片段 (Structured Memory Fragments)**: 待完善描述 `[Source: 待补充]`
- **图式 (Schema)**: 待完善描述 `[Source: 待补充]`
- **情景记忆 (Episodic Memory)**: 待完善描述 `[Source: 待补充]`
- **推理记忆 (Inferred Memory)**: 待完善描述 `[Source: 待补充]`
- **预存储推理 (Pre-Storage Reasoning)**: 待完善描述 `[Source: 待补充]`
- **跨会话聚类 (Cross-session Clustering)**: 待完善描述 `[Source: 待补充]`
- **向量数据库 (Vector Database)**: 待完善描述 `[Source: 待补充]`
- **图式演化 (Schema Evolution)**: 待完善描述 `[Source: 待补充]`
- **对话历史 (Dialogue History)**: 待完善描述 `[Source: 待补充]`
- **混合检索 (Hybrid Retrieval)**: 待完善描述 `[Source: 待补充]`
- **事实记忆 (Fact Memory)**: 待完善描述 `[Source: 待补充]`
- **增强记忆库 (Enhanced Memory Bank)**: 待完善描述 `[Source: 待补充]`
- **原始记忆 (Raw Memory)**: 待完善描述 `[Source: 待补充]`
- **记忆提取 (Memory Extraction)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **文本对话流 (Text Dialogue Flow)**: 待完善描述 `[Source: 待补充]`
- **微调大语言模型 (Micro-tuned LLM)**: 待完善描述 `[Source: 待补充]`
- **叙事记忆 (Narrative Memory)**: 待完善描述 `[Source: 待补充]`
- **键值对记忆库 (Key-Value Memory Bank)**: 待完善描述 `[Source: 待补充]`
- **层级总结 (Hierarchical Summarization)**: 待完善描述 `[Source: 待补充]`
- **竞争 - 抑制遗忘 (Competitive-Inhibitory Forgetting)**: 待完善描述 `[Source: 待补充]`
- **向量数据库 (Vector Database)**: 待完善描述 `[Source: 待补充]`
- **键值融合 (Key-Value Fusion)**: 待完善描述 `[Source: 待补充]`
- **层级化故事线 (Hierarchical Storylines)**: 待完善描述 `[Source: 待补充]`
- **人物记忆 (Character Memory)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Similarity Signal**: 待完善描述 `[Source: 待补充]`
- **Distance Signal**: 待完善描述 `[Source: 待补充]`
- **CDF-based Estimation**: 待完善描述 `[Source: 待补充]`
- **Magnitude Signal**: 待完善描述 `[Source: 待补充]`
- **Dense Matching**: 待完善描述 `[Source: 待补充]`
- **High-dimensional Input Representations**: 待完善描述 `[Source: 待补充]`
- **Empirical CDF Partition**: 待完善描述 `[Source: 待补充]`
- **SDM Activation Module**: 待完善描述 `[Source: 待补充]`
- **Training Set Embeddings**: 待完善描述 `[Source: 待补充]`
- **Signal Fusion**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Hierarchical Memory Architecture**: 待完善描述 `[Source: 待补充]`
- **Dual-layer Memory Storage**: 待完善描述 `[Source: 待补充]`
- **Low-level Execution Memory**: 待完善描述 `[Source: 待补充]`
- **Agent-Environment Interaction Trajectories**: 待完善描述 `[Source: 待补充]`
- **Hierarchical Hindsight Reflection (H2R)**: 待完善描述 `[Source: 待补充]`
- **Knowledge Fusion**: 待完善描述 `[Source: 待补充]`
- **Separate Retrieval**: 待完善描述 `[Source: 待补充]`
- **Task Execution Logs**: 待完善描述 `[Source: 待补充]`
- **High-level Planning Memory**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Agent Behavior Pre-training Data**: 待完善描述 `[Source: 待补充]`
- **Agentic Continual Pre-training (智能体持续预训练)**: 待完善描述 `[Source: 待补充]`
- **Two-stage Training Pipeline (两阶段训练管道)**: 待完善描述 `[Source: 待补充]`
- **Agent Foundation Model Architecture (智能体基座模型架构)**: 待完善描述 `[Source: 待补充]`
- **AgentFounder-30B Model**: 待完善描述 `[Source: 待补充]`
- **Tool Invocation Sequences (工具调用序列)**: 待完善描述 `[Source: 待补充]`
- **Multi-step Reasoning Chains (多步推理链)**: 待完善描述 `[Source: 待补充]`
- **Agent Behavior Trajectories (智能体行为轨迹)**: 待完善描述 `[Source: 待补充]`
- **Post-training Alignment via SFT/RL (后训练对齐)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Evidence Memory (证据记忆)**: 待完善描述 `[Source: 待补充]`
- **Cited Report Sections (引用报告章节)**: 待完善描述 `[Source: 待补充]`
- **Evidence Acquisition (证据获取)**: 待完善描述 `[Source: 待补充]`
- **Vector Database (向量数据库)**: 待完善描述 `[Source: 待补充]`
- **Targeted Retrieval (针对性检索)**: 待完善描述 `[Source: 待补充]`
- **Outline Optimization (大纲优化)**: 待完善描述 `[Source: 待补充]`
- **Web-scale Text Chunks (网络规模文本块)**: 待完善描述 `[Source: 待补充]`
- **Linked Outline Structure (链接式大纲结构)**: 待完善描述 `[Source: 待补充]`
- **Evidence Memory Bank (证据记忆库)**: 待完善描述 `[Source: 待补充]`
- **Dynamic Outline Memory (动态大纲记忆)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **基于嵌入的检索 (Embedding-based Retrieval)**: 待完善描述 `[Source: 待补充]`
- **外部策略数据库 (External Strategy Database)**: 待完善描述 `[Source: 待补充]`
- **结构化文本原则库**: 待完善描述 `[Source: 待补充]`
- **合成策略记忆 (Synthetic Strategy Memory)**: 待完善描述 `[Source: 待补充]`
- **非参数化策略记忆 (Non-parametric Strategy Memory)**: 待完善描述 `[Source: 待补充]`
- **离线自博弈生成 (Offline Self-Play Generation)**: 待完善描述 `[Source: 待补充]`
- **结构化文本原则 (Structured Text Principles)**: 待完善描述 `[Source: 待补充]`
- **语境重解释 (Contextual Re-interpretation)**: 待完善描述 `[Source: 待补充]`
- **对比原则结构 (When/Should/Rather/Because)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Sub-question Sub-answer Sequence**: 待完善描述 `[Source: 待补充]`
- **Query Decomposition**: 待完善描述 `[Source: 待补充]`
- **System 2 Deliberative Memory**: 待完善描述 `[Source: 待补充]`
- **Uncertainty-based Retrieval**: 待完善描述 `[Source: 待补充]`
- **Reflection Memory**: 待完善描述 `[Source: 待补充]`
- **Trajectory Reflection**: 待完善描述 `[Source: 待补充]`
- **Dynamic Memory Scheduling**: 待完善描述 `[Source: 待补充]`
- **System 1 Intuitive Memory**: 待完善描述 `[Source: 待补充]`
- **Confidence Assessment Log**: 待完善描述 `[Source: 待补充]`
- **Reasoning Trajectory Logs**: 待完善描述 `[Source: 待补充]`
- **External Knowledge Base Snippets**: 待完善描述 `[Source: 待补充]`
- **Multi-agent Reasoning Trace**: 待完善描述 `[Source: 待补充]`
- **Intermediate Token Streams**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **LLM Internal State**: 待完善描述 `[Source: 待补充]`
- **Procedural Memory**: 待完善描述 `[Source: 待补充]`
- **Working Memory**: 待完善描述 `[Source: 待补充]`
- **Latent Token Sequence**: 待完善描述 `[Source: 待补充]`
- **Planning Memory**: 待完善描述 `[Source: 待补充]`
- **Reasoning Augmentation**: 待完善描述 `[Source: 待补充]`
- **Latent Tokens**: 待完善描述 `[Source: 待补充]`
- **Memory Triggering**: 待完善描述 `[Source: 待补充]`
- **Generative Latent Memory**: 待完善描述 `[Source: 待补充]`
- **Memory Weaving**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **记忆检索 (Memory Retrieval)**: 待完善描述 `[Source: 待补充]`
- **记忆整合 (Memory Integration)**: 待完善描述 `[Source: 待补充]`
- **ReasoningBank 推理记忆库**: 待完善描述 `[Source: 待补充]`
- **LLM 基座模型 (LLM Base Model)**: 待完善描述 `[Source: 待补充]`
- **经验蒸馏 (Experience Distillation)**: 待完善描述 `[Source: 待补充]`
- **经验池 (Experience Pool)**: 待完善描述 `[Source: 待补充]`
- **推理记忆 (Reasoning Memory)**: 待完善描述 `[Source: 待补充]`
- **向量数据库 (Vector Database)**: 待完善描述 `[Source: 待补充]`
- **经验记忆 (Experience Memory)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **记忆块 (Memory Block)**: 待完善描述 `[Source: 待补充]`
- **核心记忆 (Core Memory)**: 待完善描述 `[Source: 待补充]`
- **记忆构建策略 (Memory Construction Strategy)**: 待完善描述 `[Source: 待补充]`
- **持久化存储 (Persistent Storage)**: 待完善描述 `[Source: 待补充]`
- **多轮交互序列 (Multi-turn Interaction Sequence)**: 待完善描述 `[Source: 待补充]`
- **记忆写入 (Memory Write)**: 待完善描述 `[Source: 待补充]`
- **混合记忆架构 (Hybrid Memory Architecture)**: 待完善描述 `[Source: 待补充]`
- **问答评估对 (QA Evaluation Pair)**: 待完善描述 `[Source: 待补充]`
- **情景记忆 (Episodic Memory)**: 待完善描述 `[Source: 待补充]`
- **记忆读取 (Memory Read)**: 待完善描述 `[Source: 待补充]`
- **语义记忆 (Semantic Memory)**: 待完善描述 `[Source: 待补充]`
- **记忆更新 (Memory Update)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Compressed Context Sequence**: 待完善描述 `[Source: 待补充]`
- **Knowledge Distillation Transfer**: 待完善描述 `[Source: 待补充]`
- **Interaction History Memory**: 待完善描述 `[Source: 待补充]`
- **Distilled Student Compressor Model**: 待完善描述 `[Source: 待补充]`
- **Guideline-Guided Compression**: 待完善描述 `[Source: 待补充]`
- **Environment Observation Memory**: 待完善描述 `[Source: 待补充]`
- **Contrastive Feedback Optimization**: 待完善描述 `[Source: 待补充]`
- **Contrastive Trajectory Pair**: 待完善描述 `[Source: 待补充]`
- **Natural Language Compression Guidelines**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Hierarchical Memory Bank**: 待完善描述 `[Source: 待补充]`
- **Common Knowledge Memory**: 待完善描述 `[Source: 待补充]`
- **Parameter Injection**: 待完善描述 `[Source: 待补充]`
- **Transformer Parameters**: 待完善描述 `[Source: 待补充]`
- **Parametric Memory**: 待完善描述 `[Source: 待补充]`
- **Long-tail Knowledge Memory**: 待完善描述 `[Source: 待补充]`
- **Feed-Forward Memory Blocks**: 待完善描述 `[Source: 待补充]`
- **Anchor Model Parameters**: 待完善描述 `[Source: 待补充]`
- **Context-dependent Memory Block Fetching**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **上下文修剪 (Context Pruning)**: 待完善描述 `[Source: 待补充]`
- **上下文窗口 (Context Window)**: 待完善描述 `[Source: 待补充]`
- **条目化子弹点 (Itemized Bullet Entries)**: 待完善描述 `[Source: 待补充]`
- **静态提示 (Static Prompt)**: 待完善描述 `[Source: 待补充]`
- **进化上下文 (Evolving Context)**: 待完善描述 `[Source: 待补充]`
- **结构化剧本 (Structured Playbook)**: 待完善描述 `[Source: 待补充]`
- **上下文数据库 (ContextDB)**: 待完善描述 `[Source: 待补充]`
- **增量 Delta 更新 (Incremental Delta Update)**: 待完善描述 `[Source: 待补充]`
- **语义去重 (Semantic Deduplication)**: 待完善描述 `[Source: 待补充]`
- **KV 缓存 (KV Cache)**: 待完善描述 `[Source: 待补充]`
- **向量数据库 (Vector Database)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Task Trajectories (任务轨迹)**: 待完善描述 `[Source: 待补充]`
- **Memory Units (记忆单元)**: 待完善描述 `[Source: 待补充]`
- **Orchestrator Memory (编排器记忆)**: 待完善描述 `[Source: 待补充]`
- **Task Agent Memory (任务代理记忆)**: 待完善描述 `[Source: 待补充]`
- **Central Memory Database (中央记忆库)**: 待完善描述 `[Source: 待补充]`
- **Modular Procedural Memory (模块化过程记忆)**: 待完善描述 `[Source: 待补充]`
- **Semantic Retrieval (语义检索)**: 待完善描述 `[Source: 待补充]`
- **Agent Context Window (代理上下文窗口)**: 待完善描述 `[Source: 待补充]`
- **Memory Decomposition (记忆分解)**: 待完善描述 `[Source: 待补充]`
- **Memory Allocation (记忆分配)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Hierarchical Schemata Memory**: 待完善描述 `[Source: 待补充]`
- **LLM-generated Node Summaries**: 待完善描述 `[Source: 待补充]`
- **Constructivist Accommodation (Incremental Clustering)**: 待完善描述 `[Source: 待补充]`
- **Constructivist Agentic Memory (CAM)**: 待完善描述 `[Source: 待补充]`
- **Prune-and-Grow Retrieval**: 待完善描述 `[Source: 待补充]`
- **Text Embeddings**: 待完善描述 `[Source: 待补充]`
- **Hierarchical Memory Graph**: 待完善描述 `[Source: 待补充]`
- **Multi-parent Memory Nodes**: 待完善描述 `[Source: 待补充]`
- **Constructivist Assimilation (Node Replication)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Tool Capability Memory (工具能力记忆)**: 待完善描述 `[Source: 待补充]`
- **Quality Feedback Scores (质量反馈分数)**: 待完善描述 `[Source: 待补充]`
- **Retrieve-Refine Update (检索 - 精炼更新)**: 待完善描述 `[Source: 待补充]`
- **Memory Induction (记忆诱导)**: 待完善描述 `[Source: 待补充]`
- **Proficiency Classification Schema (熟练度分类法)**: 待完善描述 `[Source: 待补充]`
- **Tool Solutions (工具解决方案)**: 待完善描述 `[Source: 待补充]`
- **Learnable Memory (可学习记忆)**: 待完善描述 `[Source: 待补充]`
- **Structured Capability Memory (结构化能力记忆)**: 待完善描述 `[Source: 待补充]`
- **Memory Consolidation (记忆巩固)**: 待完善描述 `[Source: 待补充]`
- **Capability Assessment Text (能力评估文本)**: 待完善描述 `[Source: 待补充]`
- **Experience-Induced Memory Entries (经验诱导记忆条目)**: 待完善描述 `[Source: 待补充]`
- **Task Prompts (任务 Prompt)**: 待完善描述 `[Source: 待补充]`
- **RAG-based Memory Retrieval (基于 RAG 的记忆检索)**: 待完善描述 `[Source: 待补充]`
- **Vector Database Memory Store (向量库记忆存储)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **画像模块 (Profile Module)**: 待完善描述 `[Source: 待补充]`
- **持久记忆 (Persistent Memory)**: 待完善描述 `[Source: 待补充]`
- **交互历史数据 (Interaction History Data)**: 待完善描述 `[Source: 待补充]`
- **用户偏好特征 (User Preference Features)**: 待完善描述 `[Source: 待补充]`
- **跨交互读写 (Cross-interaction Read/Write)**: 待完善描述 `[Source: 待补充]`
- **动态用户画像 (Dynamic User Profiles)**: 待完善描述 `[Source: 待补充]`
- **向量数据库 (Vector Database)**: 待完善描述 `[Source: 待补充]`
- **自验证 (Self-Validation)**: 待完善描述 `[Source: 待补充]`
- **多源检索 (Multi-source Retrieval)**: 待完善描述 `[Source: 待补充]`
- **多源检索模块 (Multi-source Retrieval Module)**: 待完善描述 `[Source: 待补充]`
- **动态演化更新 (Dynamic Evolution Update)**: 待完善描述 `[Source: 待补充]`
- **记忆库 (Memory Bank)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Token Prior**: 待完善描述 `[Source: 待补充]`
- **Prior Injection**: 待完善描述 `[Source: 待补充]`
- **Experiential Knowledge**: 待完善描述 `[Source: 待补充]`
- **Input Token Sequence**: 待完善描述 `[Source: 待补充]`
- **API Context Window**: 待完善描述 `[Source: 待补充]`
- **Rollout Group**: 待完善描述 `[Source: 待补充]`
- **Semantic Advantage Extraction**: 待完善描述 `[Source: 待补充]`
- **Semantic Advantage Distribution**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Action-Future State Pairs (动作 - 未来状态对)**: 待完善描述 `[Source: 待补充]`
- **Future State Collection (未来状态收集)**: 待完善描述 `[Source: 待补充]`
- **Agent Interaction Logs (智能体交互日志)**: 待完善描述 `[Source: 待补充]`
- **Reward-Free Interaction Memory (无奖励交互记忆)**: 待完善描述 `[Source: 待补充]`
- **LLM Context Window (大模型上下文窗口)**: 待完善描述 `[Source: 待补充]`
- **Implicit World Modeling (隐式世界建模)**: 待完善描述 `[Source: 待补充]`
- **Implicit World Model Representations (隐式世界模型表示)**: 待完善描述 `[Source: 待补充]`
- **Self-Reflection (自我反思)**: 待完善描述 `[Source: 待补充]`
- **Early Experience (早期经验)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Auto-scaling Collection (自动扩展收集)**: 待完善描述 `[Source: 待补充]`
- **Text Memory (文本记忆 - 基线对比)**: 待完善描述 `[Source: 待补充]`
- **Vector Database (向量数据库)**: 待完善描述 `[Source: 待补充]`
- **FAISS Vector Index (FAISS 向量索引)**: 待完善描述 `[Source: 待补充]`
- **Multimodal Trajectory Memory (多模态轨迹记忆)**: 待完善描述 `[Source: 待补充]`
- **Screenshot-Action Pairs (截图 - 动作对)**: 待完善描述 `[Source: 待补充]`
- **Fixed-length Continuous Embedding (固定长度连续嵌入)**: 待完善描述 `[Source: 待补充]`
- **Trajectory Compression (轨迹压缩)**: 待完善描述 `[Source: 待补充]`
- **Similarity-based Retrieval (基于相似度的检索)**: 待完善描述 `[Source: 待补充]`
- **Continuous Memory (连续记忆)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **DOM/Accessibility Tree (DOM/可访问性树)**: 待完善描述 `[Source: 待补充]`
- **Memory Compression (记忆压缩)**: 待完善描述 `[Source: 待补充]`
- **Intermediate Conclusion Storage (中间结论存储)**: 待完善描述 `[Source: 待补充]`
- **Key Conclusion Extraction (关键结论提取)**: 待完善描述 `[Source: 待补充]`
- **Memory Recording (记忆记录)**: 待完善描述 `[Source: 待补充]`
- **Explicit Memory (显式记忆)**: 待完善描述 `[Source: 待补充]`
- **Context-Embedded Memory (上下文嵌入记忆)**: 待完善描述 `[Source: 待补充]`
- **Reasoning Chain Memory (推理链记忆)**: 待完善描述 `[Source: 待补充]`
- **Webpage State (网页状态)**: 待完善描述 `[Source: 待补充]`
- **Text Context (文本上下文)**: 待完善描述 `[Source: 待补充]`
- **Conclusion Memory (结论记忆)**: 待完善描述 `[Source: 待补充]`
- **<conclusion> Tag Structure (结论标签结构)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Context Curation (上下文策展)**: 待完善描述 `[Source: 待补充]`
- **Interaction Record Sequence (交互记录序列)**: 待完善描述 `[Source: 待补充]`
- **Prune&Write Memory Primitives (记忆原语结构)**: 待完善描述 `[Source: 待补充]`
- **Inline Memory Action (原地记忆动作执行)**: 待完善描述 `[Source: 待补充]`
- **Segmented Trajectory (轨迹分段)**: 待完善描述 `[Source: 待补充]`
- **Token-based Context Window (基于 Token 的上下文窗口)**: 待完善描述 `[Source: 待补充]`
- **Model Policy Parameters (模型策略参数)**: 待完善描述 `[Source: 待补充]`
- **Interaction Logs (交互日志)**: 待完善描述 `[Source: 待补充]`
- **Prune (删除冗余上下文 ID)**: 待完善描述 `[Source: 待补充]`
- **Working Memory (工作记忆)**: 待完善描述 `[Source: 待补充]`
- **Task-Integrated Memory (任务整合记忆)**: 待完善描述 `[Source: 待补充]`
- **Write (写入总结内容)**: 待完善描述 `[Source: 待补充]`
- **Curated Memory (策展记忆)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **OWL Knowledge Graph**: 待完善描述 `[Source: 待补充]`
- **Non-structured Dialogue Text**: 待完善描述 `[Source: 待补充]`
- **Asynchronous Update**: 待完善描述 `[Source: 待补充]`
- **Neuro-symbolic Knowledge Extraction**: 待完善描述 `[Source: 待补充]`
- **Beam Search Path Planning**: 待完善描述 `[Source: 待补充]`
- **Conflict Resolution**: 待完善描述 `[Source: 待补充]`
- **OWL Ontology**: 待完善描述 `[Source: 待补充]`
- **Reasoning Tree (RT)**: 待完善描述 `[Source: 待补充]`
- **Dynamic Structured Memory (DSM)**: 待完善描述 `[Source: 待补充]`
- **Abstract Meaning Representation (AMR)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Graph Database**: 待完善描述 `[Source: 待补充]`
- **L0 Microscopic Evidence Memory**: 待完善描述 `[Source: 待补充]`
- **External Memory Storage**: 待完善描述 `[Source: 待补充]`
- **Multi-scale Effective Theory Structure**: 待完善描述 `[Source: 待补充]`
- **LLM Context Window**: 待完善描述 `[Source: 待补充]`
- **Threshold-triggered Evolution**: 待完善描述 `[Source: 待补充]`
- **Three-layer Memory State Space**: 待完善描述 `[Source: 待补充]`
- **Dynamic Knowledge Graph**: 待完善描述 `[Source: 待补充]`
- **Renormalization Operators (R_K1, R_K2, R_K3)**: 待完善描述 `[Source: 待补充]`
- **L2 Macroscopic Profile Memory**: 待完善描述 `[Source: 待补充]`
- **Coarse-graining**: 待完善描述 `[Source: 待补充]`
- **Fast-Slow Variable Separation**: 待完善描述 `[Source: 待补充]`
- **L1 Mesoscopic Knowledge Memory**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Soft Update (Incremental Add)**: 待完善描述 `[Source: 待补充]`
- **STM Buffer**: 待完善描述 `[Source: 待补充]`
- **Buffer-Triggered Summarization**: 待完善描述 `[Source: 待补充]`
- **Topic-Aware Segmentation**: 待完善描述 `[Source: 待补充]`
- **Offline Parallel Update Queue**: 待完善描述 `[Source: 待补充]`
- **Iterative Pre-compression**: 待完善描述 `[Source: 待补充]`
- **Topic-Summary-Turn Structure**: 待完善描述 `[Source: 待补充]`
- **Topic Summaries**: 待完善描述 `[Source: 待补充]`
- **Short-Term Memory (Light2/STM)**: 待完善描述 `[Source: 待补充]`
- **Sensory Memory (Light1)**: 待完善描述 `[Source: 待补充]`
- **Long-Term Memory (Light3/LTM)**: 待完善描述 `[Source: 待补充]`
- **Compressed Topic Fragments**: 待完善描述 `[Source: 待补充]`
- **Dialogue Text Sequences**: 待完善描述 `[Source: 待补充]`
- **Offline Parallel Update**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Tool Retrieval**: 待完善描述 `[Source: 待补充]`
- **Tool API Descriptions**: 待完善描述 `[Source: 待补充]`
- **Task Instructions**: 待完善描述 `[Source: 待补充]`
- **Working Memory**: 待完善描述 `[Source: 待补充]`
- **Multi-turn Interaction Trajectories**: 待完善描述 `[Source: 待补充]`
- **Tool Memory**: 待完善描述 `[Source: 待补充]`
- **Interaction Compression**: 待完善描述 `[Source: 待补充]`
- **Memory Folding**: 待完善描述 `[Source: 待补充]`
- **Folded Memory Representation**: 待完善描述 `[Source: 待补充]`
- **Scenario Memory**: 待完善描述 `[Source: 待补充]`
- **Structured Memory**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Procedural Tool Memory (MCP Box)**: 待完善描述 `[Source: 待补充]`
- **Self-Evolutionary Curation**: 待完善描述 `[Source: 待补充]`
- **Task Execution Logs**: 待完善描述 `[Source: 待补充]`
- **Semantic Embedding Index**: 待完善描述 `[Source: 待补充]`
- **Code Toolkits**: 待完善描述 `[Source: 待补充]`
- **Dual-Strategy Retrieval (Threshold/Top-k)**: 待完善描述 `[Source: 待补充]`
- **Abstracted MCP Repository**: 待完善描述 `[Source: 待补充]`
- **Task Trajectory Memory**: 待完善描述 `[Source: 待补充]`
- **Semantic Embeddings**: 待完善描述 `[Source: 待补充]`
- **MCP Abstraction (Parameterization)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **上下文 Token (Context Tokens)**: 待完善描述 `[Source: 待补充]`
- **折叠记忆 (Folded Memory)**: 待完善描述 `[Source: 待补充]`
- **细粒度浓缩 (Granular Condensation)**: 待完善描述 `[Source: 待补充]`
- **LLM 上下文窗口 (LLM Context Window)**: 待完善描述 `[Source: 待补充]`
- **推理 - 动作 - 观察三元组 (Reasoning-Action-Observation Triplet)**: 待完善描述 `[Source: 待补充]`
- **动态上下文工作区 (Dynamic Context Workspace)**: 待完善描述 `[Source: 待补充]`
- **主动折叠 (Proactive Folding)**: 待完善描述 `[Source: 待补充]`
- **多尺度历史轨迹 (Multi-scale History Trajectory)**: 待完善描述 `[Source: 待补充]`
- **深度整合 (Deep Consolidation)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Memory Fusion**: 待完善描述 `[Source: 待补充]`
- **Full Interaction History**: 待完善描述 `[Source: 待补充]`
- **Memory Update**: 待完善描述 `[Source: 待补充]`
- **Search Tool Response**: 待完善描述 `[Source: 待补充]`
- **Trajectory-level Advantage Propagation**: 待完善描述 `[Source: 待补充]`
- **LLM Context Window**: 待完善描述 `[Source: 待补充]`
- **Multi-context Group Structure**: 待完善描述 `[Source: 待补充]`
- **Compact Memory**: 待完善描述 `[Source: 待补充]`
- **Iterative Memory Loop**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Reasoning Model**: 待完善描述 `[Source: 待补充]`
- **Adaptive Task Generation**: 待完善描述 `[Source: 待补充]`
- **Replay Buffer**: 待完善描述 `[Source: 待补充]`
- **Experience Synthesis**: 待完善描述 `[Source: 待补充]`
- **Reasoning-based Feedback**: 待完善描述 `[Source: 待补充]`
- **Synthetic Experience**: 待完善描述 `[Source: 待补充]`
- **Abstract State**: 待完善描述 `[Source: 待补充]`
- **Sim-to-Real Transfer**: 待完善描述 `[Source: 待补充]`
- **Experience Model**: 待完善描述 `[Source: 待补充]`
- **Hybrid Replay Buffer**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **成功/失败轨迹经验 (Success/Failure Trajectory Experience)**: 待完善描述 `[Source: 待补充]`
- **反思经验 (Reflection Experience)**: 待完善描述 `[Source: 待补充]`
- **反思模块 (Reflection Module)**: 待完善描述 `[Source: 待补充]`
- **版本化经验库 (Versioned Experience Library)**: 待完善描述 `[Source: 待补充]`
- **经验库演化 (Experience Library Evolution)**: 待完善描述 `[Source: 待补充]`
- **经验检索增强 (Experience Retrieval Augmentation)**: 待完善描述 `[Source: 待补充]`
- **经验库存储系统 (Experience Library Storage System)**: 待完善描述 `[Source: 待补充]`
- **经验条目 (Experience Entries)**: 待完善描述 `[Source: 待补充]`
- **经验反思 (Experience Reflection)**: 待完善描述 `[Source: 待补充]`
- **结构化经验 (Structured Experience)**: 待完善描述 `[Source: 待补充]`
- **经验继承 (Experience Inheritance)**: 待完善描述 `[Source: 待补充]`
- **结构化经验库 (Structured Experience Library)**: 待完善描述 `[Source: 待补充]`
- **LLM 智能体 (LLM Agent)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Self-Evolving Experience Memory**: 待完善描述 `[Source: 待补充]`
- **Composite Reward Signal**: 待完善描述 `[Source: 待补充]`
- **Interaction Trajectory Log**: 待完善描述 `[Source: 待补充]`
- **Vector Embeddings**: 待完善描述 `[Source: 待补充]`
- **Textual Trajectories**: 待完善描述 `[Source: 待补充]`
- **Model Parameters**: 待完善描述 `[Source: 待补充]`
- **Environment Profile**: 待完善描述 `[Source: 待补充]`
- **Self-Attributing**: 待完善描述 `[Source: 待补充]`
- **Self-Navigating**: 待完善描述 `[Source: 待补充]`
- **Synthetic Task Memory**: 待完善描述 `[Source: 待补充]`
- **Self-Questioning**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **连续潜在上下文 (Continuous Latent Contexts)**: 待完善描述 `[Source: 待补充]`
- **潜在空间表示 (Latent Space Representations)**: 待完善描述 `[Source: 待补充]`
- **推理期无缝调用 (Inference-time Invocation)**: 待完善描述 `[Source: 待补充]`
- **双模块记忆框架 (Dual-module Memory Framework)**: 待完善描述 `[Source: 待补充]`
- **长期语义巩固记忆 (Long-term Semantic Consolidation Memory)**: 待完善描述 `[Source: 待补充]`
- **信息分流 (Information Shunting)**: 待完善描述 `[Source: 待补充]`
- **动态更新 (Dynamic Update)**: 待完善描述 `[Source: 待补充]`
- **潜在视觉记忆模块 (Latent Vision Memory Module)**: 待完善描述 `[Source: 待补充]`
- **短期感知保留记忆 (Short-term Perception Retention Memory)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Attribute-Context Dual Layer**: 待完善描述 `[Source: 待补充]`
- **User Interaction Logs**: 待完善描述 `[Source: 待补充]`
- **Active User Profile**: 待完善描述 `[Source: 待补充]`
- **Active Feature Extraction**: 待完善描述 `[Source: 待补充]`
- **Dynamic Memory Evolution**: 待完善描述 `[Source: 待补充]`
- **FAISS Vector Index**: 待完善描述 `[Source: 待补充]`
- **Interaction Event Record**: 待完善描述 `[Source: 待补充]`
- **Hierarchical Memory Architecture**: 待完善描述 `[Source: 待补充]`
- **Hierarchical Retrieval**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Event-Centric Memory (EMem)**: 待完善描述 `[Source: 待补充]`
- **Recall-oriented LLM Filtering**: 待完善描述 `[Source: 待补充]`
- **Offline Event Extraction**: 待完善描述 `[Source: 待补充]`
- **Long-Term Conversational Memory**: 待完善描述 `[Source: 待补充]`
- **Personalized PageRank Propagation**: 待完善描述 `[Source: 待补充]`
- **LLM Agent Context Window**: 待完善描述 `[Source: 待补充]`
- **Heterogeneous Memory Graph**: 待完善描述 `[Source: 待补充]`
- **Embedding Vector Index**: 待完善描述 `[Source: 待补充]`
- **Enriched EDU (Elementary Discourse Unit)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Page-based Storage**: 待完善描述 `[Source: 待补充]`
- **Token Embeddings**: 待完善描述 `[Source: 待补充]`
- **Concise Session Snapshot**: 待完善描述 `[Source: 待补充]`
- **Context Compilation**: 待完善描述 `[Source: 待补充]`
- **Offline Lightweight Memory**: 待完善描述 `[Source: 待补充]`
- **Just-In-Time Compiled Context**: 待完善描述 `[Source: 待补充]`
- **Vector Store**: 待完善描述 `[Source: 待补充]`
- **Optimized Context Window**: 待完善描述 `[Source: 待补充]`
- **Parallel Search**: 待完善描述 `[Source: 待补充]`
- **Online Deep Research Memory**: 待完善描述 `[Source: 待补充]`
- **Reflective Iteration**: 待完善描述 `[Source: 待补充]`
- **Text Session Trajectories**: 待完善描述 `[Source: 待补充]`
- **Incremental Memory Update**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **短期工作记忆**: 待完善描述 `[Source: 待补充]`
- **对话记忆**: 待完善描述 `[Source: 待补充]`
- **选择性遗忘**: 待完善描述 `[Source: 待补充]`
- **S3 加密生物信息**: 待完善描述 `[Source: 待补充]`
- **会话内缓冲区**: 待完善描述 `[Source: 待补充]`
- **冲突解决策略**: 待完善描述 `[Source: 待补充]`
- **模块化记忆服务**: 待完善描述 `[Source: 待补充]`
- **情景事件记忆**: 待完善描述 `[Source: 待补充]`
- **感官情境记忆**: 待完善描述 `[Source: 待补充]`
- **动态记忆注入**: 待完善描述 `[Source: 待补充]`
- **Firestore 对话历史**: 待完善描述 `[Source: 待补充]`
- **时间戳事件存储**: 待完善描述 `[Source: 待补充]`
- **外部 API 数据**: 待完善描述 `[Source: 待补充]`
- **中央记忆控制器**: 待完善描述 `[Source: 待补充]`
- **长期用户记忆**: 待完善描述 `[Source: 待补充]`
- **信封加密存储**: 待完善描述 `[Source: 待补充]`
- **基于 Token 的修剪机制**: 待完善描述 `[Source: 待补充]`
- **异步记忆更新**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Visual Memory**: 待完善描述 `[Source: 待补充]`
- **Semantic Memory**: 待完善描述 `[Source: 待补充]`
- **Episodic Memory**: 待完善描述 `[Source: 待补充]`
- **External Vector Database**: 待完善描述 `[Source: 待补充]`
- **Iterative Retrieval Stop**: 待完善描述 `[Source: 待补充]`
- **Text Summaries**: 待完善描述 `[Source: 待补充]`
- **Time Segments**: 待完善描述 `[Source: 待补充]`
- **Adaptive Retrieval**: 待完善描述 `[Source: 待补充]`
- **Multi-temporal Granularity Index**: 待完善描述 `[Source: 待补充]`
- **Video Frames**: 待完善描述 `[Source: 待补充]`
- **Memory Construction**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Lightweight Neural Network Parameters**: 待完善描述 `[Source: 待补充]`
- **Image Embeddings**: 待完善描述 `[Source: 待补充]`
- **Three-layer Memory System**: 待完善描述 `[Source: 待补充]`
- **Short-term Memory (STM)**: 待完善描述 `[Source: 待补充]`
- **Long-term Memory (LTM)**: 待完善描述 `[Source: 待补充]`
- **Knowledge Distillation**: 待完善描述 `[Source: 待补充]`
- **Semantic Memory**: 待完善描述 `[Source: 待补充]`
- **Retrieval Augmentation**: 待完善描述 `[Source: 待补充]`
- **Sliding Window Caching**: 待完善描述 `[Source: 待补充]`
- **Episodic Memory**: 待完善描述 `[Source: 待补充]`
- **Text Embeddings**: 待完善描述 `[Source: 待补充]`
- **Dynamic Memory Expansion**: 待完善描述 `[Source: 待补充]`
- **Parametric Memory**: 待完善描述 `[Source: 待补充]`
- **Video Embeddings**: 待完善描述 `[Source: 待补充]`
- **Multimodal Knowledge Graph (MMKG)**: 待完善描述 `[Source: 待补充]`
- **Central Memory Orchestrator**: 待完善描述 `[Source: 待补充]`
- **Core Memory**: 待完善描述 `[Source: 待补充]`
- **Supervised Fine-tuning (SFT)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Expert Adapters**: 待完善描述 `[Source: 待补充]`
- **Memory Update**: 待完善描述 `[Source: 待补充]`
- **Small Language Model (SLM)**: 待完善描述 `[Source: 待补充]`
- **Text Memory**: 待完善描述 `[Source: 待补充]`
- **Visual Memory**: 待完善描述 `[Source: 待补充]`
- **Memory Generation**: 待完善描述 `[Source: 待补充]`
- **Small Vision-Language Model (SVLM)**: 待完善描述 `[Source: 待补充]`
- **Local Memory Bank**: 待完善描述 `[Source: 待补充]`
- **Memory Extraction**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Memory Pool**: 待完善描述 `[Source: 待补充]`
- **Scenario-aware Retrieval**: 待完善描述 `[Source: 待补充]`
- **Dynamic Procedural Memory**: 待完善描述 `[Source: 待补充]`
- **Scenario-aware Index**: 待完善描述 `[Source: 待补充]`
- **Utility-based Deletion**: 待完善描述 `[Source: 待补充]`
- **Embedding Vectors**: 待完善描述 `[Source: 待补充]`
- **LLM Agent Memory System**: 待完善描述 `[Source: 待补充]`
- **Structured Experience Records**: 待完善描述 `[Source: 待补充]`
- **Structured Experience Memory**: 待完善描述 `[Source: 待补充]`
- **Failure-aware Reflection**: 待完善描述 `[Source: 待补充]`
- **Experience Rewriting**: 待完善描述 `[Source: 待补充]`
- **Experience-Driven Memory**: 待完善描述 `[Source: 待补充]`
- **Keypoint-level Experience Structure**: 待完善描述 `[Source: 待补充]`
- **Experience Distillation**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Vector Embeddings**: 待完善描述 `[Source: 待补充]`
- **Agentic Memory**: 待完善描述 `[Source: 待补充]`
- **Weighted Knowledge Graph**: 待完善描述 `[Source: 待补充]`
- **Knowledge Triples**: 待完善描述 `[Source: 待补充]`
- **Exponential Time-Decay Weighting**: 待完善描述 `[Source: 待补充]`
- **Hybrid Storage Layer (SQLite + ChromaDB)**: 待完善描述 `[Source: 待补充]`
- **Dynamic Session Summary**: 待完善描述 `[Source: 待补充]`
- **User-Input Triple Extraction**: 待完善描述 `[Source: 待补充]`
- **Structured Dialogue Logs**: 待完善描述 `[Source: 待补充]`
- **Incremental Summary Update**: 待完善描述 `[Source: 待补充]`
- **Session IDs**: 待完善描述 `[Source: 待补充]`
- **Episodic Memory (Session Summary)**: 待完善描述 `[Source: 待补充]`
- **Semantic Memory (Knowledge Graph)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **保留 (Retain)**: 待完善描述 `[Source: 待补充]`
- **合成实体摘要 (Entity Summaries)**: 待完善描述 `[Source: 待补充]`
- **结构化推理基底 (Structured First-Class Substrate)**: 待完善描述 `[Source: 待补充]`
- **回忆 (Recall)**: 待完善描述 `[Source: 待补充]`
- **结构化记忆库 (Structured Memory Bank)**: 待完善描述 `[Source: 待补充]`
- **反思 (Reflect)**: 待完善描述 `[Source: 待补充]`
- **反思层 (Reflection Layer)**: 待完善描述 `[Source: 待补充]`
- **世界事实 (World Facts)**: 待完善描述 `[Source: 待补充]`
- **四逻辑网络 (Four Logical Networks)**: 待完善描述 `[Source: 待补充]`
- **演化信念 (Evolving Beliefs)**: 待完善描述 `[Source: 待补充]`
- **智能体经验 (Agent Experience)**: 待完善描述 `[Source: 待补充]`
- **时间实体感知记忆层 (Temporal Entity-Aware Memory Layer)**: 待完善描述 `[Source: 待补充]`
- **对话流 (Dialogue Stream)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **外部向量数据库 (External Vector Database)**: 待完善描述 `[Source: 待补充]`
- **神经网络参数 (Neural Parameters)**: 待完善描述 `[Source: 待补充]`
- **记忆演化 (Memory Evolution)**: 待完善描述 `[Source: 待补充]`
- **令牌级记忆 (Token-level Memory)**: 待完善描述 `[Source: 待补充]`
- **事实记忆 (Factual Memory)**: 待完善描述 `[Source: 待补充]`
- **工作记忆 (Working Memory)**: 待完善描述 `[Source: 待补充]`
- **记忆检索 (Memory Retrieval)**: 待完善描述 `[Source: 待补充]`
- **LLM 上下文 (LLM Context)**: 待完善描述 `[Source: 待补充]`
- **潜在空间向量 (Latent Space Vectors)**: 待完善描述 `[Source: 待补充]`
- **经验记忆 (Experiential Memory)**: 待完善描述 `[Source: 待补充]`
- **潜在级记忆 (Latent Memory)**: 待完善描述 `[Source: 待补充]`
- **上下文窗口 (Context Window)**: 待完善描述 `[Source: 待补充]`
- **模型权重 (Model Weights)**: 待完善描述 `[Source: 待补充]`
- **记忆形成 (Memory Formation)**: 待完善描述 `[Source: 待补充]`
- **记忆遗忘 (Memory Forgetting)**: 待完善描述 `[Source: 待补充]`
- **参数级记忆 (Parametric Memory)**: 待完善描述 `[Source: 待补充]`
- **向量存储 (Vector Storage)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Source Index Anchored EDU Nodes**: 待完善描述 `[Source: 待补充]`
- **EDU-based Context Memory**: 待完善描述 `[Source: 待补充]`
- **Structured Discourse Memory**: 待完善描述 `[Source: 待补充]`
- **Query-Relevant Sub-Tree**: 待完善描述 `[Source: 待补充]`
- **Tree-to-Text Linearization**: 待完善描述 `[Source: 待补充]`
- **EDU Decomposition**: 待完善描述 `[Source: 待补充]`
- **Sub-Tree Ranking**: 待完善描述 `[Source: 待补充]`
- **Compressed Token Sequence**: 待完善描述 `[Source: 待补充]`
- **Elementary Discourse Unit (EDU) Tree**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Episodic Memory (情景记忆)**: 待完善描述 `[Source: 待补充]`
- **File-based State Persistence (基于文件的状态持久化)**: 待完善描述 `[Source: 待补充]`
- **Offline Browser Sandbox (离线浏览器沙盒)**: 待完善描述 `[Source: 待补充]`
- **Creed (不可变信条)**: 待完善描述 `[Source: 待补充]`
- **HTML/Markdown Logs (结构化日志)**: 待完善描述 `[Source: 待补充]`
- **Capability List (能力清单)**: 待完善描述 `[Source: 待补充]`
- **Self-Model (自我模型)**: 待完善描述 `[Source: 待补充]`
- **Synthetic User Behavior Streams (合成用户行为流)**: 待完善描述 `[Source: 待补充]`
- **Forward/Backward Learning Integration (前后向学习整合)**: 待完善描述 `[Source: 待补充]`
- **Nightly Self-Critique (夜间自评)**: 待完善描述 `[Source: 待补充]`
- **Memory Retrieval & Reuse (记忆检索复用)**: 待完善描述 `[Source: 待补充]`
- **Context Buffer (上下文缓冲区)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **模块化记忆空间 (Modular Memory Space)**: 待完善描述 `[Source: 待补充]`
- **元进化记忆系统 (Meta-Evolutionary Memory System)**: 待完善描述 `[Source: 待补充]`
- **编码模块 (Encode Module)**: 待完善描述 `[Source: 待补充]`
- **存储模块 (Store Module)**: 待完善描述 `[Source: 待补充]`
- **架构优化 (Architecture Optimization)**: 待完善描述 `[Source: 待补充]`
- **元进化 (Meta-Evolution)**: 待完善描述 `[Source: 待补充]`
- **经验知识 (Experiential Knowledge)**: 待完善描述 `[Source: 待补充]`
- **管理模块 (Manage Module)**: 待完善描述 `[Source: 待补充]`
- **元适应 (Meta-Adaptation)**: 待完善描述 `[Source: 待补充]`
- **检索模块 (Retrieve Module)**: 待完善描述 `[Source: 待补充]`
- **交互轨迹 (Interaction Trajectories)**: 待完善描述 `[Source: 待补充]`
- **记忆架构 (Memory Architecture)**: 待完善描述 `[Source: 待补充]`
- **蒸馏经验 (Distilled Experience)**: 待完善描述 `[Source: 待补充]`
- **可复用工具 (Reusable Tools)**: 待完善描述 `[Source: 待补充]`
- **联合进化 (Joint Evolution)**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Retrieve**: 待完善描述 `[Source: 待补充]`
- **Update**: 待完善描述 `[Source: 待补充]`
- **Tool-based Memory Interface**: 待完善描述 `[Source: 待补充]`
- **Text Interaction Trajectories**: 待完善描述 `[Source: 待补充]`
- **Agentic Memory**: 待完善描述 `[Source: 待补充]`
- **Long-Term Memory (LTM)**: 待完善描述 `[Source: 待补充]`
- **Summary**: 待完善描述 `[Source: 待补充]`
- **Add**: 待完善描述 `[Source: 待补充]`
- **Token-based Context**: 待完善描述 `[Source: 待补充]`
- **Short-Term Memory (STM)**: 待完善描述 `[Source: 待补充]`
- **Filter**: 待完善描述 `[Source: 待补充]`
- **Structured Memory Storage**: 待完善描述 `[Source: 待补充]`
- **Delete**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **MemCells (记忆细胞)**: 待完善描述 `[Source: 待补充]`
- **语义巩固 (Semantic Consolidation)**: 待完善描述 `[Source: 待补充]`
- **情节痕迹 (Episodic Trace)**: 待完善描述 `[Source: 待补充]`
- **MemScenes (记忆场景)**: 待完善描述 `[Source: 待补充]`
- **重构式回忆 (Reconstructed Recall)**: 待完善描述 `[Source: 待补充]`
- **MemScenes**: 待完善描述 `[Source: 待补充]`
- **语义场景 (Semantic Scene)**: 待完善描述 `[Source: 待补充]`
- **情节痕迹形成 (Episodic Trace Formation)**: 待完善描述 `[Source: 待补充]`
- **MemCells**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Intent-Experience-Utility Triplet**: 待完善描述 `[Source: 待补充]`
- **Structured Triplet (z, e, Q)**: 待完善描述 `[Source: 待补充]`
- **Vector Database**: 待完善描述 `[Source: 待补充]`
- **Episodic Memory**: 待完善描述 `[Source: 待补充]`
- **Utility-Enhanced Memory**: 待完善描述 `[Source: 待补充]`
- **Semantic Gating**: 待完善描述 `[Source: 待补充]`
- **Dual-stage Retrieval**: 待完善描述 `[Source: 待补充]`
- **External Memory Module**: 待完善描述 `[Source: 待补充]`
- **Runtime Q-value Update**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Intent-Aware Routing**: 待完善描述 `[Source: 待补充]`
- **Vector Embeddings**: 待完善描述 `[Source: 待补充]`
- **Slow Path Consolidation**: 待完善描述 `[Source: 待补充]`
- **Temporal Memory**: 待完善描述 `[Source: 待补充]`
- **Semantic Memory**: 待完善描述 `[Source: 待补充]`
- **Fast Path Ingestion**: 待完善描述 `[Source: 待补充]`
- **Adaptive Graph Traversal**: 待完善描述 `[Source: 待补充]`
- **Orthogonal Graph Representation**: 待完善描述 `[Source: 待补充]`
- **Graph Nodes**: 待完善描述 `[Source: 待补充]`
- **Entity Memory**: 待完善描述 `[Source: 待补充]`
- **Time-Varying Directed Multi-Graph**: 待完善描述 `[Source: 待补充]`
- **Causal Memory**: 待完善描述 `[Source: 待补充]`
- **Graph Edges**: 待完善描述 `[Source: 待补充]`

### 新增概念 (自动提取)
- **Event Graph**: 待完善描述 `[Source: 待补充]`
- **Incremental Event Segmentation**: 待完善描述 `[Source: 待补充]`
- **Logic Map**: 待完善描述 `[Source: 待补充]`
- **Event Nodes**: 待完善描述 `[Source: 待补充]`
- **Flat Memory**: 待完善描述 `[Source: 待补充]`
- **Event-Centric Memory**: 待完善描述 `[Source: 待补充]`
- **Structured Navigation Retrieval**: 待完善描述 `[Source: 待补充]`
- **Logical Edges**: 待完善描述 `[Source: 待补充]`
- **Logical Relation Linking**: 待完善描述 `[Source: 待补充]`

## 记忆操作机制

### 检索与遍历
- **Active Multi-Path Search** (CompassMem): 规划器-探索者-响应者架构
- **Policy-guided Graph Traversal** (MAGMA): 意图感知路由 + 自适应遍历
- **Two-Phase Retrieval** (MemRL): 语义召回 + 价值感知选择
- **EDU Decomposition** (EMem): 基于 neo-Davidsonian 事件语义学的命题分解
- **Adaptive Multi-Modal Retrieval** (WorldMM): 自适应选择文本/视觉记忆源
- **Weighted Semantic Retrieval** (Memoria): 指数衰减优先检索近期信息

### 压缩与摘要
- **Structure-then-Select** (From Context to EDUs): 先结构后选择的压缩范式
- **Failure-Driven Compression Guideline Optimization**: 分析完整上下文成功但压缩上下文失败的轨迹
- **Autonomous Memory Folding**: 压缩过去交互为结构化情景/工作/工具记忆
- **Incremental Overlapping Clustering**: 支持连贯层次化摘要和在线批量整合
- **Distilled Compressor**: 将优化后的 LLM 压缩器蒸馏到更小模型
- **Dynamic Session Summarization** (Memoria): 会话级动态摘要生成

### 核心操作框架
- **Retain-Recall-Reflect** (Hindsight): 三元核心操作框架

---

## 记忆载体类型

- **Visual Memory Corpus** (WorldMM): 视觉特征嵌入 + 时间戳索引
- **Entity-Argument Structures** (EMem): 参与者 - 时间 - 上下文的命题捆绑

---

## 记忆功能定位

- **Multi-session Conversational Memory** (Hindsight, Memoria): 多会话对话记忆
- **Long Video Reasoning** (WorldMM): 长视频推理
- **Personalized Conversational AI** (Memoria): 个性化对话 AI

---

## 评估基准

- **LongMemEval**: 长期记忆评估基准 (Hindsight 91.4%, SOTA)
- **LoCoMo**: 长时对话记忆基准 (Hindsight 89.61%)
- **VideoMME (long)**: 长视频多模态评估 (WorldMM)
- **LVBench**: 长视频基准 (WorldMM)
- **BFCL-V3**: 智能体基准 (ReMe SOTA)
- **AppWorld**: 智能体基准 (ReMe SOTA)
- **AIME25**: 数学推理基准 (FLEX +23%)
- **USPTO50k**: 化学逆合成基准 (FLEX +10%)
- **ProteinGym**: 蛋白质适应性基准 (FLEX +14%)

---

## 元进化概念

- **Meta-Evolution Framework** (MemEvolve): 共同进化经验和记忆架构
- **EvolveLab**: 统一自进化记忆代码库 (12 个系统的模块化设计空间)
- **Modular Design Space**: encode, store, retrieve, manage

---

## 过程记忆概念

- **Procedural Memory** (ReMe): 过程性"how-to"知识
- **Multi-faceted Distillation**: 成功模式识别、失败触发分析、比较洞见生成
- **Context-Adaptive Reuse**: 情境感知索引
- **Utility-based Refinement**: 自主添加有效记忆、剪枝过时记忆
- **Memory-Scaling Effect**: Qwen3-8B + ReMe > Qwen3-14B (无记忆)

---

## 设备端记忆概念

- **On-Device Memory Systems** (MemLoRA): 设备端部署，无云依赖
- **Knowledge Distillation**: 教师 LLM 蒸馏到学生 SLM
- **Expert Adapters**: 知识提取、记忆更新、记忆增强生成
- **MemLoRA-V**: 视觉扩展，小视觉语言模型 (SVLM)
- **Privacy Preservation**: 隐私保护

---

## 经验合成概念

- **Experience Synthesis** (DreamGym): 合成多样化经验用于 RL 训练
- **Reasoning-based Experience Model**: 推理基础经验模型
- **Experience Replay Buffer**: 初始化于离线数据，持续丰富
- **Curriculum Learning**: 自适应生成挑战性任务
- **Sim-to-Real Transfer**: 合成→真实迁移

---

## 经验前向学习概念

- **Forward Learning from Experience** (FLEX): 经验前向学习
- **Structured Experience Library**: 结构化经验库
- **Continual Reflection**: 持续反思成功和失败
- **Experience Inheritance**: 经验继承
- **Gradient-Free Learning**: 无梯度学习范式
- **HourVideo**: 小时级视频基准 (WorldMM)

---

## 概念关系网络

### is-a 关系
- BrowserAgent **is-a** 网页智能体
- DeepAgent **is-a** 端到端深度推理智能体
- ACON **is-a** 上下文压缩框架
- ToolMem **is-a** 工具能力记忆框架
- Training-Free GRPO **is-a** 无训练策略优化方法
- RGMem **is-a** 重正化群启发记忆框架
- LightMem **is-a** 三阶段人脑记忆框架
- CAM **is-a** 建设性记忆框架

### part-of 关系
- 人类启发式浏览器动作 **part-of** BrowserAgent
- 自主记忆折叠 **part-of** DeepAgent
- 失败驱动压缩指南优化 **part-of** ACON
- 工具能力记忆 **part-of** ToolMem
- 群相对语义优势 **part-of** Training-Free GRPO
- 层次化粗粒化 **part-of** RGMem
- 感官记忆 **part-of** LightMem
- 增量重叠聚类 **part-of** CAM

### related-to 关系
- 直接操作原始网页 **related-to** 人类启发式浏览器动作
- 单一连贯推理过程 **related-to** 端到端深度推理
- 上下文压缩 **related-to** 失败驱动压缩指南优化
- 工具选择 **related-to** 工具能力记忆
- 语义优势 **related-to** 群相对语义优势
- 多尺度演化 **related-to** 重正化群启发记忆
- 效率优化 **related-to** 知识蒸馏压缩器
- 小模型增强 **related-to** 无训练策略优化

---

## 验证公理

- **Event Segmentation Theory**: 人类自然分割连续经验的认知机制
- **Orthogonal Relation Modeling**: 多关系正交建模避免信息纠缠
- **Rhetorical Structure Theory**: 修辞结构理论指导上下文压缩
- **Model-Memory Decoupling**: 解耦稳定推理与可塑记忆
- **neo-Davidsonian Event Semantics**: 事件语义学指导记忆表示
- **Non-Compressive Preservation**: 非压缩形式保留信息 vs 激进压缩
- **Temporal Entity-aware Reasoning**: 时间感知实体推理
- **Adaptive Modality Selection**: 根据查询自适应选择记忆模态
- **Explainable Memory Reasoning**: 支持可解释推理轨迹的记忆架构

---

## 未来发展方向

### 短期 (2025-2026)
- **多模态记忆整合**: 跨视觉、语言、音频的记忆统一表示
  - *进展*: WorldMM 已证明文本 + 视觉必要性 (+8.4%)
- **实时性能优化**: 降低计算开销，提升检索效率
  - *进展*: Memoria 实现 99.7% token 减少
- **评估基准完善**: 构建更全面的记忆能力评测体系
  - *进展*: LongMemEval, LoCoMo 成为标准基准

### 中期 (2027-2028)
- **终身学习架构**: 支持跨会话、跨任务的记忆持续演化
  - *基础*: Sophia 持久化框架，Hindsight 反思层
- **认知科学深度融合**: 更深入地借鉴人类记忆认知机制
  - *基础*: neo-Davidsonian 事件语义学，Event Segmentation Theory
- **反思推理能力**: 实现可解释、可追溯的记忆推理
  - *基础*: Hindsight Reflect 操作 (91.4% LongMemEval)
- **自进化记忆系统**: 通过反思层实现记忆自我优化
  - *方向*: 从 Hindsight 扩展到自动更新和修正

### 长期 (2029+)
- **通用记忆基座**: 构建适用于所有智能体的通用记忆架构
- **意识与记忆关联**: 探索记忆在机器意识中的作用
- **群体记忆系统**: 多智能体间的记忆共享与协作
- **安全与隐私保护**: 记忆系统的安全访问控制和隐私保护

---

## 版本汇总

### 创世版本 v1.0 (2026-03-30)

**覆盖范围**: 共计 54 篇论文的研究成果

**核心统计**:
- **总概念数量**: 70+ 个
- **总公理数量**: 13 个
- **总评估基准**: 9 个
- **涉及系统**: 20+ 个记忆系统

**主要贡献**:
1. 建立完整的三维记忆本体论框架（形式-功能-动态）
2. 提出 13 条本体论公理，涵盖认知、工具、效率、性能
3. 构建跨维度概念关系网络（is-a/part-of/related-to）
4. 形成从理论到实践的完整验证体系
5. 建立长期演进路线图（短期-中期-长期）
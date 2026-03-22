# Agent Memory 领域本体论

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

## 概念关系网络

### 形式维度网络 (Forms)
- **Token-level Memory**: 显式离散存储
  - *子类型*: Event Graph, Multi-Graph, Structural Tree, Experience Pool, Modular Design Space
  - *关系*: 可转化为 Parametric/Latent 表示
  - *批次 2 新增*: Dynamic Experience Pool (ReMe), Expert Adapters (MemLoRA)
- **Parametric Memory**: 隐式权重存储  
  - *子类型*: Fine-tuning, Adapter-based
  - *关系*: 通常不可逆，但效率高
  - *批次 2 新增*: Memory Adapters (MemLoRA), Meta-Evolution Architecture (MemEvolve)
- **Latent Memory**: 隐藏状态存储
  - *子类型*: Hidden States, Attention Patterns, Visual Features
  - *关系*: 动态性强，但可解释性差
  - *批次 2 新增*: Visual Memory Corpus (WorldMM), SVLM Features (MemLoRA-V)

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

## 批次1 (2026年) 新增概念

### 新增记忆结构类型
- **Event Graph** (CompassMem): 基于事件分割理论的图结构
- **Multi-Graph** (MAGMA): 四个正交关系图的解耦表示  
- **Structural Relation Tree** (From Context to EDUs): EDU分解的树结构
- **Intent-Experience-Utility Triplet** (MemRL): 强化学习驱动的三元组

### 新增记忆操作机制  
- **Active Multi-Path Search** (CompassMem): 规划器-探索者-响应者架构
- **Policy-guided Graph Traversal** (MAGMA): 意图感知路由 + 自适应遍历
- **Structure-then-Select** (From Context to EDUs): 先结构后选择的压缩范式
- **Two-Phase Retrieval** (MemRL): 语义召回 + 价值感知选择

### 新增验证公理
- **Event Segmentation Theory**: 人类自然分割连续经验的认知机制
- **Orthogonal Relation Modeling**: 多关系正交建模避免信息纠缠  
- **Rhetorical Structure Theory**: 修辞结构理论指导上下文压缩
- **Model-Memory Decoupling**: 解耦稳定推理与可塑记忆

## 批次 2 (2025-12) 新增概念

### 新增记忆结构类型
- **Heterogeneous Graph** (EMem): Sessions-EDUs-Arguments 三层异构图
- **4 Logical Networks** (Hindsight): World Facts, Agent Experiences, Entity Summaries, Evolving Beliefs
- **Multi-Temporal Graphs** (WorldMM): 秒级/分钟级/小时级多粒度图
- **Weighted Knowledge Graph** (Memoria): 指数衰减加权的知识图谱 (α=0.02)

### 新增记忆操作机制
- **EDU Decomposition** (EMem): 基于 neo-Davidsonian 事件语义学的命题分解
- **Retain-Recall-Reflect** (Hindsight): 三元核心操作框架
- **Adaptive Multi-Modal Retrieval** (WorldMM): 自适应选择文本/视觉记忆源
- **Weighted Semantic Retrieval** (Memoria): 指数衰减优先检索近期信息
- **Dynamic Session Summarization** (Memoria): 会话级动态摘要生成

### 新增记忆载体类型
- **Visual Memory Corpus** (WorldMM): 视觉特征嵌入 + 时间戳索引
- **Entity-Argument Structures** (EMem): 参与者 - 时间 - 上下文的命题捆绑

### 新增验证公理
- **neo-Davidsonian Event Semantics**: 事件语义学指导记忆表示
- **Non-Compressive Preservation**: 非压缩形式保留信息 vs 激进压缩
- **Temporal Entity-aware Reasoning**: 时间感知实体推理
- **Adaptive Modality Selection**: 根据查询自适应选择记忆模态
- **Explainable Memory Reasoning**: 支持可解释推理轨迹的记忆架构

### 新增功能定位
- **Multi-session Conversational Memory**: 多会话对话记忆 (Hindsight, Memoria)
- **Long Video Reasoning**: 长视频推理 (WorldMM)
- **Personalized Conversational AI**: 个性化对话 AI (Memoria)

### 新增评估基准
- **LongMemEval**: 长期记忆评估基准 (Hindsight 91.4%, SOTA)
- **LoCoMo**: 长时对话记忆基准 (Hindsight 89.61%)
- **VideoMME (long)**: 长视频多模态评估 (WorldMM)
- **LVBench**: 长视频基准 (WorldMM)
- **BFCL-V3**: 智能体基准 (ReMe SOTA)
- **AppWorld**: 智能体基准 (ReMe SOTA)
- **AIME25**: 数学推理基准 (FLEX +23%)
- **USPTO50k**: 化学逆合成基准 (FLEX +10%)
- **ProteinGym**: 蛋白质适应性基准 (FLEX +14%)

### 新增元进化概念 (MemEvolve)
- **Meta-Evolution Framework**: 共同进化经验和记忆架构
- **EvolveLab**: 统一自进化记忆代码库 (12 个系统的模块化设计空间)
- **Modular Design Space**: encode, store, retrieve, manage

### 新增过程记忆概念 (ReMe)
- **Procedural Memory**: 过程性"how-to"知识
- **Multi-faceted Distillation**: 成功模式识别、失败触发分析、比较洞见生成
- **Context-Adaptive Reuse**: 情境感知索引
- **Utility-based Refinement**: 自主添加有效记忆、剪枝过时记忆
- **Memory-Scaling Effect**: Qwen3-8B + ReMe > Qwen3-14B (无记忆)

### 新增设备端记忆概念 (MemLoRA)
- **On-Device Memory Systems**: 设备端部署，无云依赖
- **Knowledge Distillation**: 教师 LLM 蒸馏到学生 SLM
- **Expert Adapters**: 知识提取、记忆更新、记忆增强生成
- **MemLoRA-V**: 视觉扩展，小视觉语言模型 (SVLM)
- **Privacy Preservation**: 隐私保护

### 新增经验合成概念 (DreamGym)
- **Experience Synthesis**: 合成多样化经验用于 RL 训练
- **Reasoning-based Experience Model**: 推理基础经验模型
- **Experience Replay Buffer**: 初始化于离线数据，持续丰富
- **Curriculum Learning**: 自适应生成挑战性任务
- **Sim-to-Real Transfer**: 合成→真实迁移

### 新增经验前向学习概念 (FLEX)
- **Forward Learning from Experience**: 经验前向学习
- **Structured Experience Library**: 结构化经验库
- **Continual Reflection**: 持续反思成功和失败
- **Experience Inheritance**: 经验继承
- **Gradient-Free Learning**: 无梯度学习范式
- **HourVideo**: 小时级视频基准 (WorldMM)

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

[6 more lines in file. Use offset=101 to continue.]
- **安全与隐私保护**: 记忆系统的安全访问控制和隐私保护

### 长期 (2029+)
- **通用记忆基座**: 构建适用于所有智能体的通用记忆架构
- **意识与记忆关联**: 探索记忆在机器意识中的作用
- **群体记忆系统**: 多智能体间的记忆共享与协作
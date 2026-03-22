# Ontology Changelog - 批次 2 (2025-12)

**版本**: v2.0  
**日期**: 2026-03-22  
**批次**: 批次 2 (2025-12) - 10 篇论文

---

## 📊 版本概览

| 项目 | v1.0 (批次 1 后) | v2.0 (批次 2 后) | 变更 |
|------|----------------|----------------|------|
| 记忆结构类型 | 4 | 15 | +11 |
| 记忆操作机制 | 4 | 20 | +16 |
| 记忆载体类型 | 3 | 8 | +5 |
| 验证公理 | 4 | 20 | +16 |
| 功能定位 | 3 | 8 | +5 |
| 评估基准 | 2 | 11 | +9 |

---

## 🆕 新增概念

### 记忆结构类型 (+11)

1. **Heterogeneous Graph** (EMem)
   - Sessions-EDUs-Arguments 三层异构图
   - 基于 neo-Davidsonian 事件语义学

2. **4 Logical Networks** (Hindsight)
   - World Facts, Agent Experiences, Entity Summaries, Evolving Beliefs
   - 支持 Retain-Recall-Reflect 三元操作

3. **Multi-Temporal Graphs** (WorldMM)
   - 秒级/分钟级/小时级多粒度图
   - 自适应多模态检索

4. **Weighted Knowledge Graph** (Memoria)
   - 指数衰减加权 (α=0.02)
   - 动态会话摘要生成

5. **Dynamic Experience Pool** (ReMe)
   - 过程性"how-to"知识存储
   - 效用精炼维护

6. **Meta-Evolution Architecture** (MemEvolve)
   - 共同进化经验和架构
   - EvolveLab 统一代码库

7. **Modular Design Space** (MemEvolve)
   - encode, store, retrieve, manage
   - 12 个代表性系统的模块化设计

8. **Expert Adapters** (MemLoRA)
   - 知识提取、记忆更新、记忆增强生成
   - 知识蒸馏到 SLM

9. **Reasoning-based Experience Model** (DreamGym)
   - 推理基础经验模型
   - 替代昂贵 rollout

10. **Structured Experience Library** (FLEX)
    - 结构化经验库
    - 持续反思成功和失败

11. **Visual Memory Corpus** (WorldMM)
    - 视觉特征嵌入 + 时间戳索引
    - 原生视觉理解

### 记忆操作机制 (+16)

1. **EDU Decomposition** (EMem)
   - 基于 neo-Davidsonian 事件语义学的命题分解
   - 参与者 - 时间 - 上下文的命题捆绑

2. **Retain-Recall-Reflect** (Hindsight)
   - 三元核心操作框架
   - 支持可解释推理轨迹

3. **Adaptive Multi-Modal Retrieval** (WorldMM)
   - 自适应选择文本/视觉记忆源
   - 多时间粒度检索

4. **Weighted Semantic Retrieval** (Memoria)
   - 指数衰减优先检索近期信息 (α=0.02)
   - 动态会话摘要

5. **Dynamic Session Summarization** (Memoria)
   - 会话级动态摘要生成
   - 加权知识图谱

6. **Multi-faceted Distillation** (ReMe)
   - 成功模式识别
   - 失败触发分析
   - 比较洞见生成

7. **Context-Adaptive Reuse** (ReMe)
   - 情境感知索引
   - 定制历史洞见

8. **Utility-based Refinement** (ReMe)
   - 自主添加有效记忆
   - 剪枝过时记忆

9. **Meta-Evolution** (MemEvolve)
   - 共同进化经验和架构
   - 架构迁移

10. **Knowledge Distillation** (MemLoRA)
    - 教师 LLM 蒸馏到学生 SLM
    - 多适配器训练

11. **Experience Synthesis** (DreamGym)
    - 合成多样化经验
    - 推理基础经验模型

12. **Experience Replay Buffer** (DreamGym)
    - 初始化于离线数据
    - 持续丰富新鲜交互

13. **Curriculum Learning** (DreamGym)
    - 自适应生成挑战性任务
    - 在线课程学习

14. **Sim-to-Real Transfer** (DreamGym)
    - 合成→真实迁移
    - 减少真实交互需求

15. **Continual Reflection** (FLEX)
    - 持续反思成功和失败
    - 提取经验

16. **Experience Inheritance** (FLEX)
    - 经验继承
    - 跨智能体经验共享

### 记忆载体类型 (+5)

1. **Entity-Argument Structures** (EMem)
   - 参与者 - 时间 - 上下文的命题捆绑
   - neo-Davidsonian 事件语义学

2. **Visual Memory Corpus** (WorldMM)
   - 视觉特征嵌入
   - 时间戳索引

3. **Parametric Adapters** (MemLoRA)
   - 专家适配器权重
   - 知识蒸馏结果

4. **SVLM Features** (MemLoRA-V)
   - 小视觉语言模型特征
   - 原生视觉理解

5. **Synthetic Experiences** (DreamGym)
   - 合成经验数据
   - 推理生成

### 验证公理 (+16)

1. **neo-Davidsonian Event Semantics** (EMem)
   - 事件语义学指导记忆表示
   - 命题分解基础

2. **Non-Compressive Preservation** (EMem)
   - 非压缩形式保留信息
   - vs 激进压缩

3. **Temporal Entity-aware Reasoning** (EMem, Hindsight)
   - 时间感知实体推理
   - 情境感知索引

4. **Adaptive Modality Selection** (WorldMM)
   - 根据查询自适应选择记忆模态
   - 避免噪声干扰

5. **Explainable Memory Reasoning** (Hindsight)
   - 支持可解释推理轨迹
   - 4 逻辑网络支持

6. **Memory-Scaling Effect** (ReMe, MemLoRA)
   - 小模型 + 记忆 > 大模型
   - Qwen3-8B + ReMe > Qwen3-14B

7. **On-Device Deployment** (MemLoRA)
   - 设备端部署
   - 无云依赖，隐私保护

8. **Experience Synthesis Principle** (DreamGym)
   - 合成多样化经验
   - 替代真实 rollout

9. **Sim-to-Real Transfer** (DreamGym)
   - 合成经验迁移到真实场景
   - 减少真实交互需求

10. **Forward Learning Principle** (FLEX)
    - 经验前向学习
    - 无梯度学习范式

11. **Gradient-Free Learning** (FLEX)
    - 无需反向传播
    - 经验驱动进化

12. **Meta-Adaptation** (MemEvolve)
    - 记忆架构元适应
    - 共同进化经验和架构

13. **Modular Design Principle** (MemEvolve)
    - 模块化设计空间
    - encode, store, retrieve, manage

14. **Procedural Memory Principle** (ReMe)
    - 过程性"how-to"知识
    - 内部化减少试错

15. **Utility-based Maintenance** (ReMe)
    - 效用驱动记忆维护
    - 自主添加/剪枝

16. **Knowledge Distillation Principle** (MemLoRA)
    - 教师 - 学生蒸馏
    - 专家适配器训练

### 功能定位 (+5)

1. **Multi-session Conversational Memory** (Hindsight, Memoria)
   - 多会话对话记忆
   - 长期个性化

2. **Long Video Reasoning** (WorldMM)
   - 长视频推理
   - 小时/天级视频

3. **Personalized Conversational AI** (Memoria)
   - 个性化对话 AI
   - 动态用户画像

4. **On-Device Memory Systems** (MemLoRA)
   - 设备端记忆系统
   - 隐私保护

5. **Experience-Driven Agent Evolution** (FLEX, ReMe, MemEvolve)
   - 经验驱动智能体进化
   - 终身学习

### 评估基准 (+9)

1. **LongMemEval** (Hindsight 91.4%, SOTA)
2. **LoCoMo** (Hindsight 89.61%)
3. **VideoMME (long)** (WorldMM)
4. **LVBench** (WorldMM)
5. **HourVideo** (WorldMM)
6. **BFCL-V3** (ReMe SOTA)
7. **AppWorld** (ReMe SOTA)
8. **AIME25** (FLEX +23%)
9. **USPTO50k** (FLEX +10%)
10. **ProteinGym** (FLEX +14%)

---

## 🔮 技术演进趋势

### 从批次 1 到批次 2 的演进

| 方面 | 批次 1 | 批次 2 | 演进 |
|------|--------|--------|------|
| 图结构 | 83% | 70% | -13% (更多样化) |
| 多模态 | 17% | 30% | +13% |
| 时间感知 | 67% | 70% | +3% |
| 智能检索 | 83% | 80% | -3% (稳定) |
| 反思能力 | 17% | 20% | +3% |
| 设备端 | 0% | 10% | +10% (新增) |

### 新兴趋势

1. **多模态融合** (30% → 未来主流)
   - WorldMM: 文本 + 视觉
   - MemLoRA-V: SVLM 原生视觉

2. **设备端部署** (0% → 10% → 未来增长)
   - MemLoRA: 知识蒸馏 + 专家适配器
   - 隐私保护需求驱动

3. **元进化** (新增)
   - MemEvolve: 共同进化经验和架构
   - 自进化记忆系统

4. **过程记忆** (新增)
   - ReMe: 过程性"how-to"知识
   - 内部化减少试错

5. **经验合成** (新增)
   - DreamGym: 合成多样化经验
   - 替代昂贵 rollout

---

## 📈 性能里程碑

| 基准 | 批次 1 最佳 | 批次 2 最佳 | 提升 |
|------|-----------|-----------|------|
| LongMemEval | 91.4% (Hindsight) | 91.4% (Hindsight) | - |
| LoCoMo | 89.61% (Hindsight) | 89.61% (Hindsight) | - |
| 5 视频基准 | - | +8.4% (WorldMM) | 新增 |
| BFCL-V3 | - | SOTA (ReMe) | 新增 |
| AppWorld | - | SOTA (ReMe) | 新增 |
| AIME25 | - | +23% (FLEX) | 新增 |
| Token 减少 | - | 99.7% (Memoria) | 新增 |
| 延迟降低 | - | 41.1% (DreamGym) | 新增 |
| 记忆缩放 | - | 8B+ReMe > 14B (ReMe) | 新增 |
| 设备端性能 | - | 媲美 120B (MemLoRA) | 新增 |

---

## 🎯 下一版本展望 (v3.0 - 批次 3)

**预期新增概念**:
- 更多设备端部署方法
- 更强多模态融合
- 跨领域迁移
- 联邦学习支持

**预期性能提升**:
- LongMemEval: 92%+
- LoCoMo: 90%+
- 设备端性能：超越云端

---

**Changelog 生成时间**: 2026-03-22 17:50 UTC  
**本体论版本**: v2.0  
**下一版本**: v3.0 (批次 3 完成后)

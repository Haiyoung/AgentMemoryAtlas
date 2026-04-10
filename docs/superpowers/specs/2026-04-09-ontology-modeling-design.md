# AgentMemory 本体论建模 Skill + GitHub Pages 站点设计

**日期**: 2026-04-09
**作者**: AgentMemoryAtlas Team
**状态**: 待审核

---

## 一、项目目标

将 AgentMemoryAtlas 打造为 Agent Memory 领域的本体论知识库，包含两个核心交付物：

1. **本体论建模 Skill**（`/ontology-update` 命令）— 批量分析增量论文分析文档，更新本体论模型
2. **GitHub Pages 站点** — 交互式词云浏览器，展示本体论全景和论文证据

---

## 二、本体论 1.0 模型框架

### 2.1 输入源（三个）

| 输入 | 路径 | 作用 |
|------|------|------|
| 基础模型骨架 | `ontology/Agent Memory 本体论领域模型（完整版）.md` | 10个顶层类、子类层级、属性、关系定义 |
| 已聚合知识库 | `ontology/ontology_base.md` (2316行) | 公理体系、概念关系网络、160+ 待完善概念 |
| 结构化分析证据 | `ontology/ontology_XXXX.md` (所有) | 概念/关系/公理的结构化映射，提供 Source 追溯 |

### 2.2 核心架构：三维正交分类

每个记忆概念由三个维度的坐标唯一确定：

```
载体维度 (Carrier)     功能维度 (Function)     动态维度 (Dynamic)
─────────────────      ──────────────────      ──────────────────
Token-level            Factual                 Formation
Parametric             Experiential            Evolution
External               Procedural              Retrieval
Latent                 Working                 Forgetting
                       Episodic                Reflection
                       Semantic                Association
```

### 2.3 顶层类重构（8个，精简去重）

| 顶层类 | 核心定位 | 变化说明 |
|--------|---------|---------|
| Agent | 记忆主体 | 保留 |
| Memory | 记忆载体（含参数/外部/Token） | 合并原 Memory + MemoryContent |
| MemorySystem | 记忆管理架构 | 保留，增加架构子类 |
| MemoryEvent | 记忆触发源 | 保留 |
| MemoryOperation | 记忆操作行为 | 保留，增加 Reflect/Associate |
| Context | 记忆关联场景 | 保留 |
| Entity | 记忆关联对象 | 合并原 Entity + Relation |
| Policy | 记忆操作规则 | 保留，增加安全策略子类 |

**删除说明**：
- `MemoryContent` 与 `Memory` 边界模糊——记忆是内容+载体的统一体
- `Relation` 作为独立顶层类过重——关系是 Entity 之间的连接属性

**新增隐含维度**（通过属性而非顶层类表达）：
- SecurityDimension：作为 Policy 的子类和 Memory 的属性
- MetaMemory：作为 Memory 的自引用属性
- QualityDimension：作为 Memory 的属性（置信度/一致性/新鲜度）

### 2.4 公理体系（补全）

```
存在公理: 每个记忆实例必须占据至少一个载体维度位置
操作公理: 检索必有索引；遗忘不可逆；反思产生新知
质量公理: 记忆质量 = f(新鲜度, 一致性, 置信度)
安全公理: 检索深度与隐私风险正相关；格式化检索更易被攻击
演进公理: 记忆随使用而强化；记忆随时间而衰减
```

### 2.5 概念处理规则

每个概念在 1.0 中被完整定位：

```
概念: "GatedWrite"
  → 载体维度: Parametric
  → 功能维度: Procedural
  → 动态维度: Formation
  → 所属类: MemoryOperation → AdvancedOperation → GatedOperation
  → 来源论文: LM2(2502.06049), MemLoRA
  → 关联概念: ["CrossAttentionRead", "ForgetGate"]
  → 描述: "通过门控机制控制记忆向量的写入/更新操作"
```

去重规则：同一概念多次出现时合并，保留最高频的表述和所有来源论文。

---

## 三、Skill 架构

### 3.0 核心约束：输入只读

**`ontology/` 目录下的所有 `.md` 分析文档和 `paper/` 目录下的所有论文简报，均为只读输入，Skill 执行期间和之后均不得修改。**

这些文件是本体论建模的**证据源**，不可变。Skill 只能读取它们的内容，从中提取概念、关系、公理，写入输出文件（见 3.4）。

违反此约束 = 破坏可追溯性。

### 3.0.1 更新前备份

每次执行本体论更新前，**必须先备份当前版本**的主文档和词库：

```
备份路径: ontology/backups/
  ├── ontology_base_v1.0.md          # 更新前版本
  ├── lexicon_v1.0.json              # 更新前词库
  └── ...
```

备份文件以当前版本号命名，格式：`{filename}_v{major}.{minor}.{patch}.{timestamp}`。

**恢复方式**：git checkout 或手动复制备份文件覆盖。

**触发时机**：无论增量更新还是结构性重写，每次执行 Skill 都必须备份。

### 3.1 触发方式

手动命令触发：`/ontology-update`

文件位置：`.claude/commands/ontology-update.md`（扁平 Markdown 文件，Claude Code 命令格式）

可通过 `$ARGUMENTS` 接收参数，如：
- `/ontology-update` — 扫描所有新增的 ontology 分析文档
- `/ontology-update --batch 2025-11` — 仅处理指定批次

### 3.2 输入管道

```
输入管道 1: 本体论分析文档 (ontology/ 目录)
  → ontology_XXXX.md — 结构化的本体映射
  → 主要输入

输入管道 2: 论文简报 (paper/ 目录)
  → 提供实验细节、量化数据
  → 辅助输入
```

### 3.3 执行流程（6步）

```
Step 1: 识别增量
  - git diff 识别新增的 ontology/ 分析文档
  - 定位对应的 paper/ 简报

Step 2: 概念归并（Taxonomy Update）
  - 提取新概念 → 匹配现有类层级
  - 判断：已存在实例？新子类？新维度？

Step 3: 关系图更新（Relation Graph Update）
  - 新关系 → 更新概念关系图
  - 检查一致性、发现隐式关系

Step 4: 公理演化（Axiom Evolution）
  - 合并/细化/修正公理
  - 冲突检测与条件限定
  - 标注置信度

Step 5: 结构重构（按需）
  - 维度膨胀时拆分，高度耦合时合并
  - 更新类的属性定义

Step 6: 输出生成
  - 更新 ontology_base.md（结构性重写）
  - 更新 lexicon.json（词库数据同步）
  - 生成 CHANGELOG_NNN.md
  - 重建 site/index.html
  - git commit
```

### 3.4 输出文件

| 文件 | 格式 | 用途 |
|------|------|------|
| `ontology/ontology_base.md` | Markdown | 本体论主文档 |
| `ontology/lexicon.json` | JSON | 独立词库（概念/词频/关联/分类着色） |
| `ontology/changelogs/CHANGELOG_NNN.md` | Markdown | 每次变更摘要 |
| `site/index.html` | HTML | 站点首页（含词云数据） |

---

## 四、GitHub Pages 站点设计

### 4.1 页面结构

```
┌─────────────────────────────────────────────────────────────┐
│  HEADER                                                      │
│  AgentMemoryAtlas | 领域本体论知识库                          │
│  [进度: 20/204] [概念: 82+] [批次: 2/15]                      │
├─────────────────────────────────────────────────────────────┤
│  动态词云区 — 本体概念全景图                                  │
│  d3-cloud 布局 + SVG 关联线                                   │
│  颜色=分类  大小=词频  hover=高亮关联  click=跳转论文          │
│  筛选栏: 全部 | 记忆类型 | 记忆结构 | 操作机制 | 公理           │
├─────────────────────────────────────────────────────────────┤
│  侧边导航栏 (sticky)              本体论正文区                  │
│  ├ 核心基础                     从 ontology_base.md 渲染       │
│  ├ 顶层类                       Mermaid 图自动渲染             │
│  ├ 子类层级                     锚点导航                       │
│  ├ 关系网络                                                   │
│  ├ 公理体系                                                   │
│  └ 技术演进                                                   │
├─────────────────────────────────────────────────────────────┤
│  论文简报区 (点击词云锚点后滚动至此)                            │
│  展示与选中概念相关的论文卡片                                   │
└─────────────────────────────────────────────────────────────┘
```

### 4.2 词云技术方案

**混合方案**：
- 默认：d3-cloud 渲染词云，按 weight 决定大小，按 category 着色
- 交互：hover 某个词时，高亮关联词并画虚线连接
- 点击：平滑滚动到下方论文简报区，高亮相关论文卡片

**数据源**：`lexicon.json`，由 Skill 生成并维护

### 4.3 技术选型

| 组件 | 技术 | 理由 |
|------|------|------|
| 词云布局 | d3-cloud | 成熟稳定，GitHub Pages 原生支持 |
| 关联线渲染 | SVG | 与 d3-cloud 兼容，性能好 |
| Markdown 渲染 | marked.js | 轻量，支持 GFM |
| 图表渲染 | mermaid.js | 自动渲染 Mermaid 代码块 |
| 数据获取 | fetch API | 读取本地 lexicon.json |
| 构建方式 | 无（纯静态） | GitHub Pages 原生支持，零服务端依赖 |

### 4.4 CI/CD

保持现有 `deploy-pages.yml` 流程，新增一步：

```yaml
- name: Build site from lexicon
  run: python scripts/build-site.py
```

Python 脚本读取 `lexicon.json` + `ontology_base.md` → 生成 `site/index.html`。

---

## 五、1.0 初始化流程

### 5.1 输入处理

```
Step 1: 读取 "Agent Memory 本体论领域模型（完整版）.md"
  → 提取 10 个顶层类、子类层级、属性、关系
  → 作为分类骨架

Step 2: 读取 ontology_base.md
  → 提取公理体系、关系网络、验证公理
  → 提取 160+ 待完善概念

Step 3: 批量扫描所有 ontology_XXXX.md
  → 聚合 new_concepts → 去重 → 归类到骨架
  → 聚合 new_relations → 更新关系网络
  → 聚合 new_axioms → 更新/冲突检测公理
  → 聚合 technical_contributions → 补充技术演进
  → 用分析数据填充"待完善描述"

Step 4: 融合生成 ontology_base.md 1.0
  → 以完整版为分类框架
  → 注入 ontology_XXXX.md 的发现
  → 去重、合并、规范化概念名称
  → 补全截断的逻辑推理约束

Step 5: 生成 lexicon.json
  → 从 1.0 本体提取所有概念
  → 计算词频（被多少论文提及）
  → 提取概念关联
  → 分类着色

Step 6: 生成 CHANGELOG_001.md
  → 1.0 基线说明、覆盖范围、概念统计
```

---

## 六、文件结构

```
AgentMemoryAtlas/
├── .claude/
│   └── commands/
│       └── ontology-update.md       # /ontology-update 触发（扁平 MD 命令文件）
├── scripts/
│   ├── build-site.py                # 站点生成脚本
│   └── generate-index.py            # 已有：索引生成
├── ontology/
│   ├── lexicon.json                 # 独立词库（Skill 生成，站点消费）
│   ├── ontology_base.md             # 本体论主文档（Skill 更新目标）
│   ├── Agent Memory 本体论领域模型（完整版）.md  # 分类骨架参考（保留）
│   ├── backups/                     # 更新前版本备份
│   │   ├── ontology_base_v1.0.md
│   │   └── lexicon_v1.0.json
│   └── changelogs/
│       └── CHANGELOG_001.md         # 1.0 基线说明
├── site/
│   ├── index.html                   # GitHub Pages 首页
│   └── papers/                      # 论文报告
├── docs/
│   └── superpowers/
│       └── specs/
│           └── 2026-04-09-ontology-modeling-design.md
├── paper/                           # 论文简报
└── ontology/                        # 本体论分析文档
    ├── 2021/ontology_2104.08164.md
    ├── 2022/ontology_2207.07115.md
    ├── ...
```

---

## 七、约束与原则

1. **输入只读**：`ontology/` 和 `paper/` 目录下的所有文件均为只读证据源，Skill 不得修改它们
2. **YAGNI**：不添加当前需求不需要的功能（如多语言支持、分页、搜索）
2. **一源数据**：lexicon.json 是唯一数据源，Skill 写，站点读
3. **纯静态**：站点零服务端依赖，GitHub Pages 原生部署
4. **可追溯**：每个概念必须关联至少一个来源论文
5. **去重优先**：Skill 必须检测并合并重复概念，而非追加
6. **增量更新**：1.0 初始化是结构性重写（未归类概念归位），后续 Skill 运行是增量更新，非全量重写
7. **主文档角色**：`ontology_base.md` 是主文档（Skill 更新目标），"完整版.md" 保留为分类骨架参考，不作为运行时的主文档

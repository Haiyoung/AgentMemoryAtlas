<div align="center">

# AgentMemoryAtlas

**Agent Memory 领域本体论 · 论文阅读简报库**

</div>

---

## 关于本项目

AgentMemoryAtlas 是 Agent Memory 领域的系统性知识基础设施，包含两大核心内容：

### 1. Agent Memory 领域本体论

从 146+ 篇 Agent Memory 领域论文中归纳提炼出的**统一概念框架**，采用"三维正交分类 + 类层级"双轨架构：

- **三维正交分类**：载体维度（Carrier）× 功能维度（Function）× 动态维度（Dynamic），为每个概念提供精确坐标
- **类层级体系**：8 个顶层核心类（Agent / Memory / MemorySystem / MemoryEvent / MemoryOperation / Context / Entity / Policy）
- **核心公理体系**：存在、操作、质量、安全、演进五大类公理，构成领域的推理基础
- **架构范式归纳**：外部检索、上下文窗口、参数化、图结构、混合多层五种主导架构
- **功能范式归纳**：陈述性、程序与经验、工作、长期、反思五大功能范式
- **生命周期模型**：形成 → 组织 → 巩固 → 检索 → 遗忘 → 反思的闭环
- **安全与治理**：隐私、一致性、质量、演化约束、结构完整性五大治理维度

阅读本体论：
- 在线：[GitHub Pages → 本体论](https://haiyoung.github.io/AgentMemoryAtlas/)
- 本地：[ontology/ontology_base.md](ontology/ontology_base.md)（318 行凝练模型）
- 完整词库：[ontology/lexicon.json](ontology/lexicon.json)（1411 个概念，744 条关系）

### 2. Agent Memory 论文阅读简报

按年份组织的论文阅读简报库，每篇论文从多个维度进行结构化分析：

- **基础元数据**：标题、作者、发表渠道、研究领域
- **7 维度本体标注**：记忆类型 / 记忆结构 / 记忆操作 / 功能定位 / 设计模式 / 公理约束 / 记忆载体
- **综合评价**：理论基础、问题核心性、方法创新性、技术壁垒、实验严谨性、落地可行性、应用前景
- **核心主张**：问题 / 方案 / 优势的通俗概括
- **实验结果**：关键性能指标与对比数据
- **局限性与未来方向**

阅读论文简报：
- 在线：[GitHub Pages → 论文列表](https://haiyoung.github.io/AgentMemoryAtlas/)（按年份浏览）
- 本地：`paper/{year}/` 目录下的 Markdown 文档

---

## 目录结构

```
AgentMemoryAtlas/
├── ontology/              # 本体论领域模型
│   ├── ontology_base.md   # 本体论正文（318 行，8 节）
│   ├── lexicon.json       # 完整词库（1411 概念，744 关系）
│   ├── changelogs/        # 模型更新日志
│   └── backups/           # 历史版本备份
│
├── paper/                 # 论文阅读简报
│   ├── 2021/              # 1 篇
│   ├── 2022/              # 1 篇
│   ├── 2023/              # 18 篇
│   ├── 2024/              # 23 篇
│   ├── 2025/              # 100 篇
│   └── 2026/              # 5 篇
│
├── site/                  # GitHub Pages 站点源码
│   └── index.html         # 动态词云 + 本体论正文 + 论文导航
│
├── scripts/               # 构建脚本
│   ├── extract-lexicon.py # 从分析文档提取词库
│   └── build-site.py      # 构建 GitHub Pages 站点
│
└── .claude/commands/      # Claude Code 技能
    └── ontology-update.md # 增量更新本体论的自动化命令
```

---

## 使用方式

### 在线阅读

访问 [GitHub Pages 站点](https://haiyoung.github.io/AgentMemoryAtlas/)：
- 顶部为 Agent Memory 核心概念词云（基于词频权重动态排列）
- 中部为本体论正文
- 底部按年份浏览论文阅读简报

### 本地阅读

```bash
git clone https://github.com/Haiyoung/AgentMemoryAtlas.git
cd AgentMemoryAtlas

# 阅读本体论
cat ontology/ontology_base.md

# 浏览论文简报
ls paper/2025/
```

### 增量更新本体论

```bash
# 将新增论文的本体论分析文档放入 ontology/ 目录后
claude /ontology-update
```

该命令自动完成：备份 → 识别增量 → 概念归并 → 关系图更新 → 公理演化 → 生成 changelog → 重建站点

---

## 许可证

MIT

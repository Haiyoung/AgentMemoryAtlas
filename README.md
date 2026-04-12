<h1 align="center">
  <img src="site/logo.svg" alt="logo" width="36" height="36" style="vertical-align: middle; margin-right: 8px;">
  AgentMemoryAtlas
</h1>

<p align="center">
  <strong>Agent Memory 领域本体论 · 论文阅读简报库</strong>
</p>

---

## 关于

AgentMemoryAtlas 是一个系统梳理 **Agent Memory（智能体记忆）** 领域研究的开源项目。

Agent Memory 是 LLM Agent 方向最活跃的研究领域之一——从 2023 年的 MemoryBank、MemGPT 到如今的多模态记忆、记忆操作系统、自进化记忆，论文数量快速增长但缺乏统一的概念框架。本项目的目标是：

- **构建统一的领域本体论**——从大量论文中归纳提炼出 Agent Memory 的概念体系，形成一个内聚、简洁、可扩展的领域模型
- **提供结构化的论文阅读简报**——每篇论文从记忆类型、记忆结构、记忆操作、功能定位等 7 个本体维度进行标注，帮助快速定位论文贡献并理解其在领域中的位置

随着新论文不断涌现，本项目将持续补充论文简报并迭代本体论模型。

---

## 快速开始

### 在线阅读

访问 [GitHub Pages 站点](https://haiyoung.github.io/AgentMemoryAtlas/)：

| 页面区域 | 内容 |
|:---:|------|
| **顶部** | Agent Memory 核心概念动态词云（按论文出现频次排列，鼠标悬停可点击） |
| **中部** | 本体论正文——三维正交分类、核心类、公理体系、架构范式、功能范式、生命周期、安全治理 |
| **底部** | 论文阅读简报列表，按年份分组，点击可跳转阅读 |

### 本地阅读

```bash
git clone https://github.com/Haiyoung/AgentMemoryAtlas.git
cd AgentMemoryAtlas
```

**阅读本体论**：

```bash
cat ontology/ontology_base.md
```

本体论正文约 300 行，8 个章节，建议从头到尾完整阅读以建立领域框架认知。

**阅读论文简报**：

```bash
ls paper/2025/          # 浏览论文列表
cat paper/2025/2512.12818_Hindsight_is_20_20_*.md   # 阅读具体论文
```

每篇简报包含：基础元数据 → 综合评价 → 领域本体论映射 → 核心问题与解决方案 → 方法与技术架构。

### 本地部署站点

```bash
python3 -m http.server 8081
# 浏览器访问 http://localhost:8081/site/index.html
```

---

## 本体论概览

本体论采用 **"三维正交分类 + 类层级"** 双轨架构，涵盖 1400+ 概念、700+ 关系：

**三维正交分类**——每个概念由三个维度的坐标唯一确定：

| 载体 (Carrier) | 功能 (Function) | 动态 (Dynamic) |
|:---:|:---:|:---:|
| Token-level | Factual | Formation |
| Parametric | Semantic | Retrieval |
| External | Episodic | Evolution |
| Latent | Procedural | Forgetting |
| | Experiential | Reflection |
| | Working | Association |

**8 个顶层类**——Agent / Memory / MemorySystem / MemoryEvent / MemoryOperation / Context / Entity / Policy

**5 类公理**——存在公理、操作公理、质量公理、安全公理、演进公理

完整本体论详见 [ontology_base.md](ontology/ontology_base.md)，完整概念词库详见 [lexicon.json](ontology/lexicon.json)。

---

## 目录结构

```
AgentMemoryAtlas/
├── ontology/              # 本体论领域模型
│   ├── ontology_base.md   # 本体论正文（~300 行）
│   ├── lexicon.json       # 完整概念词库（1411 概念，744 关系）
│   ├── changelogs/        # 模型更新日志
│   └── {year}/            # 每篇论文的本体论分析文档
│
├── paper/                 # 论文阅读简报（按年份）
│   ├── 2021/              # 1 篇
│   ├── 2022/              # 1 篇
│   ├── 2023/              # 18 篇
│   ├── 2024/              # 23 篇
│   ├── 2025/              # 100+ 篇
│   └── 2026/              # 5 篇
│
├── site/                  # GitHub Pages 站点
│   └── index.html         # 词云 + 本体论 + 论文浏览
│
└── scripts/               # 构建脚本
    ├── extract-lexicon.py # 从分析文档提取概念词库
    └── build-site.py      # 构建 GitHub Pages 站点
```

---

## 持续更新

本仓库是**持续演进**的：

- **新论文**：随着 Agent Memory 领域新论文发布，将持续补充阅读简报
- **本体论迭代**：每批新增论文将触发本体论模型的增量更新——概念归并、关系演化、公理修正
- **模型版本**：本体论遵循语义化版本管理，每次更新生成 changelog 并保留历史备份

增量更新可通过 `claude /ontology-update` 命令自动化完成。

---

## 许可证

本项目采用 [MIT 许可证](LICENSE)。

---

<p align="center">
  <sub>Built with ontology-driven analysis of Agent Memory research</sub>
</p>

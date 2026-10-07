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
- **提供结构化的论文阅读简报**——每篇论文按统一的本体论映射结构化标注（研究对象、技术路径、载体形态、功能目标、验证指标等），帮助快速定位论文贡献并理解其在领域中的位置

随着新论文不断涌现，本项目将持续补充论文简报并迭代本体论模型。

---

## 快速开始

### 在线阅读

访问 [GitHub Pages 站点](https://haiyoung.github.io/AgentMemoryAtlas/)：

| 页面区域 | 内容 |
|:---:|------|
| **顶部** | 领域发展时间轴（2021 → 2026）——每年一个节点，标注当年的重大进展与论文数量 |
| **下方** | 多 Tab 区域：默认展示**本体论**正文（三维正交分类、核心类、公理体系、架构范式、功能范式、生命周期、安全治理），其余 Tab 按年份展示论文标签 |
| **点击论文标签** | 在当前页弹窗渲染该论文的阅读简报（不跳转、不下载） |

### 本地阅读

```bash
git clone https://github.com/Haiyoung/AgentMemoryAtlas.git
cd AgentMemoryAtlas
```

**阅读本体论**：

```bash
cat ontology/ontology_base.md
```

本体论正文约 366 行，8 个章节，建议从头到尾完整阅读以建立领域框架认知。

**阅读论文简报**：

```bash
ls paper/2025/          # 浏览论文列表
cat "paper/2025/2512.12818_Hindsight is 20_20_ Building Agent Memory that Ret.md"   # 阅读具体论文
```

每篇简报包含：基础元数据 → 综合评价 → 领域本体论映射 → 核心问题与解决方案 → 方法与技术架构。

### 本地部署站点

`site/index.html` 的词库、本体正文、时间轴与论文索引已在构建期嵌入，克隆后即可直接打开。论文简报的正文通过**相对路径**读取（与线上一致），如需完全离线查看，先把简报与本体数据拷贝进站点目录：

```bash
mkdir -p site/paper site/ontology
cp -r paper/* site/paper/
cp ontology/lexicon.json ontology/ontology_base.md site/ontology/

python3 -m http.server 8081
# 浏览器访问 http://localhost:8081/site/index.html
```

> 未拷贝时论文简报会回退到线上站点读取；本体论 Tab 与时间轴不受影响。

---

## 本体论概览

本体论采用 **"三维正交分类 + 类层级"** 双轨架构，涵盖 1700+ 概念、900+ 关系：

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
│   ├── ontology_base.md   # 本体论正文（366 行）
│   ├── lexicon.json       # 完整概念词库（1749 概念，965 关系）
│   ├── timeline.json      # 时间轴策展数据（2021–2026 重大进展）
│   ├── changelogs/        # 模型更新日志
│   ├── backups/           # 历史备份
│   └── {year}/            # 每篇论文的本体论分析文档
│
├── paper/                 # 论文阅读简报（按年份）
│   ├── 2021/              # 1 篇
│   ├── 2022/              # 1 篇
│   ├── 2023/              # 18 篇
│   ├── 2024/              # 23 篇
│   ├── 2025/              # 100 篇
│   └── 2026/              # 82 篇
│
├── site/                  # GitHub Pages 站点
│   ├── index.html         # 领域时间轴 + 多 Tab（本体论 / 分年论文）+ 简报弹窗
│   ├── paper/             # 部署期拷贝的论文简报（本地预览用，已 gitignore）
│   └── ontology/          # 部署期拷贝的本体数据（本地预览用，已 gitignore）
│
└── scripts/               # 构建脚本
    ├── extract-lexicon.py # 从分析文档提取概念词库
    └── build-site.py      # 构建站点：把词库/本体/时间轴/论文索引幂等嵌入 index.html
```

---

## 持续更新

本仓库是**持续演进**的：

- **新论文**：随着 Agent Memory 领域新论文发布，将持续补充阅读简报
- **本体论迭代**：每批新增论文将触发本体论模型的增量更新——概念归并、关系演化、公理修正
- **模型版本**：本体论遵循语义化版本管理，每次更新生成 changelog 并保留历史备份
- **站点构建**：`build-site.py` 在 CI 构建期把词库、本体正文、时间轴与论文索引**幂等**嵌入 `site/index.html`，可重复执行而不会产生重复声明

增量更新可通过 `claude /ontology-update` 命令自动化完成。

---

## 许可证

本项目采用 [MIT 许可证](LICENSE)。

---

<p align="center">
  <sub>Built with ontology-driven analysis of Agent Memory research</sub>
</p>

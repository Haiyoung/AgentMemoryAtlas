# AgentMemoryAtlas 🧭

[![Stars](https://img.shields.io/badge/stars-0-blue)]()
[![Papers](https://img.shields.io/badge/papers-3-green)]()
[![Updated](https://img.shields.io/badge/updated-2026--03--19-success)]()
[![License](https://img.shields.io/badge/license-MIT--0-yellow)]()

> 🗺️ **Navigating the Landscape of Agent Memory Research**
>
> 🧠 基于**本体论 (Ontology)** 的智能体记忆领域论文地图集
> 🔗 7 维度标注 · 可视化 HTML 总结 · 持续更新

---

## 🌐 在线阅读

**🚀 GitHub Pages 已上线！**

🔗 [https://haiyoung.github.io/AgentMemoryAtlas/](https://haiyoung.github.io/AgentMemoryAtlas/)

访问 GitHub Pages 查看：
- 📊 实时统计数据
- 📄 已读论文列表
- 🎨 精美页面设计
- 🔗 快速导航链接

---

## 🌟 核心特色

### 🎯 本体论驱动分析

不同于传统论文仓库的简单收集，我们使用**7 维度本体模型**深度标注每篇论文：

| 维度 | 说明 | 示例值 |
|------|------|--------|
| **记忆类型** | 记忆的本质分类 | 情景式/程序式/语义式/经验式 |
| **记忆结构** | 组织形式 | 向量/图/层次化/混合 |
| **记忆操作** | 核心操作 | 编码/存储/检索/更新/遗忘 |
| **记忆载体** | 物理/逻辑载体 | Token 级/隐藏状态/外部数据库 |
| **功能定位** | 在智能体中的角色 | 规划/推理/对话/学习 |
| **模式识别** | 设计范式 | 检索增强/反思/自进化 |
| **公理约束** | 底层原则 | 稳定性 - 可塑性/泛化性 |

### 📊 可视化总结

每篇论文生成**交互式 HTML 报告**，包含：
- Mermaid 架构图
- 本体论映射可视化
- 6 维度评分雷达图
- 关键洞见时间线

### 🔄 持续更新

由 OpenClaw 技能驱动，**每周自动处理 5-10 篇新论文**：
- 自动提取 arXiv/ACL/OpenReview 论文
- 生成本体论标注
- 输出 HTML 总结
- 更新统计索引

---

## 📊 统计概览

| 指标 | 数值 |
|------|------|
| 📄 **已读论文** | **3 篇** (2026-03-19) |
| 📅 最新年份 | 2026 |
| ⭐ 平均评分 | **4.7/5.0** |
| 🧠 记忆操作 | 10 个 |
| 🔁 模式识别 | 11 个 |
| ✅ 公理约束 | 7 个 |
| 📚 本体论文档 | 3 个 |

---

## 📄 已读论文列表

### 2026 年论文 (3 篇)

| # | 论文 | arXiv | 机构 | 评分 | HTML |
|---|------|-------|------|------|------|
| 1 | **🧭 CompassMem** - 事件中心记忆作为逻辑地图 | [2601.04726](https://arxiv.org/abs/2601.04726) | 中国人民大学 | ⭐4.8/5.0 | [📖 阅读](papers/2026/01_2026-01_CompassMem-事件中心记忆作为逻辑地图_2026-03-19.html) |
| 2 | **🧲 MAGMA** - 多图智能体记忆架构 | [2601.03236](https://arxiv.org/abs/2601.03236) | UT Dallas | ⭐4.7/5.0 | [📖 阅读](papers/2026/02_2026-01_MAGMA-多图智能体记忆架构_2026-03-19.html) |
| 3 | **🌱 EverMemOS** - 自组织记忆操作系统 | [2601.02163](https://arxiv.org/abs/2601.02163) | 阿里巴巴 + 武大 | ⭐4.6/5.0 | [📖 阅读](papers/2026/03_2026-01_EverMemOS-自组织记忆操作系统_2026-03-19.html) |

### 论文简介

#### 1. CompassMem (2601.04726) ⭐4.8/5.0
- **核心**: 受事件分割理论启发，将记忆组织为事件图
- **创新**: 主动多路径搜索 + 逻辑感知导航
- **结果**: LoCoMo F1 52.18% (+4.26% vs HippoRAG)
- **本体**: 情景式 + 图式 + RAG+ 图导航

#### 2. MAGMA (2601.03236) ⭐4.7/5.0
- **核心**: 4 个正交关系图 (语义/时序/因果/实体)
- **创新**: 意图感知检索 + 结构化上下文构建
- **结果**: LoCoMo Judge 0.700 (+18.6% vs 次优)
- **本体**: 语义式 + 情景式 + 多图式 + 策略引导遍历

#### 3. EverMemOS (2601.02163) ⭐4.6/5.0
- **核心**: 印迹启发的记忆生命周期
- **创新**: MemCells→MemScenes 层次化 + Foresight 信号
- **结果**: LoCoMo/LongMemEval SOTA
- **本体**: 情景式 + 语义式 + 层次化 + OS 启发

---

## 📂 目录结构

```
AgentMemoryAtlas/
├── 📄 papers/              # 论文总结（按年份组织）
│   ├── 2026/              # 2026 年论文 (3 篇已读)
│   ├── 2025/              # 2025 年论文 (待处理)
│   └── 2024/              # 2024 年论文 (待处理)
├── 🔗 ontology/            # 本体模型
│   ├── AGENT_MEMORY_ONTOLOGY.md  # 领域本体文档 (v1.1)
│   ├── 00_本体论入门.md          # 本体论入门指南
│   └── 99_本体论优化建议.md      # 优化讨论记录
├── 🛠️ skills/              # 阅读技能
│   └── paper-reader/      # 论文提取与总结技能 (v8 模板)
├── 📊 stats/              # 统计数据
│   └── monthly-report-template.md
└── 🌐 site/               # GitHub Pages 网站
    └── index.html         # 交互式主页
```

---

## 🔗 快速链接

| 资源 | 链接 |
|------|------|
| 🌐 **GitHub Pages** | [https://haiyoung.github.io/AgentMemoryAtlas/](https://haiyoung.github.io/AgentMemoryAtlas/) |
| 📊 **本体论模型** | [ontology/AGENT_MEMORY_ONTOLOGY.md](ontology/AGENT_MEMORY_ONTOLOGY.md) |
| 📖 **本体论入门** | [ontology/00_本体论入门.md](ontology/00_本体论入门.md) |
| 🤝 **贡献指南** | [CONTRIBUTING.md](CONTRIBUTING.md) |
| 📄 **许可证** | [LICENSE](LICENSE) |

---

## 📅 更新日志

### 2026-03-19 - 首批论文发布
- ✅ 发布 3 篇 2026 年论文 HTML 总结
- ✅ 本体论模型更新到 v1.1 (10 操作/11 模式/7 公理)
- ✅ GitHub Pages 上线 (https://haiyoung.github.io/AgentMemoryAtlas/)
- ✅ v8 HTML 模板 (深色/浅色主题切换 + 局限性区块)

### 即将更新
- ⏳ 继续处理 2026 年剩余论文 (目标 10 篇/批次)
- ⏳ 本体论模型自动优化 (每 10 篇)
- ⏳ 飞书进度汇报 (每 10 篇)
- ⏳ 交互式搜索功能
- ⏳ 本体论可视化探索器

---

## 🤝 贡献指南

欢迎通过以下方式参与：

### 📬 推荐论文
创建 [Issue](https://github.com/Haiyoung/AgentMemoryAtlas/issues/new?template=paper-request.md) 推荐值得分析的论文

### 🐛 纠错改进
发现分析错误或有改进建议？创建 [Issue](https://github.com/Haiyoung/AgentMemoryAtlas/issues/new?template=correction.md)

### 💻 代码贡献
欢迎 PR 改进：
- 论文提取脚本
- HTML 模板优化
- 本体模型扩展

详见 [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📧 联系方式

- 📬 **Issues**: [论文推荐/纠错](https://github.com/Haiyoung/AgentMemoryAtlas/issues)
- 📧 **Email**: (待配置)
- 🐦 **Twitter**: (待配置)

---

## 📄 许可证

**MIT-0** - 自由使用，无需署名

[![License: MIT-0](https://img.shields.io/badge/license-MIT--0-yellow)](https://opensource.org/licenses/MIT-0)

---

## 🙏 致谢

感谢所有被分析论文的作者们，你们的工作构成了智能体记忆领域的知识版图。

---

<div align="center">

**🗺️ 探索智能体记忆的完整版图**

[🌐 GitHub Pages](https://haiyoung.github.io/AgentMemoryAtlas/) · [📄 浏览论文](papers/2026/) · [🔗 查看本体](ontology/AGENT_MEMORY_ONTOLOGY.md)

**当前进度**: 3/10 篇 (2026 年第 1 批次)

</div>

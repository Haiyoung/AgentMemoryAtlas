# AgentMemoryAtlas 🧭

[![Stars](https://img.shields.io/badge/stars-0-blue)]()
[![Papers](https://img.shields.io/badge/papers-49-green)]()
[![Updated](https://img.shields.io/badge/updated-2026--03--19-success)]()
[![License](https://img.shields.io/badge/license-MIT--0-yellow)]()

> 🗺️ **Navigating the Landscape of Agent Memory Research**
>
> 🧠 基于**本体论 (Ontology)** 的智能体记忆领域论文地图集
> 🔗 7 维度标注 · 可视化总结 · 持续更新

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

### 🔄 自动化更新

由 OpenClaw 技能驱动，**每周自动处理 5-10 篇新论文**：
- 自动提取 arXiv/ACL/OpenReview 论文
- 生成本体论标注
- 输出 HTML 总结
- 更新统计索引

---

## 📊 统计概览

| 指标 | 数值 |
|------|------|
| 📄 已读论文 | 49 篇 |
| 📅 时间跨度 | 2023-2026 |
| 🏫 涉及机构 | 50+ |
| ⭐ 平均评分 | 4.2/5.0 |
| 🧠 本体概念 | 120+ |

### 热门论文 TOP 5

| 排名 | 论文 | 评分 | 亮点 |
|------|------|------|------|
| 🥇 | **FLEX** (2025) | ⭐⭐⭐⭐⭐ 5.0 | 经验库范式，跨模型继承 |
| 🥈 | **MAGMA** (2026) | ⭐⭐⭐⭐⭐ 5.0 | 多图架构，+18.6% 提升 |
| 🥉 | **CompassMem** (2026) | ⭐⭐⭐⭐⭐ 4.8 | 事件图框架 |
| 4 | **AgeMem** (2026) | ⭐⭐⭐⭐⭐ 4.7 | 智能体记忆操作系统 |
| 5 | **MemEvolve** (2025) | ⭐⭐⭐⭐⭐ 4.6 | 记忆自进化机制 |

---

## 📂 目录结构

```
AgentMemoryAtlas/
├── 📄 papers/              # 论文总结（按年份组织）
│   ├── 2026/              # 2026 年论文
│   ├── 2025/              # 2025 年论文
│   └── 2024/              # 2024 年论文
├── 🔗 ontology/            # 本体模型
│   ├── AGENT_MEMORY_ONTOLOGY.md  # 领域本体文档
│   └── ontology.json      # 机器可读格式
├── 🛠️ skills/              # 阅读技能
│   └── paper-reader/      # 论文提取与总结技能
├── 📊 stats/              # 统计数据
│   └── monthly-report.md  # 月度报告
└── 🌐 site/               # GitHub Pages 网站
    └── index.html         # 交互式主页
```

---

## 🚀 快速开始

### 在线阅读
🔗 [GitHub Pages](https://yourusername.github.io/AgentMemoryAtlas/) *(即将上线)*

### 本地查看
```bash
git clone https://github.com/YOUR_USERNAME/AgentMemoryAtlas.git
cd AgentMemoryAtlas
open papers/2026/01_2026-01_CompassMem/summary.html
```

### 推荐论文
```bash
# 查看评分最高的论文
ls -la papers/2026/ | head -10
```

---

## 📅 更新日志

### 2026-03-19
- 🎉 仓库创建，首批 49 篇论文就绪
- 📊 本体模型 v1.0 发布
- 🛠️ 自动化技能 v2.2 集成

### 即将更新
- [ ] GitHub Pages 网站部署
- [ ] 交互式搜索功能
- [ ] 本体论可视化探索器

---

## 🤝 贡献指南

欢迎通过以下方式参与：

### 📬 推荐论文
创建 [Issue](https://github.com/YOUR_USERNAME/AgentMemoryAtlas/issues/new?template=paper-request.md) 推荐值得分析的论文

### 🐛 纠错改进
发现分析错误或有改进建议？创建 [Issue](https://github.com/YOUR_USERNAME/AgentMemoryAtlas/issues/new?template=correction.md)

### 💻 代码贡献
欢迎 PR 改进：
- 论文提取脚本
- HTML 模板优化
- 本体模型扩展

详见 [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📧 联系方式

- 📬 **Issues**: 论文推荐/纠错
- 📧 **Email**: *(待配置)*
- 🐦 **Twitter**: *(待配置)*

---

## 📄 许可证

**MIT-0** - 自由使用，无需署名

[![License: MIT-0](https://img.shields.io/badge/license-MIT--0-yellow.svg)](https://opensource.org/licenses/MIT-0)

---

## 🙏 致谢

感谢所有被分析论文的作者们，你们的工作构成了智能体记忆领域的知识版图。

---

<div align="center">

**🗺️ 探索智能体记忆的完整版图**

[📄 浏览论文](papers/) · [🔗 查看本体](ontology/) · [📊 统计数据](stats/)

</div>

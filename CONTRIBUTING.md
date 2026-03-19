# 贡献指南

欢迎为 **AgentMemoryAtlas** 做出贡献！🎉

---

## 🚀 快速开始

### 1. Fork 仓库
点击右上角 **Fork** 按钮

### 2. 克隆到本地
```bash
git clone https://github.com/YOUR_USERNAME/AgentMemoryAtlas.git
cd AgentMemoryAtlas
```

### 3. 创建分支
```bash
git checkout -b feature/your-feature-name
```

---

## 📬 贡献方式

### 方式一：推荐论文

创建 [Issue](https://github.com/YOUR_USERNAME/AgentMemoryAtlas/issues/new?template=paper-request.md)，包含：
- 论文标题
- arXiv/会议链接
- 推荐理由（1-2 句）

### 方式二：纠错改进

发现分析错误？创建 [Issue](https://github.com/YOUR_USERNAME/AgentMemoryAtlas/issues/new?template=correction.md)：
- 论文 ID
- 错误描述
- 建议修正

### 方式三：代码贡献

改进脚本、模板或功能：
1. 修改代码
2. 测试通过
3. 提交 PR

### 方式四：完善本体

发现本体模型需要扩展：
1. 在 Issue 中说明新增概念
2. 提供定义和示例
3. 讨论后合并

---

## 📝 代码规范

### Python 脚本
```python
# 使用 type hints
def extract_paper(arxiv_id: str) -> dict:
    """提取论文元数据"""
    pass

# 添加文档字符串
```

### Git 提交信息
```bash
# 格式：<type>: <description>
git commit -m "feat: 添加 FLEX 论文总结"
git commit -m "fix: 修正本体标注错误"
git commit -m "docs: 更新 README 安装说明"
```

类型说明：
- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `style`: 格式调整
- `refactor`: 重构
- `test`: 测试相关
- `chore`: 构建/工具

---

## 🎨 论文总结规范

### 目录结构
```
papers/2026/01_2026-01_CompassMem/
├── summary.html          # 可视化总结（必需）
├── notes.md              # 详细笔记（可选）
├── ontology-mapping.json # 本体标注（必需）
└── code/                 # 相关代码（可选）
```

### 命名规范
- 目录名：`序号_年份 - 月份_论文简称`
- 示例：`01_2026-01_CompassMem`

### 本体标注格式
```json
{
  "ontology": {
    "memory_type": ["Episodic", "Semantic"],
    "memory_structure": ["Graph"],
    "memory_operation": ["Encoding", "Retrieval"],
    "memory_carrier": ["External DB"],
    "function": ["Planning", "Reasoning"],
    "patterns": ["RAG", "Reflection"],
    "axioms": ["Stability-Plasticity"]
  }
}
```

---

## 🔍 PR 审核流程

1. **自动检查**
   - HTML 有效性
   - JSON 格式
   - 链接完整性

2. **人工审核**
   - 内容准确性
   - 本体标注合理性
   - 代码质量

3. **合并**
   - 审核通过后合并到 main
   - 自动部署 GitHub Pages

---

## 🏆 贡献者认可

### 贡献者墙
所有贡献者将出现在：
- README 贡献者列表
- GitHub Contributors 页面
- 月度感谢 Issue

### 贡献等级
| 等级 | 要求 | 权益 |
|------|------|------|
| 🥉 青铜 | 1 篇论文推荐 | 贡献者列表 |
| 🥈 白银 | 5 篇论文/代码改进 | 特别感谢 |
| 🥇 黄金 | 20 篇/重大功能 | 核心贡献者 |
| 💎 钻石 | 持续贡献 3 月+ | 协作成员 |

---

## ❓ 常见问题

### Q: 如何推荐自己发表的论文？
A: 欢迎！请在推荐时说明作者身份，我们会优先处理。

### Q: 可以推荐预印本吗？
A: 可以，arXiv 预印本同样欢迎。

### Q: 发现本体模型有遗漏怎么办？
A: 创建 Issue 详细说明，我们会讨论后决定是否扩展。

### Q: 如何联系维护者？
A: 通过 Issue 或查看 README 中的联系方式。

---

## 📧 联系方式

- 📬 **Issues**: 首选沟通渠道
- 📧 **Email**: *(待配置)*
- 💬 **Discord**: *(待配置)*

---

<div align="center">

**感谢你的贡献，一起构建智能体记忆的知识版图！** 🗺️

[📄 返回主页](README.md)

</div>

# Skills - 论文处理技能

本目录包含自动化处理论文的技能代码。

## 📁 目录结构

```
skills/
└── paper-reader/
    ├── SKILL.md           # 技能说明
    ├── extract-paper.py   # 论文提取脚本
    └── templates/
        └── summary-template.html  # HTML 总结模板
```

## 🔧 使用方式

这些技能由 OpenClaw 自动调用，无需手动运行。

### 手动测试（可选）

```bash
cd skills/paper-reader
python extract-paper.py 2511.06449  # arXiv ID
```

## 📝 技能说明

详见主项目的 paper-reader 技能文档。

---

**注意**: 技能代码会与主 OpenClaw 工作区的技能保持同步。

# 论文阅读处理经验教训

## 📋 Mermaid 架构图绘制规范

### ✅ **正确做法**
1. **遵循 CompassMem 模板标准**
   - 使用 emoji + 中文标题格式（如 "📥 用户查询"）
   - 保持与模板一致的配色和文字大小
   - 确保图表区域自适应显示

2. **双语标注要求**
   - 所有节点必须包含中英文双语
   - 格式：`中文\nEnglish`（使用 `\n` 换行）
   - 保持术语一致性

3. **连接关系完整性**
   - 必须有明确的数据流向箭头
   - 展示完整的输入→处理→输出流程
   - 层间交互关系要准确反映论文描述

4. **架构准确性**
   - 严格按照论文的架构图设计
   - 准确反映核心组件和模块关系
   - 避免过度简化或错误抽象

### ❌ **避免的错误**
1. **样式不一致**
   - 不要使用纯英文节点
   - 不要忽略 emoji 标识
   - 不要改变模板的视觉风格

2. **连接缺失**
   - 不要创建孤立的节点
   - 不要省略关键的数据流向
   - 不要使用双向连接（除非论文明确说明）

3. **技术细节错误**
   - 不要凭印象绘制架构
   - 不要忽略论文中的关键组件
   - 不要过度简化复杂关系

## 🛠️ 质量检查清单

在生成每篇论文文档前，必须检查：

- [ ] Mermaid 图表是否遵循 CompassMem 模板样式？
- [ ] 所有节点是否包含中英文双语标注？
- [ ] 数据流向是否完整且准确？
- [ ] 架构图是否真实反映论文内容？
- [ ] MD 和 HTML 文档是否保持完全一致？
- [ ] **实验数据是否从 PDF 提取（优先）或项目主页获取？**

## 🔧 技术实现要点

1. **Mermaid 语法验证**
   - 使用 `flowchart TB` 作为起始
   - subgraph 标题使用 `"emoji 标题"` 格式
   - 节点内容使用 `名称[中文\nEnglish]` 格式

2. **响应式设计**
   - 确保图表在移动端正常显示
   - 使用 `min-width: 600px` 保证可读性
   - 测试不同屏幕尺寸下的渲染效果

3. **版本控制**
   - 每次修改都要单独提交
   - 提交信息要明确说明修复内容
   - 保持 Git 历史的清晰可追溯

## ⚠️ **批次处理关键提醒**

### **批次完成必须执行完整12步流程**
- **步骤9-12是批次价值的核心体现，绝不能遗漏**
- **批次结束时必须生成分析报告、更新本体论、同步README和site/index.html**
- **单篇处理完成后立即提交，但批次价值体现在整体分析中**
- **批次最终提交必须包含远程推送和批次总结消息**

## 📥 PDF 下载和解析流程 ⭐ **新增**

### 何时使用 PDF
- arXiv HTML 版本实验数据不完整
- 需要提取具体数值（如 57.36, 38.84 等）
- 表格数据在 HTML 中被截断

### 下载方法
```bash
# arXiv PDF URL 格式
https://arxiv.org/pdf/{arxiv_id}.pdf
示例：https://arxiv.org/pdf/2512.02425.pdf
```

### 解析工具
```python
# 方法 1: pymupdf (推荐，已安装)
import fitz
doc = fitz.open(pdf_path)
for page in doc:
    text = page.get_text()
    tables = page.find_tables()

# 方法 2: pdfplumber (表格提取更好，已安装 ✅)
import pdfplumber
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
```

### 数据提取策略 ⭐ **优化**

**核心原则**: 按需提取，而非固定提取 Table 1

**1. 明确数据需求** (在提取前先思考)
```
需要提取什么？
├─ 主实验结果？→ 找 "main results", "comparison with SOTA"
├─ 消融实验？→ 找 "ablation study", "analysis"
├─ 效率对比？→ 找 "efficiency", "runtime", "FLOPs"
├─ 用户研究？→ 找 "user study", "human evaluation"
└─ 特定基准？→ 找基准名称 "LVBench", "VideoMME" 等
```

**2. 智能定位表格**
```python
# 方法 1: 搜索关键词定位页面
keywords = ["Table", "Benchmark", "Results", "Performance", "Comparison"]
for i, page in enumerate(pdf.pages):
    text = page.extract_text()
    for keyword in keywords:
        if keyword.lower() in text.lower():
            print(f"找到 '{keyword}' 在第 {i+1} 页")
            tables = page.extract_tables()
            # 分析表格内容，判断是否需要

# 方法 2: 直接提取所有表格，按需筛选
all_tables = []
for i, page in enumerate(pdf.pages):
    tables = page.extract_tables()
    for table in tables:
        if table and len(table) > 2:  # 至少 3 行才是有效表格
            all_tables.append({
                'page': i+1,
                'table': table,
                'preview': str(table[0])[:100]  # 第一行预览
            })

# 根据预览判断哪些表格需要详细处理
```

**3. 按需提取具体数据**
```
根据论文类型和任务需求:

长视频理解论文 (如 WorldMM):
├─ 主实验：5 个基准的平均提升和各项数据
├─ 消融实验：各组件贡献 (视觉记忆、语义记忆等)
└─ 效率数据：推理时间、内存占用 (如有)

RAG/检索论文:
├─ 检索准确率：R@1, R@5, R@10
├─ 生成质量：BLEU, ROUGE, METEOR
└─ 端到端指标：F1, EM, Accuracy

多模态论文:
├─ 各模态贡献：text-only, image-only, multimodal
├─ 跨模态检索：text→image, image→text
└─ 生成质量：FID, CLIP Score 等
```

**4. 验证和整理**
```python
# 提取后验证数据完整性
def validate_extracted_data(data):
    checks = {
        '有具体数值': any(str(c).replace('.','').isdigit() for c in data),
        '有模型对比': len(set(data)) > 1,
        '有基准名称': any(name in str(data) for name in ['LVBench', 'VideoMME']),
        '有关键指标': any(metric in str(data) for metric in ['%', 'F1', 'Accuracy'])
    }
    return all(checks.values())
```

---
**最后更新**: 2026-03-22  
**适用范围**: 所有后续论文处理
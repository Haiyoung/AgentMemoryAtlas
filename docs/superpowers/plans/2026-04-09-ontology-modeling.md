# AgentMemory 本体论建模 + 站点重构 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create the `/ontology-update` skill, build the 1.0 ontology model, and redesign the GitHub Pages site with an interactive word cloud.

**Architecture:** Three sequential phases — (1) Generate data outputs (lexicon.json, ontology_base.md), (2) Build the site to consume that data, (3) Create the skill command for future updates. All output files are generated once and committed incrementally.

**Tech Stack:** Python (lexicon extraction + site generation), Markdown (ontology docs), HTML/JS/CSS (d3-cloud word cloud), Claude Code commands (skill definition).

---

## File Structure

| File | Action | Responsibility |
|------|--------|----------------|
| `.claude/commands/ontology-update.md` | Create | Skill command prompt |
| `scripts/extract-lexicon.py` | Create | Parse ontology_XXXX.md docs → extract concepts → generate lexicon.json |
| `scripts/build-site.py` | Create | Read lexicon.json + ontology_base.md → generate site/index.html |
| `ontology/lexicon.json` | Create (by script) | Word cloud data source (concepts, weights, relations, categories) |
| `ontology/ontology_base.md` | Rewrite | Structured ontology model (replaces current auto-extracted dump) |
| `ontology/changelogs/CHANGELOG_001.md` | Create | 1.0 baseline changelog |
| `ontology/backups/` | Create (dir) | Backup directory for future updates |
| `site/index.html` | Rewrite | GitHub Pages site with word cloud |
| `.gitignore` | Modify | Add `ontology/backups/` exclusion if needed |

---

### Task 1: Create directory structure + lexicon extraction script

**Files:**
- Create: `scripts/extract-lexicon.py`
- Create: `.claude/commands/` (dir)
- Create: `ontology/changelogs/` (dir)
- Create: `ontology/backups/` (dir)
- Output: `ontology/lexicon.json`

- [ ] **Step 1: Create directories**

```bash
mkdir -p .claude/commands
mkdir -p ontology/changelogs
mkdir -p ontology/backups
```

- [ ] **Step 2: Write lexicon extraction script**

`scripts/extract-lexicon.py` reads all `ontology/ontology_*.md` files and `ontology/Agent Memory 本体论领域模型（完整版）.md`, extracts concepts, deduplicates, calculates frequencies, and outputs `ontology/lexicon.json`.

```python
#!/usr/bin/env python3
"""
Extract concepts from ontology analysis documents and the base model
to generate lexicon.json for the word cloud.

Reads:
  - ontology/ontology_*.md (structured analysis docs)
  - ontology/Agent Memory 本体论领域模型（完整版）.md (base model)

Writes:
  - ontology/lexicon.json
"""

import json
import re
import glob
import os
from collections import defaultdict
from pathlib import Path

# Category definitions with colors
CATEGORIES = {
    "memory_type": {"name": "记忆类型", "nameEn": "Memory Type", "color": "#3b82f6"},
    "memory_structure": {"name": "记忆结构", "nameEn": "Memory Structure", "color": "#8b5cf6"},
    "memory_operation": {"name": "记忆操作", "nameEn": "Memory Operation", "color": "#f59e0b"},
    "memory_carrier": {"name": "记忆载体", "nameEn": "Memory Carrier", "color": "#16a34a"},
    "axiom": {"name": "公理约束", "nameEn": "Axiom", "color": "#ef4444"},
    "function": {"name": "功能定位", "nameEn": "Function", "color": "#0ea5e9"},
    "agent": {"name": "智能体类型", "nameEn": "Agent Type", "color": "#ec4899"},
    "context": {"name": "上下文", "nameEn": "Context", "color": "#14b8a6"},
    "entity": {"name": "实体", "nameEn": "Entity", "color": "#f97316"},
    "policy": {"name": "策略", "nameEn": "Policy", "color": "#a855f7"},
    "evaluation": {"name": "评估基准", "nameEn": "Evaluation", "color": "#64748b"},
    "security": {"name": "安全", "nameEn": "Security", "color": "#dc2626"},
}

# Mapping from ontology analysis section names to categories
SECTION_TO_CATEGORY = {
    "memory_types": "memory_type",
    "memory_structures": "memory_structure",
    "memory_operations": "memory_operation",
    "memory_carriers": "memory_carrier",
}


def clean_concept_name(name):
    """Normalize concept name for deduplication."""
    name = name.strip()
    # Remove parentheses content for matching (but keep for display)
    base = re.sub(r'\s*\(.*?\)\s*', '', name).strip()
    return base, name


def parse_ontology_analysis_doc(filepath):
    """Parse an ontology_XXXX.md file and extract concepts, relations, axioms."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    arxiv_id = None
    title = None
    concepts = []  # (name, category, arxiv_id)
    relations = []
    axioms = []

    # Extract arxiv_id
    m = re.search(r'arxiv_id[：:]\s*(.+)', content)
    if m:
        arxiv_id = m.group(1).strip()

    # Extract title
    m = re.search(r'title[：:]\s*(.+)', content)
    if m:
        title = m.group(1).strip()

    # Extract concepts from ### new_concepts section
    # Pattern: - **memory_types**: ['Concept1', 'Concept2']
    for section, category in SECTION_TO_CATEGORY.items():
        pattern = rf'\*\*{section}\*\*.*?\[(.*?)\]'
        m = re.search(pattern, content, re.DOTALL)
        if m:
            items_str = m.group(1)
            items = re.findall(r"'([^']+)'", items_str)
            for item in items:
                base, display = clean_concept_name(item)
                concepts.append((base, display, category, arxiv_id))

    # Extract relations from ### new_relations section
    for rel_type in ['is_a', 'part_of', 'related_to']:
        pattern = rf'\*\*{rel_type}\*\*.*?\[(.*?)\]'
        m = re.search(pattern, content, re.DOTALL)
        if m:
            items_str = m.group(1)
            # Parse dict-like strings: {'source': 'X', 'target': 'Y', 'description': 'Z'}
            dict_matches = re.findall(r"\{'source':\s*'([^']+)',\s*'target':\s*'([^']+)',\s*'description':\s*'([^']*)'\}", items_str)
            for src, tgt, desc in dict_matches:
                relations.append({"from": src, "to": tgt, "type": rel_type, "description": desc})

    # Extract axioms from ### new_axioms section
    for axiom_type in ['theoretical', 'validation']:
        pattern = rf'\*\*{axiom_type}\*\*.*?\[(.*?)\]'
        m = re.search(pattern, content, re.DOTALL)
        if m:
            items_str = m.group(1)
            items = re.findall(r"'([^']+)'", items_str)
            for item in items:
                axioms.append({"type": axiom_type, "text": item, "source": arxiv_id})

    return {
        "arxiv_id": arxiv_id,
        "title": title,
        "concepts": concepts,
        "relations": relations,
        "axioms": axioms,
    }


def parse_base_model(filepath):
    """Parse the base model MD and extract concepts with their categories."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    concepts = []

    # Extract concepts from specific subsections
    # 3.2 Memory subclasses
    memory_patterns = [
        (r'\*\*SensoryMemory.*?\*\*', 'memory_type'),
        (r'\*\*ShortTermMemory.*?\*\*', 'memory_type'),
        (r'\*\*LongTermMemory.*?\*\*', 'memory_type'),
        (r'\*\*EpisodicMemory.*?\*\*', 'memory_type'),
        (r'\*\*SemanticMemory.*?\*\*', 'memory_type'),
        (r'\*\*ProceduralMemory.*?\*\*', 'memory_type'),
        (r'\*\*WorkingMemory.*?\*\*', 'memory_type'),
    ]
    for pattern, category in memory_patterns:
        matches = re.findall(pattern, content)
        for m in matches:
            name = re.sub(r'[（\(].*?[）\)]', '', m).replace('**', '').replace('*', '').strip()
            if name:
                concepts.append((name.lower(), name, category, None))

    return concepts


def main():
    repo_root = Path(__file__).parent.parent
    ontology_dir = repo_root / "ontology"

    # Collect all concept data
    concept_map = defaultdict(lambda: {
        "display_names": set(),
        "categories": set(),
        "sources": set(),
        "weight": 0,
    })
    all_relations = []
    all_axioms = []

    # Parse all ontology analysis docs
    analysis_files = sorted(glob.glob(str(ontology_dir / "ontology_*.md")))
    print(f"Found {len(analysis_files)} ontology analysis docs")

    for filepath in analysis_files:
        result = parse_ontology_analysis_doc(filepath)
        arxiv_id = result["arxiv_id"]

        for base, display, category, src in result["concepts"]:
            entry = concept_map[base]
            entry["display_names"].add(display)
            entry["categories"].add(category)
            if arxiv_id:
                entry["sources"].add(arxiv_id)
            entry["weight"] += 1

        all_relations.extend(result["relations"])
        all_axioms.extend(result["axioms"])

    # Parse base model
    base_model_path = ontology_dir / "Agent Memory 本体论领域模型（完整版）.md"
    if base_model_path.exists():
        base_concepts = parse_base_model(str(base_model_path))
        for base, display, category, src in base_concepts:
            entry = concept_map[base]
            entry["display_names"].add(display)
            entry["categories"].add(category)
            entry["weight"] = max(entry["weight"], 1)  # Ensure weight >= 1

    # Deduplicate relations
    unique_relations = []
    seen_relations = set()
    for r in all_relations:
        key = (r["from"], r["to"], r["type"])
        if key not in seen_relations:
            seen_relations.add(key)
            unique_relations.append(r)

    # Build lexicon
    concepts_list = []
    for base, data in sorted(concept_map.items(), key=lambda x: -x[1]["weight"]):
        primary_name = max(data["display_names"], key=len)  # Use longest name as display
        concept = {
            "id": base.lower().replace(' ', '-').replace('_', '-'),
            "name": primary_name,
            "category": list(data["categories"])[0] if data["categories"] else "memory_type",
            "weight": data["weight"],
            "relatedConcepts": [
                r["to"] for r in unique_relations if r["from"] == primary_name
            ] + [
                r["from"] for r in unique_relations if r["to"] == primary_name
            ],
            "sourcePapers": sorted(list(data["sources"])),
        }
        concepts_list.append(concept)

    # Deduplicate relations for output
    relations_list = []
    for r in unique_relations:
        relations_list.append({
            "from": r["from"],
            "to": r["to"],
            "type": r["type"],
            "description": r["description"],
        })

    lexicon = {
        "version": "1.0.0",
        "generatedAt": "2026-04-10",
        "conceptCount": len(concepts_list),
        "relationCount": len(relations_list),
        "concepts": concepts_list,
        "relations": relations_list,
        "axioms": all_axioms,
        "categories": CATEGORIES,
    }

    # Write lexicon.json
    output_path = ontology_dir / "lexicon.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(lexicon, f, ensure_ascii=False, indent=2)

    print(f"Generated lexicon.json: {len(concepts_list)} concepts, {len(relations_list)} relations")
    print(f"Top concepts by weight:")
    for c in sorted(concepts_list, key=lambda x: -x["weight"])[:10]:
        print(f"  {c['name']}: weight={c['weight']}, sources={len(c['sourcePapers'])}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 3: Run the script**

```bash
cd /Users/haiyoung/workspace/AgentMemoryAtlas
python scripts/extract-lexicon.py
```

Expected output: `Generated lexicon.json: XXX concepts, YYY relations` with top 10 concepts listed.

- [ ] **Step 4: Verify lexicon.json**

```bash
python3 -c "import json; d=json.load(open('ontology/lexicon.json')); print(f'Concepts: {d[\"conceptCount\"]}, Relations: {d[\"relationCount\"]}, Categories: {len(d[\"categories\"])}')"
```

- [ ] **Step 5: Commit**

```bash
git add scripts/extract-lexicon.py .claude/commands/ ontology/changelogs/ ontology/backups/ ontology/lexicon.json
git commit -m "feat: generate lexicon.json from 147 ontology analysis docs"
```

---

### Task 2: Generate ontology_base.md 1.0

**Files:**
- Read: `ontology/Agent Memory 本体论领域模型（完整版）.md`
- Read: `ontology/lexicon.json` (from Task 1)
- Rewrite: `ontology/ontology_base.md`

This task requires LLM reasoning to synthesize a structured ontology model. It reads the base model skeleton, the extracted lexicon, and reorganizes ontology_base.md into a clean, structured document.

- [ ] **Step 1: Back up current ontology_base.md**

```bash
cp ontology/ontology_base.md ontology/backups/ontology_base_pre_v1.0.md
```

- [ ] **Step 2: Generate new ontology_base.md**

The new document structure:

```markdown
---
title: Agent Memory 领域本体论
description: Agent Memory 领域本体论模型 v1.0
current_version: '1.0'
based_on_version: '0'
created_at: 2026-04-10
updated_at: '2026-04-10T00:00:00'
papers_covered: <actual count from ontology analysis docs>
---

# Agent Memory 领域本体论 v1.0

## 一、本体论核心基础

Agent Memory 本体遵循"三维正交分类 + 类层级"双轨架构。

### 1.1 三维正交分类

每个记忆概念由三个维度的坐标唯一确定：

| 载体维度 (Carrier) | 功能维度 (Function) | 动态维度 (Dynamic) |
|--------------------|--------------------|--------------------|
| Token-level | Factual | Formation |
| Parametric | Experiential | Evolution |
| External | Procedural | Retrieval |
| Latent | Working | Forgetting |
| | Episodic | Reflection |
| | Semantic | Association |

### 1.2 顶层核心类（8个）

| 顶层类 | 核心定位 |
|--------|---------|
| Agent | 记忆主体 |
| Memory | 记忆载体（含参数/外部/Token） |
| MemorySystem | 记忆管理架构 |
| MemoryEvent | 记忆触发源 |
| MemoryOperation | 记忆操作行为 |
| Context | 记忆关联场景 |
| Entity | 记忆关联对象（含关系） |
| Policy | 记忆操作规则（含安全策略） |

### 1.3 核心原则

- 语义唯一性
- 层级清晰性
- 工程适配性
- 可扩展性

---

## 二、核心公理体系

### 2.1 存在公理

- 每个记忆实例必须占据至少一个载体维度位置
- 没有无来源的记忆（每条记忆必须关联至少一个 MemoryEvent）

### 2.2 操作公理

- 检索必有索引
- 遗忘不可逆
- 反思产生新知

### 2.3 质量公理

- 记忆质量 = f(新鲜度, 一致性, 置信度)

### 2.4 安全公理

- 检索深度与隐私风险正相关（源自 2502.13172）
- 格式化检索比语义检索更易被攻击

### 2.5 演进公理

- 记忆随使用而强化（accessCount↑ → importance↑）
- 记忆随时间而衰减（未访问 → importance↓）

---

## 三、概念关系网络

### 3.1 形式维度网络 (Forms)

...从 lexicon.json 中按 category 聚合...

### 3.2 功能维度网络 (Functions)

...从 lexicon.json 中按 category 聚合...

### 3.3 动态维度网络 (Dynamics)

...从 lexicon.json 中按 category 聚合...

---

## 四、跨维度整合网络

### 4.1 三维一体记忆模型

```
[Form] ←→ [Function] ←→ [Dynamics]
   ↑         ↑           ↑
结构化     目标导向     生命周期
表示       应用        管理
```

### 4.2 认知架构集成

- 感知层: 原始输入 → 记忆形成
- 记忆层: 结构化存储 ↔ 动态演化 ↔ 目标检索
- 推理层: 记忆检索 → 上下文合成 → 决策生成
- 行动层: 决策执行 → 经验反馈 → 记忆更新

---

## 五、记忆结构类型

...从 lexicon.json 中提取所有 memory_structure 概念，按论文来源分组...

## 六、记忆操作机制

...从 lexicon.json 中提取所有 memory_operation 概念...

## 七、记忆载体类型

...从 lexicon.json 中提取所有 memory_carrier 概念...

## 八、记忆功能定位

...从 lexicon.json 中提取所有 memory_type 概念...

## 九、概念关系网络

### 9.1 is-a 关系

...从 lexicon.json relations 中提取...

### 9.2 part-of 关系

...从 lexicon.json relations 中提取...

### 9.3 related-to 关系

...从 lexicon.json relations 中提取...

---

## 十、验证公理

...从 ontology analysis docs 的 new_axioms 中提取...

## 十一、未来发展方向

### 短期 (2025-2026)
### 中期 (2027-2028)
### 长期 (2029+)

---

## 十二、概念索引

...完整的去重概念列表，每个概念标注来源论文...
```

The content for each section **must be fully written with actual content** — do not leave empty sections or placeholders. Specifically:

1. Read `ontology/lexicon.json` to get the complete concept list
2. Read `ontology/Agent Memory 本体论领域模型（完整版）.md` for class hierarchy definitions
3. Sample 5-10 ontology analysis docs (e.g., ontology_2502.13172.md, ontology_2502.06049.md, ontology_2410.14052.md) to understand detailed concept descriptions
4. **Write the full ontology_base.md** following the structure above, filling in every section with real content:
   - Section 五 (记忆结构类型): List every memory_structure concept from lexicon.json with its source papers
   - Section 六 (记忆操作机制): List every memory_operation concept with descriptions
   - Section 七 (记忆载体类型): List every memory_carrier concept
   - Section 八 (记忆功能定位): List every memory_type concept grouped by function
   - Section 九 (概念关系网络): Include all relations from lexicon.json organized by type
   - Section 十 (验证公理): Include all axioms from ontology analysis docs, with source citations
5. Ensure all 8 top-level classes from the spec are covered
6. Include the 5 axiom categories (存在/操作/质量/安全/演进)
7. The document should be comprehensive and readable — this is the canonical reference for the domain

- [ ] **Step 3: Verify the new ontology_base.md**

```bash
wc -l ontology/ontology_base.md
head -15 ontology/ontology_base.md
```

Should have a clean YAML frontmatter and start with the v1.0 title.

- [ ] **Step 4: Commit**

```bash
git add ontology/ontology_base.md
git commit -m "feat: generate ontology_base.md v1.0 - structured ontology model"
```

---

### Task 3: Generate CHANGELOG_001.md

**Files:**
- Create: `ontology/changelogs/CHANGELOG_001.md`

- [ ] **Step 1: Write CHANGELOG_001.md**

```markdown
# CHANGELOG_001 — 本体论 v1.0 基线

**日期**: 2026-04-10
**类型**: 首次建模（结构性重写）

## 概述

基于 147 篇本体论分析文档（ontology_XXXX.md）和基础模型骨架（"完整版.md"），
首次构建 Agent Memory 领域本体论 v1.0 模型。

## 概念统计

- 总概念数: <N>（从 lexicon.json 读取）
- 总关系数: <M>（从 lexicon.json 读取）
- 覆盖论文: <K> 篇
- 分类维度: 12 个

## 顶层类（8个）

- Agent — 记忆主体（保留）
- Memory — 记忆载体（合并原 Memory + MemoryContent）
- MemorySystem — 记忆管理架构
- MemoryEvent — 记忆触发源
- MemoryOperation — 记忆操作行为
- Context — 记忆关联场景
- Entity — 记忆关联对象（合并原 Entity + Relation）
- Policy — 记忆操作规则（新增安全策略子类）

## 公理体系

- 存在公理: 2 条
- 操作公理: 3 条
- 质量公理: 1 条
- 安全公理: 2 条（源自 2502.13172 隐私研究）
- 演进公理: 2 条

## 三维分类架构

- 载体维度: Token-level, Parametric, External, Latent
- 功能维度: Factual, Experiential, Procedural, Working, Episodic, Semantic
- 动态维度: Formation, Evolution, Retrieval, Forgetting, Reflection, Association

## 来源依据

- `ontology/Agent Memory 本体论领域模型（完整版）.md` — 分类骨架
- `ontology/ontology_XXXX.md` (147 篇) — 结构化分析证据
- `ontology/lexicon.json` — 概念词库
```

Read lexicon.json to fill in the `<N>`, `<M>`, `<K>` values before writing.

- [ ] **Step 2: Commit**

```bash
git add ontology/changelogs/CHANGELOG_001.md
git commit -m "docs: add CHANGELOG_001 — ontology v1.0 baseline"
```

---

### Task 4: Build site/index.html with word cloud

**Files:**
- Rewrite: `site/index.html`

This is a single-page HTML file with:
- d3-cloud for word cloud layout
- SVG overlay for relation lines
- Filter bar by category
- Sidebar navigation (sticky)
- Ontology body content (embedded or fetched)
- Paper brief section (populated from lexicon.json)

- [ ] **Step 1: Write site/index.html**

The HTML file is self-contained, using CDN-loaded libraries:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AgentMemoryAtlas - Agent Memory 领域本体论知识库</title>
    <meta name="description" content="Agent Memory 领域本体论知识库 — 交互式词云浏览器">
    <style>
        /* CSS variables */
        :root {
            --bg-primary: #ffffff;
            --bg-secondary: #f8fafc;
            --text-primary: #1e293b;
            --text-secondary: #64748b;
            --border-color: #e2e8f0;
            --primary: #3b82f6;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
            --shadow-md: 0 4px 12px rgba(0,0,0,0.12);
            --radius-md: 12px;
            --radius-lg: 20px;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', sans-serif;
            background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
            color: var(--text-primary);
            line-height: 1.6;
        }

        /* Header */
        header {
            text-align: center;
            padding: 2.5rem 1.5rem 1.5rem;
        }

        .header-title {
            font-size: 2.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, var(--primary), #0ea5e9);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .header-subtitle {
            font-size: 1.1rem;
            color: var(--text-secondary);
            margin-top: 0.25rem;
        }

        /* Stats bar */
        .stats-bar {
            display: flex;
            justify-content: center;
            gap: 2rem;
            padding: 1rem;
            font-size: 0.9rem;
            color: var(--text-secondary);
        }

        .stats-bar span { font-weight: 600; color: var(--primary); }

        /* Container */
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 1.5rem;
        }

        /* Filter bar */
        .filter-bar {
            display: flex;
            justify-content: center;
            gap: 0.5rem;
            flex-wrap: wrap;
            padding: 1rem 0;
            margin-bottom: 1rem;
        }

        .filter-btn {
            padding: 0.4rem 1rem;
            border: 1.5px solid var(--border-color);
            border-radius: 20px;
            background: var(--bg-primary);
            color: var(--text-secondary);
            font-size: 0.85rem;
            cursor: pointer;
            transition: all 0.2s;
        }

        .filter-btn:hover, .filter-btn.active {
            border-color: var(--primary);
            color: var(--primary);
            background: #eff6ff;
        }

        /* Word cloud */
        .wordcloud-section {
            background: var(--bg-primary);
            border-radius: var(--radius-lg);
            box-shadow: var(--shadow-md);
            padding: 1.5rem;
            margin-bottom: 2rem;
            position: relative;
            min-height: 500px;
        }

        #wordcloud-svg {
            width: 100%;
            height: 500px;
        }

        .wordcloud-svg .word {
            cursor: pointer;
            transition: opacity 0.2s;
        }

        .wordcloud-svg .word:hover { opacity: 0.8; }
        .wordcloud-svg .word.highlighted {
            font-weight: bold !important;
        }
        .wordcloud-svg .word.dimmed { opacity: 0.2 !important; }

        .wordcloud-svg .relation-line {
            stroke-dasharray: 4, 4;
            stroke-width: 1.5;
            opacity: 0.6;
        }

        /* Main content: sidebar + ontology body */
        .main-content {
            display: grid;
            grid-template-columns: 220px 1fr;
            gap: 2rem;
            margin-bottom: 3rem;
        }

        @media (max-width: 900px) {
            .main-content { grid-template-columns: 1fr; }
        }

        /* Sidebar */
        .sidebar {
            position: sticky;
            top: 1rem;
            align-self: start;
            background: var(--bg-primary);
            border-radius: var(--radius-md);
            padding: 1.5rem;
            box-shadow: var(--shadow-sm);
        }

        .sidebar h3 {
            font-size: 1rem;
            margin-bottom: 1rem;
            color: var(--text-primary);
        }

        .sidebar nav a {
            display: block;
            padding: 0.35rem 0.75rem;
            color: var(--text-secondary);
            text-decoration: none;
            font-size: 0.9rem;
            border-left: 2px solid transparent;
            transition: all 0.15s;
        }

        .sidebar nav a:hover, .sidebar nav a.active {
            color: var(--primary);
            border-left-color: var(--primary);
            background: #f0f7ff;
        }

        /* Ontology body */
        .ontology-body {
            background: var(--bg-primary);
            border-radius: var(--radius-md);
            padding: 2rem;
            box-shadow: var(--shadow-sm);
        }

        .ontology-body h2 {
            font-size: 1.5rem;
            margin-top: 2rem;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid var(--border-color);
        }

        .ontology-body h2:first-child { margin-top: 0; }

        .ontology-body h3 {
            font-size: 1.2rem;
            margin-top: 1.5rem;
            margin-bottom: 0.75rem;
            color: var(--text-primary);
        }

        .ontology-body p {
            margin-bottom: 1rem;
            color: var(--text-secondary);
        }

        .ontology-body table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 1.5rem;
        }

        .ontology-body table th,
        .ontology-body table td {
            padding: 0.6rem 1rem;
            border: 1px solid var(--border-color);
            text-align: left;
            font-size: 0.9rem;
        }

        .ontology-body table th {
            background: var(--bg-secondary);
            font-weight: 600;
        }

        .ontology-body code {
            background: var(--bg-secondary);
            padding: 0.15rem 0.4rem;
            border-radius: 4px;
            font-size: 0.85rem;
        }

        .ontology-body pre {
            background: #1e293b;
            color: #e2e8f0;
            padding: 1rem;
            border-radius: var(--radius-md);
            overflow-x: auto;
            margin-bottom: 1.5rem;
        }

        .ontology-body pre code {
            background: none;
            padding: 0;
            color: inherit;
        }

        /* Paper brief section */
        .paper-section {
            margin-bottom: 3rem;
        }

        .paper-section h2 {
            font-size: 1.4rem;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .concept-tag {
            display: inline-block;
            padding: 0.2rem 0.6rem;
            border-radius: 12px;
            font-size: 0.8rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }

        .paper-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 1rem;
        }

        .paper-card {
            background: var(--bg-primary);
            border-radius: var(--radius-md);
            padding: 1.25rem;
            box-shadow: var(--shadow-sm);
            border: 2px solid transparent;
            transition: all 0.2s;
        }

        .paper-card.highlighted {
            border-color: var(--primary);
            box-shadow: var(--shadow-md);
        }

        .paper-card h4 {
            font-size: 1rem;
            margin-bottom: 0.4rem;
        }

        .paper-card .arxiv {
            font-size: 0.8rem;
            color: var(--primary);
            font-weight: 600;
        }

        .paper-card .desc {
            font-size: 0.85rem;
            color: var(--text-secondary);
            margin: 0.5rem 0;
        }

        /* Footer */
        footer {
            text-align: center;
            padding: 2rem;
            border-top: 1px solid var(--border-color);
            color: var(--text-secondary);
            font-size: 0.85rem;
        }

        footer a { color: var(--primary); text-decoration: none; }
    </style>
</head>
<body>
    <!-- Header -->
    <header>
        <h1 class="header-title">AgentMemoryAtlas</h1>
        <p class="header-subtitle">Agent Memory 领域本体论知识库</p>
        <div class="stats-bar" id="stats-bar"></div>
    </header>

    <div class="container">
        <!-- Filter bar -->
        <div class="filter-bar" id="filter-bar"></div>

        <!-- Word cloud -->
        <div class="wordcloud-section">
            <svg id="wordcloud-svg"></svg>
        </div>

        <!-- Main content: sidebar + ontology body -->
        <div class="main-content">
            <aside class="sidebar">
                <h3>📋 目录</h3>
                <nav id="sidebar-nav"></nav>
            </aside>
            <main class="ontology-body" id="ontology-body"></main>
        </div>

        <!-- Paper brief section -->
        <div class="paper-section" id="paper-section" style="display:none;">
            <h2>📚 相关论文: <span id="selected-concept"></span></h2>
            <div class="paper-grid" id="paper-grid"></div>
        </div>
    </div>

    <!-- Footer -->
    <footer>
        <p>&copy; 2026 AgentMemoryAtlas · 最后更新: <span id="last-updated"></span> ·
           <a href="https://github.com/Haiyoung/AgentMemoryAtlas">View on GitHub</a></p>
    </footer>

    <!-- Scripts: d3 + d3-cloud + marked -->
    <script src="https://cdn.jsdelivr.net/npm/d3@7"></script>
    <script src="https://cdn.jsdelivr.net/npm/d3-cloud@1.2.7/build/d3.layout.cloud.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <script>
    (function() {
        // Config
        const LEXICON_URL = '../ontology/lexicon.json';
        const ONTOLOGY_URL = '../ontology/ontology_base.md';
        const GITHUB_PAGES_BASE = 'https://haiyoung.github.io/AgentMemoryAtlas/';

        let lexicon = null;
        let ontologyMarkdown = '';
        let activeFilter = null;
        let hoveredWord = null;

        // Initialize
        async function init() {
            try {
                // Fetch data
                const [lexRes, ontoRes] = await Promise.all([
                    fetch(LEXICON_URL),
                    fetch(ONTOLOGY_URL)
                ]);

                if (!lexRes.ok) throw new Error('Failed to load lexicon.json');

                lexicon = await lexRes.json();

                if (ontoRes.ok) {
                    ontologyMarkdown = await ontoRes.text();
                }

                renderStats();
                renderFilters();
                renderWordCloud();
                renderSidebar();
                renderOntologyBody();
                renderFooter();
            } catch (err) {
                console.error('Failed to initialize:', err);
                document.getElementById('ontology-body').innerHTML =
                    '<p style="color:red;">Failed to load ontology data: ' + err.message + '</p>';
            }
        }

        // Render stats bar
        function renderStats() {
            const bar = document.getElementById('stats-bar');
            bar.innerHTML = `
                概念: <span>${lexicon.conceptCount}</span> &nbsp;|&nbsp;
                关系: <span>${lexicon.relationCount}</span> &nbsp;|&nbsp;
                版本: <span>${lexicon.version}</span>
            `;
            document.getElementById('last-updated').textContent = lexicon.generatedAt || '2026-04-10';
        }

        // Render filter buttons
        function renderFilters() {
            const bar = document.getElementById('filter-bar');
            const cats = lexicon.categories;
            let html = `<button class="filter-btn active" data-cat="all">全部</button>`;
            for (const [key, val] of Object.entries(cats)) {
                html += `<button class="filter-btn" data-cat="${key}">${val.name}</button>`;
            }
            bar.innerHTML = html;

            bar.addEventListener('click', (e) => {
                if (!e.target.classList.contains('filter-btn')) return;
                document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
                e.target.classList.add('active');
                activeFilter = e.target.dataset.cat === 'all' ? null : e.target.dataset.cat;
                renderWordCloud();
            });
        }

        // Render word cloud
        function renderWordCloud() {
            const svg = d3.select('#wordcloud-svg');
            svg.selectAll('*').remove();

            const container = document.querySelector('.wordcloud-section');
            const width = container.clientWidth - 48;
            const height = 500;

            svg.attr('viewBox', `0 0 ${width} ${height}`);

            // Filter concepts
            let concepts = lexicon.concepts;
            if (activeFilter) {
                concepts = concepts.filter(c => c.category === activeFilter);
            }

            // Limit to top 100 for readability
            concepts = concepts.slice(0, 100);

            const words = concepts.map(c => ({
                text: c.name,
                size: Math.max(12, Math.min(48, 10 + c.weight * 3)),
                category: c.category,
                id: c.id,
            }));

            const colorMap = {};
            for (const [key, val] of Object.entries(lexicon.categories)) {
                colorMap[key] = val.color;
            }

            const layout = d3.layout.cloud()
                .size([width, height])
                .words(words)
                .padding(4)
                .rotate(() => (~~(Math.random() * 3) - 1) * 15)
                .fontSize(d => d.size)
                .on('end', draw);

            layout.start();

            function draw(words) {
                const g = svg.append('g')
                    .attr('transform', `translate(${width/2},${height/2})`);

                // Draw relation lines first (behind words)
                const relationLayer = g.append('g').attr('class', 'relations');
                if (hoveredWord) {
                    const hwConcept = concepts.find(c => c.id === hoveredWord);
                    if (hwConcept) {
                        const relatedIds = new Set(hwConcept.relatedConcepts || []);
                        const relatedWords = words.filter(w => relatedIds.has(w.text) || relatedIds.has(w.id));

                        const hoveredWordEl = words.find(w => w.id === hoveredWord || w.text === hoveredWord);
                        if (hoveredWordEl) {
                            relatedWords.forEach(rw => {
                                relationLayer.append('line')
                                    .attr('class', 'relation-line')
                                    .attr('x1', hoveredWordEl.x)
                                    .attr('y1', hoveredWordEl.y)
                                    .attr('x2', rw.x)
                                    .attr('y2', rw.y)
                                    .attr('stroke', colorMap[hwConcept.category] || '#94a3b8');
                            });
                        }
                    }
                }

                const textLayer = g.selectAll('text')
                    .data(words)
                    .enter()
                    .append('text')
                    .attr('class', d => {
                        let cls = 'word';
                        if (hoveredWord) {
                            const hwConcept = concepts.find(c => c.id === hoveredWord);
                            const relatedIds = new Set((hwConcept?.relatedConcepts || []).concat(hoveredWord));
                            if (d.id === hoveredWord || relatedIds.has(d.text) || relatedIds.has(d.id)) {
                                cls += ' highlighted';
                            } else {
                                cls += ' dimmed';
                            }
                        }
                        return cls;
                    })
                    .attr('text-anchor', 'middle')
                    .attr('transform', d => `translate(${d.x},${d.y})rotate(${d.rotate})`)
                    .attr('font-size', d => d.size)
                    .attr('fill', d => colorMap[d.category] || '#94a3b8')
                    .attr('font-family', 'Inter, sans-serif')
                    .style('cursor', 'pointer')
                    .text(d => d.text)
                    .on('mouseenter', function(event, d) {
                        hoveredWord = d.id;
                        renderWordCloud();
                    })
                    .on('mouseleave', function() {
                        hoveredWord = null;
                        renderWordCloud();
                    })
                    .on('click', function(event, d) {
                        showPaperSection(d);
                    });
            }
        }

        // Show paper section for a concept
        function showPaperSection(concept) {
            const section = document.getElementById('paper-section');
            const title = document.getElementById('selected-concept');
            const grid = document.getElementById('paper-grid');

            const catInfo = lexicon.categories[concept.category] || {name: concept.category, color: '#94a3b8'};
            title.textContent = concept.name;
            title.style.color = catInfo.color;

            // Build paper cards from sourcePapers
            const papers = concept.sourcePapers || [];
            if (papers.length === 0) {
                grid.innerHTML = '<p style="color:var(--text-secondary);">暂无关联论文</p>';
            } else {
                grid.innerHTML = papers.map(arxivId => `
                    <div class="paper-card">
                        <span class="arxiv">${arxivId}</span>
                        <p class="desc">概念 "${concept.name}" 的来源论文</p>
                        <a href="${GITHUB_PAGES_BASE}papers/${findPaperPath(arxivId)}" class="paper-link" target="_blank">查看完整报告 →</a>
                    </div>
                `).join('');
            }

            section.style.display = 'block';
            section.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }

        // Helper to find paper HTML path from arxiv ID
        // NOTE: This placeholder is replaced by build-site.py (Task 5) with actual paper path mapping.
        // If running locally before build-site.py, this falls back to a search path.
        function findPaperPath(arxivId) {
            // This is a best-effort mapping — replaced by build-site.py with actual mapping
            return `paper/search/${arxivId}`;
        }

        // Render sidebar navigation
        function renderSidebar() {
            const nav = document.getElementById('sidebar-nav');
            if (!ontologyMarkdown) {
                nav.innerHTML = '<p style="font-size:0.85rem;color:var(--text-secondary);">加载中...</p>';
                return;
            }

            // Extract headings from markdown
            const headings = [];
            const regex = /^(#{2,3})\s+(.+)$/gm;
            let match;
            while ((match = regex.exec(ontologyMarkdown)) !== null) {
                const level = match[1].length;
                const text = match[2].replace(/[*_`]/g, '').trim();
                const id = text.toLowerCase().replace(/[^\w\u4e00-\u9fff]+/g, '-');
                headings.push({ level, text, id });
            }

            nav.innerHTML = headings.map(h =>
                `<a href="#${h.id}" style="padding-left:${(h.level - 2) * 0.75 + 0.75}rem">${h.text}</a>`
            ).join('');
        }

        // Render ontology body
        function renderOntologyBody() {
            const body = document.getElementById('ontology-body');
            if (!ontologyMarkdown) {
                body.innerHTML = '<p style="color:var(--text-secondary);">本体论正文加载中...</p>';
                return;
            }

            // Use marked to convert MD to HTML
            body.innerHTML = marked.parse(ontologyMarkdown);

            // Add IDs to headings for anchor navigation
            body.querySelectorAll('h2, h3').forEach(h => {
                const id = h.textContent.toLowerCase().replace(/[^\w\u4e00-\u9fff]+/g, '-');
                h.id = id;
            });
        }

        // Render footer
        function renderFooter() {
            // Already in HTML
        }

        // Start
        init();

        // Re-render word cloud on resize
        let resizeTimer;
        window.addEventListener('resize', () => {
            clearTimeout(resizeTimer);
            resizeTimer = setTimeout(renderWordCloud, 250);
        });
    })();
    </script>
</body>
</html>
```

- [ ] **Step 2: Preview the site locally**

```bash
cd /Users/haiyoung/workspace/AgentMemoryAtlas
python3 -m http.server 8080
```

Open `http://localhost:8080/site/index.html` in browser. Verify:
- Word cloud renders with colored words
- Filter buttons work
- Hover highlights related words with dashed lines
- Click shows paper section below
- Sidebar navigation links work
- Ontology body content loads from markdown

- [ ] **Step 3: Commit**

```bash
git add site/index.html
git commit -m "feat: redesign site with interactive word cloud browser"
```

---

### Task 5: Create build-site.py for CI/CD

**Files:**
- Create: `scripts/build-site.py`

- [ ] **Step 1: Write build-site.py**

This script reads `lexicon.json` and embeds stats into `site/index.html` for the initial page load (avoiding fetch latency for stats). It also validates that both files exist.

```python
#!/usr/bin/env python3
"""
Build script for GitHub Pages site.
Reads lexicon.json and updates site/index.html with current stats.

Used by CI/CD (.github/workflows/deploy-pages.yml) and local development.
"""

import json
import sys
from pathlib import Path

def main():
    repo_root = Path(__file__).parent.parent
    lexicon_path = repo_root / "ontology" / "lexicon.json"
    site_path = repo_root / "site" / "index.html"

    if not lexicon_path.exists():
        print("ERROR: ontology/lexicon.json not found. Run extract-lexicon.py first.")
        sys.exit(1)

    with open(lexicon_path, 'r', encoding='utf-8') as f:
        lexicon = json.load(f)

    print(f"Lexicon loaded: {lexicon['conceptCount']} concepts, {lexicon['relationCount']} relations, version {lexicon['version']}")

    if not site_path.exists():
        print("ERROR: site/index.html not found.")
        sys.exit(1)

    # Read current HTML
    with open(site_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Inject concept count into paper section mapping
    # Build a quick arxiv -> paper path mapping from the paper/ directory
    paper_dir = repo_root / "paper"
    paper_files = list(paper_dir.rglob("*.md"))

    arxiv_to_path = {}
    for pf in paper_files:
        fname = pf.stem  # e.g., "2502.13172_Unveiling Privacy Risks..."
        arxiv_id = fname.split('_')[0]  # e.g., "2502.13172"
        arxiv_to_path[arxiv_id] = pf.relative_to(repo_root)

    print(f"Found {len(arxiv_to_path)} papers in paper/ directory")

    # Update the findPaperPath function in the HTML to use the mapping
    # Replace the placeholder function with actual mapping
    mapping_json = json.dumps(arxiv_to_path, ensure_ascii=False)
    old_func = '''function findPaperPath(arxivId) {
            // This is a best-effort mapping
            return `search/${arxivId}`;
        }'''
    new_func = f'''function findPaperPath(arxivId) {{
            const mapping = {mapping_json};
            return mapping[arxivId] || `paper/search/${{arxivId}}`;
        }}'''

    html = html.replace(old_func, new_func)

    # Write back
    with open(site_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print("site/index.html updated with paper path mapping")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run the build script**

```bash
cd /Users/haiyoung/workspace/AgentMemoryAtlas
python scripts/build-site.py
```

- [ ] **Step 3: Commit**

```bash
git add scripts/build-site.py site/index.html
git commit -m "feat: add build-site.py for CI/CD paper path mapping"
```

---

### Task 6: Create the /ontology-update skill command

**Files:**
- Create: `.claude/commands/ontology-update.md`

- [ ] **Step 1: Write the skill command**

```markdown
# /ontology-update

## 角色

你是 AgentMemoryAtlas 项目的本体论建模工程师。你的任务是分析增量论文的本体论分析报告，更新本体论模型，生成词库和变更日志。

## 核心约束（必须遵守）

### 输入只读
**绝对禁止**修改 `ontology/` 目录下的任何 `ontology_*.md` 文件，也**绝对禁止**修改 `paper/` 目录下的任何文件。这些是证据源，不可变。你只能读取它们。

### 更新前备份
每次执行前，必须先备份当前的主文档和词库：

```bash
# 创建备份目录（如果不存在）
mkdir -p ontology/backups

# 获取时间戳
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# 备份当前版本
cp ontology/ontology_base.md "ontology/backups/ontology_base_backup_${TIMESTAMP}.md" 2>/dev/null
cp ontology/lexicon.json "ontology/backups/lexicon_backup_${TIMESTAMP}.json" 2>/dev/null

echo "备份完成: ${TIMESTAMP}"
```

## 执行流程

### Step 1: 识别增量

```bash
# 识别新增的本体论分析文档（最近 7 天内修改的）
find ontology/ -name "ontology_*.md" -mtime -7 -type f

# 如果用户传了参数 $ARGUMENTS，只处理指定批次
# 例如: /ontology-update --batch 2025-11
# 则只处理 ontology/2025-11/ 或文件名中包含 2511 的文档
```

如果没有新增文档，输出："未检测到新增的本体论分析文档。" 并停止。

### Step 2: 阅读输入

读取以下文件：
1. 新增的 `ontology/ontology_*.md` 分析文档
2. 当前的 `ontology/ontology_base.md`（了解现有模型结构）
3. 当前的 `ontology/lexicon.json`（了解现有词库）

对于每篇新增的分析文档，提取：
- `new_concepts`（memory_types, memory_structures, memory_operations, memory_carriers）
- `new_relations`（is_a, part_of, related_to）
- `new_axioms`（theoretical, validation）
- `technical_contributions`
- `coverage_dimensions`

### Step 3: 概念归并（Taxonomy Update）

对每个新概念，判断：
1. **已存在**：是否在 lexicon.json 中已有同名或语义相近的概念？如果是，增加 weight，添加来源论文
2. **新子类**：是否属于已有类的子类？如果是，归入对应类的子类下
3. **新维度**：是否代表全新的概念维度？如果是，考虑是否需要新增维度

去重规则：
- 名称相同或语义高度相似的概念必须合并
- 合并后保留最长的描述文本
- 来源论文列表取并集

### Step 4: 关系图更新（Relation Graph Update）

- 新增关系添加到 lexicon.json 的 relations 数组
- 检查是否有重复关系（相同 from-to-type 三元组）
- 检查是否有循环依赖或孤立节点
- 更新概念的 relatedConcepts 字段

### Step 5: 公理演化（Axiom Evolution）

- 新公理：如果与现有公理不冲突，直接添加
- 冲突公理：如果新论文的数据反驳了现有公理，添加条件限定（如"在 X 前提下成立"）
- 合并公理：多篇论文指向同一规律时，合并为一条，标注所有来源

### Step 6: 输出生成

#### 6.1 更新 ontology/ontology_base.md

按照以下结构重写（保留已有完善的描述，注入新发现）：

```
---
title: Agent Memory 领域本体论
current_version: '<新版本号>'
updated_at: '<当前时间>'
papers_covered: <更新后的总数>
---

[保持现有结构，增量更新内容]
```

#### 6.2 运行 lexicon 提取脚本

```bash
python scripts/extract-lexicon.py
```

#### 6.3 生成 CHANGELOG

在 `ontology/changelogs/` 下创建 `CHANGELOG_NNN.md`（NNN 按顺序递增）：

```markdown
# CHANGELOG_NNN — 基于 [批次/论文列表] 分析

**日期**: YYYY-MM-DD
**类型**: 增量更新

## 概念变更
- 新增: ...
- 合并: ...
- 修正: ...

## 关系变更
- 新增: ...

## 公理演化
- ...

## 依据论文
- ...
```

#### 6.4 重建站点

```bash
python scripts/build-site.py
```

### Step 7: 提交

```bash
git add ontology/ontology_base.md ontology/lexicon.json ontology/changelogs/CHANGELOG_NNN.md ontology/backups/ site/index.html
git commit -m "feat: ontology update v<版本号> — <简要描述>"
```

## 版本编号规则

版本号格式: `major.minor.patch`
- major: 结构性重写时增加（如 1.0, 2.0）
- minor: 大量新增概念时增加（如 1.1, 1.2）
- patch: 少量增量更新时增加（如 1.0.1, 1.0.2）

从当前版本号的 patch 位 +1 开始。如果当前没有版本号，从 1.0.1 开始。
```

- [ ] **Step 2: Test the command structure**

Verify the file is discoverable by Claude Code:

```bash
ls -la .claude/commands/ontology-update.md
```

The file should exist. Claude Code will automatically discover it and make `/ontology-update` available.

- [ ] **Step 3: Commit**

```bash
git add .claude/commands/ontology-update.md
git commit -m "feat: add /ontology-update skill command for incremental ontology updates"
```

---

### Task 7: Update CI/CD workflow

**Files:**
- Modify: `.github/workflows/deploy-pages.yml`

- [ ] **Step 1: Update deploy-pages.yml**

Add the build-site.py step before uploading:

```yaml
name: Deploy GitHub Pages

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Pages
        uses: actions/configure-pages@v4

      - name: Build site from lexicon
        run: |
          python scripts/build-site.py || echo "Site build failed, continuing with existing index.html"

      - name: Generate Index
        run: |
          python scripts/generate-index.py || echo "Index generation skipped"

      - name: Copy papers to site
        run: |
          mkdir -p site/papers
          cp -r papers/2026 site/papers/ 2>/dev/null || echo "No 2026 papers"
          cp -r papers/2025 site/papers/ 2>/dev/null || echo "No 2025 papers"
          cp -r papers/2024 site/papers/ 2>/dev/null || echo "No 2024 papers"

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: './site'

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

- [ ] **Step 2: Commit**

```bash
git add .github/workflows/deploy-pages.yml
git commit -m "ci: add build-site.py step to GitHub Pages deployment"
```

---

## Task Dependency Graph

```
Task 1 (lexicon extraction) → Task 2 (ontology_base.md) → Task 3 (changelog)
         ↓
Task 4 (site HTML) → Task 5 (build-site.py) → Task 6 (skill command)
                                          → Task 7 (CI/CD update)
```

Tasks 4-7 can start after Task 1 produces lexicon.json. Task 2 depends on lexicon.json existing. Task 3 is lightweight metadata.

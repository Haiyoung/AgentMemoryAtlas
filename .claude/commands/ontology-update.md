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

按照当前已有的结构（12 节），增量更新内容。保留已有完善的描述，注入新发现。

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
git add ontology/ontology_base.md ontology/lexicon.json ontology/changelogs/CHANGELOG_NNN.md site/index.html
git commit -m "feat: ontology update v<版本号> — <简要描述>"
```

## 版本编号规则

版本号格式: `major.minor.patch`
- major: 结构性重写时增加（如 1.0, 2.0）
- minor: 大量新增概念时增加（如 1.1, 1.2）
- patch: 少量增量更新时增加（如 1.0.1, 1.0.2）

从当前版本的 patch 位 +1 开始。读取 `ontology/lexicon.json` 的 `version` 字段获取当前版本。如果当前没有版本号，从 1.0.1 开始。

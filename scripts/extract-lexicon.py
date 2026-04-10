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
from datetime import date
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

SECTION_TO_CATEGORY = {
    "memory_types": "memory_type",
    "memory_structures": "memory_structure",
    "memory_operations": "memory_operation",
    "memory_carriers": "memory_carrier",
}


def clean_concept_name(name):
    """Normalize concept name for deduplication."""
    name = name.strip()
    base = re.sub(r'\s*\(.*?\)\s*', '', name).strip()
    return base, name


def parse_ontology_analysis_doc(filepath):
    """Parse an ontology_XXXX.md file and extract concepts, relations, axioms."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    arxiv_id = None
    title = None
    concepts = []
    relations = []
    axioms = []

    m = re.search(r'arxiv_id[^\n]*?[：:]\s*(\S+)', content)
    if m:
        arxiv_id = m.group(1).strip()

    m = re.search(r'title[^\n]*?[：:]\s*(.+)', content)
    if m:
        title = m.group(1).strip()

    for section, category in SECTION_TO_CATEGORY.items():
        pattern = rf'\*\*{section}\*\*.*?\[(.*?)\]'
        m = re.search(pattern, content, re.DOTALL)
        if m:
            items_str = m.group(1)
            items = re.findall(r"'([^']+)'", items_str)
            for item in items:
                base, display = clean_concept_name(item)
                concepts.append((base, display, category, arxiv_id))

    for rel_type in ['is_a', 'part_of', 'related_to']:
        pattern = rf'\*\*{rel_type}\*\*.*?\[(.*?)\]'
        m = re.search(pattern, content, re.DOTALL)
        if m:
            items_str = m.group(1)
            dict_matches = re.findall(r"\{'source':\s*'([^']+)',\s*'target':\s*'([^']+)',\s*'description':\s*'([^']*)'\}", items_str)
            for src, tgt, desc in dict_matches:
                relations.append({"from": src, "to": tgt, "type": rel_type, "description": desc})

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

    concept_map = defaultdict(lambda: {
        "display_names": set(),
        "categories": set(),
        "sources": set(),
        "weight": 0,
    })
    all_relations = []
    all_axioms = []

    analysis_files = sorted(glob.glob(str(ontology_dir / "**" / "ontology_*.md"), recursive=True))
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

    base_model_path = ontology_dir / "Agent Memory 本体论领域模型（完整版）.md"
    if base_model_path.exists():
        base_concepts = parse_base_model(str(base_model_path))
        for base, display, category, src in base_concepts:
            entry = concept_map[base]
            entry["display_names"].add(display)
            entry["categories"].add(category)
            entry["weight"] = max(entry["weight"], 1)

    unique_relations = []
    seen_relations = set()
    for r in all_relations:
        key = (r["from"], r["to"], r["type"])
        if key not in seen_relations:
            seen_relations.add(key)
            unique_relations.append(r)

    concepts_list = []
    seen_ids = set()
    for base, data in sorted(concept_map.items(), key=lambda x: -x[1]["weight"]):
        primary_name = max(data["display_names"], key=len)
        concept_id = base.lower().replace(' ', '-').replace('_', '-')
        if concept_id in seen_ids:
            counter = 1
            while f"{concept_id}-{counter}" in seen_ids:
                counter += 1
            concept_id = f"{concept_id}-{counter}"
        seen_ids.add(concept_id)
        concept = {
            "id": concept_id,
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
        "generatedAt": date.today().isoformat(),
        "conceptCount": len(concepts_list),
        "relationCount": len(relations_list),
        "concepts": concepts_list,
        "relations": relations_list,
        "axioms": all_axioms,
        "categories": CATEGORIES,
    }

    output_path = ontology_dir / "lexicon.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(lexicon, f, ensure_ascii=False, indent=2)

    print(f"Generated lexicon.json: {len(concepts_list)} concepts, {len(relations_list)} relations")
    print(f"Top concepts by weight:")
    for c in sorted(concepts_list, key=lambda x: -x["weight"])[:10]:
        print(f"  {c['name']}: weight={c['weight']}, sources={len(c['sourcePapers'])}")


if __name__ == "__main__":
    main()

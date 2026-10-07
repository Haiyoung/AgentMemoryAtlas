#!/usr/bin/env python3
"""
Build script for GitHub Pages site.
Reads lexicon.json / ontology_base.md / timeline.json and paper/ directory,
and rewrites the embedded `var X = ...;` declarations in site/index.html:

- ONTOLOGY_EMBEDDED   whole ontology_base.md as a JS template literal
- LEXICON_EMBEDDED    lexicon.json
- TIMELINE_EMBEDDED   timeline.json (curated milestones)
- PAPER_LIST          papers grouped by year
- PAPER_MAP           arxiv id -> paper path

Each declaration is replaced in place, so running the script twice is a no-op
(idempotent). Used by CI/CD (.github/workflows/deploy-pages.yml) and locally.
"""

import json
import re
import sys
from pathlib import Path


def extract_paper_title(md_path):
    """Extract title from a paper markdown file."""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Try YAML frontmatter first
    m = re.search(r'^---\n.*?title:\s*(.*?)\n', content, re.DOTALL)
    if m:
        return m.group(1).strip().strip('"').strip("'")
    # Fall back to first heading
    m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if m:
        return m.group(1).strip()
    # Fall back to filename
    return md_path.stem


def upsert_js_var(html, name, value_js, multiline):
    """Idempotently replace the `var NAME = ...;` declaration in `html`.

    ``multiline`` selects the JS template-literal form (``var NAME = `...`;``
    whose closing ``;`` sits on its own line) versus the single-line JSON
    object form. Returns ``(html, found)``.
    """
    if multiline:
        pattern = re.compile(r'(?ms)^[ \t]*var ' + re.escape(name) + r" = `[\s\S]*?^`;$")
        repl = 'var ' + name + ' = `' + value_js + '`;'
    else:
        pattern = re.compile(r'(?m)^[ \t]*var ' + re.escape(name) + r' = \{.*\};[ \t]*$')
        repl = '        var ' + name + ' = ' + value_js + ';'
    new_html, count = pattern.subn(lambda _m: repl, html, count=1)
    return new_html, count > 0


def main():
    repo_root = Path(__file__).parent.parent
    lexicon_path = repo_root / "ontology" / "lexicon.json"
    ontology_path = repo_root / "ontology" / "ontology_base.md"
    timeline_path = repo_root / "ontology" / "timeline.json"
    site_path = repo_root / "site" / "index.html"

    if not lexicon_path.exists():
        print("ERROR: ontology/lexicon.json not found. Run extract-lexicon.py first.")
        sys.exit(1)

    with open(lexicon_path, 'r', encoding='utf-8') as f:
        lexicon = json.load(f)

    print(f"Lexicon loaded: {lexicon['conceptCount']} concepts, {lexicon['relationCount']} relations, version {lexicon['version']}")

    # Load ontology markdown for embedding
    ontology_md = ""
    if ontology_path.exists():
        with open(ontology_path, 'r', encoding='utf-8') as f:
            ontology_md = f.read()
        print(f"Ontology loaded: {len(ontology_md)} chars")

    # Load curated timeline milestones (optional)
    timeline_json = None
    if timeline_path.exists():
        with open(timeline_path, 'r', encoding='utf-8') as f:
            timeline = json.load(f)
        timeline_json = json.dumps(timeline, ensure_ascii=False)
        print(f"Timeline loaded: {len(timeline.get('years', []))} year nodes")
    else:
        print("WARN: ontology/timeline.json not found; TIMELINE_EMBEDDED left as-is.")

    if not site_path.exists():
        print("ERROR: site/index.html not found.")
        sys.exit(1)

    with open(site_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # ── Build arxiv -> paper path mapping and per-year paper list ──
    paper_dir = repo_root / "paper"
    paper_files = sorted(paper_dir.rglob("*.md"))

    arxiv_to_path = {}
    paper_list = []
    for pf in paper_files:
        arxiv_id = pf.stem.split('_')[0]
        rel_path = "paper/" + "/".join(pf.relative_to(paper_dir).parts)
        arxiv_to_path[arxiv_id] = rel_path
        year = pf.relative_to(paper_dir).parts[0]
        paper_list.append({
            "arxivId": arxiv_id,
            "title": extract_paper_title(pf),
            "path": rel_path,
            "year": year,
        })

    print(f"Found {len(arxiv_to_path)} papers in paper/ directory")

    paper_by_year = {}
    for p in paper_list:
        paper_by_year.setdefault(p["year"], []).append(p)
    # Sort years descending
    paper_by_year = dict(sorted(paper_by_year.items(), reverse=True))

    # ── Inject into HTML (each declaration replaced in place) ──
    safe_ontology_md = ontology_md.replace('\\', '\\\\').replace('`', '\\`').replace('$', '\\$')
    # Keep the closing backtick+semicolon on its own line so the declaration
    # matches the pattern again on the next (idempotent) run.
    if not safe_ontology_md.endswith('\n'):
        safe_ontology_md += '\n'

    updates = [
        ("ONTOLOGY_EMBEDDED", safe_ontology_md, True),
        ("LEXICON_EMBEDDED", json.dumps(lexicon, ensure_ascii=False), False),
        ("PAPER_LIST", json.dumps(paper_by_year, ensure_ascii=False), False),
        ("PAPER_MAP", json.dumps(arxiv_to_path, ensure_ascii=False), False),
    ]
    if timeline_json is not None:
        updates.insert(2, ("TIMELINE_EMBEDDED", timeline_json, False))

    for name, value, multiline in updates:
        html, found = upsert_js_var(html, name, value, multiline)
        if found:
            print(f"Updated {name} in site/index.html")
        else:
            print(f"ERROR: `var {name} = ...;` declaration not found in site/index.html")
            sys.exit(1)

    with open(site_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print("Build complete.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Build script for GitHub Pages site.
Reads lexicon.json and paper/ directory, updates site/index.html with:
- paper path mapping (PAPER_MAP)
- paper browsing list (PAPER_LIST)
- ontology body

Used by CI/CD (.github/workflows/deploy-pages.yml) and local development.
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

    with open(site_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # ── Build arxiv -> paper path mapping ──
    paper_dir = repo_root / "paper"
    paper_files = sorted(paper_dir.rglob("*.md"))

    arxiv_to_path = {}
    paper_list = []
    for pf in paper_files:
        fname = pf.stem
        arxiv_id = fname.split('_')[0]
        rel_path = "paper/" + "/".join(pf.relative_to(paper_dir).parts)
        arxiv_to_path[arxiv_id] = rel_path
        # Determine year from path
        year = pf.relative_to(paper_dir).parts[0]
        title = extract_paper_title(pf)
        paper_list.append({
            "arxivId": arxiv_id,
            "title": title,
            "path": rel_path,
            "year": year,
        })

    print(f"Found {len(arxiv_to_path)} papers in paper/ directory")

    # ── Build paper list grouped by year ──
    paper_by_year = {}
    for p in paper_list:
        paper_by_year.setdefault(p["year"], []).append(p)
    # Sort years descending
    paper_by_year = dict(sorted(paper_by_year.items(), reverse=True))

    paper_list_json = json.dumps(paper_by_year, ensure_ascii=False)

    # ── Inject into HTML ──
    mapping_json = json.dumps(arxiv_to_path, ensure_ascii=False)

    # 1. Inject or update PAPER_MAP const
    inject_const = f"        var PAPER_MAP = {mapping_json};"
    if "var PAPER_MAP = " in html:
        html = re.sub(
            r'var PAPER_MAP = \{[^;]+\};',
            inject_const,
            html,
            count=1
        )
        print("Updated PAPER_MAP in site/index.html")
    else:
        html = html.replace(
            "var GITHUB_PAGES_BASE = 'https://haiyoung.github.io/AgentMemoryAtlas/';",
            "var GITHUB_PAGES_BASE = 'https://haiyoung.github.io/AgentMemoryAtlas/';\n" + inject_const
        )
        print("Injected PAPER_MAP const into site/index.html")

    # 2. Inject or update PAPER_LIST const
    inject_papers = f"        var PAPER_LIST = {paper_list_json};"
    if "var PAPER_LIST = " in html:
        html = re.sub(
            r'var PAPER_LIST = \{[^;]+\};',
            inject_papers,
            html,
            count=1
        )
        print("Updated PAPER_LIST in site/index.html")
    else:
        html = html.replace(
            "var GITHUB_PAGES_BASE = 'https://haiyoung.github.io/AgentMemoryAtlas/';",
            "var GITHUB_PAGES_BASE = 'https://haiyoung.github.io/AgentMemoryAtlas/';\n" + inject_papers
        )
        print("Injected PAPER_LIST into site/index.html")

    # 3. Replace search-based fallback with actual mapping lookup
    old_link = "'paper/search/' + arxivId"
    new_link = "(PAPER_MAP[arxivId] || 'paper/search/' + arxivId)"

    if old_link in html and "PAPER_MAP[arxivId] || 'paper/search/'" not in html:
        html = html.replace(old_link, new_link)
        print("Updated paper links to use PAPER_MAP lookup")
    elif "PAPER_MAP[arxivId] || 'paper/search/'" in html:
        print("Paper links already use PAPER_MAP lookup, skipping")
    else:
        print("WARNING: Could not find placeholder paper link pattern in site/index.html")

    # 4. Inject paper browsing section after the ontology-body div, before footer
    if 'class="papers-section"' not in html:
        papers_section = '''
        <section class="papers-section">
            <h2 class="section-title">
                <span class="section-icon">&#128218;</span> 论文阅读简报
            </h2>
            <div id="paper-list-container"></div>
        </section>
'''
        html = html.replace('</footer>', papers_section + '\n    </footer>')
        print("Injected paper browsing section into site/index.html")

    with open(site_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print("Build complete.")


if __name__ == "__main__":
    main()

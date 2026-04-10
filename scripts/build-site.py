#!/usr/bin/env python3
"""
Build script for GitHub Pages site.
Reads lexicon.json and updates site/index.html with paper path mapping.

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

    with open(site_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Build arxiv -> paper path mapping from the paper/ directory
    paper_dir = repo_root / "paper"
    paper_files = sorted(paper_dir.rglob("*.md"))

    arxiv_to_path = {}
    for pf in paper_files:
        fname = pf.stem
        arxiv_id = fname.split('_')[0]
        # Path relative to repo root, for GitHub Pages
        rel_path = "paper/" + "/".join(pf.relative_to(paper_dir).parts)
        arxiv_to_path[arxiv_id] = rel_path

    print(f"Found {len(arxiv_to_path)} papers in paper/ directory")

    # Inject the paper mapping as a const near the top of the IIFE,
    # and replace the placeholder link with a lookup.
    mapping_json = json.dumps(arxiv_to_path, ensure_ascii=False)

    # 1. Inject paper mapping const after GITHUB_PAGES_BASE
    inject_const = f"        const PAPER_MAP = {mapping_json};"
    if "const PAPER_MAP = " in html:
        print("site/index.html already has PAPER_MAP, skipping injection")
    else:
        html = html.replace(
            "const GITHUB_PAGES_BASE = 'https://haiyoung.github.io/AgentMemoryAtlas/';",
            "const GITHUB_PAGES_BASE = 'https://haiyoung.github.io/AgentMemoryAtlas/';\n" + inject_const
        )
        print("Injected PAPER_MAP const into site/index.html")

    # 2. Replace the search-based fallback with actual mapping lookup
    old_link = "'paper/search/' + arxivId"
    new_link = "(PAPER_MAP[arxivId] || 'paper/search/' + arxivId)"

    if old_link in html:
        html = html.replace(old_link, new_link)
        print("Updated paper links to use PAPER_MAP lookup")
    else:
        print("WARNING: Could not find placeholder paper link pattern in site/index.html")

    with open(site_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print("Build complete.")


if __name__ == "__main__":
    main()

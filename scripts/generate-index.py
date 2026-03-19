#!/usr/bin/env python3
"""
Generate paper index and statistics for AgentMemoryAtlas.

This script scans the papers/ directory and generates:
- site/papers.json: Paper metadata index
- stats/paper-stats.json: Aggregate statistics
"""

import json
import os
from pathlib import Path
from datetime import datetime

def scan_papers(papers_dir: str) -> list:
    """Scan papers directory and collect metadata."""
    papers = []
    
    for year in sorted(os.listdir(papers_dir), reverse=True):
        year_path = Path(papers_dir) / year
        if not year_path.is_dir():
            continue
            
        for paper_dir in os.listdir(year_path):
            paper_path = year_path / paper_dir
            if not paper_path.is_dir():
                continue
            
            # Look for ontology mapping
            ontology_file = paper_path / 'ontology-mapping.json'
            if ontology_file.exists():
                with open(ontology_file, 'r') as f:
                    ontology = json.load(f)
            else:
                ontology = {}
            
            papers.append({
                'id': paper_dir,
                'year': year,
                'path': str(paper_path),
                'ontology': ontology.get('ontology', {}),
            })
    
    return papers

def generate_statistics(papers: list) -> dict:
    """Generate aggregate statistics."""
    stats = {
        'total_papers': len(papers),
        'by_year': {},
        'ontology_stats': {
            'memory_types': {},
            'memory_structures': {},
            'patterns': {},
        }
    }
    
    for paper in papers:
        # Count by year
        year = paper['year']
        stats['by_year'][year] = stats['by_year'].get(year, 0) + 1
        
        # Count ontology concepts
        ontology = paper.get('ontology', {})
        
        for mem_type in ontology.get('memory_type', []):
            stats['ontology_stats']['memory_types'][mem_type] = \
                stats['ontology_stats']['memory_types'].get(mem_type, 0) + 1
        
        for struct in ontology.get('memory_structure', []):
            stats['ontology_stats']['memory_structures'][struct] = \
                stats['ontology_stats']['memory_structures'].get(struct, 0) + 1
        
        for pattern in ontology.get('patterns', []):
            stats['ontology_stats']['patterns'][pattern] = \
                stats['ontology_stats']['patterns'].get(pattern, 0) + 1
    
    stats['generated_at'] = datetime.utcnow().isoformat() + 'Z'
    return stats

def main():
    repo_root = Path(__file__).parent.parent
    papers_dir = repo_root / 'papers'
    site_dir = repo_root / 'site'
    stats_dir = repo_root / 'stats'
    
    # Ensure directories exist
    site_dir.mkdir(exist_ok=True)
    stats_dir.mkdir(exist_ok=True)
    
    # Scan papers
    print(f"Scanning papers in {papers_dir}...")
    papers = scan_papers(str(papers_dir))
    print(f"Found {len(papers)} papers")
    
    # Generate papers index
    papers_index = site_dir / 'papers.json'
    with open(papers_index, 'w') as f:
        json.dump(papers, f, indent=2)
    print(f"Generated {papers_index}")
    
    # Generate statistics
    stats = generate_statistics(papers)
    stats_file = stats_dir / 'paper-stats.json'
    with open(stats_file, 'w') as f:
        json.dump(stats, f, indent=2)
    print(f"Generated {stats_file}")
    
    print("Done!")

if __name__ == '__main__':
    main()

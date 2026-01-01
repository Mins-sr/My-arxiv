#!/usr/bin/env python3
"""
Convert arXiv digest markdown files to JSON for web display
Generates indexed JSON structure for improved performance
"""

import json
import re
from pathlib import Path
from datetime import datetime


def parse_digest_markdown(md_file):
    """Parse a digest markdown file and extract paper information"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract metadata
    date_match = re.search(r'# arXiv Daily Digest - ([\d-]+)', content)
    total_match = re.search(r'Total papers: (\d+)', content)

    date = date_match.group(1) if date_match else ""
    total_papers = int(total_match.group(1)) if total_match else 0

    # Split by category sections
    category_sections = re.split(r'\n## ([\w.]+)\n', content)[1:]

    papers_by_category = {}

    for i in range(0, len(category_sections), 2):
        if i + 1 >= len(category_sections):
            break

        category = category_sections[i]
        section_content = category_sections[i + 1]

        # Extract papers from this section
        paper_blocks = re.split(r'\n### \d+\. ', section_content)[1:]

        papers = []
        for block in paper_blocks:
            # Extract paper details
            lines = block.split('\n')
            title = lines[0] if lines else ""

            authors_match = re.search(r'\*\*Authors:\*\* (.+)', block)
            published_match = re.search(r'\*\*Published:\*\* ([\d-]+)', block)
            paper_link_match = re.search(r'🔗 \[Paper\]\(([^)]+)\)', block)
            pdf_link_match = re.search(r'📄 \[PDF\]\(([^)]+)\)', block)
            summary_match = re.search(r'\*\*Summary:\*\* (.+?)(?:\n\n---|\Z)', block, re.DOTALL)

            paper = {
                'title': title.strip(),
                'authors': authors_match.group(1).strip() if authors_match else "",
                'published': published_match.group(1) if published_match else "",
                'link': paper_link_match.group(1) if paper_link_match else "",
                'pdf_link': pdf_link_match.group(1) if pdf_link_match else "",
                'summary': summary_match.group(1).strip() if summary_match else "",
                'category': category
            }
            papers.append(paper)

        papers_by_category[category] = papers

    return {
        'date': date,
        'total_papers': total_papers,
        'categories': papers_by_category
    }


def generate_indexed_json(digests_dir='digests', output_dir='pages'):
    """Generate indexed JSON structure for improved performance"""
    digests_path = Path(digests_dir)
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    # Create digests subdirectory for individual date files
    digests_json_dir = output_path / 'digests'
    digests_json_dir.mkdir(exist_ok=True)

    # Find all digest markdown files
    digest_files = sorted(digests_path.glob('arxiv_digest_*.md'), reverse=True)

    if not digest_files:
        print("No digest files found")
        return

    index_data = []
    all_categories = set()

    for digest_file in digest_files:
        print(f"Processing {digest_file.name}")
        try:
            digest_data = parse_digest_markdown(digest_file)

            # Collect categories
            categories = list(digest_data['categories'].keys())
            all_categories.update(categories)

            # Create index entry with metadata only
            index_entry = {
                'date': digest_data['date'],
                'total_papers': digest_data['total_papers'],
                'categories': categories,
                'category_counts': {
                    cat: len(papers)
                    for cat, papers in digest_data['categories'].items()
                }
            }
            index_data.append(index_entry)

            # Save individual date file
            date_file = digests_json_dir / f"{digest_data['date']}.json"
            with open(date_file, 'w', encoding='utf-8') as f:
                json.dump(digest_data, f, ensure_ascii=False, indent=2)
            print(f"  → Created {date_file.name}")

        except Exception as e:
            print(f"Error processing {digest_file.name}: {e}")

    # Save index file
    index_file = output_path / 'digests_index.json'
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump({
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'total_digests': len(index_data),
            'all_categories': sorted(list(all_categories)),
            'digests': index_data
        }, f, ensure_ascii=False, indent=2)

    print(f"\n✓ Generated index file: {index_file}")
    print(f"  - {len(index_data)} digests")
    print(f"  - {len(all_categories)} unique categories")
    print(f"  - Total papers: {sum(d['total_papers'] for d in index_data)}")


def generate_legacy_json(digests_dir='digests', output_dir='pages'):
    """Generate legacy monolithic JSON file for backwards compatibility"""
    digests_path = Path(digests_dir)
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    # Find all digest markdown files
    digest_files = sorted(digests_path.glob('arxiv_digest_*.md'), reverse=True)

    if not digest_files:
        print("No digest files found")
        return

    all_digests = []

    for digest_file in digest_files:
        try:
            digest_data = parse_digest_markdown(digest_file)
            all_digests.append(digest_data)
        except Exception as e:
            print(f"Error processing {digest_file.name}: {e}")

    # Save to JSON
    output_file = output_path / 'digests.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_digests, f, ensure_ascii=False, indent=2)

    print(f"✓ Generated legacy file: {output_file} ({len(all_digests)} digests)")


def main():
    """Main function"""
    print("=" * 60)
    print("arXiv Digest JSON Generator")
    print("=" * 60)
    print()

    # Generate indexed JSON structure (new format)
    print("Generating indexed JSON structure...")
    print("-" * 60)
    generate_indexed_json()

    print()
    print("-" * 60)
    print("Generating legacy JSON (backwards compatibility)...")
    print("-" * 60)
    generate_legacy_json()

    print()
    print("=" * 60)
    print("✓ All JSON files generated successfully")
    print("=" * 60)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Convert arXiv digest markdown files to JSON for web display
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


def generate_json_data(digests_dir='digests', output_dir='pages'):
    """Generate JSON data from all digest markdown files"""
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
        print(f"Processing {digest_file.name}")
        try:
            digest_data = parse_digest_markdown(digest_file)
            all_digests.append(digest_data)
        except Exception as e:
            print(f"Error processing {digest_file.name}: {e}")

    # Save to JSON
    output_file = output_path / 'digests.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_digests, f, ensure_ascii=False, indent=2)

    print(f"\nGenerated {output_file} with {len(all_digests)} digests")
    print(f"Total papers across all digests: {sum(d['total_papers'] for d in all_digests)}")


def main():
    """Main function"""
    generate_json_data()


if __name__ == '__main__':
    main()

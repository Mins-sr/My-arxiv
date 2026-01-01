#!/usr/bin/env python3
"""
arXiv Daily Digest
Fetches new papers from arXiv based on specified categories and generates a daily digest.
"""

import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from pathlib import Path
import json
import time


class ArxivFetcher:
    """Fetches papers from arXiv API"""

    BASE_URL = 'https://export.arxiv.org/api/query?'

    def __init__(self, config_path='config.json'):
        """Initialize with configuration"""
        self.config = self._load_config(config_path)
        self.papers = []

    def _load_config(self, config_path):
        """Load configuration from JSON file"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Configuration file {config_path} not found. Using defaults.")
            return {
                'categories': ['cs.AI', 'cs.LG', 'cs.CL'],
                'max_results': 50,
                'lookback_days': 1
            }

    def fetch_papers(self, category, max_results=50):
        """Fetch papers from a specific arXiv category"""
        # Calculate date range
        end_date = datetime.now()
        start_date = end_date - timedelta(days=self.config.get('lookback_days', 1))

        # Build query
        query = f'cat:{category}'
        params = {
            'search_query': query,
            'start': 0,
            'max_results': max_results,
            'sortBy': 'submittedDate',
            'sortOrder': 'descending'
        }

        url = self.BASE_URL + urllib.parse.urlencode(params)

        try:
            print(f"Fetching papers from category: {category}")
            # Add proper headers to avoid 403 errors
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (arXiv Daily Digest Bot)')

            with urllib.request.urlopen(req) as response:
                data = response.read()

            # Parse XML
            root = ET.fromstring(data)
            namespace = {'atom': 'http://www.w3.org/2005/Atom',
                        'arxiv': 'http://arxiv.org/schemas/atom'}

            papers = []
            for entry in root.findall('atom:entry', namespace):
                # Extract paper information
                published_str = entry.find('atom:published', namespace).text
                published_date = datetime.strptime(published_str, '%Y-%m-%dT%H:%M:%SZ')

                # Only include recent papers
                if published_date >= start_date:
                    paper = {
                        'title': entry.find('atom:title', namespace).text.strip().replace('\n', ' '),
                        'authors': [author.find('atom:name', namespace).text
                                  for author in entry.findall('atom:author', namespace)],
                        'summary': entry.find('atom:summary', namespace).text.strip().replace('\n', ' '),
                        'link': entry.find('atom:id', namespace).text,
                        'pdf_link': None,
                        'published': published_date.strftime('%Y-%m-%d'),
                        'category': category
                    }

                    # Get PDF link
                    for link in entry.findall('atom:link', namespace):
                        if link.get('title') == 'pdf':
                            paper['pdf_link'] = link.get('href')
                            break

                    papers.append(paper)

            print(f"Found {len(papers)} recent papers in {category}")
            return papers

        except Exception as e:
            print(f"Error fetching papers from {category}: {e}")
            return []

    def fetch_all_categories(self):
        """Fetch papers from all configured categories"""
        all_papers = []
        categories = self.config.get('categories', [])
        max_results = self.config.get('max_results', 50)

        for category in categories:
            papers = self.fetch_papers(category, max_results)
            all_papers.extend(papers)
            time.sleep(3)  # Be nice to the API

        self.papers = all_papers
        return all_papers

    def generate_digest(self, output_dir='digests'):
        """Generate markdown digest of papers"""
        if not self.papers:
            print("No papers to generate digest from")
            return

        # Create output directory
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)

        # Generate filename with date
        date_str = datetime.now().strftime('%Y-%m-%d')
        filename = output_path / f'arxiv_digest_{date_str}.md'

        # Group papers by category
        papers_by_category = {}
        for paper in self.papers:
            category = paper['category']
            if category not in papers_by_category:
                papers_by_category[category] = []
            papers_by_category[category].append(paper)

        # Generate markdown
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# arXiv Daily Digest - {date_str}\n\n")
            f.write(f"Total papers: {len(self.papers)}\n\n")
            f.write("---\n\n")

            for category in sorted(papers_by_category.keys()):
                papers = papers_by_category[category]
                f.write(f"## {category}\n\n")
                f.write(f"**{len(papers)} papers**\n\n")

                for i, paper in enumerate(papers, 1):
                    f.write(f"### {i}. {paper['title']}\n\n")

                    # Authors
                    if len(paper['authors']) > 3:
                        authors = ', '.join(paper['authors'][:3]) + ', et al.'
                    else:
                        authors = ', '.join(paper['authors'])
                    f.write(f"**Authors:** {authors}\n\n")

                    # Links
                    f.write(f"**Published:** {paper['published']}\n\n")
                    f.write(f"🔗 [Paper]({paper['link']})")
                    if paper['pdf_link']:
                        f.write(f" | 📄 [PDF]({paper['pdf_link']})")
                    f.write("\n\n")

                    # Summary
                    summary = paper['summary']
                    if len(summary) > 500:
                        summary = summary[:500] + "..."
                    f.write(f"**Summary:** {summary}\n\n")
                    f.write("---\n\n")

        print(f"Digest generated: {filename}")
        return filename


def main():
    """Main function"""
    fetcher = ArxivFetcher()

    # Fetch papers
    papers = fetcher.fetch_all_categories()

    if papers:
        # Generate digest
        digest_file = fetcher.generate_digest()
        print(f"\n✓ Successfully generated digest with {len(papers)} papers")

        # Generate JSON for web UI
        try:
            import subprocess
            print("\nGenerating JSON for web UI...")
            result = subprocess.run(['python3', 'generate_json.py'],
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print("✓ JSON generated successfully")
            else:
                print(f"⚠ JSON generation failed: {result.stderr}")
        except Exception as e:
            print(f"⚠ Could not generate JSON: {e}")
    else:
        print("\n✗ No papers found")


if __name__ == '__main__':
    main()

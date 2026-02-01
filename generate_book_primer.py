#!/usr/bin/env python3
"""
Daily Book Primer Generator
Generates a chronologically sorted summary page of book primers
"""

import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict
import sys


def load_books_data(file_path: str = "books-data.json") -> Dict:
    """Load book data from JSON file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {file_path} not found!", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)


def sort_books_chronologically(books: List[Dict]) -> List[Dict]:
    """Sort books by publication date (oldest first)"""
    return sorted(books, key=lambda x: datetime.fromisoformat(x['date']))


def format_date(date_str: str) -> str:
    """Format date string to human-readable format"""
    date = datetime.fromisoformat(date_str)
    return date.strftime("%B %d, %Y")


def format_authors(authors: List[str]) -> str:
    """Format author list into a readable string"""
    if len(authors) == 1:
        return authors[0]
    elif len(authors) == 2:
        return f"{authors[0]} and {authors[1]}"
    else:
        return ", ".join(authors[:-1]) + f", and {authors[-1]}"


def generate_summary_markdown(books: List[Dict]) -> str:
    """Generate markdown summary page"""
    now = datetime.now()

    markdown = f"""# Book Primer Summary

*Last updated: {now.strftime("%B %d, %Y at %H:%M UTC")}*

This page contains a chronologically sorted list of essential books, automatically updated daily.

---

## Books in Chronological Order

"""

    # Group by decade
    decades = {}
    for book in books:
        year = datetime.fromisoformat(book['date']).year
        decade = (year // 10) * 10
        if decade not in decades:
            decades[decade] = []
        decades[decade].append(book)

    # Generate content by decade
    for decade in sorted(decades.keys()):
        markdown += f"\n### {decade}s\n\n"
        for book in decades[decade]:
            date = datetime.fromisoformat(book['date'])
            year = date.year

            markdown += f"#### [{book['title']}]({book['link']}) ({year})\n\n"
            markdown += f"**Authors:** {format_authors(book['authors'])}  \n"
            markdown += f"**Category:** {book['category']}  \n"
            markdown += f"**Published:** {format_date(book['date'])}  \n\n"
            markdown += f"{book['description']}\n\n"
            markdown += "---\n\n"

    # Add statistics
    markdown += "\n## Statistics\n\n"
    markdown += f"- **Total Books:** {len(books)}\n"

    # Count by category
    categories = {}
    for book in books:
        cat = book['category']
        categories[cat] = categories.get(cat, 0) + 1

    markdown += "- **By Category:**\n"
    for category, count in sorted(categories.items()):
        markdown += f"  - {category}: {count}\n"

    # Date range
    if books:
        oldest = books[0]['date']
        newest = books[-1]['date']
        markdown += f"- **Date Range:** {format_date(oldest)} to {format_date(newest)}\n"

    markdown += "\n---\n\n"
    markdown += "*This summary is automatically generated daily by the Book Primer Generator.*\n"

    return markdown


def generate_task_checklist() -> str:
    """Generate daily task checklist"""
    today = datetime.now().strftime("%Y-%m-%d")

    checklist = f"""# Daily Book Primer Task - {today}

## Today's Tasks

- [ ] Review the chronologically sorted book list
- [ ] Add any new books to `books-data.json`
- [ ] Verify all publication dates are accurate
- [ ] Check that all links are working
- [ ] Update book descriptions if needed
- [ ] Review categorization
- [ ] Commit any changes

## Quick Commands

To add a new book, edit `books-data.json` and add an entry like:

```json
{{
  "title": "Book Title",
  "authors": ["Author Name"],
  "date": "YYYY-MM-DD",
  "category": "Category Name",
  "description": "Brief description",
  "link": "https://book-url.com"
}}
```

Then run:
```bash
python3 generate_book_primer.py
```

---

*Generated: {datetime.now().strftime("%B %d, %Y at %H:%M UTC")}*
"""

    return checklist


def main():
    """Main function to generate book primer summary"""
    print("📚 Book Primer Generator Starting...")

    # Load data
    print("Loading books data...")
    data = load_books_data()
    books = data.get('books', [])

    if not books:
        print("Warning: No books found in data file!", file=sys.stderr)
        return

    print(f"Loaded {len(books)} books")

    # Sort chronologically
    print("Sorting books chronologically...")
    sorted_books = sort_books_chronologically(books)

    # Generate summary
    print("Generating summary markdown...")
    summary = generate_summary_markdown(sorted_books)

    # Write summary file
    output_file = "BOOK_PRIMER_SUMMARY.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(summary)
    print(f"✅ Summary written to {output_file}")

    # Generate daily task
    print("Generating daily task checklist...")
    task = generate_task_checklist()

    task_file = "DAILY_BOOK_TASK.md"
    with open(task_file, 'w', encoding='utf-8') as f:
        f.write(task)
    print(f"✅ Daily task written to {task_file}")

    print("\n🎉 Book Primer Generation Complete!")
    print(f"\nFiles generated:")
    print(f"  - {output_file} - Chronologically sorted summary")
    print(f"  - {task_file} - Today's task checklist")


if __name__ == "__main__":
    main()

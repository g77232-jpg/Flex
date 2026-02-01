# 📚 Daily Book Primer System

An automated system that generates daily tasks for organizing book primers in chronological order on a single summary page.

## 🎯 What This Does

This system:
- ✅ Maintains a structured database of books with publication dates
- ✅ Automatically sorts books chronologically
- ✅ Generates a beautiful summary page organized by decade
- ✅ Creates daily task checklists to help you maintain the list
- ✅ Runs automatically every day via GitHub Actions
- ✅ Updates automatically when you add new books

## 📁 Files Overview

| File | Purpose |
|------|---------|
| `books-data.json` | Source data for all books (you edit this) |
| `generate_book_primer.py` | Python script that generates the outputs |
| `BOOK_PRIMER_SUMMARY.md` | Auto-generated chronological summary ⭐ |
| `DAILY_BOOK_TASK.md` | Auto-generated daily task checklist ⭐ |
| `.github/workflows/daily-book-primer.yml` | GitHub Actions workflow for automation |

## 🚀 Quick Start

### 1. Add a New Book

Edit `books-data.json` and add your book:

```json
{
  "title": "Your Book Title",
  "authors": ["Author Name"],
  "date": "YYYY-MM-DD",
  "category": "Category Name",
  "description": "Brief description of the book",
  "link": "https://link-to-book.com"
}
```

### 2. Generate the Summary

Run locally:
```bash
python3 generate_book_primer.py
```

Or just commit your changes - GitHub Actions will run automatically!

### 3. Check Your Daily Task

Open `DAILY_BOOK_TASK.md` to see today's checklist.

## 📊 Features

### Chronological Organization
Books are automatically sorted by publication date and grouped by decade for easy browsing.

### Statistics
The summary page includes:
- Total book count
- Books by category
- Date range coverage

### Daily Tasks
Every day, a fresh task checklist is generated with:
- Review reminders
- Verification steps
- Quick reference commands

## 🔄 Automation

### GitHub Actions
The workflow runs:
- **Daily at 9:00 AM UTC** (scheduled)
- **When you push changes** to `books-data.json` or `generate_book_primer.py`
- **Manually** via workflow dispatch

### What Happens Automatically
1. Python script runs
2. Summary and task files are generated
3. If changes detected, files are committed and pushed
4. You get an updated summary!

## 🛠️ Manual Usage

### Run the Script
```bash
python3 generate_book_primer.py
```

### View the Summary
```bash
cat BOOK_PRIMER_SUMMARY.md
```

### Check Today's Task
```bash
cat DAILY_BOOK_TASK.md
```

## 📝 Data Structure

Each book entry in `books-data.json` requires:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `title` | string | Book title | "Clean Code" |
| `authors` | array | List of authors | ["Robert C. Martin"] |
| `date` | string | Publication date (ISO 8601) | "2008-08-01" |
| `category` | string | Book category | "Software Engineering" |
| `description` | string | Brief description | "A Handbook of Agile Software Craftsmanship" |
| `link` | string | URL to book | "https://..." |

## 🎨 Customization

### Change the Schedule
Edit `.github/workflows/daily-book-primer.yml`:

```yaml
schedule:
  - cron: '0 9 * * *'  # Change this line
```

Cron format: `minute hour day month weekday`

Examples:
- `0 9 * * *` - Daily at 9 AM UTC
- `0 12 * * 1` - Every Monday at noon UTC
- `0 0 1 * *` - First day of each month at midnight UTC

### Modify the Output Format
Edit `generate_book_primer.py` and customize the `generate_summary_markdown()` function.

### Add New Categories
Just add books with new category names - they'll automatically appear in the statistics!

## 🔍 Example Output

### Summary Page
```markdown
# Book Primer Summary

*Last updated: December 26, 2025 at 09:00 UTC*

## Books in Chronological Order

### 1970s

#### [The Mythical Man-Month](https://...) (1975)
**Authors:** Frederick P. Brooks Jr.
**Category:** Project Management
**Published:** January 01, 1975

Essays on Software Engineering
```

### Daily Task
```markdown
# Daily Book Primer Task - 2025-12-26

## Today's Tasks
- [ ] Review the chronologically sorted book list
- [ ] Add any new books to `books-data.json`
- [ ] Verify all publication dates are accurate
...
```

## 🤝 Contributing

1. Add your books to `books-data.json`
2. Run the script to test locally
3. Commit and push
4. GitHub Actions handles the rest!

## 📌 Tips

- **Use ISO 8601 date format**: `YYYY-MM-DD` for accurate sorting
- **Keep descriptions concise**: One sentence is usually enough
- **Verify links**: Make sure book URLs are working
- **Categorize thoughtfully**: Consistent categories help with organization
- **Check the daily task**: It's your daily reminder to maintain the list!

## 🐛 Troubleshooting

### Script fails to run
- Check Python 3 is installed: `python3 --version`
- Verify `books-data.json` is valid JSON
- Look for syntax errors in the data file

### GitHub Actions not running
- Check the workflow file permissions
- Ensure the workflow file is in `.github/workflows/`
- Check repository settings → Actions → General

### Changes not being committed
- Verify the bot has write permissions
- Check if there are actually changes to commit
- Look at the GitHub Actions logs

## 📚 What's Next?

Ideas for expansion:
- Add reading status (to-read, reading, completed)
- Include ratings or reviews
- Add tags for better organization
- Generate reading statistics
- Create a web page version
- Add search functionality

## 📄 License

This is part of the Awesome repository. Use and modify as needed!

---

*Happy reading! 📖✨*

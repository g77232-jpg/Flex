#!/usr/bin/env python3
"""
Poimea Project Daily Task Generator
Generates daily tasks and tracks progress for the Poimea book and animation project
"""

import json
from datetime import datetime, date, timedelta
from pathlib import Path
from typing import Dict, List, Tuple
import sys


def load_project_data(file_path: str = "poimea-project.json") -> Dict:
    """Load Poimea project data from JSON file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {file_path} not found!", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)


def save_project_data(data: Dict, file_path: str = "poimea-project.json"):
    """Save updated project data"""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def calculate_days_remaining(target_date_str: str) -> int:
    """Calculate days remaining until target date"""
    target = datetime.fromisoformat(target_date_str).date()
    today = date.today()
    return (target - today).days


def calculate_daily_targets(project: Dict) -> Dict:
    """Calculate daily targets based on remaining time"""
    days_to_storyboard = calculate_days_remaining(project['deadlines']['storyboard_complete'])
    days_to_draft = calculate_days_remaining(project['deadlines']['book1_rough_draft'])

    # Account for rest days (assuming 6 days/week work schedule)
    working_days_storyboard = int(days_to_storyboard * 6/7)
    working_days_draft = int(days_to_draft * 6/7)

    book1 = project['phases']['book1']
    storyboard = project['storyboard']

    words_remaining = book1['target_word_count'] - book1['current_word_count']
    scenes_remaining = storyboard['total_scenes'] - storyboard['scenes_completed']

    daily_words = words_remaining / max(working_days_draft, 1)
    daily_scenes = scenes_remaining / max(working_days_storyboard, 1)

    return {
        'daily_words': int(daily_words),
        'daily_scenes': round(daily_scenes, 2),
        'days_to_storyboard': days_to_storyboard,
        'days_to_draft': days_to_draft,
        'working_days_storyboard': working_days_storyboard,
        'working_days_draft': working_days_draft,
        'words_remaining': words_remaining,
        'scenes_remaining': scenes_remaining
    }


def get_week_progress(project: Dict) -> Tuple[int, int]:
    """Calculate week number and progress percentage"""
    start_date = datetime.fromisoformat(project['project']['created_date']).date()
    today = date.today()
    days_elapsed = (today - start_date).days
    week_number = (days_elapsed // 7) + 1

    days_to_final = calculate_days_remaining(project['deadlines']['book1_rough_draft'])
    total_days = 121  # Dec 26 to Apr 26
    progress_pct = int(((total_days - days_to_final) / total_days) * 100)

    return week_number, progress_pct


def get_upcoming_milestones(project: Dict, limit: int = 3) -> List[Dict]:
    """Get upcoming incomplete milestones"""
    today = date.today()
    milestones = project['milestones']

    upcoming = []
    for milestone in milestones:
        if not milestone['completed']:
            target = datetime.fromisoformat(milestone['target_date']).date()
            days_until = (target - today).days
            milestone['days_until'] = days_until
            upcoming.append(milestone)

    # Sort by date
    upcoming.sort(key=lambda x: x['days_until'])
    return upcoming[:limit]


def get_current_chapter(project: Dict) -> Dict:
    """Get the current chapter being worked on"""
    for chapter in project['chapters']:
        if chapter['status'] != 'completed':
            return chapter
    return project['chapters'][0] if project['chapters'] else None


def generate_daily_tasks(project: Dict, targets: Dict) -> str:
    """Generate daily task markdown"""
    today = date.today()
    day_name = today.strftime("%A")

    # Check if it's a rest day
    is_rest_day = day_name in project['daily_goals'].get('rest_days', ['Sunday'])

    week_num, progress_pct = get_week_progress(project)
    current_chapter = get_current_chapter(project)
    upcoming_milestones = get_upcoming_milestones(project)

    # Build the markdown
    md = f"""# 📖 Poimea Daily Task - {today.strftime('%B %d, %Y')} ({day_name})

## 🎯 Project Overview

**Week {week_num}** | Overall Progress: **{progress_pct}%**

| Metric | Current | Target | Remaining |
|--------|---------|--------|-----------|
| **Book 1 Words** | {project['phases']['book1']['current_word_count']:,} | {project['phases']['book1']['target_word_count']:,} | {targets['words_remaining']:,} |
| **Chapters** | {project['phases']['book1']['chapters_completed']} / {project['phases']['book1']['chapters_planned']} | {project['phases']['book1']['chapters_planned']} | {project['phases']['book1']['chapters_planned'] - project['phases']['book1']['chapters_completed']} |
| **Storyboard Scenes** | {project['storyboard']['scenes_completed']} / {project['storyboard']['total_scenes']} | {project['storyboard']['total_scenes']} | {targets['scenes_remaining']} |

## ⏰ Countdown

- **🎬 Storyboard Due:** {targets['days_to_storyboard']} days ({project['deadlines']['storyboard_complete']})
- **📝 Rough Draft Due:** {targets['days_to_draft']} days ({project['deadlines']['book1_rough_draft']})

---

"""

    if is_rest_day:
        md += f"""## 🌟 Rest Day

Today is {day_name} - your designated rest day!

### Optional Light Tasks:
- [ ] Review this week's writing
- [ ] Brainstorm ideas for upcoming chapters
- [ ] Character development notes
- [ ] World-building sketches
- [ ] Read for inspiration
- [ ] Mind mapping for story arcs

**Remember:** Rest is essential for creativity! 🧘

"""
    else:
        md += f"""## ✍️ Today's Writing Goals

### Primary Task: Write {targets['daily_words']} words

"""
        if current_chapter:
            chapter_progress = (current_chapter['current_words'] / current_chapter['target_words'] * 100) if current_chapter['target_words'] > 0 else 0
            md += f"""**Current Chapter:** {current_chapter['title']}
- Progress: {current_chapter['current_words']} / {current_chapter['target_words']} words ({chapter_progress:.1f}%)
- Status: {current_chapter['status'].replace('_', ' ').title()}

"""

        md += f"""### Writing Tasks:
- [ ] Morning writing session ({targets['daily_words'] // 2} words)
- [ ] Afternoon/Evening session ({targets['daily_words'] // 2} words)
- [ ] Review and edit today's work
- [ ] Update word count in poimea-project.json

### Writing Prompts:
- What is the main conflict in this scene?
- How does this chapter advance the plot?
- What emotions should the reader feel?
- Are character motivations clear?

---

## 🎬 Storyboard Tasks

### Daily Goal: {targets['daily_scenes']:.2f} scenes

- [ ] Sketch scene layouts
- [ ] Define camera angles
- [ ] Note key character positions
- [ ] Add dialogue/action notes
- [ ] Mark scene transitions
- [ ] Update scene count in poimea-project.json

### Storyboard Focus:
- Composition and framing
- Character expressions and body language
- Environmental details
- Pacing and flow
- Visual storytelling

---

## 🎯 Upcoming Milestones

"""

        for milestone in upcoming_milestones:
            status_icon = "⏰" if milestone['days_until'] < 7 else "📅"
            urgency = "**URGENT**" if milestone['days_until'] < 7 else ""
            md += f"{status_icon} **{milestone['name']}** - {milestone['days_until']} days {urgency}\n"

        md += """
---

## 📊 Progress Tracking

### Update Your Progress:

```bash
# After your writing session, update the project file
# Edit poimea-project.json and update:
# - phases.book1.current_word_count
# - storyboard.scenes_completed
# - chapters[].current_words
# - chapters[].status

# Then regenerate tasks
python3 generate_poimea_tasks.py
```

### Quick Log Entry:
- **Words written today:** _____
- **Scenes completed:** _____
- **Time spent:** _____ hours
- **Notes/Reflections:**
  -
  -

---

## 💡 Productivity Tips

"""

        tips = [
            "🍅 Use the Pomodoro Technique: 25 min writing, 5 min break",
            "📝 Write first, edit later - don't let perfectionism slow you down",
            "🎵 Create a playlist that matches your scene's mood",
            "🚶 Take a short walk to brainstorm difficult scenes",
            "💭 Keep a notebook for random ideas that come to you",
            "🎯 Focus on progress, not perfection - this is a rough draft!",
            "📚 Read a page from your favorite book for inspiration",
            "🌅 Write during your peak energy time"
        ]

        import random
        selected_tips = random.sample(tips, 3)
        for tip in selected_tips:
            md += f"- {tip}\n"

        md += """
---

## 🎨 Creative Inspiration

**Remember:** You're building a world, creating characters, telling a story that only you can tell.
Every word written is progress. Every scene sketched is one step closer to bringing Poimea to life.

**Today's Mantra:** "I am a storyteller, and today I add to my story."

"""

    md += f"""---

## 📈 Statistics Dashboard

- **Total Project Days:** 121
- **Days Elapsed:** {121 - targets['days_to_draft']}
- **Days Remaining:** {targets['days_to_draft']}
- **Working Days Left (Draft):** {targets['working_days_draft']}
- **Working Days Left (Storyboard):** {targets['working_days_storyboard']}
- **Average Daily Pace Needed:** {targets['daily_words']} words + {targets['daily_scenes']:.2f} scenes

---

*Generated: {datetime.now().strftime('%B %d, %Y at %H:%M UTC')}*
*Next update: Tomorrow at 9:00 AM UTC*

"""

    return md


def generate_progress_report(project: Dict) -> str:
    """Generate comprehensive progress report"""
    today = date.today()
    targets = calculate_daily_targets(project)
    week_num, progress_pct = get_week_progress(project)

    md = f"""# 📊 Poimea Project Progress Report

*Generated: {today.strftime('%B %d, %Y')}*

---

## 🎯 Executive Summary

**Project:** {project['project']['title']}
**Author:** {project['project']['author']}
**Overall Progress:** {progress_pct}%
**Project Week:** {week_num}

---

## 📖 Book 1 Progress

### Writing Statistics

| Metric | Value |
|--------|-------|
| **Total Word Count** | {project['phases']['book1']['current_word_count']:,} / {project['phases']['book1']['target_word_count']:,} |
| **Completion** | {(project['phases']['book1']['current_word_count'] / project['phases']['book1']['target_word_count'] * 100):.1f}% |
| **Chapters Completed** | {project['phases']['book1']['chapters_completed']} / {project['phases']['book1']['chapters_planned']} |
| **Words Remaining** | {targets['words_remaining']:,} |
| **Days to Deadline** | {targets['days_to_draft']} days |
| **Required Daily Pace** | {targets['daily_words']} words/day |

### Chapter Breakdown

"""

    for chapter in project['chapters']:
        progress = (chapter['current_words'] / chapter['target_words'] * 100) if chapter['target_words'] > 0 else 0
        status_emoji = {
            'completed': '✅',
            'in_progress': '🔄',
            'not_started': '⭕'
        }.get(chapter['status'], '⭕')

        md += f"""**{status_emoji} {chapter['title']}**
- Words: {chapter['current_words']} / {chapter['target_words']} ({progress:.1f}%)
- Status: {chapter['status'].replace('_', ' ').title()}

"""

    md += f"""---

## 🎬 Storyboard Progress

| Metric | Value |
|--------|-------|
| **Scenes Completed** | {project['storyboard']['scenes_completed']} / {project['storyboard']['total_scenes']} |
| **Completion** | {(project['storyboard']['scenes_completed'] / project['storyboard']['total_scenes'] * 100):.1f}% |
| **Scenes Remaining** | {targets['scenes_remaining']} |
| **Days to Deadline** | {targets['days_to_storyboard']} days |
| **Required Daily Pace** | {targets['daily_scenes']:.2f} scenes/day |
| **Target Runtime** | {project['storyboard']['target_runtime_minutes']} minutes |

---

## 🎯 Milestones Status

"""

    for milestone in project['milestones']:
        status = '✅ Completed' if milestone['completed'] else f"⏳ {calculate_days_remaining(milestone['target_date'])} days remaining"
        md += f"- **{milestone['name']}** ({milestone['target_date']}): {status}\n"

    md += f"""
---

## 📅 Timeline Analysis

### Critical Path

1. **Storyboard Completion** - {targets['days_to_storyboard']} days
   - Requires {targets['daily_scenes']:.2f} scenes/day
   - Working days available: {targets['working_days_storyboard']}

2. **Book 1 Rough Draft** - {targets['days_to_draft']} days
   - Requires {targets['daily_words']} words/day
   - Working days available: {targets['working_days_draft']}

### Pace Assessment

"""

    # Calculate if on track
    days_elapsed = 121 - targets['days_to_draft']
    expected_words = int((project['phases']['book1']['target_word_count'] / 121) * days_elapsed)
    expected_scenes = int((project['storyboard']['total_scenes'] / 96) * min(days_elapsed, 96))

    words_diff = project['phases']['book1']['current_word_count'] - expected_words
    scenes_diff = project['storyboard']['scenes_completed'] - expected_scenes

    writing_status = "✅ On track" if words_diff >= 0 else "⚠️ Behind schedule"
    storyboard_status = "✅ On track" if scenes_diff >= 0 else "⚠️ Behind schedule"

    md += f"""**Writing Pace:** {writing_status}
- Expected words by now: {expected_words:,}
- Actual words: {project['phases']['book1']['current_word_count']:,}
- Difference: {words_diff:+,}

**Storyboard Pace:** {storyboard_status}
- Expected scenes by now: {expected_scenes}
- Actual scenes: {project['storyboard']['scenes_completed']}
- Difference: {scenes_diff:+}

---

## 💪 Recommendations

"""

    recommendations = []

    if words_diff < -5000:
        recommendations.append("🚨 **Critical:** Significantly behind on word count. Consider extended writing sessions this week.")
    elif words_diff < 0:
        recommendations.append("⚠️ Slightly behind on word count. Add 200-300 words daily to catch up.")
    else:
        recommendations.append("✅ Writing pace is good! Maintain current momentum.")

    if scenes_diff < -10:
        recommendations.append("🚨 **Critical:** Storyboard is falling behind. Dedicate focused time to scene planning.")
    elif scenes_diff < 0:
        recommendations.append("⚠️ Storyboard needs attention. Try to complete 1-2 extra scenes this week.")
    else:
        recommendations.append("✅ Storyboard pace is solid! Keep up the great work.")

    # Check upcoming milestones
    urgent_milestones = [m for m in project['milestones'] if not m['completed'] and calculate_days_remaining(m['target_date']) < 7]
    if urgent_milestones:
        for milestone in urgent_milestones:
            recommendations.append(f"🎯 **Urgent:** {milestone['name']} due in {calculate_days_remaining(milestone['target_date'])} days!")

    for rec in recommendations:
        md += f"{rec}\n\n"

    md += """---

## 🌟 Motivation

"""

    motivational_quotes = [
        "\"The first draft is just you telling yourself the story.\" - Terry Pratchett",
        "\"You can always edit a bad page. You can't edit a blank page.\" - Jodi Picoult",
        "\"Start writing, no matter what. The water does not flow until the faucet is turned on.\" - Louis L'Amour",
        "\"The scariest moment is always just before you start.\" - Stephen King",
        "\"Write what should not be forgotten.\" - Isabel Allende",
        "\"One day I will find the right words, and they will be simple.\" - Jack Kerouac"
    ]

    import random
    md += f"{random.choice(motivational_quotes)}\n\n"
    md += f"**You've got this! Keep writing, keep creating, keep bringing Poimea to life!** 🚀\n\n"
    md += "---\n\n"
    md += "*This report is automatically generated daily. For daily tasks, see POIMEA_DAILY_TASK.md*\n"

    return md


def main():
    """Main function to generate Poimea tasks"""
    print("📖 Poimea Task Generator Starting...")

    # Load project data
    print("Loading project data...")
    project = load_project_data()

    # Calculate targets
    print("Calculating daily targets...")
    targets = calculate_daily_targets(project)

    # Generate daily tasks
    print("Generating daily tasks...")
    daily_tasks = generate_daily_tasks(project, targets)

    task_file = "POIMEA_DAILY_TASK.md"
    with open(task_file, 'w', encoding='utf-8') as f:
        f.write(daily_tasks)
    print(f"✅ Daily tasks written to {task_file}")

    # Generate progress report
    print("Generating progress report...")
    progress_report = generate_progress_report(project)

    report_file = "POIMEA_PROGRESS_REPORT.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(progress_report)
    print(f"✅ Progress report written to {report_file}")

    # Display summary
    print("\n🎉 Poimea Task Generation Complete!")
    print(f"\n📊 Quick Stats:")
    print(f"  - Words to write today: {targets['daily_words']}")
    print(f"  - Scenes to storyboard: {targets['daily_scenes']:.2f}")
    print(f"  - Days until storyboard: {targets['days_to_storyboard']}")
    print(f"  - Days until rough draft: {targets['days_to_draft']}")
    print(f"\nFiles generated:")
    print(f"  - {task_file} - Today's task list")
    print(f"  - {report_file} - Comprehensive progress report")
    print(f"\n💪 Keep writing! You're building something amazing!")


if __name__ == "__main__":
    main()

# 📖 Poimea Project - Daily Task & Progress Tracking System

An automated daily task generation and progress tracking system for the **Poimea** 4-phase book and animation project.

---

## 🎯 Project Goals

### Primary Objectives (Book 1 Focus)
- ✅ **Rough Draft Complete:** April 26, 2026 (121 days)
- ✅ **Animation Storyboard Complete:** April 1, 2026 (96 days)

### Future Phases
- 📚 Book 2, 3, and 4 (planned for future development)

---

## 📊 Current Status (Auto-Updated Daily)

See `POIMEA_PROGRESS_REPORT.md` for detailed statistics!

**Quick Stats:**
- **Daily Writing Target:** ~776 words
- **Daily Storyboard Target:** ~1.2 scenes
- **Working Days:** 6 days/week (Sunday rest day)

---

## 📁 System Files

| File | Purpose | Update Frequency |
|------|---------|------------------|
| `poimea-project.json` | **Your master data file** - Edit this! | Manual (by you) |
| `generate_poimea_tasks.py` | Task generator script | Rarely needs editing |
| `POIMEA_DAILY_TASK.md` | Today's specific tasks ⭐ | Auto (daily) |
| `POIMEA_PROGRESS_REPORT.md` | Comprehensive progress tracking ⭐ | Auto (daily) |
| `.github/workflows/daily-poimea-tasks.yml` | Automation workflow | Rarely needs editing |
| `POIMEA_README.md` | This documentation | As needed |

---

## 🚀 Quick Start Guide

### 1️⃣ Understanding Your Daily Workflow

Every morning, check `POIMEA_DAILY_TASK.md` for:
- Your writing word count goal
- Storyboard scene requirements
- Upcoming milestones
- Productivity tips
- Progress tracking instructions

### 2️⃣ After Your Writing Session

Update `poimea-project.json` with your progress:

```json
{
  "phases": {
    "book1": {
      "current_word_count": 1500,  // Update this!
      "chapters_completed": 0
    }
  },
  "storyboard": {
    "scenes_completed": 2  // Update this!
  },
  "chapters": [
    {
      "number": 1,
      "current_words": 1500,  // Update this!
      "status": "in_progress"  // Update this!
    }
  ]
}
```

### 3️⃣ Regenerate Your Tasks

```bash
python3 generate_poimea_tasks.py
```

Or just commit your changes - GitHub Actions will auto-update!

---

## 📖 Detailed Usage

### Daily Writing Routine

1. **Morning:** Open `POIMEA_DAILY_TASK.md`
2. **Write:** Complete your word count goal (split into sessions)
3. **Storyboard:** Work on scene sketches and layouts
4. **Update:** Edit `poimea-project.json` with your progress
5. **Regenerate:** Run the script to see updated stats
6. **Commit:** Push your progress (triggers auto-update)

### Weekly Review

Every Sunday (rest day):
- Review `POIMEA_PROGRESS_REPORT.md`
- Check milestone progress
- Adjust your schedule if needed
- Plan next week's chapters

---

## 🎨 Customizing Your Project

### Changing Word Count Target

Edit `poimea-project.json`:

```json
{
  "phases": {
    "book1": {
      "target_word_count": 100000  // Change from 80,000
    }
  }
}
```

### Adding More Chapters

```json
{
  "chapters": [
    {
      "number": 3,
      "title": "Chapter 3 - Your Title",
      "target_words": 4000,
      "current_words": 0,
      "status": "not_started",
      "scenes": ["Scene 6", "Scene 7"]
    }
  ]
}
```

### Adjusting Storyboard Goals

```json
{
  "storyboard": {
    "total_scenes": 120,  // Change from 100
    "target_runtime_minutes": 120  // Change from 90
  }
}
```

### Adding Custom Milestones

```json
{
  "milestones": [
    {
      "name": "First Act Complete",
      "target_date": "2026-03-01",
      "completed": false
    }
  ]
}
```

### Changing Rest Days

```json
{
  "daily_goals": {
    "rest_days": ["Saturday", "Sunday"]  // Add/remove days
  }
}
```

---

## 📊 Understanding Your Metrics

### Word Count Tracking
- **Target:** 80,000 words for Book 1
- **Daily Goal:** Auto-calculated based on remaining days
- **Adjusts automatically** as you make progress

### Storyboard Tracking
- **Total Scenes:** 100 scenes (customizable)
- **Runtime Target:** 90 minutes
- **Daily Goal:** Calculated to meet April 1st deadline

### Chapter Status Options
- `not_started` - Haven't begun writing
- `in_progress` - Currently working on it
- `completed` - Chapter draft finished

---

## 🎯 Milestone System

The system tracks 10 key milestones:

### Phase 1: Planning (Jan 2026)
- World Building Complete (Jan 15)
- Character Development Complete (Jan 20)
- Plot Outline Complete (Jan 25)

### Phase 2: Writing (Feb-Mar 2026)
- First 5 Chapters Draft (Feb 15)
- Midpoint - 10 Chapters Draft (Mar 15)

### Phase 3: Storyboard (Progressive)
- 25% Complete (Feb 1)
- 50% Complete (Feb 25)
- 75% Complete (Mar 15)
- 100% Complete (Apr 1) ⭐

### Phase 4: Completion
- Full Rough Draft Complete (Apr 26) ⭐

Mark milestones as completed:
```json
{
  "milestones": [
    {
      "name": "World Building Complete",
      "completed": true  // Change to true when done
    }
  ]
}
```

---

## 🤖 Automation

### GitHub Actions Workflow

The system automatically runs:
- **Daily at 9:00 AM UTC** (generates fresh tasks)
- **When you update** `poimea-project.json`
- **Manually** via workflow dispatch button

### What Gets Automated
✅ Daily task generation
✅ Progress report updates
✅ Pace analysis (are you on track?)
✅ Milestone reminders
✅ Motivational content
✅ Auto-commit and push

### Manual Run
```bash
python3 generate_poimea_tasks.py
```

---

## 📈 Progress Tracking Features

### Automatic Calculations
- Days remaining to each deadline
- Required daily word count
- Required daily scene count
- Overall project completion percentage
- Per-chapter progress
- Pace assessment (on track vs behind)

### Visual Indicators
- ⭕ Not Started
- 🔄 In Progress
- ✅ Completed
- ⚠️ Behind Schedule
- 🚨 Critically Behind

### Smart Recommendations
The system analyzes your pace and provides:
- Catch-up strategies if behind
- Encouragement if on track
- Urgent warnings for approaching milestones
- Suggested daily word count adjustments

---

## 💡 Productivity Tips Built-In

Each day you'll receive:
- 🍅 Pomodoro technique reminders
- 📝 Writing prompts for your scenes
- 🎨 Storyboard focus areas
- 💭 Creative inspiration
- 📚 Motivational quotes
- 🎯 Daily mantras

---

## 🔧 Troubleshooting

### Script Won't Run
```bash
# Check Python version
python3 --version  # Need 3.7+

# Verify JSON is valid
python3 -m json.tool poimea-project.json
```

### Numbers Don't Look Right
- Check that `current_word_count` is updated
- Verify dates are in ISO format (YYYY-MM-DD)
- Ensure `target_word_count` matches your goal

### GitHub Actions Not Running
- Verify workflow file is in `.github/workflows/`
- Check repository Actions are enabled
- Review Actions logs for errors

### Progress Not Tracking
- Make sure you're editing `poimea-project.json`
- Regenerate tasks after each writing session
- Commit and push to trigger auto-update

---

## 📅 Sample Timeline

### January 2026 - Foundation
- Week 1-2: World building, character development
- Week 3-4: Detailed plot outline

### February 2026 - Writing Begins
- Week 1: Start Chapter 1-2
- Week 2: Chapters 3-5
- Week 3-4: Chapters 6-10 (midpoint)
- Storyboard: 50% complete by end of month

### March 2026 - Push to Completion
- Week 1-2: Chapters 11-15
- Week 3-4: Chapters 16-20
- Storyboard: 75% complete, then 100%

### April 2026 - Final Sprint
- Week 1: Storyboard completion (Apr 1) ✅
- Week 2-3: Final chapters
- Week 4: Complete rough draft (Apr 26) ✅

---

## 🎨 Book 1 Structure Recommendations

### Suggested Chapter Breakdown
- **Chapters 1-5:** Introduction, world, characters
- **Chapters 6-10:** Rising action, first obstacles
- **Chapters 11-15:** Midpoint crisis, escalation
- **Chapters 16-20:** Climax and resolution

### Target Words per Chapter
- Average: 4,000 words
- Range: 3,000 - 5,000 words
- Total: 80,000 words

---

## 🎬 Storyboard Best Practices

### Scene Planning
- Start with key moments (action, emotional beats)
- Work backward/forward from climax
- Consider pacing and rhythm
- Note camera angles and composition

### Daily Storyboard Workflow
1. Review corresponding book chapter
2. Identify 1-2 scenes to visualize
3. Rough sketch layouts
4. Add notes for animation
5. Update scene count

---

## 📊 Example Progress Update

After a productive day:

**Before:**
```json
{
  "current_word_count": 0,
  "scenes_completed": 0
}
```

**After:**
```json
{
  "current_word_count": 1200,
  "scenes_completed": 2,
  "chapters": [
    {
      "number": 1,
      "current_words": 1200,
      "status": "in_progress"
    }
  ]
}
```

Then run:
```bash
python3 generate_poimea_tasks.py
```

See updated metrics instantly!

---

## 🌟 Motivation & Mindset

### Remember
- **Progress over perfection** - This is a rough draft!
- **Consistency beats intensity** - Small daily wins add up
- **Rest is productive** - Your brain needs downtime
- **Every word counts** - Even 100 words is progress
- **You're building a world** - Trust the creative process

### On Difficult Days
- Lower your word count goal temporarily
- Focus on outlining instead of writing
- Work on storyboards for a change of pace
- Read your favorite book for inspiration
- Remember why you started this project

### Celebrate Milestones
When you hit a milestone:
- Mark it complete in the JSON
- Take a moment to celebrate
- Share your progress with someone
- Reward yourself
- Then keep going! 🚀

---

## 🔄 Future Enhancements

Ideas for expanding the system:
- [ ] Character database tracking
- [ ] World-building notes integration
- [ ] Scene-by-scene breakdown
- [ ] Visual word count charts
- [ ] Weekly summary emails
- [ ] Integration with writing apps
- [ ] Voice recording for ideas
- [ ] Mobile app for progress tracking

---

## 📚 Resources

### Writing
- Save the Cat! Writes a Novel
- Story Engineering by Larry Brooks
- The Anatomy of Story by John Truby

### Storyboarding
- The Animator's Survival Kit
- Framed Ink: Drawing and Composition
- Storyboarding: Motion in Art

### Animation
- The Illusion of Life by Frank Thomas
- Timing for Animation by Harold Whitaker

---

## 🤝 Contributing Your Progress

This system is designed for your solo journey, but you can:
- Fork and customize for other projects
- Share your progress screenshots
- Adapt for different creative projects
- Build on top of the automation

---

## 📝 Quick Reference Commands

```bash
# Generate today's tasks
python3 generate_poimea_tasks.py

# Check your JSON is valid
python3 -m json.tool poimea-project.json

# View daily task
cat POIMEA_DAILY_TASK.md

# View progress report
cat POIMEA_PROGRESS_REPORT.md

# Commit progress
git add poimea-project.json
git commit -m "Progress: [words] words, [scenes] scenes"
git push
```

---

## 🎯 Your Mission

**You have 121 days to complete Book 1's rough draft.**

**You have 96 days to complete the storyboard.**

**The system will guide you. You just need to show up and write.**

**Every day you write, you're one step closer to bringing Poimea to life.**

---

## 💪 Let's Do This!

Open `POIMEA_DAILY_TASK.md` and start your journey today.

The world of Poimea awaits. Your characters are waiting for their story.

**Write. Create. Complete.**

🚀 **You've got this!** 🚀

---

*System created: December 26, 2025*
*Target completion: April 26, 2026*
*Project: Poimea - A 4-Phase Epic*

**Now go write something amazing!** ✍️

# 🚀 Poimea Quick Start - Get Writing Today!

**Welcome to your Poimea writing journey!** This guide gets you started in 5 minutes.

---

## ⚡ 3-Step Daily Routine

### 1. Check Today's Tasks (30 seconds)
```bash
cat POIMEA_DAILY_TASK.md
```

You'll see:
- ✍️ How many words to write today (~776)
- 🎬 How many storyboard scenes (~1-2)
- 🎯 Upcoming milestones
- 💡 Writing prompts and tips

### 2. Write & Create (2-3 hours)
- **Morning:** Write ~400 words
- **Afternoon/Evening:** Write ~400 words
- **Anytime:** Sketch 1-2 storyboard scenes

### 3. Update Your Progress (2 minutes)
Open `poimea-project.json` and edit these numbers:

```json
{
  "phases": {
    "book1": {
      "current_word_count": 800  // ← Add today's words here
    }
  },
  "storyboard": {
    "scenes_completed": 2  // ← Add scenes completed
  },
  "chapters": [
    {
      "number": 1,
      "current_words": 800,  // ← Update chapter words
      "status": "in_progress"  // ← Change when done
    }
  ]
}
```

Then regenerate:
```bash
python3 generate_poimea_tasks.py
```

**Done!** Tomorrow you'll get updated tasks automatically! ✅

---

## 📅 Your First Week Plan

### Day 1 (Today - Dec 26)
- [ ] Read this guide
- [ ] Read `POIMEA_DAILY_TASK.md`
- [ ] Write 776 words (Chapter 1 opening)
- [ ] Sketch 1-2 scenes
- [ ] Update `poimea-project.json`

### Day 2-6 (This Week)
- [ ] Write 776 words daily
- [ ] Storyboard 1-2 scenes daily
- [ ] Track your progress
- [ ] Build momentum!

### Day 7 (Sunday - Rest!)
- [ ] Review your week
- [ ] Check `POIMEA_PROGRESS_REPORT.md`
- [ ] Plan next week
- [ ] Celebrate progress! 🎉

---

## 🎯 Quick Goals Cheat Sheet

| Goal | Deadline | Daily Target |
|------|----------|--------------|
| **Storyboard** | April 1, 2026 | 1.2 scenes |
| **Rough Draft** | April 26, 2026 | 776 words |
| **Work Days** | 6 per week | Mon-Sat |
| **Rest** | 1 per week | Sunday |

---

## 📝 Editing poimea-project.json - Copy/Paste Examples

### After Writing 1,000 Words Today
```json
"current_word_count": 1000,
```

### After Completing 3 Storyboard Scenes
```json
"scenes_completed": 3,
```

### When Starting Chapter 1
```json
{
  "number": 1,
  "title": "Chapter 1 - Opening",
  "current_words": 850,
  "status": "in_progress"
}
```

### When Finishing Chapter 1
```json
{
  "number": 1,
  "current_words": 4200,
  "status": "completed"
}
```

### When Completing a Milestone
```json
{
  "name": "World Building Complete",
  "completed": true
}
```

---

## 🆘 Common Questions

### Q: What if I can't hit the daily word count?
**A:** Write what you can! Even 300 words is progress. The system auto-adjusts future targets.

### Q: Sunday is my writing day. Can I change the rest day?
**A:** Yes! Edit `poimea-project.json`:
```json
"rest_days": ["Friday"]
```

### Q: Can I write more than 776 words?
**A:** Absolutely! Write as much as you want. Update your count and future targets will adjust.

### Q: What if I miss a day?
**A:** No problem! The system redistributes the work across remaining days. Just keep going.

### Q: Do I have to do storyboard and writing every day?
**A:** No! Some days focus on writing, some on storyboard. The targets are guidelines.

---

## 🎨 Storyboard Tips for Beginners

Don't worry if you can't draw! Storyboards are about:
- **Stick figures are fine!** It's about composition, not art
- **Show camera angles** - close-up, wide shot, etc.
- **Mark character positions** - where are they in the scene?
- **Note the action** - what happens?
- **Add dialogue snippets** - key lines

Example simple scene notation:
```
Scene 1: EXT. FOREST - DAY
[Wide shot]
Character A enters from left
Character B hiding behind tree (right)
Mood: Tense, mysterious
Camera: Slow pan following A
```

---

## 💪 Motivation Boosters

### When You Don't Feel Like Writing
- Just write ONE sentence
- Set a timer for 10 minutes
- Write the fun scene you're excited about
- Describe what you see in your mind
- Remember: rough drafts are supposed to be rough!

### Progress Milestones to Celebrate
- ✨ First 1,000 words
- ✨ First chapter complete
- ✨ 10,000 words (12.5% done!)
- ✨ 25,000 words (31% done!)
- ✨ 40,000 words (halfway!)
- ✨ First storyboard sequence done
- ✨ Every milestone achieved

---

## 📊 Check Your Progress Anytime

```bash
# See comprehensive stats
cat POIMEA_PROGRESS_REPORT.md

# See today's tasks
cat POIMEA_DAILY_TASK.md

# Update everything
python3 generate_poimea_tasks.py
```

---

## 🎯 Your First Writing Session - RIGHT NOW!

1. **Set a timer for 25 minutes**
2. **Open your writing app**
3. **Write Chapter 1 opening** - Don't overthink, just write!
4. **When timer ends** - Count your words
5. **Update** `poimea-project.json`
6. **Celebrate** - You started! 🎉

---

## 🌟 Remember

**You don't need to be perfect. You just need to START.**

- ✍️ Write something (anything!)
- 📊 Track it
- 🔄 Repeat tomorrow

**That's the system. That's how you finish a book.**

---

## 📱 Daily Checklist

Save this checklist:

```
☐ Morning: Check POIMEA_DAILY_TASK.md
☐ Session 1: Write ~400 words
☐ Session 2: Write ~400 words
☐ Storyboard: Sketch 1-2 scenes
☐ Update: Edit poimea-project.json
☐ Regenerate: Run the script
☐ Evening: Feel accomplished! ✅
```

---

## 🚀 Ready? Let's Go!

**Your first task:** Write 776 words today.

**Right now.** Open your document and start typing.

**Chapter 1, Scene 1.** Just begin.

The world of Poimea is waiting for you to bring it to life.

**GO! ✍️**

---

*Remember: 121 days to rough draft. Starting today: December 26, 2025.*

**Every day you write, you're closer to finishing.**

**Now go create something amazing!** 🌟

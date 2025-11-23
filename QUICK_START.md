# Quick Start Guide

This guide will help you get up and running quickly with The Founder's Way book project.

---

## Setup (5 minutes)

### 1. Install Dependencies

```bash
# Install Python dependencies
make install

# Activate virtual environment
source .venv/bin/activate
```

### 2. Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your API keys (use your preferred editor)
nano .env
```

---

## Working with AI Agents

### Using Claude (for coding/scripts)

Claude will automatically read `.claude/CLAUDE.md` when working in this directory. You can reference it by saying:

> "Follow the guidelines in .claude/CLAUDE.md"

### Using Gemini (for research/writing)

Point Gemini to the instruction manual:

> "Read .gemini/GEMINI.md for writing guidelines, then draft chapter X"

---

## Creating a New Chapter

### Step 1: Create Chapter Directory

```bash
mkdir docs/01-chapter-name
cd docs/01-chapter-name
```

### Step 2: Create Standard Files

Use the template from `templates/chapter-template.md`:

```bash
# Create basic structure
touch 01-title.md
touch 02-introduction.md
touch 03-key-concepts.md
touch 04-key-takeaways.md
touch 05-recommended-readings.md
```

### Step 3: Fill in Content

Follow the templates in `.claude/CLAUDE.md` or `.gemini/GEMINI.md`

---

## Useful Commands

### Check Content Statistics

```bash
python scripts/content_stats.py
```

### Open Jupyter Lab (if needed)

```bash
make jupyter
```

### Clean Virtual Environment

```bash
make clean
```

---

## File Naming Rules

✅ **Do this:**
- `01-introduction.md`
- `02-key-concepts.md`
- `15-case-study-example.md`

❌ **Don't do this:**
- `Introduction.md` (no number)
- `01_introduction.md` (underscore instead of hyphen)
- `01 introduction.md` (spaces)

---

## Common Workflows

### Research → Write Workflow

1. Add research notes to `.context/research.md`
2. Update strategy in `.context/strategy.md`
3. Use Gemini to draft content based on research
4. Review and edit

### Write → Code Workflow

1. Identify need for automation (e.g., data analysis)
2. Add specification to `.context/spec.md`
3. Use Claude to implement the script
4. Test and integrate

---

## Context Files

The `.context/` directory tracks shared state:

| File | Purpose |
|------|---------|
| `strategy.md` | Book outline and high-level plan |
| `research.md` | Research notes and sources |
| `spec.md` | Technical specifications for scripts |
| `constraints.md` | Global rules and guidelines |

Update these as you work to keep AI agents in sync.

---

## Getting Help

### AI Instructions
- **Claude**: See `.claude/CLAUDE.md`
- **Gemini**: See `.gemini/GEMINI.md`

### Templates
- Chapter structure: `templates/chapter-template.md`

### Full Documentation
- Complete guide: `README.md`

---

## Next Steps

1. ✅ Complete setup (above)
2. ⬜ Define book outline in `.context/strategy.md`
3. ⬜ Start research in `.context/research.md`
4. ⬜ Create your first chapter
5. ⬜ Run `python scripts/content_stats.py` to check progress

---

*Happy writing! 📚*

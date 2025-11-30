# The Founder's Way

## Project Overview

**The Founder's Way** is a book project exploring the journeys, challenges, and lessons learned by founders building successful companies.

**Status:** In active development  
**License:** [To be determined]

---

## Table of Contents

- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Multi-AI Workflow](#multi-ai-workflow)
- [Development Workflow](#development-workflow)
- [Writing Guidelines](#writing-guidelines)
- [Technical Setup](#technical-setup)

---

## Repository Structure

```
founders_way_book/
├── .claude/                     # Claude AI configuration
│   └── CLAUDE.md               # Claude AI instruction manual
├── .gemini/                     # Gemini AI configuration
│   └── GEMINI.md               # Gemini AI instruction manual
├── .context/                    # Shared context for multi-agent workflow
│   ├── constraints.md          # Global rules and constraints
│   ├── research.md             # Research notes and data
│   ├── spec.md                 # Technical specifications
│   └── strategy.md             # High-level strategy and planning
│
├── README.md                    # This file - Project overview
├── .gitignore                   # Git ignore rules
├── .env.example                 # Environment variables template
│
├── docs/                        # Book chapters (79 sub-chapter files)
│   ├── 00-prologue.md
│   ├── 01-the-founders-condition-01-introduction.md
│   ├── 01-the-founders-condition-02-*.md
│   ├── 02-startup-and-idea-01-introduction.md
│   └── ... (organized by chapter prefix)
│
├── original_text/               # Original full-chapter markdown files
│   ├── Module-01-*.md through Module-07-*.md
│   └── original-text.md
│
├── templates/                   # Reusable templates
│   └── chapter-template.md
│
├── scripts/                     # Python automation tools
│   ├── split_chapters.py       # Split chapters into sub-chapters
│   └── content_stats.py        # Generate content statistics
│
├── .venv/                       # Python virtual environment (local)
├── requirements.txt             # Python dependencies
└── Makefile                     # Development tasks
```

---

## Getting Started

### Prerequisites

- Git
- Python 3.12+ (managed via `uv` or system Python)
- Text editor (VS Code recommended)

### Quick Start

```bash
# Clone or navigate to repository
cd /Users/jlim/Projects/founders_way_book

# Install Python dependencies
make install

# Activate virtual environment
source .venv/bin/activate

# Copy environment template and add your API keys
cp .env.example .env
# Edit .env with your API keys
```

### Environment Setup

Create a `.env` file with your API keys:

```bash
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

---

## Multi-AI Workflow

This project uses a **Context-Driven Multi-Agent Architecture** to ensure high-quality, well-researched, and technically sound content.

### Agent Roles

| Agent | Role | Responsibilities |
| :--- | :--- | :--- |
| **Claude** | **Coder & Technical Reviewer** | • Write Python scripts for automation<br>• Review code for correctness and efficiency<br>• Implement technical tools |
| **Gemini** | **Researcher & Drafter** | • Research and gather data from trusted sources<br>• Write chapter content<br>• Proofread and fact-check |

### Shared Context (`.context/`)

The `.context/` directory contains shared state across agents:

1. **`strategy.md`**: The high-level plan and book outline
2. **`research.md`**: Research notes and data gathered
3. **`spec.md`**: Technical specifications for scripts
4. **`constraints.md`**: Global rules and style guides

### How to Work with AI Agents

1. **For Content Creation**: Point Gemini to `.gemini/GEMINI.md` for writing guidelines
2. **For Scripting**: Point Claude to `.claude/CLAUDE.md` for coding standards
3. **Update Context**: Add research notes to `.context/research.md` as you gather data
4. **Track Strategy**: Update `.context/strategy.md` with chapter outlines and milestones

---

## Development Workflow

### File Naming Conventions

**Sub-chapter files:** All chapters are split into sub-chapter files in a flat structure within `docs/`

Format: `##-chapter-name-##-sub-chapter-title.md`

Examples:
- `00-prologue.md` (single file, no sub-chapters)
- `01-the-founders-condition-01-introduction.md`
- `01-the-founders-condition-02-나는-창업가일까.md`
- `02-startup-and-idea-01-introduction.md`
- `02-startup-and-idea-02-아이디어는-시작일-뿐.md`

**Documentation:** UPPERCASE or lowercase_underscore
- `README.md`
- `roadmap.md`, `status.md`

### Chapter Structure

The book is organized into **8 chapters** with **79 total files** (including prologue):

- **Chapter 00:** Prologue (1 file)
- **Chapter 01:** The Founder's Condition (10 sub-chapters)
- **Chapter 02:** Startup and Idea (9 sub-chapters)
- **Chapter 03:** Market and Competition (10 sub-chapters)
- **Chapter 04:** The Founder's Work (20 sub-chapters)
- **Chapter 05:** Reverse Startup Practice (12 sub-chapters)
- **Chapter 06:** Problems Founders Must Solve (6 sub-chapters)
- **Chapter 07:** Appendix - Unicorn Fundraising (11 sub-chapters)

All sub-chapter files are located directly in the `docs/` directory. Original full-chapter files are preserved in `original_text/` for reference.

### Working with Chapters

**To view a chapter:** Browse files in `docs/` with the same chapter prefix (e.g., `01-*` for Chapter 01)

**To add new sub-chapters:**
1. Follow the naming convention: `##-chapter-name-##-sub-chapter-title.md`
2. Use the next sequential number for the sub-chapter
3. Include an H1 heading: `# ##-## – Sub-chapter Title`
4. Follow templates in `.claude/CLAUDE.md` and `.gemini/GEMINI.md`

**To reorganize chapters:** Use the `scripts/split_chapters.py` tool to re-split chapters from original files

---

## Writing Guidelines

### Content Standards

- **Action-oriented:** Focus on practical insights and actionable advice
- **Evidence-based:** Cite sources with links for all claims and data
- **Progressive:** Build concepts from simple to complex
- **Engaging:** Use real-world examples and case studies

### Source Priorities

When researching, prioritize these trusted sources:

**Business & Startup Coverage:**
- Harvard Business Review
- Stanford GSB publications
- Wall Street Journal, Bloomberg, Financial Times
- TechCrunch, Reuters

**Academic & Research:**
- SSRN, NBER
- Academic journals and peer-reviewed papers

**Data & Reports:**
- CB Insights, PitchBook, Crunchbase

See `.gemini/GEMINI.md` for complete research guidelines.

---

## Technical Setup

### Python Scripts (Optional)

**Available Make targets:**
- `make venv` - Create virtual environment
- `make install` - Install dependencies
- `make update` - Update dependencies
- `make jupyter` - Launch JupyterLab
- `make clean` - Remove virtual environment

See `Makefile` for all targets.

### AI Assistant Setup

When opening this project with AI assistants:

1. **Claude**: Read `.claude/CLAUDE.md` for coding and technical standards
2. **Gemini**: Read `.gemini/GEMINI.md` for research and writing guidelines
3. **All AI tools should:**
   - Follow the file naming conventions
   - Update context files in `.context/` as work progresses
   - Cite sources for all claims and data

---

## Project Status

**Version:** 0.2
**Last Updated:** November 30, 2024
**Status:** Content structure organized, 79 sub-chapters created

### Content Summary

- ✅ **79 sub-chapter files** created across 8 chapters
- ✅ **Original text preserved** in `original_text/` directory
- ✅ **Chapter splitting automation** complete
- ✅ **File organization** restructured for better workflow

---

## Next Steps

1. ✅ Set up project structure
2. ✅ Create AI instruction manuals
3. ✅ Configure development environment
4. ✅ Split chapters into sub-chapter files
5. ✅ Organize directory structure
6. ⬜ Content editing and refinement
7. ⬜ Add cross-references between sub-chapters
8. ⬜ Develop additional automation scripts

---

*For detailed writing and technical guidelines, see `.claude/CLAUDE.md` and `.gemini/GEMINI.md`*

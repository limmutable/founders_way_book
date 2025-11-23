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
├── docs/                        # Book chapters (main content)
│   └── [To be created]
│
├── templates/                   # Reusable templates
│   └── [To be created]
│
├── scripts/                     # Python automation tools
│   └── [To be created]
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

**Chapter content files:** `kebab-case` with numeric prefix
- `01-introduction.md`
- `02-key-concepts.md`
- `22-qa.md`
- `23-key-takeaways.md`

**Documentation:** UPPERCASE or lowercase_underscore
- `README.md`
- `roadmap.md`, `status.md`

### Chapter Structure

Each chapter follows this pattern:

```
docs/ChapterName/
├── 01-title.md
├── 02-introduction.md
├── 03-[topic].md
├── ...
├── [N-1]-qa.md
├── [N]-key-takeaways.md
└── [N+1]-recommended-readings.md
```

### Creating New Chapters

1. Create directory: `mkdir docs/chapter-name`
2. Start with standard files: `01-title.md`, `02-introduction.md`
3. Follow templates in `.claude/CLAUDE.md` and `.gemini/GEMINI.md`
4. Update this README with chapter progress

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

**Version:** 0.1  
**Last Updated:** November 2024  
**Status:** Initial setup complete, ready for content creation

---

## Next Steps

1. ✅ Set up project structure
2. ✅ Create AI instruction manuals
3. ✅ Configure development environment
4. ⬜ Define book outline in `.context/strategy.md`
5. ⬜ Create first chapter
6. ⬜ Develop automation scripts

---

*For detailed writing and technical guidelines, see `.claude/CLAUDE.md` and `.gemini/GEMINI.md`*

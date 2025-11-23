# Claude AI Reference for The Founder's Way

This document contains templates, standards, and workflow guidelines for authoring **The Founder's Way** book.

## Role Definition
**Role:** Coder & Technical Reviewer
**Mode:** EXECUTION

### Responsibilities
1. **Scripting:** Write Python scripts for automation, data analysis, and content generation in `scripts/`.
2. **Code Review:** Review all code for:
   - **Correctness:** Does the logic work as expected?
   - **Efficiency:** Is the code optimized?
   - **Documentation:** Are functions well-documented?

---

## AI Interaction Guidelines

### Core Principles
1. **Action-Oriented Approach**
   - Bias toward doing rather than explaining
   - Execute commands and make changes when requested
   - Only ask for clarification on genuinely ambiguous requests

2. **Communication Style**
   - Concise explanations followed by immediate action
   - Show relevant code snippets with proper file paths and line numbers
   - Use relative paths for project files
   - Provide next-step suggestions after completing tasks

### Git Workflow
- **Do not commit or push to git unless explicitly requested**
- When you say **"prepare to commit"**, perform pre-commit actions (cleanup, documentation updates, generate commit message) but **do not actually commit**
- Only commit when explicitly instructed to do so

---

## File Naming Conventions

### Chapter Content Files
Use **lowercase-with-hyphens (kebab-case)** with two-digit numeric prefix:
- `01-introduction.md`
- `02-key-concepts.md`
- `22-qa.md`
- `23-key-takeaways.md`

### Documentation Files
- **Standard docs:** UPPERCASE → `README.md`, `CLAUDE.md`, `.gitignore`
- **Living docs:** lowercase_underscore → `roadmap.md`, `status.md`
- **Snapshots:** lowercase_YYYYMMDD → `status_20241123.md`

### Avoid
- ❌ camelCase, PascalCase
- ❌ Spaces in filenames
- ❌ Mixed conventions

---

## Chapter Structure

Each chapter directory follows this pattern:

```
ChapterName/
├── 01-title.md
├── 02-introduction.md
├── 03-[topic].md
├── ...
├── [N-1]-qa.md
├── [N]-key-takeaways.md
└── [N+1]-recommended-readings.md
```

**Organization Tips:**
1. Start with context: Title → Introduction → Core Concepts
2. Build progressively: Concepts → Frameworks → Examples
3. Include interaction: Questions or discussions mid-chapter
4. Close with reflection: Q&A → Key Takeaways → Next Steps

---

## Standard File Templates

### Title File (01-title.md)
```markdown
# 01 – Title

## [Chapter Title: Descriptive Name]
```

### Introduction (02-introduction.md)
```markdown
# 02 – Introduction

## Introduction

[Brief chapter overview]

### Learning Objectives

* [Objective 1]
* [Objective 2]
* [Objective 3]
```

### Content File - Concept
```markdown
# [NN] – [Concept Name]

## [Concept Name]

**Definition:** [Brief definition]

[Additional explanation and context]
```

### Key Takeaways
```markdown
# [NN] – Key Takeaways

## Key Takeaways

* [Takeaway 1]
* [Takeaway 2]
* [Takeaway 3]
```

---

## Project Structure

```
founders_way_book/
├── .claude/                     # Claude AI configuration
│   └── CLAUDE.md               # This file
├── .gemini/                     # Gemini AI configuration
│   └── GEMINI.md               # Gemini AI instructions
├── .context/                    # Shared context for multi-agent workflow
│   ├── constraints.md          # Global rules and constraints
│   ├── research.md             # Research notes and data
│   ├── spec.md                 # Technical specifications
│   └── strategy.md             # High-level strategy
├── README.md                    # Project overview
├── .gitignore                   # Git ignore rules
├── docs/                        # Book chapters (main content)
├── templates/                   # Reusable templates
├── scripts/                     # Python automation tools
├── .venv/                       # Python virtual environment (local)
└── requirements.txt             # Python dependencies
```

---

## Development Workflow

### Creating New Chapters
1. Create new directory: `mkdir docs/ChapterName`
2. Start with standard files: `01-title.md`, `02-introduction.md`
3. Follow the chapter structure pattern
4. Use templates from this document
5. Maintain sequential numbering

### Modifying Existing Content
1. Read the file first to understand current content
2. Use Edit tool for targeted changes (preserve formatting)
3. Maintain file numbering consistency
4. Update documentation if adding new patterns

---

## Best Practices

### Content Creation
- Start with clear learning objectives
- Build concepts progressively
- Include real-world examples and case studies
- Close with reflection and next steps

### File Management
- Use consistent naming conventions (kebab-case with numeric prefix)
- Keep file numbers sequential without gaps
- When inserting new files, renumber subsequent files
- Update documentation when making structural changes

### Quality Standards
- Each file should be self-contained but connected to the chapter narrative
- Use tables and bullet points for clarity
- Keep content concise and scannable
- Include real-world examples and sources when possible
- Link to external resources for deeper learning

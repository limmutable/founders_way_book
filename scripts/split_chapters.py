#!/usr/bin/env python3
"""
Split chapter markdown files into sub-chapter files based on [중제목] markers.

This script:
1. Reads each chapter file in the docs/ directory
2. Identifies sub-chapters marked with ## **\[중제목\]...**
3. Splits them into separate files with sequential numbering
4. Renames the original file to Module-*.md for reference
"""

import re
import os
import glob
import shutil


def extract_subtitle(line):
    """Extract the Korean subtitle from a [중제목] heading line."""
    # Pattern: ## **\[중제목\]TITLE** {optional anchor}
    match = re.match(r'##\s+\*\*\\\[중제목\\\](.+?)\*\*', line)
    if match:
        return match.group(1).strip()
    return None


def create_slug(title):
    """Create a URL-friendly slug from a Korean/English title."""
    # Remove special characters and spaces
    slug = re.sub(r'[^\w\s가-힣-]', '', title)
    slug = slug.strip().replace(' ', '-').lower()
    return slug if slug else "section"


def split_chapter_file(filepath, docs_dir="docs"):
    """Split a single chapter file into sub-chapter files."""

    filename = os.path.basename(filepath)
    print(f"\n📄 Processing: {filename}")

    # Extract chapter prefix (e.g., "01-the-founders-condition")
    chapter_prefix = os.path.splitext(filename)[0]
    chapter_number = chapter_prefix.split('-')[0]  # e.g., "01"

    # Read the file
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by lines for processing
    lines = content.split('\n')

    # Find all sub-chapter markers
    sub_chapters = []
    current_section = []
    current_title = None

    for i, line in enumerate(lines):
        # Check if this is a sub-chapter heading
        subtitle = extract_subtitle(line)

        if subtitle:
            # Save previous section if exists
            if current_section:
                sub_chapters.append({
                    'title': current_title,
                    'content': '\n'.join(current_section).strip()
                })

            # Start new section
            current_title = subtitle
            current_section = []
        else:
            current_section.append(line)

    # Don't forget the last section
    if current_section:
        sub_chapters.append({
            'title': current_title,
            'content': '\n'.join(current_section).strip()
        })

    # If no sub-chapters found, skip this file
    if not sub_chapters or (len(sub_chapters) == 1 and sub_chapters[0]['title'] is None):
        print(f"  ⏭️  No sub-chapters found, skipping")
        return []

    print(f"  ✅ Found {len(sub_chapters)} sub-chapters")

    # Rename original file to Module-*.md
    module_filepath = os.path.join(docs_dir, f"Module-{filename}")
    shutil.move(filepath, module_filepath)
    print(f"  📦 Renamed original to: Module-{filename}")

    # Create sub-chapter files
    created_files = []
    sub_index = 1

    for sub in sub_chapters:
        title = sub['title']
        content = sub['content']

        # Skip if no title (introduction section before first sub-chapter)
        if title is None:
            # This is intro content - save as 01-introduction.md
            slug = "introduction"
            title_display = "Introduction"
        else:
            slug = create_slug(title)
            title_display = title

        # Create filename: 01-01-title-slug.md
        sub_filename = f"{chapter_prefix}-{str(sub_index).zfill(2)}-{slug}.md"
        sub_filepath = os.path.join(docs_dir, sub_filename)

        # Create H1 heading
        h1_heading = f"# {chapter_number}-{str(sub_index).zfill(2)} – {title_display}\n\n"

        # Write file
        with open(sub_filepath, 'w', encoding='utf-8') as f:
            f.write(h1_heading + content)

        created_files.append(sub_filename)
        print(f"    📝 Created: {sub_filename}")

        sub_index += 1

    return created_files


def main():
    """Main function to process all chapter files."""
    docs_dir = "docs"

    print("=" * 70)
    print("🚀 Chapter Splitting Tool")
    print("=" * 70)

    # Find all chapter files (pattern: ##-*.md)
    pattern = os.path.join(docs_dir, '[0-9][0-9]-*.md')
    chapter_files = sorted(glob.glob(pattern))

    if not chapter_files:
        print("\n❌ No chapter files found matching pattern: ##-*.md")
        return

    print(f"\n📚 Found {len(chapter_files)} chapter file(s) to process\n")

    all_created = []
    for filepath in chapter_files:
        created = split_chapter_file(filepath, docs_dir)
        all_created.extend(created)

    print("\n" + "=" * 70)
    print(f"✨ Complete! Created {len(all_created)} sub-chapter files")
    print("=" * 70)


if __name__ == "__main__":
    main()

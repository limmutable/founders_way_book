#!/usr/bin/env python3
"""
Content Statistics Script

Analyzes markdown files and provides statistics:
- Word count
- Reading time estimate
- Number of chapters
- Number of files per chapter
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple


def count_words(text: str) -> int:
    """
    Count words in text, excluding markdown syntax.
    
    Args:
        text: Raw markdown text
        
    Returns:
        Word count
    """
    # Remove markdown headers
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    # Remove markdown links but keep link text
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Remove inline code
    text = re.sub(r'`[^`]+`', '', text)
    # Remove code blocks
    text = re.sub(r'```[\s\S]*?```', '', text)
    # Count words
    words = text.split()
    return len(words)


def estimate_reading_time(word_count: int, wpm: int = 200) -> float:
    """
    Estimate reading time in minutes.
    
    Args:
        word_count: Number of words
        wpm: Words per minute (default: 200)
        
    Returns:
        Reading time in minutes
    """
    return word_count / wpm


def analyze_chapter(chapter_path: Path) -> Dict:
    """
    Analyze a single chapter directory.
    
    Args:
        chapter_path: Path to chapter directory
        
    Returns:
        Dictionary with chapter statistics
    """
    md_files = sorted(chapter_path.glob("*.md"))
    total_words = 0
    
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            total_words += count_words(content)
    
    return {
        'name': chapter_path.name,
        'files': len(md_files),
        'words': total_words,
        'reading_time': estimate_reading_time(total_words)
    }


def analyze_book(chapters_dir: Path) -> Tuple[List[Dict], Dict]:
    """
    Analyze all chapters in the book.
    
    Args:
        chapters_dir: Path to chapters directory
        
    Returns:
        Tuple of (list of chapter stats, overall stats)
    """
    chapter_dirs = sorted([d for d in chapters_dir.iterdir() if d.is_dir()])
    chapter_stats = []
    
    for chapter_dir in chapter_dirs:
        stats = analyze_chapter(chapter_dir)
        chapter_stats.append(stats)
    
    total_words = sum(ch['words'] for ch in chapter_stats)
    total_files = sum(ch['files'] for ch in chapter_stats)
    
    overall = {
        'chapters': len(chapter_stats),
        'files': total_files,
        'words': total_words,
        'reading_time': estimate_reading_time(total_words)
    }
    
    return chapter_stats, overall


def print_stats(chapter_stats: List[Dict], overall: Dict):
    """
    Print statistics in a formatted table.
    
    Args:
        chapter_stats: List of chapter statistics
        overall: Overall book statistics
    """
    print("\n" + "="*70)
    print("BOOK CONTENT STATISTICS")
    print("="*70)
    
    if chapter_stats:
        print("\nCHAPTER DETAILS:")
        print("-"*70)
        print(f"{'Chapter':<30} {'Files':>8} {'Words':>10} {'Time (min)':>12}")
        print("-"*70)
        
        for stats in chapter_stats:
            print(f"{stats['name']:<30} {stats['files']:>8} "
                  f"{stats['words']:>10} {stats['reading_time']:>12.1f}")
    
    print("-"*70)
    print(f"{'TOTAL':<30} {overall['files']:>8} "
          f"{overall['words']:>10} {overall['reading_time']:>12.1f}")
    print("="*70)
    print(f"\nEstimated reading time: {overall['reading_time']:.0f} minutes "
          f"({overall['reading_time']/60:.1f} hours)")
    print()


def main():
    """Main function."""
    # Get project root (parent of scripts directory)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    chapters_dir = project_root / "docs"
    
    if not chapters_dir.exists():
        print(f"Chapters directory not found: {chapters_dir}")
        print("Creating chapters directory...")
        chapters_dir.mkdir(parents=True, exist_ok=True)
        print("No chapters to analyze yet.")
        return
    
    chapter_stats, overall = analyze_book(chapters_dir)
    
    if not chapter_stats:
        print("No chapters found in docs directory.")
        return
    
    print_stats(chapter_stats, overall)


if __name__ == "__main__":
    main()

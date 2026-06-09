#!/usr/bin/env python3
"""
SEO URL Slug Generator - Convert any title into a clean, search-engine-friendly slug.
Usage:
    python slugify.py "My Title Here"
    python slugify.py --file titles.txt
    python slugify.py --demo
"""

import re
import sys
from pathlib import Path

# ========== CONFIGURATION (change these if you like) ==========
SEPARATOR = '-'            # hyphen is best for SEO
LOWERCASE = True
REMOVE_STOPWORDS = True    # removes a, an, the, of, for, etc.
MAX_LENGTH = 60            # Google truncates after ~60 chars
# ===============================================================

# Common stop words (articles, conjunctions, prepositions)
STOP_WORDS = {
    'a', 'an', 'and', 'the', 'of', 'for', 'to', 'in', 'on', 'at', 'with', 'by',
    'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
    'having', 'do', 'does', 'did', 'doing', 'but', 'or', 'so', 'nor', 'yet',
    'up', 'down', 'out', 'off', 'over', 'under', 'again', 'further', 'then',
    'once', 'here', 'there', 'all', 'any', 'both', 'each', 'few', 'more',
    'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same',
    'than', 'that', 'these', 'those', 'through', 'until', 'unto', 'upon',
    'without', 'after', 'before', 'above', 'below', 'between', 'via'
}

def slugify(title: str) -> str:
    """Convert a title into an SEO-friendly slug."""
    # 1. Lowercase
    if LOWERCASE:
        title = title.lower()
    
    # 2. Remove punctuation & special chars (keep letters, numbers, spaces, hyphens)
    title = re.sub(r'[^\w\s-]', '', title)
    
    # 3. Split into words (spaces or hyphens)
    words = re.split(r'[-\s]+', title)
    
    # 4. Remove stop words (if enabled)
    if REMOVE_STOPWORDS:
        words = [w for w in words if w not in STOP_WORDS]
    
    # 5. Join with separator
    slug = SEPARATOR.join(words)
    
    # 6. Remove multiple consecutive separators
    slug = re.sub(rf'{re.escape(SEPARATOR)}+', SEPARATOR, slug)
    
    # 7. Trim leading/trailing separator
    slug = slug.strip(SEPARATOR)
    
    # 8. Truncate to max length (without breaking a word)
    if MAX_LENGTH > 0 and len(slug) > MAX_LENGTH:
        truncated = slug[:MAX_LENGTH]
        last_sep = truncated.rfind(SEPARATOR)
        if last_sep > 0:
            slug = truncated[:last_sep]
        else:
            slug = truncated
    
    return slug

def process_file(input_file: str, output_file: str = None):
    """Read titles from a text file (one per line) and convert to slugs."""
    input_path = Path(input_file)
    if not input_path.exists():
        print(f"❌ File not found: {input_file}")
        return
    
    with open(input_path, 'r', encoding='utf-8') as f:
        titles = [line.strip() for line in f if line.strip()]
    
    if not titles:
        print("❌ No titles found in file.")
        return
    
    slugs = [slugify(t) for t in titles]
    
    # Print to console
    print("\n📝 Results:")
    print("-" * 60)
    for orig, slug in zip(titles, slugs):
        print(f"{orig[:50]:<50} -> {slug}")
    print("-" * 60)
    
    # Save to file if output specified
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            for slug in slugs:
                f.write(slug + '\n')
        print(f"\n✅ Saved {len(slugs)} slugs to: {output_file}")
    else:
        # Auto-save to slugs_output.txt in same folder
        auto_output = input_path.parent / "slugs_output.txt"
        with open(auto_output, 'w', encoding='utf-8') as f:
            for slug in slugs:
                f.write(slug + '\n')
        print(f"\n✅ Slugs also auto-saved to: {auto_output}")

def demo():
    """Run a demo with example titles."""
    demo_titles = [
        "The 5 Best Python Libraries for SEO!",
        "How to Bake a Perfect Chocolate Cake",
        "What's New in Django 5.0?",
        "A Complete Guide to URL Slugs (with Examples)",
        "SEO Best Practices 2026 - The Ultimate Checklist"
    ]
    print("\n🎯 Demo: Converting example titles to SEO slugs\n")
    for title in demo_titles:
        print(f"📌 {title}")
        print(f"🔗 {slugify(title)}\n")

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    
    if sys.argv[1] == '--file':
        # Batch mode: python slugify.py --file titles.txt [--output out.txt]
        input_file = sys.argv[2]
        output_file = sys.argv[4] if len(sys.argv) > 4 and sys.argv[3] == '--output' else None
        process_file(input_file, output_file)
    elif sys.argv[1] == '--demo':
        demo()
    else:
        # Single title mode: python slugify.py "My Title"
        title = ' '.join(sys.argv[1:])
        print(slugify(title))

if __name__ == '__main__':
    main()
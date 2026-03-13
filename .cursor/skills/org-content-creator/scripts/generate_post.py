import os
import argparse
from datetime import datetime
import re
from pathlib import Path

def slugify(text):
    text = text.lower()
    return re.sub(r'[^a-z0-9]+', '-', text).strip('-')

def generate_post(target_dir, title, description, tags_str, author):
    dir_path = Path(target_dir)
    dir_path.mkdir(parents=True, exist_ok=True)
    
    slug = slugify(title)
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    filename = f"{date_str}-{slug}.md"
    filepath = dir_path / filename
    
    tags = [t.strip() for t in tags_str.split(',')] if tags_str else []
    tags_formatted = "\n".join([f"  - {t}" for t in tags])
    
    frontmatter = f"""---
title: "{title}"
description: "{description}"
pubDate: "{date_str}"
author: "{author}"
tags:
{tags_formatted}
---

<!-- Write your content below this line. Do not use an H1 tag. -->

"""
    
    if filepath.exists():
        print(f"⚠️ File {filepath} already exists. Aborting to prevent overwrite.")
        return
        
    with open(filepath, "w") as f:
        f.write(frontmatter)
        
    print(f"✅ Scaffolded new post at: {filepath}")
    print("You can now use the Cursor Write tool to append the actual content to this file.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scaffold a new markdown blog post with frontmatter")
    parser.add_argument("--dir", required=True, help="Target directory (e.g., src/content/blog)")
    parser.add_argument("--title", required=True, help="Post title")
    parser.add_argument("--desc", required=True, help="SEO Description (under 160 chars)")
    parser.add_argument("--tags", default="", help="Comma-separated tags")
    parser.add_argument("--author", default="System", help="Author name")
    
    args = parser.parse_args()
    
    generate_post(args.dir, args.title, args.desc, args.tags, args.author)
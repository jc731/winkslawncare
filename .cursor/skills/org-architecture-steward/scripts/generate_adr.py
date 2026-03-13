import os
import argparse
from datetime import datetime
import re
from pathlib import Path

def slugify(text):
    text = text.lower()
    return re.sub(r'[^a-z0-9]+', '-', text).strip('-')

def get_next_adr_number(docs_dir):
    if not docs_dir.exists():
        return 1
    
    max_num = 0
    for file in docs_dir.glob("*.md"):
        match = re.match(r'^(\d+)-', file.name)
        if match:
            num = int(match.group(1))
            if num > max_num:
                max_num = num
    return max_num + 1

def generate_adr(title, status, context, decision, rationale, consequences, alternatives=None):
    docs_dir = Path("docs/adr")
    if not docs_dir.exists():
        docs_dir = Path("docs/decisions")
        if not docs_dir.exists():
            docs_dir = Path("docs/adr")
            docs_dir.mkdir(parents=True, exist_ok=True)
            
    adr_num = get_next_adr_number(docs_dir)
    date_str = datetime.now().strftime("%Y-%m-%d")
    slug = slugify(title)
    
    filename = f"{adr_num:04d}-{slug}.md"
    filepath = docs_dir / filename
    
    consequences_list = "\n".join([f"- {c.strip()}" for c in consequences.split(",") if c.strip()])
    
    alternatives_section = ""
    if alternatives:
        alt_list = "\n".join([f"- {a.strip()}" for a in alternatives.split(",") if a.strip()])
        alternatives_section = f"## Alternatives Considered\n{alt_list}\n"
    
    content = f"""# {adr_num}. {title}

Date: {date_str}

## Status
{status}

## Context
{context}

## Decision
{decision}

## Rationale
{rationale}

{alternatives_section}
## Consequences
{consequences_list}
"""
    
    with open(filepath, "w") as f:
        f.write(content)
        
    print(f"ADR created successfully at: {filepath}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Architectural Decision Record (ADR)")
    parser.add_argument("--title", required=True, help="Title of the ADR")
    parser.add_argument("--status", default="Proposed", help="Status (e.g., Proposed, Accepted, Rejected)")
    parser.add_argument("--context", required=True, help="Context and problem statement")
    parser.add_argument("--decision", required=True, help="The decision that was made")
    parser.add_argument("--rationale", required=True, help="Reasoning behind the decision")
    parser.add_argument("--consequences", required=True, help="Comma-separated list of consequences")
    parser.add_argument("--alternatives", help="Comma-separated list of alternatives considered")
    
    args = parser.parse_args()
    
    generate_adr(
        args.title, 
        args.status, 
        args.context, 
        args.decision, 
        args.rationale, 
        args.consequences,
        args.alternatives
    )
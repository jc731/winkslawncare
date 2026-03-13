import os
import argparse
import re
import json

def extract_frontmatter(content):
    """Attempt to extract YAML frontmatter from markdown."""
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if match:
        yaml_str = match.group(1)
        data = {}
        for line in yaml_str.split('\n'):
            if ':' in line:
                key, val = line.split(':', 1)
                data[key.strip()] = val.strip().strip("'").strip('"')
        return data
    return {}

def extract_h1(content):
    """Extract the first H1 tag if no frontmatter title exists."""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1)
    return None

def analyze_directory(target_dir):
    if not os.path.exists(target_dir):
        return {"error": f"Directory {target_dir} not found."}
        
    results = {
        "total_files": 0,
        "articles": [],
        "tags": set()
    }
    
    for root, _, files in os.walk(target_dir):
        for file in files:
            if file.endswith(('.md', '.mdx')):
                results["total_files"] += 1
                filepath = os.path.join(root, file)
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    frontmatter = extract_frontmatter(content)
                    title = frontmatter.get('title') or extract_h1(content) or file
                    
                    # Try to extract tags/categories
                    tags = frontmatter.get('tags', '')
                    if tags:
                        if isinstance(tags, str):
                            # Handle simple comma-separated or list-like strings
                            tags = [t.strip().strip('[]"') for t in tags.split(',')]
                        for t in tags:
                            if t: results["tags"].add(t)
                            
                    results["articles"].append({
                        "title": title,
                        "file": file,
                        "description": frontmatter.get('description', 'No description')
                    })
                except Exception as e:
                    pass
                    
    # Convert set to list for JSON serialization
    results["tags"] = list(results["tags"])
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze project content directories")
    parser.add_argument("--target", required=True, help="Directory containing markdown/mdx content")
    
    args = parser.parse_args()
    
    print(f"Analyzing content in {args.target}...\n")
    analysis = analyze_directory(args.target)
    
    if "error" in analysis:
        print(f"⚠️ {analysis['error']}")
        print("Tip: Ask the user where their blog/content files are stored.")
    else:
        print(json.dumps(analysis, indent=2))
        print("\n---")
        print("Use this data to infer content gaps and generate a strategy.")
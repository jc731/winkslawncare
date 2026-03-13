import sys
import argparse
import re

def parse_diff(diff_text):
    files_changed = []
    current_file = None
    additions = 0
    deletions = 0
    
    for line in diff_text.split('\n'):
        if line.startswith('diff --git'):
            match = re.search(r' b/(.+)$', line)
            if match:
                current_file = match.group(1)
                files_changed.append(current_file)
        elif line.startswith('+') and not line.startswith('+++'):
            additions += 1
        elif line.startswith('-') and not line.startswith('---'):
            deletions += 1
            
    return {
        'files': files_changed,
        'additions': additions,
        'deletions': deletions
    }

def analyze_risk(parsed_diff, intent, strictness):
    risks = []
    
    # Check file types
    has_tests = any('test' in f or 'spec' in f for f in parsed_diff['files'])
    has_core = any('src/' in f or 'core/' in f for f in parsed_diff['files'])
    has_config = any(f.endswith('.json') or f.endswith('.yml') or f.endswith('.yaml') for f in parsed_diff['files'])
    
    if intent == 'feature' and not has_tests and strictness in ['medium', 'high']:
        risks.append("Feature added but no tests included.")
        
    if has_config and strictness == 'high':
        risks.append("Configuration files changed. Ensure no secrets are exposed and syntax is valid.")
        
    if parsed_diff['additions'] + parsed_diff['deletions'] > 500 and strictness != 'low':
        risks.append(f"Large diff ({parsed_diff['additions']} additions, {parsed_diff['deletions']} deletions). Consider breaking this up.")
        
    return risks

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze Git Diff for Risks")
    parser.add_argument("--file", help="Path to patch file. If not provided, reads from stdin.")
    parser.add_argument("--intent", choices=["feature", "bugfix", "refactor"], default="feature", help="Intent of the change")
    parser.add_argument("--strictness", choices=["low", "medium", "high"], default="medium", help="Review strictness")
    
    args = parser.parse_args()
    
    diff_text = ""
    if args.file:
        with open(args.file, 'r') as f:
            diff_text = f.read()
    else:
        diff_text = sys.stdin.read()
        
    if not diff_text.strip():
        print("No diff provided.")
        sys.exit(1)
        
    parsed = parse_diff(diff_text)
    risks = analyze_risk(parsed, args.intent, args.strictness)
    
    print("=== Diff Analysis ===")
    print(f"Files changed: {len(parsed['files'])}")
    for f in parsed['files'][:5]:
        print(f"  - {f}")
    if len(parsed['files']) > 5:
        print(f"  ... and {len(parsed['files']) - 5} more.")
        
    print(f"Additions: +{parsed['additions']}")
    print(f"Deletions: -{parsed['deletions']}")
    
    print("\n=== Identified Risks ===")
    if risks:
        for r in risks:
            print(f"- ⚠️ {r}")
    else:
        print("- ✅ No automated risks identified.")

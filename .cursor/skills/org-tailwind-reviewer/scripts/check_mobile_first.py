import os
import argparse
import re

def check_file_for_tailwind(filepath):
    warnings = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Simple heuristic: find className="..." or className={...}
            class_matches = re.finditer(r'className=["\']([^"\']+)["\']', content)
            
            for match in class_matches:
                classes = match.group(1).split()
                
                # Check for flex without flex-col or flex-wrap
                if 'flex' in classes and not any(c in classes for c in ['flex-col', 'flex-wrap', 'md:flex-row', 'sm:flex-row', 'lg:flex-row']):
                    # Check if it's explicitly a row that's safe, hard to know statically, but flag it
                    warnings.append(f"Line ?? : Found 'flex' without mobile-first column wrapping: {match.group(1)}")
                    
                # Check for fixed widths that might break 360px
                for c in classes:
                    if re.match(r'^w-\[(?P<val>\d+)px\]', c):
                        val = int(re.search(r'\d+', c).group())
                        if val > 350:
                            warnings.append(f"Line ?? : Found fixed width > 350px which breaks mobile: {c}")
                            
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        
    return warnings

def main():
    parser = argparse.ArgumentParser(description="Check Tailwind classes for mobile-first issues")
    parser.add_argument("--target", required=True, help="File or directory to scan")
    
    args = parser.parse_args()
    target = args.target
    
    files_to_check = []
    if os.path.isfile(target):
        files_to_check.append(target)
    elif os.path.isdir(target):
        for root, _, files in os.walk(target):
            if 'node_modules' in root:
                continue
            for f in files:
                if f.endswith(('.tsx', '.jsx', '.html', '.vue', '.svelte')):
                    files_to_check.append(os.path.join(root, f))
                    
    print(f"Scanning {len(files_to_check)} files for Tailwind mobile-first issues...")
    
    total_warnings = 0
    for f in files_to_check:
        warnings = check_file_for_tailwind(f)
        if warnings:
            print(f"\n[File: {f}]")
            for w in warnings:
                print(f"  - ⚠️ {w}")
                total_warnings += 1
                
    if total_warnings == 0:
        print("\n✅ No obvious mobile-first issues found.")
    else:
        print(f"\nFound {total_warnings} potential issues. Please review manually.")

if __name__ == "__main__":
    main()
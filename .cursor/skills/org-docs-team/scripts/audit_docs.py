import os
import argparse
import glob
from pathlib import Path

def find_env_vars_in_code(repo_path):
    env_vars = set()
    for root, _, files in os.walk(repo_path):
        if 'node_modules' in root or '.git' in root or 'venv' in root:
            continue
        for file in files:
            if file.endswith(('.js', '.ts', '.py', '.go')):
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Very simple heuristic for finding process.env.VAR or os.environ['VAR']
                        import re
                        js_matches = re.findall(r'process\.env\.([A-Z0-9_]+)', content)
                        py_matches = re.findall(r'os\.environ(?:\[["\']|\.get\(["\'])([A-Z0-9_]+)', content)
                        env_vars.update(js_matches)
                        env_vars.update(py_matches)
                except Exception:
                    pass
    return env_vars

def check_env_example(repo_path, found_vars):
    example_path = os.path.join(repo_path, '.env.example')
    if not os.path.exists(example_path):
        return found_vars # All are missing
        
    missing = set()
    try:
        with open(example_path, 'r', encoding='utf-8') as f:
            content = f.read()
            for var in found_vars:
                if var not in content:
                    missing.add(var)
    except Exception:
        return found_vars
    return missing

def main():
    parser = argparse.ArgumentParser(description="Audit documentation based on scope indicators.")
    parser.add_argument("--repo-path", default=".", help="Path to repository")
    parser.add_argument("--scope-indicators", default="", help="Comma-separated scope indicators")
    
    args = parser.parse_args()
    scopes = [s.strip() for s in args.scope_indicators.split(',') if s.strip()]
    
    print("=== Documentation Audit ===")
    
    if "new_config_or_env_var" in scopes:
        print("\n[Checking Environment Variables]")
        found_vars = find_env_vars_in_code(args.repo_path)
        missing_vars = check_env_example(args.repo_path, found_vars)
        if missing_vars:
            print("⚠️ The following env vars were found in code but might be missing from .env.example:")
            for v in sorted(missing_vars):
                print(f"  - {v}")
        else:
            print("✅ .env.example appears up-to-date with code.")
            
    if "new_or_changed_api" in scopes:
        print("\n[API Documentation]")
        print("⚠️ API changes indicated. Please manually verify OpenAPI specs, Postman collections, or API.md.")
        
    if "onboarding_impact" in scopes:
        print("\n[Onboarding]")
        print("⚠️ Onboarding changes indicated. Please verify README.md setup steps.")
        
    if not scopes:
        print("\nNo specific scope indicators provided. Consider running with --scope-indicators")
        print("Available: new_or_changed_api, new_config_or_env_var, data_shape_or_cache_change, onboarding_impact")

if __name__ == "__main__":
    main()
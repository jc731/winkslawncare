import json
import os
import argparse
from pathlib import Path

DEFAULT_PREFERENCES = {
    "strictness": "high",
    "ask_before": ["breaking_change", "security_sensitive", "schema_migration", "unknown_requirements"]
}

def get_preferences_path():
    # Try mcp/preferences.json first, then fallback to .cursor/org-preferences.json
    paths = [
        Path("mcp/preferences.json"),
        Path(".cursor/org-preferences.json")
    ]
    for p in paths:
        if p.exists():
            return p
    return paths[1] # Default to .cursor/org-preferences.json

def get_preferences():
    path = get_preferences_path()
    if path.exists():
        try:
            with open(path, "r") as f:
                prefs = json.load(f)
                # Merge with defaults to ensure all keys exist
                merged = DEFAULT_PREFERENCES.copy()
                merged.update(prefs)
                return merged
        except json.JSONDecodeError:
            print(f"Error reading {path}. Using defaults.")
    return DEFAULT_PREFERENCES

def set_preferences(strictness=None, ask_before=None):
    prefs = get_preferences()
    if strictness:
        prefs["strictness"] = strictness
    if ask_before is not None:
        prefs["ask_before"] = [item.strip() for item in ask_before.split(",")]
    
    path = get_preferences_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, "w") as f:
        json.dump(prefs, f, indent=2)
    
    print(f"Preferences saved to {path}")
    print(json.dumps(prefs, indent=2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manage Org Preferences")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    get_parser = subparsers.add_parser("get", help="Get current preferences")
    
    set_parser = subparsers.add_parser("set", help="Set preferences")
    set_parser.add_argument("--strictness", choices=["low", "medium", "high"], help="Strictness level")
    set_parser.add_argument("--ask_before", help="Comma-separated list of ask_before triggers")
    
    args = parser.parse_args()
    
    if args.command == "get":
        print(json.dumps(get_preferences(), indent=2))
    elif args.command == "set":
        set_preferences(args.strictness, args.ask_before)
    else:
        parser.print_help()
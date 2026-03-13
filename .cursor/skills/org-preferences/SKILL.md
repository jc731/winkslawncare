---
name: org-preferences
description: Gets or sets organizational preferences (strictness, ask_before). Use when the user asks to change or view policy strictness, approval triggers, or org preferences; or when another skill needs current preferences (e.g. orchestrator, senior-dev).
---

# Org Preferences

## Quick Start

This skill owns **getting** (read) and **setting** (update and persist) organizational preferences. Storage: `mcp/preferences.json` in the project repository.

1. **Get**: Read current strictness and ask_before so other workflows (e.g. orchestrator, senior-dev) can apply policy.
2. **Set**: Update one or both of strictness and ask_before; merge with existing; persist to `mcp/preferences.json` per tool or merge rules.

## Getting Preferences

**When org-controller MCP is available**, call:
- **Tool**: `org_get_preferences`
- **Optional**: Pass `project_preferences` if you have already read `mcp/preferences.json` (e.g. from a prior read of the file).

**Without MCP**: Read `mcp/preferences.json` from the project; if missing or invalid, use defaults (e.g. `strictness`: `"high"`, `ask_before`: `["breaking_change", "security_sensitive", "schema_migration", "unknown_requirements"]` or `[]`).

## Setting Preferences

**When org-controller MCP is available**, call:
- **Tool**: `org_set_preferences`
- **Parameters**: `strictness` (optional), `ask_before` (optional). To merge with current state, pass `project_preferences` with the current file contents.
- The tool returns updated preferences and guidance; write the result to `mcp/preferences.json` in the project.

**Without MCP**: Merge the requested keys with existing preferences (read from `mcp/preferences.json` if present), then write the merged object to `mcp/preferences.json`. Do not overwrite with only partial keys without merging.

## Schema

- **strictness**: `"low"` | `"medium"` | `"high"` — policy enforcement level.
- **ask_before**: array of strings — trigger types that require explicit user approval before proceeding. Common values: `breaking_change`, `security_sensitive`, `schema_migration`, `unknown_requirements`.

## When to Involve Other Skills

- **After updating preferences**, if the user wants to run a plan or workflow with the new policy → **org-orchestrator** (or MCP `org_run` with the new preferences).
- **Vague request** about "how we approve things" or "policy" → **org-receptionist** to route.

## Constraints

- Preferences are project-scoped; persist under `mcp/preferences.json`.
- Do not overwrite with only partial keys unless merging (set merges with existing).

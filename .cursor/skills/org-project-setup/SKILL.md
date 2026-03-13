---
name: org-project-setup
description: Sets up Cursor rules and project-specific config for a project in the workspace. Discovers README, docs, and key files first, then generates .cursor/rules from a template. Org preferences (strictness, ask_before) are for skills to reference and live at org level—use org-preferences skill; this skill does not create preferences or mcp/ in projects.
---

# Org Project Setup

## Quick Start

This skill configures a **project** (a folder in the workspace that is a distinct app or repo) with Cursor rules and optional org preferences. It does **not** write rules from scratch blindly: it **discovers** the project first, **confirms** with the user, then **generates** rules using a template with defaults.

1. **Identify project root**: The folder to set up (e.g. `accension-order-form`, `gailrogers`, or a path the user names).
2. **Discover**: Read README, docs, and key files in that project (see Discovery sources).
3. **Confirm**: Summarize what was found (stack, conventions, docs) and get user confirmation before writing.
4. **Generate**: Merge the default template with discovered context; write `.cursor/rules/` under the project root. Do **not** create `mcp/` or any preferences file in the project—org preferences are used by skills and live at org level; use **org-preferences** to read or update them.

Never overwrite existing `.cursor/rules/` without explicit user confirmation. If the user says "use defaults" or "overwrite", then proceed.

---

## Workflow

### Step 1: Discover

Read the following in the **project root** (adjust paths if the project uses different layout):

| Priority | Source | Purpose |
|----------|--------|---------|
| 1 | `README.md`, `README` (or `docs/README.md`) | Project name, purpose, stack, conventions, scripts |
| 2 | `docs/` | Any `.md` or `.mdx` (architecture, contributing, style guides) |
| 3 | `package.json` | Name, scripts, dependencies (framework, lang, tooling) |
| 4 | `tsconfig.json`, `jsconfig.json`, `astro.config.*`, `vite.config.*`, etc. | Build stack, paths, strictness |
| 5 | `.cursor/rules/*.mdc` (if present) | Existing rules to preserve or merge |

Infer: **project name**, **stack** (e.g. Astro, React, Vue, Node), **conventions** (file structure, testing, lint), **docs that define standards**.

### Step 2: Summarize and confirm

Present a short summary to the user:

```markdown
## Project setup: [project root]

**Discovered:**
- Name / purpose: [from README]
- Stack: [from package.json + configs]
- Conventions: [from README or docs]
- Existing .cursor/rules: [yes/no]

**Planned writes:**
- [ ] .cursor/rules/project-context.mdc (org + project-specific)
- [ ] .cursor/rules/[stack]-conventions.mdc (optional, from stack)

Confirm to generate, or say what to change. (Org preferences are at org level; use **org-preferences** skill—this setup does not create preferences in the project.)
```

If the user wants changes (e.g. different rules, skip preferences), adjust the plan. Only proceed to generate after explicit confirmation (or clear "go ahead" / "use defaults").

### Step 3: Generate

- Use the **default template** in [templates/default-org-context.mdc](templates/default-org-context.mdc) as the base for the main rule.
- Replace placeholders with discovered (and user-corrected) values:
  - `{{PROJECT_NAME}}`: project or repo name
  - `{{STACK_SUMMARY}}`: e.g. "Astro + Tailwind", "React + TypeScript"
  - `{{CONVENTIONS_SUMMARY}}`: 1–3 sentences from README/docs (paths, components, tests)
- Write files **under the project root**:
  - `.cursor/rules/project-context.mdc` (or a name that matches the project; `alwaysApply: true` for org + project context).
  - Optionally a second rule with `globs` for the main codebase (e.g. `**/*.astro`, `**/*.tsx`) if stack-specific conventions are documented.
- Do **not** create `mcp/` or `preferences.json` in the project. Org preferences (strictness, ask_before) are for skills to reference and are managed at org level via **org-preferences**.
- If the project already had `.cursor/rules/`, merge: keep existing rule files unless the user asked to replace; add or update only the project-context rule as needed.

---

## Discovery sources (reference)

- **README**: Project name, description, setup, scripts, coding/convention notes.
- **docs/**: Architecture, ADRs, contributing, style guides, API docs.
- **package.json**: `name`, `scripts`, `dependencies` / `devDependencies` (framework, linter, formatter, test runner).
- **Config files**: `tsconfig.json` (paths, strict), `astro.config.*`, `vite.config.*`, `tailwind.config.*` → stack and paths.
- **Existing .cursor**: Avoid deleting; merge or add.

For full template contents and placeholder list, see [templates/default-org-context.mdc](templates/default-org-context.mdc) and [reference.md](reference.md).

---

## When to involve other skills

- **Unclear which folder is the "project"** (multi-repo workspace) → **org-receptionist** to clarify, or list workspace roots and ask user to pick.
- **After writing rules**, user wants to change org policy (strictness, ask_before) → **org-preferences** (reads/writes org-level preferences used by skills).
- **Project needs a full plan** (features, ADRs, risk) → **org-orchestrator** and **org-architecture-steward** as appropriate.

---

## Constraints

- All generated paths are relative to the **project root** (the folder being set up).
- Do not create `.cursor/rules/` outside the project root. Do not create `mcp/` or preferences files in any project.
- Template defaults must be overridden by discovered content where applicable; do not leave placeholders in final files.

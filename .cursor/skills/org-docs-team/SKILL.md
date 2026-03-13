---
name: org-docs-team
description: Executes documentation finalization or audits existing docs based on scope indicators. Use when PRs merge, new features are completed, or when the user asks for a documentation audit.
---

# Org Docs Team

## Quick Start

The Docs Team ensures documentation stays up-to-date with codebase changes. It operates in two main modes:
- **Mode A (Finalization)**: Post Dev/QA, when a feature or bugfix is completed.
- **Mode B (Audit)**: Refreshing and verifying existing docs.

## Workflows

### Mode A: Finalization
1. Identify the scope of the completed change (e.g., new API, new env var, data shape change).
2. Run the `audit_docs.py` script to identify potentially stale files based on the recent changes.
3. Update relevant documentation (README, API docs, comments).
4. Do NOT mark a task as fully complete until docs are updated.

### Mode B: Audit
1. Run a comprehensive sweep of a directory using the utility script.
2. Check for missing code comments, outdated setup instructions, or missing env vars.

## Scope Indicators

Determine documentation rigor based on:
- `new_or_changed_api`: Requires API doc updates.
- `new_config_or_env_var`: Requires `.env.example` and setup doc updates.
- `data_shape_or_cache_change`: Requires schema doc updates.
- `onboarding_impact`: Requires README or setup guide review.

## When to Involve Other Skills

- **Vague or unclear doc request** → **org-receptionist** (or MCP `org_receptionist`) to route.
- **Audit finds architecture or risk gaps** (e.g. undocumented security or architectural assumptions) → Use **org-feedback-loop** (e.g. `docs_to_architecture_risk`) so **org-architecture-steward** or **org-risk-assessor** can address.
- **Finalizing after a feature** → Prefer **org-qa-team** sign-off first when quality gates apply; if code quality or review is in question, recommend **org-senior-dev** for a diff review before marking complete.
- **Documenting risk or mitigation decisions** → Align with **org-risk-assessor** (risk Decision Records) or **org-architecture-steward** (ADRs).
- **Content or blog strategy** is missing or stale (e.g. no content calendar) → Suggest **org-content-strategist** to build a backlog; **org-content-creator** to write specific pieces.

## Using the Utility Script

Run the audit script to find out which files might need your attention:

```bash
python scripts/audit_docs.py --repo-path . --scope-indicators "new_or_changed_api,new_config_or_env_var"
```

The script will scan for undocumented environment variables or highlight docs that haven't been touched recently compared to source files.

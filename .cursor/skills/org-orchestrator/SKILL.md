---
name: org-orchestrator
description: Acts as the project manager. Normalizes requests, enforces organizational policies (ask_before triggers like breaking changes), and builds structured plans. Use when a user asks for a task that requires organizational policy enforcement or when they start a new complex request.
---

# Org Orchestrator

## Quick Start

The orchestrator normalizes incoming requests, checks against organizational preferences, and builds structured plans.

1. **Understand the Request**: Determine if it's a feature, bugfix, refactor, or question.
2. **Check Preferences**: Get current policies via **org-preferences** or MCP `org_get_preferences` (or `manage_preferences.py get` if the script exists). Preference ownership (get/set) lives in **org-preferences**.
3. **Enforce Policies**: If the request triggers an `ask_before` policy (e.g., breaking change, security sensitive, schema migration), ask the user for explicit approval before proceeding.
4. **Build Plan**: Formulate a structured plan with acceptance criteria based on the request and policies. For frontend or UI work that involves new or refactored components, the plan should call out that component boundaries and structure follow the **component-philosophy** skill (e.g., "when implementing, apply component-philosophy to decide what should be its own component").

## When to Involve Other Skills

Route work and call out these skills in the plan so the right expertise is applied:

- **Vague or unclear request** → **org-receptionist** (or MCP `org_receptionist`) to route the query to the right workflow.
- **Code or PR review** → **org-senior-dev** (strictness-based diff review). For Tailwind/React/Next/Nuxt UI changes, also **org-tailwind-reviewer** for mobile-first checks.
- **Stack choice, technology decision, or formal ADR** → **org-architecture-steward**; for risk and tradeoff analysis involve **org-risk-assessor**.
- **Risk assessment, tradeoffs, or mitigation guidance** → **org-risk-assessor**.
- **Documentation** after a feature/PR or doc audit → **org-docs-team** (finalization or audit). Plan should call for **org-qa-team** sign-off before docs when quality gates apply.
- **Blog ideas, content calendar, what to write next** → **org-content-strategist**; **org-content-creator** to write a specific post.
- **Cross-domain issues** (e.g. code fixed but docs not updated, or implementation violates an ADR) → **org-feedback-loop** to create an artifact and hand off to the right skill.
- **QA sign-off** before documentation phase → **org-qa-team** (verify acceptance criteria, quality gates, then hand off to **org-docs-team**).
- **Change or view org preferences (strictness, ask_before)** → **org-preferences** (or MCP `org_get_preferences` / `org_set_preferences`). Orchestrator consumes preferences when building plans; preference updates are done via org-preferences.

## Workflow

1. Get current preferences via **org-preferences** or MCP `org_get_preferences` (or `manage_preferences.py get` if the script is present).
2. Compare the user's request against the `ask_before` list and the `strictness` level.
3. If an approval is required, halt and ask the user.
4. If approved or no approval is required, return a structured plan to the user.

## Updating Preferences

When the user asks to update preferences, use **org-preferences** or MCP `org_set_preferences`; persist to `mcp/preferences.json` per returned guidance. If a script exists (`manage_preferences.py set`), it may be used as fallback.

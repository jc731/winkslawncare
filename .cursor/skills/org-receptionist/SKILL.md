---
name: org-receptionist
description: Routes vague or unclear user requests to the appropriate org-control skill or MCP tool. Use when the user's intent is ambiguous, the request spans multiple concerns, or you need to recommend which org workflow or skill to invoke.
---

# Org Receptionist

## Quick Start

The Receptionist analyzes user intent and directs the request to the right org skill or MCP tool. It does not execute the work; it routes and recommends.

1. **Parse the request**: Identify type (feature, bugfix, review, docs, content, risk, stack, etc.) and whether it is vague or multi-part.
2. **Route**: When org-controller MCP is available, call **org_receptionist** with the user's query for guided routing. Otherwise use the routing table below.
3. **Recommend**: Tell the user which skill(s) to invoke and in what order (e.g. "Use **org-orchestrator** to build a plan, then **org-qa-team** for sign-off before docs.").

## When to Use This Skill

- User request is vague or high-level ("I want to improve the app", "help with the project").
- Request could be handled by several skills and the right sequence is unclear.
- User asks "who should do this?" or "what workflow should I use?".
- After an escalation or feedback artifact, to decide which skill should act next.

## Routing Table (when MCP is not used or to double-check)

| User intent / keywords | Primary skill(s) | Notes |
|------------------------|------------------|--------|
| New feature, bugfix, refactor, complex task, "plan this", policy/approval | **org-orchestrator** | Normalize request, build plan, enforce ask_before |
| Change policy, strictness, ask_before, org preferences, approval triggers | **org-preferences** | Get or set org preferences; then **org-orchestrator** if user wants to run a workflow with new policy |
| Code review, PR review, patch review, diff review | **org-senior-dev** | Strictness-based diff review |
| Tailwind, mobile, responsive, breakpoints, 360px | **org-tailwind-reviewer** | Mobile-first Tailwind review |
| Stack choice, tech recommendation, ADR, decision record | **org-architecture-steward** | Stack + ADR; involve **org-risk-assessor** for risk |
| Risk assessment, tradeoffs, failure modes, mitigation | **org-risk-assessor** | Risk + risk Decision Records |
| Docs after feature/PR, doc audit, finalize docs | **org-docs-team** | Finalization or audit |
| Blog ideas, content calendar, what to write | **org-content-strategist** | Then **org-content-creator** for specific posts |
| Write a blog post, draft an article | **org-content-creator** | Refer to **org-content-strategist** if no topic |
| Cross-domain issue, QA found doc gap, code violates ADR | **org-feedback-loop** | Create artifact; then target **org-docs-team**, **org-senior-dev**, **org-architecture-steward**, or **org-risk-assessor** |
| QA, acceptance criteria, sign-off, test review | **org-qa-team** | Before docs phase; creates qa_to_documentation artifacts |
| Component structure, split/combine components, layout vs content | **component-philosophy** | Often used by **org-senior-dev** or **org-tailwind-reviewer** |

## MCP Integration

**When org-controller MCP is available**, call:
- **Tool**: `org_receptionist`
- **Argument**: `query` — the user's vague or unclear request (string).

The MCP returns guidance on which tool to use. Follow that and/or reinforce with the routing table above when suggesting next steps.

## When to Involve Other Skills

- After routing, the **primary** skill does the work. Receptionist only routes.
- If the chosen skill suggests another (e.g. orchestrator plan calls for QA → **org-qa-team**), the user or agent invokes that skill; receptionist does not need to be invoked again unless the request becomes vague again.
- For "risk + architecture" decisions, recommend **org-architecture-steward** and **org-risk-assessor** together (steward for ADR, risk assessor for risk assessment and risk Decision Records).

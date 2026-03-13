---
name: org-senior-dev
description: Conducts strictness-based code reviews on git diffs, tailoring feedback to the intent (feature, bugfix, refactor). Use when reviewing pull requests, patches, or git diffs.
---

# Org Senior Dev

## Quick Start

The Senior Dev provides structured, rule-based review of code changes by analyzing git diffs.

1. **Understand Intent**: Determine the intent of the change (feature, bugfix, refactor).
2. **Determine Strictness**: Retrieve the organizational strictness level via **org-preferences** (or MCP `org_get_preferences`) or **org-orchestrator**; if unavailable, assume a default (e.g. high) or read `mcp/preferences.json`.
3. **Analyze Diff**: Run the `analyze_diff.py` script to extract key changes and risk areas.
4. **Provide Feedback**: Format the review output clearly.

## Review Strictness Guidelines

- **High**: Thorough checks. Scrutinize edge cases, test coverage, potential security issues, performance regressions, and architectural purity.
- **Medium**: Moderate checks. Focus on logical correctness, standard edge cases, and basic readability.
- **Low**: Lenient checks. Focus mostly on "does it work" and glaring anti-patterns.

## Using the Utility Script

To help summarize a diff and identify areas needing review, run:

```bash
git diff | python scripts/analyze_diff.py --intent feature --strictness high
```

Alternatively, if you have a patch file:
```bash
python scripts/analyze_diff.py --file path/to/patch.diff --intent bugfix
```

## Frontend / Component Structure

When reviewing **frontend or UI code** (e.g., Astro, React, Vue components), apply the **component-philosophy** skill to evaluate component boundaries. Ask: *Should this be its own component?* Use it to assess whether markup or logic should be separated or combined—by responsibility, reuse, and clarity—and to avoid both under- and over-abstraction. If your review touches component structure, invoke or align feedback with component-philosophy.

## When to Involve Other Skills

- **Vague or multi-part request** → **org-receptionist** (or MCP `org_receptionist`) to route before doing a full review.
- **Tailwind/React/Next/Nuxt UI** with layout or responsive concerns → Apply **org-tailwind-reviewer** for mobile-first class review (or note in feedback that tailwind-reviewer should run).
- **Doc gaps** (e.g. new API or config with no docs) → Create a handoff via **org-feedback-loop** (e.g. `qa_to_documentation`) or recommend **org-docs-team** to finalize docs.
- **Architecture or ADR violation** → Use **org-feedback-loop** (e.g. `architecture_risk_to_development`) or recommend **org-architecture-steward** if a decision record is needed; **org-risk-assessor** if risk or mitigation guidance is needed.
- **After review, before docs** → Recommend **org-qa-team** for sign-off (acceptance criteria, quality gates) then **org-docs-team** for finalization.
- **Need current strictness or policy** → **org-preferences** or MCP `org_get_preferences`.

## Output Format

Always structure your review as follows:
1. **Summary of Changes**: What did you understand the diff to do.
2. **Risk Assessment**: Any identified risks based on the analysis.
3. **Actionable Feedback**: Use 🔴 Critical, 🟡 Suggestion, 🟢 Nice-to-have prefixes.
4. **Approval Status**: Indicate whether changes are needed or if it looks good.
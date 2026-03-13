---
name: org-architecture-steward
description: Recommends tech stacks based on constraints and generates Architectural Decision Records (ADRs). Use when the user asks for technology recommendations, stack choices, or requests a formal decision record.
---

# Org Architecture Steward

## Quick Start

The Architecture Steward provides informed technology recommendations and formalizes decisions through Architectural Decision Records (ADRs).

1. **Stack Recommendations**: When a user asks for a stack choice, evaluate the constraints (budget, timeline, team size, scale) and recommend appropriate technologies.
2. **Generating ADRs**: When a decision is made, execute the ADR generation script to formalize it.

## Stack Recommendation Guidelines
- Prioritize boring, battle-tested technologies for standard use cases.
- Call out trade-offs clearly (e.g., development speed vs. scalability).
- Ensure the stack aligns with the project's preferences (if any). Project preferences (e.g. strictness, ask_before) can be read via **org-preferences** or MCP `org_get_preferences` so stack advice aligns with org policy.

## When to Involve Other Skills

- **Vague or unclear stack/decision request** → **org-receptionist** (or MCP `org_receptionist`) to route.
- **Frontend or UI stack / structure** (e.g. component architecture, Astro vs React) → Apply or reference **component-philosophy** so recommendations align with responsibility-based component design.
- **Risk or tradeoff analysis** for a decision → **org-risk-assessor** (collaborate on risk assessment and risk Decision Records; steward owns ADRs, risk assessor owns risk-focused records).
- **After a decision is recorded** → Recommend **org-docs-team** to update docs (README, ADR index, or setup guides) so the decision is discoverable.
- **Decision needs to be acted on by development** (e.g. "all new UI must follow this pattern") → Use **org-feedback-loop** (e.g. `architecture_risk_to_development`) so the artifact routes to **org-senior-dev** or **org-risk-assessor** as appropriate.

## Generating Decision Records

When a decision is reached, run the `generate_adr.py` script to scaffold the document:

```bash
python scripts/generate_adr.py \
  --title "Choosing PostgreSQL for the user database" \
  --decision "Use PostgreSQL" \
  --status "Accepted" \
  --context "We need a relational database to store user credentials and profile data." \
  --rationale "ACID guarantees, JSON support, and excellent performance for our use case." \
  --consequences "Team needs PostgreSQL expertise, Requires connection pooling setup"
```

This will generate an ADR in `docs/adr/` (or `docs/decisions/`). Ask the user to review the generated file.
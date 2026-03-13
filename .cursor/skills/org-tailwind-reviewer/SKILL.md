---
name: org-tailwind-reviewer
description: Specializes in mobile responsiveness for Tailwind projects, ensuring mobile-first utility classes are correctly applied. Use when reviewing UI changes, specifically in React/Next/Nuxt projects using Tailwind CSS.
---

# Org Tailwind Mobile Reviewer

## Quick Start

The Tailwind Mobile Reviewer focuses purely on mobile readiness (360-390px viewports) in Tailwind CSS codebases. 

1. **Check Configuration**: Verify the project uses Tailwind.
2. **Scan Classes**: Ensure components follow the mobile-first paradigm (e.g., base classes for mobile, `md:` or `lg:` for desktop).
3. **Run Utility Script**: Use the python script to scan files for potentially problematic flex/grid layouts lacking mobile consideration.

## Core Rules
- Base utility classes (no prefix) represent mobile.
- Never use `flex` or `grid` without considering mobile wrapping. If a row is used, check if it overflows on mobile.
- Use `flex-col` by default, and `md:flex-row` for larger screens unless it fits side-by-side on 360px width.
- Padding on containers should typically be `p-4` on mobile, scaling up to `md:p-8`.

## Component Boundaries

When your review suggests that layout or repeated patterns might warrant a **different component structure** (e.g., "this should be a layout component" or "this pattern repeats—consider a composite"), apply or reference the **component-philosophy** skill. Use it to decide whether something should be its own component before recommending class changes alone.

## When to Involve Other Skills

- **Vague or multi-part UI request** → **org-receptionist** (or MCP `org_receptionist`) to route.
- **Broader code review** (logic, security, tests, not just layout) → Recommend or defer to **org-senior-dev** for full diff review.
- **Full QA sign-off** (acceptance criteria, tests, then docs) → **org-qa-team**; Tailwind review can be one input to that process.
- **Structural or technical-debt risk** from layout choices → **org-risk-assessor** or **org-feedback-loop** (`docs_to_architecture_risk`) if it affects architecture/risk.
- **Doc or architecture impact** from UI changes (e.g. new breakpoints or patterns to document) → **org-feedback-loop** or **org-docs-team** as appropriate.

## Using the Utility Script

Run the following script to identify layout classes that might break on mobile:

```bash
python scripts/check_mobile_first.py --target src/components/
```

This script will output warnings for files that have `flex` but no `flex-col` or `flex-wrap`, or `w-full` without max-width constraints.

## Output Format
When returning your review:
1. Provide the file path and specific line numbers.
2. Show the "Before" (problematic) classes.
3. Show the "After" (fixed) classes.
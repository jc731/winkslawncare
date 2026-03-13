---
name: org-seo-reviewer
description: Reviews pages and markup for on-page SEO (meta tags, headings, URLs, alt text, structure). Use when the user asks for an SEO review, wants pages checked for search readiness, or mentions meta titles, descriptions, or heading structure.
---

# Org SEO Reviewer

## Quick Start

The SEO Reviewer focuses on on-page SEO: meta tags, heading hierarchy, URLs, image alt text, and basic crawlability. It does not replace keyword research or content strategy.

1. **Identify scope**: Page(s), layout(s), or route(s) to review (e.g. `src/pages/*.astro`, `src/layouts/BaseLayout.astro`).
2. **Run checklist**: Apply the rules below to the provided files.
3. **Report**: Use the output format with severity and concrete fixes.

## Review Checklist

### Meta & document head
- **Title**: Unique per page; 50–60 characters; includes primary keyword where natural.
- **Meta description**: Unique per page; 150–160 characters; actionable or descriptive, no keyword stuffing.
- **Canonical**: Set when duplicate content or multiple URLs could target the same content.
- **Robots**: No accidental `noindex` on pages that should be indexed (e.g. main landing, key content).

### Headings
- **H1**: Exactly one per page; describes the page topic; avoid generic "Home" or "Welcome" alone.
- **Hierarchy**: Logical order (H1 → H2 → H3); no skipped levels (e.g. no H2 after H4).

### URLs
- Short, readable, lowercase; hyphens for word separation; key topic in path when possible (e.g. `/blog/my-post` not `/p/123`).

### Images & media
- **Alt text**: Present and descriptive for meaningful images; decorative images use empty `alt=""` or equivalent.
- **File names**: Descriptive when possible (e.g. `product-name.jpg` not `IMG_001.jpg`).

### Content & links
- **Internal links**: Key pages linked from homepage or main nav; anchor text descriptive, not "click here."
- **First paragraph**: Main topic or primary keyword appears early in the main content where it fits naturally.

### Technical (when visible in scope)
- **Structured data**: If the project uses JSON-LD or similar, validate required fields and avoid invalid or empty objects.
- **Mobile**: Page is usable on small viewports (layout/UX); defer deep mobile audit to **org-tailwind-reviewer**.

## Output Format

For each finding:

1. **Location**: File path and line or section (e.g. `src/pages/index.astro`, `<title>`).
2. **Finding**: What is wrong or missing.
3. **Severity**: Critical | High | Medium | Low.
4. **Suggestion**: Concrete change (e.g. suggested title text, alt text, or heading rewrite).

Use this template:

```markdown
## SEO Review: [page or scope]

### Critical / High
- **[File:line]** — [Finding]. **Suggestion:** [Change].

### Medium / Low
- **[File:line]** — [Finding]. **Suggestion:** [Change].

### Summary
- [N] critical, [N] high, [N] medium, [N] low.
```

## When to Involve Other Skills

- **Vague or broad request** ("improve SEO") → **org-receptionist** to clarify scope (one page vs site-wide, content vs technical).
- **What to write about / content strategy** → **org-content-strategist** for themes and topics; **org-content-creator** for drafting or rewriting copy.
- **Documentation or docs site** → **org-docs-team** so doc structure and SEO stay aligned.
- **Full code/PR review** (logic, security, not just SEO) → **org-senior-dev**.
- **Architecture or stack choices** (SSR vs SSG, routing) → **org-architecture-steward** or **org-feedback-loop** as appropriate.

## Severity Guide

| Severity  | When to use |
|-----------|-------------|
| Critical  | Missing or broken title/meta; no H1; canonical/robots blocking indexation. |
| High     | Duplicate titles/descriptions; broken heading hierarchy; important images without alt. |
| Medium   | Title/description too long or generic; weak URL; weak anchor text. |
| Low      | Minor wording or naming improvements; optional structured data. |

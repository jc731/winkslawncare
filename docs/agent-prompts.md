# Agent prompts (copy into new Cursor agent chats)

Use these in separate agent conversations as needed.

---

## 10 — Code / senior-dev review

```
Use the org-senior-dev skill to review the codebase for launch readiness. This is an Astro static site (Wink's Lawn Care) with Tailwind and Netlify. Review for: correctness, edge cases, security (no leaked secrets), performance, and any glaring anti-patterns. Assume high strictness. If there's no git diff to review, do a general pass on src/ (pages, components, layouts) and report Summary of Changes (what you reviewed), Risk Assessment, Actionable Feedback (Critical / Suggestion / Nice-to-have), and Approval Status. For frontend components, apply component-philosophy where relevant.
```

---

## 12 — Content strategy

```
Use the org-content-strategist skill. This project is Wink's Lawn Care (Astro site, blog in src/content/blog/). Analyze existing blog content to infer themes, target audience, and gaps. Provide: (1) Current content analysis summary, (2) Content pillars (3–4 main themes), (3) Target audience, (4) Proposed content backlog (5–10 article ideas) by pillar. If the project has a script like scripts/analyze_content.py, run it against src/content/blog/; otherwise scan the blog markdown files and frontmatter manually.
```

---

## 13 — Documentation audit

```
Use the org-docs-team skill in audit mode. This is Wink's Lawn Care (Astro static site, Netlify). Do a documentation audit: check README and any docs/ for accuracy, missing setup steps, and alignment with the codebase (e.g. project layout, build/deploy, where content and images live — src/images/, public/blog/, Layout vs PageLayout, Nav/Footer). Report what's in good shape and what should be updated or added. Scope: onboarding and maintainer docs, not blog content strategy.
```

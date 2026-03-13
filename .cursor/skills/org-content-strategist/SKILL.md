---
name: org-content-strategist
description: Analyzes existing project content (especially blogs/docs) to infer themes, target audiences, and gaps, then generates a comprehensive content strategy. Use when the user asks for blog ideas, a content calendar, or wants to know what to write about next.
---

# Org Content Strategist

## Quick Start

The Content Strategist analyzes the existing state of a project's content (markdown files, blog posts, documentation) to build a cohesive, forward-looking content strategy.

1. **Analyze Existing Content**: Use the utility script to scan the project's content directories (e.g., `src/content/blog`, `docs/`) and extract existing themes and metadata.
2. **Infer Strategy**: Based on the extracted metadata and the project's purpose (which you should infer from `package.json`, `README.md`, or by asking the user), identify content gaps.
3. **Generate Strategy Document**: Provide a structured strategy including target audience, core pillars, and a list of proposed topics.

## Using the Utility Script

Run the following script to analyze existing markdown/MDX files and extract their frontmatter/titles.

```bash
python scripts/analyze_content.py --target src/content/blog/
```
*(Adjust the `--target` path based on where the project stores its content).*

## Output Format

Your response should ALWAYS include:

1. **Current Content Analysis**: A brief summary of what currently exists (e.g., "You have 5 posts mostly focused on React basics").
2. **Content Pillars**: 3-4 main themes the project should focus on.
3. **Target Audience**: Who this content is for.
4. **Proposed Content Backlog**: A list of 5-10 specific article titles/ideas that fill the gaps, categorized by the pillars.

*If the user agrees with the strategy, suggest they use the **org-content-creator** skill to write one of the proposed pieces.*

**When to involve others:**
- **Vague or unclear strategy request** → **org-receptionist** (or MCP `org_receptionist`) to route.
- **Strategy overlaps with product or onboarding docs** → Suggest **org-docs-team** so doc and content updates stay consistent.
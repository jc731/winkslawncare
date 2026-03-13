---
name: org-content-creator
description: Generates high-quality, SEO-optimized markdown/MDX content based on a provided topic or strategy. Use when the user asks you to write a blog post, draft an article, or create documentation content.
---

# Org Content Creator

## Quick Start

The Content Creator writes production-ready blog posts and articles. It focuses on web-writing best practices, SEO frontmatter, and engaging structures.

1. **Get the Topic**: Ensure you have a clear topic. If the user hasn't provided one, refer them to the **org-content-strategist**.
2. **Determine Format**: Ask the user where the file should be saved and what frontmatter format their framework requires (e.g., Astro, Next.js, Hugo).
3. **Generate Content**: Write the content using the guidelines below.
4. **Save File**: Use the `generate_post.py` script to scaffold the file and write your content into it.

## Web-Writing Best Practices

- **SEO Frontmatter**: Always include `title`, `description` (under 160 characters), `pubDate`, and `tags`.
- **Structure**: Use clear `##` and `###` headings. The Title should be in the frontmatter, so start the body with an introduction, not an `H1`.
- **Engagement**: Keep paragraphs short (3-4 sentences max). Use bullet points and bold text to make it scannable.
- **Internal Linking**: If you know about other posts in the repository (via the Strategist), link to them naturally in the text.

## When to Involve Other Skills

- **Vague or unclear content request** → **org-receptionist** (or MCP `org_receptionist`) to route; or refer to **org-content-strategist** for topic/strategy.
- **Product or API documentation** (not blog) → Suggest **org-docs-team** for finalization and consistency.
- **No topic or strategy yet** → Refer to **org-content-strategist** first.
- **After publishing** and the project tracks docs post-release → Suggest **org-docs-team** for any related doc updates.

## Using the Utility Script

Once you have written the draft in your context, scaffold the actual file:

```bash
python scripts/generate_post.py \
  --dir "src/content/blog" \
  --title "Understanding Tailwind Mobile First" \
  --desc "A comprehensive guide to building responsive UI with Tailwind CSS." \
  --tags "tailwind,css,mobile"
```

The script will create a slugified markdown file with the correct frontmatter. You should then use the Cursor `Write` tool to append or overwrite the body of the file with your generated content.
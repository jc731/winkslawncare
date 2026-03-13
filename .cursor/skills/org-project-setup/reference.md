# Org Project Setup — reference

## Placeholders in default template

| Placeholder | Source | Example |
|------------|--------|---------|
| `{{PROJECT_NAME}}` | README title, `package.json` name, or folder name | `accension-order-form` |
| `{{STACK_SUMMARY}}` | package.json deps + config files | `Astro, Tailwind CSS, TypeScript` |
| `{{CONVENTIONS_SUMMARY}}` | README or docs (contributing, structure) | `Components in src/components; pages in src/pages; use pnpm.` |

If a value cannot be inferred, use a short generic (e.g. "See README") and do not leave the literal `{{...}}` in the output.

## Discovery file list (canonical)

1. **README**: `README.md`, `README`, `readme.md`, or `docs/README.md`
2. **Docs**: All markdown under `docs/` (limit to first ~10 files or key names like CONTRIBUTING, ARCHITECTURE, STYLE)
3. **Package**: `package.json`
4. **Config**: `tsconfig.json`, `jsconfig.json`, `astro.config.mjs`, `vite.config.ts`, `tailwind.config.mjs`, `next.config.js` (any present)
5. **Existing Cursor**: `.cursor/rules/*.mdc`

## Org preferences (not created by this skill)

Org preferences (strictness, ask_before) are used by org skills and live at org level. This skill does **not** create `mcp/` or any preferences file in projects. To read or update preferences, use the **org-preferences** skill.

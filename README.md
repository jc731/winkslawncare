# Wink's Lawn Care

Website for Wink's Lawn Care — lawn care services in Central Illinois (Champaign area and surrounding).

## Stack

- [Astro](https://astro.build), static site. Deploy to Netlify, Vercel, or any static host.

## Develop

- **Node:** 18+ (20 LTS recommended).
- **Package manager:** pnpm 8+ or npm 9+ (suggested; any compatible version may work).

```bash
pnpm install
pnpm dev
```

Open [http://localhost:4321](http://localhost:4321).

## Build & deploy

Build output is in `dist/`. Developed with pnpm; any package manager works for CI.

```bash
pnpm build
pnpm preview
```

- **Netlify**: Connect repo, build command `pnpm build` (or `npm run build`), publish directory `dist`.
- **Other hosts**: Run `npm run build` / `yarn build` / `pnpm build`, serve `dist/`.

## Project layout

```
├── public/           # Static files only (favicons, manifest). Avoid images here — they skip processing.
├── src/
│   ├── assets/       # Images (Astro processes these). Use for blog and page images.
│   ├── content.config.ts   # Content collection config (blog schema)
│   ├── layouts/
│   ├── pages/
│   ├── components/
│   └── content/      # Blog: src/content/blog/ (Markdown)
└── package.json
```

## Component structure

- **Primitives:** `Container`, `Button`, `Badge`, `FormField` — small, focused, reusable.
- **Composites:** `Card`, `PageSection`, `ContactForm` — combinations of primitives for common patterns.
- **Sections:** Page-specific blocks (e.g. hero, CTA band) live in pages; extract to a component when the same pattern repeats or clarity improves.

## See also

- [Astro docs](https://docs.astro.build).
- **Maintainers:** [docs/agent-prompts.md](docs/agent-prompts.md) (review/audit prompts), [AGENTS.md](AGENTS.md) (Cursor agent instructions).

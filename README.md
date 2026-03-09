# Wink's Lawn Care

Website for Wink's Lawn Care — lawn care services in Central Illinois (Champaign area and surrounding).

## Stack

- [Astro](https://astro.build), static site. Deploy to Netlify, Vercel, or any static host.

## Develop

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
├── public/
├── src/
│   ├── layouts/
│   ├── pages/        # index, blog (optional), etc.
│   ├── components/
│   └── content/      # optional: Astro content collections for blog
├── DO_THIS.md
└── package.json
```

## See also

- [DO_THIS.md](./DO_THIS.md) — contact info, content, and owner tasks.
- [Astro docs](https://docs.astro.build).

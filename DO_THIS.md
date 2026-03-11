# Wink's Lawn Care — Do This / Owner Tasks

Things to handle yourself or with the team.

---

## GitHub & deployment

- [x] **Create GitHub repo** (e.g. `your-org/winkslawncare` or `your-org/winkslawncare-website`).
- [x] **Add remote and push**:
  ```bash
  git remote add origin https://github.com/YOUR_ORG/winkslawncare.git
  git branch -M master
  git push -u origin master
  ```
- [x] **Connect to Netlify (or other host)**: connect repo, build `pnpm build` (or `npm run build`), publish `dist/`.

---

## Content

- [ ] **Contact info (TBD)**: Phone (217) 487-6264 is on the site. Add email or contact form if desired.
- [ ] **Service areas**: Champaign, Rantoul, Paxton, Mahomet, St. Joseph are listed. Adjust towns if needed.
- [ ] **Blog**: Start adding posts (see `src/content/blog/` or the blog section in the project). Configure Astro content collections when you’re ready to add real posts.

---

## Optional

- [ ] Add a contact form (e.g. Netlify Forms, Formspree, or your backend).
- [ ] Add photos, testimonials, or a services/pricing section.
- [ ] Set up analytics and/or cookie consent if needed.

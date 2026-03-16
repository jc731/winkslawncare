// @ts-check
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

import netlify from '@astrojs/netlify';

// https://astro.build/config
export default defineConfig({
  site: import.meta.env.SITE || 'https://winkslawncare.com',
  integrations: [tailwind()],

  adapter: netlify(),
});
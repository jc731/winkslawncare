/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      keyframes: {
        'hero-slow-zoom': {
          '0%': { transform: 'scale(1)' },
          '100%': { transform: 'scale(1.06)' },
        },
        'badge-subtle-pulse': {
          '0%, 100%': {
            transform: 'translateY(0)',
            boxShadow: '0 8px 24px -18px rgba(16, 185, 129, 0.65)',
          },
          '50%': {
            transform: 'translateY(-2px)',
            boxShadow: '0 16px 32px -20px rgba(16, 185, 129, 0.85)',
          },
        },
      },
      animation: {
        'hero-slow-zoom': 'hero-slow-zoom 22s ease-in-out infinite alternate',
        'badge-subtle-pulse': 'badge-subtle-pulse 5s ease-in-out infinite',
      },
    },
  },
  plugins: [],
};

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{svelte, html, js, ts}'],
  theme: {
    extend: {
      colors: {
        transparent: 'transparent',
        current: 'currentColor',
        red: {
          DEFAULT: '#a92f0f',
          light: '#f18065'
        }
      }
    }
  },
  plugins: []
};

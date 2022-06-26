const { transparent } = require('tailwindcss/colors');
const colors = require('tailwindcss/colors');

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{svelte, html, js, ts}'],
  theme: {
    colors: {
      transparent: 'transparent',
      current: 'currentColor',
      red: {
        DEFAULT: '#a92f0f',
        light: '#f18065'
      },
      black: colors.black,
      white: colors.white,
      gray: colors.gray
    },
    extend: {}
  },
  plugins: []
};

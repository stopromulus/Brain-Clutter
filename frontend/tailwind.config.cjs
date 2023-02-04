/** @type {import('tailwindcss').Config} */

module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    fontFamily: {
      'serif': [ui-serif, ...defaulttheme.fontFamily.serif],
    },
    extend: {},
  },
  plugins: []
};

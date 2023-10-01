/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './static/**/*.{js,ts,jsx,html}',
    './templates/**/*.{js,ts,jsx,html}',
    './templates/*.{js,ts,jsx,html}',
    './templates/dnf.html',
    './templates/***/**/*.{js,ts,jsx,html}'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

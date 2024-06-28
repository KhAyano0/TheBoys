/** @type {import('tailwindcss').Config} */
export default {
  content: [ "./index.html",
  "./src/**/*.{svelte,js,ts,jsx,tsx}",],
  theme: {
    extend: {
      colors:{
        'home-red': '#AE1C1C',
      }
    },
  },
  plugins: [],
}


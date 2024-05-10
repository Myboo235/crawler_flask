/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html", 
    "./src/**/*.{vue,js,ts,jsx,tsx}", 
    'node_modules/flowbite-vue/**/*.{js,jsx,ts,tsx,vue}',
    'node_modules/flowbite/**/*.{js,jsx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: "#292523",
        secondary: "#e6a349",
        tertiary: "#d5ccbb",
      },
      keyframes: {
        waves: {
          "0%": { transform: "translate(-50%, -75%) rotate(0deg)" },
          "100%": { transform: "translate(-50%, -75%) rotate(360deg)" },
        },
      },
      animation: {
        waves: "waves 15s linear infinite",
      },
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
};

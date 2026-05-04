/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#0f4c81",
        accent:  "#00b4d8",
      },
    },
  },
  plugins: [],
}

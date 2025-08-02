/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx}"
  ],
  theme: {
    extend: {
      fontFamily: {
        futuristic: ['"Orbitron"', 'sans-serif'],
        soft: ['"Poppins"', 'sans-serif'],
      },
      colors: {
        primary: "#00BFA6",
        dark: "#0F0F0F",
        glass: "rgba(255, 255, 255, 0.1)",
        gradient1: "#1D2671",
        gradient2: "#C33764",
      },
      backgroundImage: {
        hero: "linear-gradient(to right, #1D2671, #C33764)",
        glassy: "linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05))"
      },
      animation: {
        fadeIn: "fadeIn 1s ease-in-out",
        slideUp: "slideUp 0.5s ease-in-out",
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: 0 },
          '100%': { opacity: 1 },
        },
        slideUp: {
          '0%': { transform: 'translateY(50px)', opacity: 0 },
          '100%': { transform: 'translateY(0)', opacity: 1 },
        }
      }
    },
  },
  plugins: [require("tailwind-scrollbar-hide")],
}

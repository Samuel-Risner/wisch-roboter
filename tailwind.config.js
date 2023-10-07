/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./index.html"],
    theme: {
        extend: {
            animation: {
                "spin-slow": "spin 1.5s linear infinite"
            }
        },
    },
    plugins: [],
}

module.exports = {
  content: [
      './files/index.html',
      './files/mainpage.html',
      './files/index.js',
  ],
  theme: {
  },
  plugins: [require("@tailwindcss/typography"), require("daisyui")],
    daisyui: {
        styled: true,
        themes: ["cupcake", "dark", "cmyk"],
        base: true,
        utils: true,
        logs: false,
        rtl: false,
        prefix: "",
        darkTheme: "dark",
    }

}

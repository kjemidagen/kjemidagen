module.exports = {
  content: ['./src/**/*.svelte'],
  theme: {
    extend: {
      textColor: {
        skin: {
          base: 'var(--color-text-base)',
          inverted: 'var(--color-text-inverted)',
          loud: 'var(--color-text-loud)',
          brand: 'var(--color-text-brand)'
        }
      },
      backgroundColor: {
        skin: {
          primary: 'var(--color-bg-primary)',
          secondary: 'var(--color-bg-secondary)'
        }
      },
      gradientColorStops: {
        skin: {
          hue: 'var(--color-bg-primary)'
        }
      }
    }
  },
  plugins: []
};

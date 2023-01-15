import { sveltekit } from '@sveltejs/kit/vite';

/** @type {import('vite').UserConfig} */
const config = {
  plugins: [sveltekit()],
  server: {
    watch: {
      usePolling: true
    }
  },
  ssr: {
    noExternal: ['three', 'troika-three-text']
  }
};

export default config;

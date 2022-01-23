import adapter from '@sveltejs/adapter-node';
import preprocess from 'svelte-preprocess';
import precompileIntl from 'svelte-intl-precompile/sveltekit-plugin';

/** @type {import('@sveltejs/kit').Config} */
const config = {
  // Consult https://github.com/sveltejs/svelte-preprocess
  // for more information about preprocessors
  preprocess: preprocess(),

  kit: {
    adapter: adapter({
      out: 'build',
      precompress: false
    }),

    // hydrate the <div id="svelte"> element in src/app.html
    target: '#svelte',
    vite: {
      plugins: [precompileIntl('translations')]
    }
  }
};

export default config;

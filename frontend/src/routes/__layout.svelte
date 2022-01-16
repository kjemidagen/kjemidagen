<script context="module" lang="ts">
  import '../app.css';
  import { addMessages, init, getLocaleFromQueryString } from 'svelte-intl-precompile';
  import no from '$lib/translations/no.json';
  import en from '$lib/translations/en.json';
  /* DOCS: https://svelte-intl-precompile.com/en/docs/ */
  addMessages('no', no);
  addMessages('en', en);

  /** @type {import('@sveltejs/kit').Load} */
  export async function load({ url }) {
    const lang = url.searchParams.get('lang');
    init({
      initialLocale: lang,
      fallbackLocale: 'no'
    });
    return {};
  }
</script>

<script lang="ts">
  import Header from '$lib/layout/Header.svelte';
  import Footer from '$lib/layout/Footer.svelte';
</script>

<Header />

<main>
  <slot />
</main>

<Footer />

<style>
  main {
    align-items: center;
    margin: auto;
  }
</style>

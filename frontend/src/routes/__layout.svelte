<script context="module" lang="ts">
  /* DOCS: https://svelte-intl-precompile.com/en/docs/ */
  import { addMessages, init, getLocaleFromQueryString } from 'svelte-intl-precompile';
  import { session } from '$app/stores';
  import no from '$lib/translations/no.json';
  import en from '$lib/translations/en.json';
  addMessages('no', no);
  addMessages('en', en);

  import '../app.css';
</script>

<script lang="ts">
  import Header from '$lib/layout/Header.svelte';
  import Footer from '$lib/layout/Footer.svelte';
  init({
    fallbackLocale: 'no',
    initialLocale: getLocaleFromQueryString('lang')
  });
</script>

<Header />

<main>
  <slot />
</main>

<Footer />

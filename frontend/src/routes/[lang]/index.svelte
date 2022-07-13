<script context="module">
  import { browser } from '$app/env';
  import { t } from '$lib/translations/translations';

  // We need js for the mobile menu on every page
  export const hydrate = true;

  // ...but if the client-side router is already loaded
  // (i.e. we came here from elsewhere in the app), use it
  export const router = browser;

  // since there's no dynamic data here, we can prerender
  // it so that it gets served as a static asset in prod
  export const prerender = true;
  // See more at kit.svelte.dev/docs/page-options
</script>

<svelte:head>
  <title>{$t('common.chemday')}</title>
</svelte:head>

<section class="banner" id="banner">
  <div class="mx-auto max-w-4xl my-24 grid grid-cols-1 md:grid-cols-3">
    <img class="w-60 row-start-2 mx-auto md:row-start-1" src="/logo.svg" alt="logo" />
    <div class="font-bold text-red mx-auto md:col-span-2">
      <h1 class="text-4xl md:text-7xl">{$t('common.chemday')}</h1>
      <h2 class="text-xl md:text-4xl">{$t('frontpage.when')}</h2>
      <h2 class="text-xl md:text-4xl">{$t('frontpage.where')}</h2>
    </div>
  </div>
</section>

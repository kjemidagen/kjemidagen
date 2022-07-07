<script context="module">
  import { browser, dev } from '$app/env';
  import { t } from '$lib/translations/translations';

  // we don't need any JS on this page, though we'll load
  // it in dev so that we get hot module replacement...
  export const hydrate = dev;

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
  <div class="grid grid-cols-3 mx-64 my-24">
    <img class="w-60" src="/logo.svg" alt="logo" />
    <div class="font-bold text-red col-span-2">
      <h1 class="text-7xl">{$t('common.chemday')}</h1>
      <h2 class="text-4xl">{$t('frontpage.when')}</h2>
      <h2 class="text-4xl">{$t('frontpage.where')}</h2>
    </div>
  </div>
</section>

<script lang="ts">
  import { browser } from '$app/env';
  import { t } from '$lib/translations/translations';
  export const hydrate = true;
  export const router = browser;
  export const prerender = true;
</script>

<svelte:head>
  <title>{$t('common.companies')}</title>
</svelte:head>

<section class="companies">
  <div class="content" id="companies">
    <h1 class="text-3xl mb-8">{$t('companies.companies')}</h1>
    <p class="text-lg">{$t('companies.moreinfo')}</p>
  </div>
</section>

<style>
  .companies {
    background: var(--color-text-loud);
    padding: 40px 0;
  }

  p {
    color: var(--color-text-base);
    padding: 0 1rem;
  }
</style>

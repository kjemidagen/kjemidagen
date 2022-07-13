<script lang="ts">
  import { browser } from '$app/env';
  export const hydrate = true;
  export const router = browser;
  export const prerender = true;
  import { t } from '$lib/translations/translations';
</script>

<svelte:head>
  <title>{$t('common.sponsors')}</title>
</svelte:head>

<section class="sponsors">
  <div class="content" id="sponsors">
    <h3>{$t('sponsors.sponsors')}</h3>
    <p>{$t('sponsors.moreinfo')}</p>
    <!-- <img src="/sponsors_22.png" alt="bedriftene som er med på kjemidagen" /> -->
  </div>
</section>

<style>
  .sponsors {
    background: var(--color-text-loud);
    padding: 40px 0;
  }

  p {
    color: var(--color-text-base);
    padding: 0 1rem;
  }
</style>

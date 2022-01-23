<script context="module" lang="ts">
  import { browser, dev } from '$app/env';
  export const hydrate = dev;
  export const router = browser;
  export const prerender = false;
  import { t } from 'svelte-intl-precompile';
</script>

<h1>
  {$t('error')}
</h1>

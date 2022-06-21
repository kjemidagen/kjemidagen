<script lang="ts">
  import { browser, dev } from '$app/env';
  import Sponsors from '$lib/frontpage/Sponsors.svelte';
  export const hydrate = dev;
  export const router = browser;
  export const prerender = true;
</script>

<svelte:head>
  <title>Ta kontakt</title>
</svelte:head>

<Sponsors />

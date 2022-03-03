<script lang="ts">
  import { browser, dev } from '$app/env';
  import English from '$lib/frontpage/English.svelte';
  export const hydrate = dev;
  export const router = browser;
  export const prerender = true;
</script>

<svelte:head>
  <title>Chemistry day</title>
</svelte:head>

<English />

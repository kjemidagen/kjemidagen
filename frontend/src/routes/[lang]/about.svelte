<script lang="ts">
  import { browser, dev } from '$app/env';
  import About from '$lib/frontpage/About.svelte';
  export const hydrate = dev;
  export const router = browser;
  export const prerender = true;
</script>

<svelte:head>
  <title>Om kjemidagen</title>
</svelte:head>

<About />

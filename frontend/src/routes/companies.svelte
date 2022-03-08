<script lang="ts">
  import { browser, dev } from '$app/env';
  import Companies from '$lib/frontpage/Companies.svelte';
  export const hydrate = dev;
  export const router = browser;
  export const prerender = true;
</script>

<svelte:head>
  <title>Bedrifter</title>
</svelte:head>

<Companies />

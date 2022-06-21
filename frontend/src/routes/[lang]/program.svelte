<script lang="ts">
  import { browser, dev } from '$app/env';
  import Program from '$lib/frontpage/Program.svelte';
  export const hydrate = dev;
  export const router = browser;
  export const prerender = true;
</script>

<svelte:head>
  <title>Program</title>
</svelte:head>

<Program />

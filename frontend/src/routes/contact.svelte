<script lang="ts">
  import { browser, dev } from '$app/env';
  import Contact from '$lib/frontpage/Contact.svelte';
  export const hydrate = dev;
  export const router = browser;
  export const prerender = true;
</script>

<svelte:head>
  <title>Ta kontakt</title>
</svelte:head>

<Contact />

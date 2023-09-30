<script context="module">
  import favicon from '$lib/assets/favicon.ico';
  import { dev } from '$app/environment';
  import { inject } from '@vercel/analytics';

  inject({ mode: dev ? 'development' : 'production' });
</script>

<svelte:head>
  <link rel="icon" href={favicon} />
</svelte:head>

<slot />

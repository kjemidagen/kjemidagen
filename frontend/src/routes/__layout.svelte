<script context="module" lang="ts">
  import '../app.css';
</script>

<script lang="ts">
  import { isLoginOpen } from '$lib/stores';
  import Header from '$lib/layout/Header.svelte';
  import Footer from '$lib/layout/Footer.svelte';
  import Login from '$lib/internal/Login.svelte';
</script>

<Header />

<main>
  <slot />
</main>

<Footer />

{#if $isLoginOpen}
  <Login />
{/if}

<style>
  main {
    align-items: center;
    margin: auto;
  }
</style>

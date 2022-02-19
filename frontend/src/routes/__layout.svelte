<script context="module" lang="ts">
  import '../app.css';
</script>

<script lang="ts">
  import Header from '$lib/layout/Header.svelte';
  import Footer from '$lib/layout/Footer.svelte';
</script>

<Header />

<main>
  <slot />
</main>

<Footer />

<style>
  main {
    align-items: center;
    margin: auto;
  }
</style>

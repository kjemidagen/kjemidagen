<script lang="ts">
  import Header from '$lib/header/Header.svelte';
  import '../app.css';
</script>

<Header />

<main>
  <slot />
</main>

<footer>
  <span>Footer</span>
</footer>

<style>
</style>

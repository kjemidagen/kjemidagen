<script lang="ts">
  import Header from '$lib/layout/Header.svelte';
  import Footer from '$lib/layout/Footer.svelte';
</script>

<Header />

<div class="h-96 mb-auto">
  <slot />
</div>

<Footer />

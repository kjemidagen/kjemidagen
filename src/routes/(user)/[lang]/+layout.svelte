<script lang="ts">
  import Header from '$lib/layout/Header.svelte';
  import Footer from '$lib/layout/Footer.svelte';
  import { t } from '$lib/translations/translations';
</script>

<div class="flex flex-col justify-between h-screen">
  <Header />

  <main id="main" class="mt-16 border-y-8 border-red-light p-0 flex-grow px-2 md:border-x-8">
    <slot />
  </main>

  <Footer />
</div>

<style>
  main::before {
    display: block;
    content: ' ';
    margin-top: -285px;
    height: 285px;
    visibility: hidden;
    pointer-events: none;
  }
</style>

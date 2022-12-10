<script lang="ts">
  import Header from '$lib/layout/AdminHeader.svelte';
  import Footer from '$lib/layout/AdminFooter.svelte';
</script>

<div class="flex flex-col justify-between h-screen">
  <Header />

  <main id="main" class="border-y-8 border-red-light p-0 flex-grow px-2 md:border-x-8">
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

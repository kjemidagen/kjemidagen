<script lang="ts">
  import Header from '$lib/layout/AdminHeader.svelte';
  import Footer from '$lib/layout/AdminFooter.svelte';
</script>

<svelte:head>
  <title>Admin • Kjemidagen</title>
</svelte:head>

<div class="flex h-screen flex-col justify-between">
  <Header />

  <main id="main" class="flex-grow border-y-8 border-red-light p-0 px-2 md:border-x-8">
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

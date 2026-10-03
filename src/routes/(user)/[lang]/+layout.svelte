<script lang="ts">
  import Header from '#lib/layout/Header.svelte';
  import Footer from '#lib/layout/Footer.svelte';
  import { t } from '#lib/translations/translations.js';
  interface Props {
    children?: import('svelte').Snippet;
  }

  let { children }: Props = $props();
</script>

<div class="flex h-screen flex-col justify-between">
  <Header />

  <main id="main" class="mt-16 flex-grow border-y-8 border-red-light p-0 px-2 md:border-x-8">
    {@render children?.()}
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

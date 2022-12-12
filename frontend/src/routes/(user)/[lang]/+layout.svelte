<script lang="ts">
  import Header from '$lib/layout/Header.svelte';
  import Footer from '$lib/layout/Footer.svelte';
  import { t } from '$lib/translations/translations';
</script>

<a class="skiptocontent" href="#main">{$t('common.skiptocontent')}</a>
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

  .skiptocontent {
    position: absolute;
    top: 3px;
    left: 50%;
    transform: translateX(-50%);
    z-index: -2000;
    border: 1px solid var(--color-text-inverted);
    color: var(--color-text-inverted);
    padding: 0.3rem 1.5rem;
    background-color: var(--color-bg-secondary);
    border-radius: 0.2rem;
    font-size: large;
  }

  .skiptocontent:focus,
  .skiptocontent:active {
    z-index: 2000;
  }
</style>

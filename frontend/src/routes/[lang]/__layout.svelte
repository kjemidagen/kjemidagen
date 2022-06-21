<script context="module" lang="ts">
  import '../../app.css';
</script>

<script lang="ts">
  import { isLoginOpen } from '$lib/stores';
  import Header from '$lib/layout/Header.svelte';
  import Footer from '$lib/layout/Footer.svelte';
  import Login from '$lib/internal/Login.svelte';
  import { t } from '$lib/translations/translations';

  export const mobile = true;
</script>

<a class="skiptocontent" href="#main">{$t('common.skiptocontent')}</a>
<Header />

<div class="border">
  <main id="main">
    <slot />
  </main>
</div>

<Footer />

{#if $isLoginOpen}
  <Login />
{/if}

<style>
  main {
    align-items: center;
    margin: auto;
  }

  main::before {
    display: block;
    content: ' ';
    margin-top: -285px;
    height: 285px;
    visibility: hidden;
    pointer-events: none;
  }

  .border {
    width: 100%;
    height: 100%;
    border: 10px solid var(--color-bg-secondary);
    box-sizing: border-box;
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

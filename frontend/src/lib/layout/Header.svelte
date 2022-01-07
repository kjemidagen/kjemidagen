<script lang="ts">
  import { t, locale, locales } from 'svelte-intl-precompile';
</script>

<header id="header">
  <div class="center">
    <a href="/"><img src="logo_inverted.svg" alt="logo" width="20" />Kjemidagen</a>
    <aside class="language-selector">
      {#each $locales as loc}
        <button
          type="button"
          class={loc === $locale && 'current-locale'}
          on:click={() => ($locale = loc)}>{loc}</button
        >
      {/each}
    </aside>
  </div>
</header>

<style>
  header {
    display: block;
    width: 100%;
    justify-content: right;
    position: sticky;
    top: 0;
    left: 0;
    background-color: var(--color-bg-primary);
    color: var(--color-text-base);
  }
  .center {
    align-items: center;
    max-width: var(--document-width);
    display: flex;
    justify-content: space-between;
    margin: auto;
  }
</style>

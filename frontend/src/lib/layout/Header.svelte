<script lang="ts">
  import { t, locale, locales } from 'svelte-intl-precompile';

  const handleLangChange = (loc) => {
    $locale = loc;
    if (window && 'URLSearchParams' in window) {
      let searchParams = new URLSearchParams(window.location.search);
      searchParams.set('lang', $locale);
      const newRelativePathQuery =
        window.location.pathname + '?' + searchParams.toString() + window.location.hash;
      history.pushState(null, '', newRelativePathQuery);
    }
  };
</script>

<header id="header">
  <div class="center">
    <a class="home" href="/">
      <img class="logo" src="logo_inverted.svg" alt="logo" width="40" />
      <span>Kjemidagen</span>
    </a>
    <aside class="language-selector">
      {#each $locales as loc}
        <a
          class={'lang ' + (loc === $locale && 'current-locale')}
          href={'?lang=' + loc}
          on:click|preventDefault={(e) => handleLangChange(loc)}>{loc}</a
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
    z-index: 1000;
  }
  .center {
    align-items: center;
    max-width: var(--document-width);
    display: flex;
    justify-content: space-between;
    margin: auto;
    padding: 1rem;
  }
  .home {
    display: flex;
    text-decoration: none;
    font-size: larger;
    color: var(--color-text-loud);
    align-items: center;
  }
  .logo {
    margin-right: 0.5rem;
  }
  a.lang {
    border: none;
    background-color: inherit;
    color: var(--color-text-inverted);
    margin: 0.25rem;
  }
</style>

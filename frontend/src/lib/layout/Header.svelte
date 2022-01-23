<script lang="ts">
  import { locale, locales } from 'svelte-intl-precompile';
  import 

  const handleLangChange = (loc) => {
    $locale = loc;
    if (window && 'URLSearchParams' in window) {
      const pathname = window.location.pathname.split('/');
      const newPathname = '/' + loc + '/' + pathname.slice(2).join('/');
      const newRelativePathQuery = newPathname + window.location.search + window.location.hash;
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
          href={loc}
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

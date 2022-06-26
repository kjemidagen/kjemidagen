<script lang="ts">
  import { isLoginOpen } from '$lib/stores';

  import { t, locales, locale } from '$lib/translations/translations';
  import { page } from '$app/stores';

  $: ({ route } = $page.stuff);
  const routes = ['/', '/about/', '/program/', '/companies/', '/sponsors/'];
</script>

<header id="header" class="bg-red">
  <div class="px-4 grid grid-cols-8 h-16">
    <a class="home col-span-2" href={'/'}>
      <img class="logo" src="/logo_inverted.svg" alt="logo" width="40" />
      <span>{$t('common.chemday')}</span>
    </a>
    <ul class="navigation col-span-5">
      {#each routes as routeName}
        <li class="h-full flex flex-col float-left {route === routeName ? 'bg-red-light' : ''}">
          <a class="justify-self-center m-auto" href="/{$locale}{routeName}">
            {#if routeName === '/'}
              {$t('common.home')}
            {:else}
              {$t('common.' + routeName.replace('/', '').replace('/', ''))}
            {/if}
          </a>
        </li>
      {/each}
    </ul>
    <button class="hidden">
      <img class="w-8" src="/hamburgermeny.svg" alt="hamburgermeny" />
    </button>
    <ul class="language">
      {#each $locales as lc}
        <li><a href="/{lc}{route}">{lc}</a></li>
      {/each}
    </ul>
    <button
      class="hidden login"
      href="/login"
      on:click={(event) => {
        event.preventDefault;
        $isLoginOpen = true;
        return false;
      }}>{$t('common.login')}</button
    >
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
    z-index: 1000;
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

  .login {
    border: 1px solid var(--color-text-inverted);
    border-radius: 3px;
    background-color: inherit;
    color: var(--color-text-inverted);
    cursor: pointer;
  }

  li {
    display: inline-flex;
    margin: auto 0;
    padding: 0 0.5rem;
  }

  a {
    color: var(--color-text-loud);
  }

  .navigation {
    list-style: none;
  }

  @media screen and (max-width: 768px) {
    .navigation {
      visibility: hidden;
    }
  }
</style>

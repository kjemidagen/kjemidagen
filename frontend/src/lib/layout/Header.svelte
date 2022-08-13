<script lang="ts">
  import { t, locales, locale } from '$lib/translations/translations';
  import { page } from '$app/stores';

  import MobileMenu from '$lib/components/MobileMenu.svelte';

  import logo from '$lib/assets/logo_inverted.svg';
  import hamburgerMenuPic from '$lib/assets/hamburgermeny.svg';

  $: ({ route } = $page.stuff);
  const routes = ['', '/about', '/program', '/companies', '/sponsors'];

  let navOpen = false;
</script>

<header id="header" class="bg-red px-25 sticky top-0 left-0 z-50">
  <div class="text-white px-6 flex h-16 justify-between md:justify-evenly">
    <a class="flex text-lg items-center color-white lg:w-40" href={'/'}>
      <img class="mr-1" src={logo} alt="logo" width="40" />
      <span class="hidden lg:inline">{$t('common.chemday')}</span>
    </a>
    <ul class="list-none hidden md:block flex-grow max-w-5xl mx-4 overflow-hidden">
      {#each routes as routeName}
        <li class="h-full flex flex-col float-left px-2" class:bg-red-light={route === routeName}>
          <a class="justify-self-center m-auto" href="/{$locale}{routeName}">
            {#if routeName === ''}
              {$t('common.home')}
            {:else}
              {$t('common.' + routeName.replace('/', ''))}
            {/if}
          </a>
        </li>
      {/each}
    </ul>
    <ul class="language list-none col-span-4 overflow-hidden lg:w-40">
      {#each $locales as lc}
        <li class="h-full flex flex-col px-2 float-left md:float-right ">
          <a class="justify-self-center m-auto" href="/{lc}{route}">{lc}</a>
        </li>
      {/each}
    </ul>
    <button
      class="md:hidden items-right"
      on:click|preventDefault={() => {
        navOpen = !navOpen;
      }}
    >
      <img class="w-8 m-auto" src={hamburgerMenuPic} alt="hamburgermeny" />
    </button>
  </div>
  {#if navOpen}
    <MobileMenu
      {routes}
      on:closemenu={() => {
        navOpen = false;
      }}
    />
  {/if}
</header>

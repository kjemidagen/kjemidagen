<script lang="ts">
  import { t, locales, locale } from '$lib/translations/translations';
  import { page } from '$app/stores';

  import MobileMenu from '$lib/components/MobileMenu.svelte';

  import logo from '$lib/assets/logo_inverted.svg';
  import hamburgerMenuPic from '$lib/assets/hamburgermeny.svg';

  let currentRoute = '';
  let currentRouteNoLang = '';
  $: {
    currentRoute = $page.routeId || '';
  }
  $: {
    currentRouteNoLang = $page.routeId?.split('/').splice(1, undefined).join('/') || '';
  }

  const routes = [
    {
      link: `/${$locale}`,
      label: $t('common.home')
    },
    {
      link: `/${$locale}/about`,
      label: $t('common.about')
    },
    {
      link: `/${$locale}/program`,
      label: $t('common.program')
    },
    {
      link: `/${$locale}/companies`,
      label: $t('common.companies')
    },
    {
      link: `/${$locale}/sponsors`,
      label: $t('common.sponsors')
    }
    // {
    //   link: `/${$locale}/login`,
    //   label: $t('common.login')
    // }
  ];

  let navOpen = false;
</script>

<header id="header" class="bg-red px-25 sticky top-0 left-0 z-50">
  <div class="text-white px-6 flex h-16 justify-between md:justify-evenly">
    <a class="flex text-lg text-white items-center color-white lg:w-40" href={'/'}>
      <img class="mr-1" src={logo} alt="logo" width="40" />
      <span class="hidden lg:inline">{$t('common.chemday')}</span>
    </a>
    <ul class="list-none hidden md:block flex-grow max-w-5xl mx-4 overflow-hidden">
      {#each routes as route}
        <li
          class="h-full flex flex-col float-left px-2"
          class:bg-red-light={currentRoute === route.link}
        >
          <a class="justify-self-center m-auto text-white" href={route.link}>
            {route.label}
          </a>
        </li>
      {/each}
    </ul>
    <ul class="language list-none col-span-4 overflow-hidden lg:w-40">
      {#each $locales as lc}
        <li class="h-full flex flex-col px-2 float-left md:float-right ">
          <a class="justify-self-center m-auto text-white" href={`/${lc}/${currentRouteNoLang}`}
            >{lc}</a
          >
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
      {currentRoute}
      on:closemenu={() => {
        navOpen = false;
      }}
    />
  {/if}
</header>

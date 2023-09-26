<script lang="ts">
  import { t, locales, locale } from '$lib/translations/translations';
  import { page } from '$app/stores';

  import MobileMenu from '$lib/components/MobileMenu.svelte';

  import logo from '$lib/assets/logo_inverted.svg';
  import hamburgerMenuPic from '$lib/assets/hamburgermeny.svg';

  $: currentRoute = $page.route.id?.split('/').slice(1, undefined).join('/') || '';
  $: currentRouteNoLang = currentRoute.split('/').slice(2, undefined).join('/');

  $: routes = [
    {
      link: `/${$locale}`,
      label: $t('common.home'),
      linkNoLang: ``
    },
    {
      link: `/${$locale}/about`,
      label: $t('common.about'),
      linkNoLang: `about`
    },
    {
      link: `/${$locale}/program`,
      label: $t('common.program'),
      linkNoLang: `program`
    },
    {
      link: `/${$locale}/companies`,
      label: $t('common.companies'),
      linkNoLang: `companies`
    },
    {
      link: `/${$locale}/sponsors`,
      label: $t('common.sponsors'),
      linkNoLang: `sponsors`
    },
    {
      link: `/${$locale}/map`,
      label: $t('common.map'),
      linkNoLang: `map`
    }
    // {
    //   link: `/${$locale}/login`,
    //   label: $t('common.login'),
    //   linkNoLang: `/login`
    // }
  ];

  $: langRoutes = $locales.map((locale) => ({
    link: `/${locale}/${currentRouteNoLang}`,
    label: locale
  }));

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
          class:bg-red-light={currentRouteNoLang === route.linkNoLang}
        >
          <a class="justify-self-center m-auto text-white" href={route.link}>
            {route.label}
          </a>
        </li>
      {/each}
    </ul>
    <ul class="language list-none col-span-4 overflow-hidden lg:w-40">
      {#each langRoutes as lc}
        <li class="h-full flex flex-col px-2 float-left md:float-right">
          <a class="justify-self-center m-auto text-white" href={lc.link}>{lc.label}</a>
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
      currentRoute={currentRouteNoLang}
      on:closemenu={() => {
        navOpen = false;
      }}
    />
  {/if}
</header>

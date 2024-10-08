<script lang="ts">
  import { t, locales, locale } from '$lib/translations/translations';
  import { page } from '$app/stores';

  import MobileMenu from '$lib/components/MobileMenu.svelte';
  import InfoPill from '$lib/components/InfoPill.svelte';

  import logo from '$lib/assets/logo_inverted.svg';
  import hamburgerMenuPic from '$lib/assets/hamburgermeny.svg';

  import { writable } from 'svelte/store';
  import { onMount } from 'svelte';

  const createWritableStore = (key: string, startValue: any) => {
    const { subscribe, set } = writable(startValue);

    return {
      subscribe,
      set,
      useLocalStorage: () => {
        const json = localStorage.getItem(key);
        if (json) {
          set(JSON.parse(json));
        }

        subscribe((current) => {
          localStorage.setItem(key, JSON.stringify(current));
        });
      }
    };
  };

  export const visitedStore = createWritableStore('visited', ['program']);

  onMount(() => {
    visitedStore.set([]);
    visitedStore.useLocalStorage();
  });

  $: currentRoute = $page.url.pathname;
  $: currentRouteNoLang = currentRoute.split('/').slice(2, undefined).join('/');

  $: visitedStore.set([...new Set([...$visitedStore, currentRouteNoLang])]);

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
      linkNoLang: `program`,
      new: !$visitedStore.includes('program')
    },
    {
      link: `/${$locale}/companies`,
      label: $t('common.companies'),
      linkNoLang: `companies`,
      new: !$visitedStore.includes('companies')
    },
    {
      link: `/${$locale}/sponsors`,
      label: $t('common.sponsors'),
      linkNoLang: `sponsors`
    },
    {
      link: `/${$locale}/map`,
      label: $t('common.map'),
      linkNoLang: `map`,
      new: !$visitedStore.includes('map')
    },
    {
      link: `/${$locale}/jobs`,
      label: $t('common.jobs'),
      linkNoLang: `jobs`,
      new: !$visitedStore.includes('jobs')
    }
  ];

  $: langRoutes = $locales.map((locale) => ({
    link: `/${locale}/${currentRouteNoLang}`,
    label: locale
  }));

  let navOpen = false;
</script>

<header id="header" class="px-25 fixed w-full left-0 top-0 z-50 bg-red border-b-8 border-red-light">
  <div class="flex h-16 justify-between px-6 text-white md:justify-evenly">
    <a class="color-white flex items-center text-lg text-white lg:w-40" href={`/${$locale}`}>
      <img class="mr-1" src={logo} alt="logo" width="40" />
      <span class="hidden lg:inline">{$t('common.chemday')}</span>
    </a>
    <ul class="mx-4 hidden max-w-5xl flex-grow list-none overflow-hidden md:block">
      {#each routes as route}
        <li
          class="float-left inline-flex h-full items-center justify-center px-4"
          class:bg-red-light={currentRouteNoLang === route.linkNoLang}
        >
          <a class="m-auto justify-self-center text-white flex-inline flex" href={route.link}>
            <span class="group transition duration-300">
              {route.label}
              <span
                class="block h-0.5 max-w-0 bg-white transition-all duration-500 group-hover:max-w-full"
              />
            </span>
            <InfoPill
              class="transistion-all ml-2 h-fit duration-500 {route.new
                ? 'visible'
                : 'hidden'} bg-blue-500 text-sm"
            ></InfoPill>
          </a>
        </li>
      {/each}
    </ul>
    <ul class="language col-span-4 list-none overflow-hidden lg:w-40">
      {#each langRoutes as lc}
        <li
          class="float-left flex h-full flex-col px-2 transition-all duration-200 md:float-right"
        >
          <a class="m-auto justify-self-center text-white group transition duration-300" href={lc.link}>
            {lc.label}
            <span
                class="block h-0.5 max-w-0 bg-white transition-all duration-500 group-hover:max-w-full"
              />
          </a>
        </li>
      {/each}
    </ul>
    <button
      class="items-right md:hidden"
      on:click|preventDefault={() => {
        navOpen = !navOpen;
      }}
    >
      <img class="m-auto w-8" src={hamburgerMenuPic} alt="hamburgermeny" />
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

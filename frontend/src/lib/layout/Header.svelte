<script lang="ts">
  import { isLoginOpen } from '$lib/stores';
  import { t, locales, locale } from '$lib/translations/translations';
  import { page } from '$app/stores';

  import MobileMenu from '$lib/components/MobileMenu.svelte';

  $: ({ route } = $page.stuff);
  const routes = ['', '/about', '/program', '/companies', '/sponsors'];

  let navOpen = false;
</script>

<header id="header" class="bg-red px-25 sticky top-0 left-0">
  <div class="text-white px-6 grid h-16 grid-cols-8">
    <a class="flex text-lg items-center color-white col-span-2" href={'/'}>
      <img class="mr-1" src="/logo_inverted.svg" alt="logo" width="40" />
      <span class="hidden md:inline">{$t('common.chemday')}</span>
    </a>
    <ul class="list-none col-span-5 hidden md:block">
      {#each routes as routeName}
        <li
          class="h-full flex flex-col float-left px-2 {route === routeName ? 'bg-red-light' : ''}"
        >
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
    <ul class="language list-none col-span-4 md:col-span-1">
      {#each $locales as lc}
        <li class="h-full flex flex-col px-2 float-left md:float-right ">
          <a class="justify-self-center m-auto" href="/{lc}{route}">{lc}</a>
        </li>
      {/each}
    </ul>
    <button
      class="col-span-2 md:hidden items-right"
      on:click|preventDefault={() => {
        navOpen = !navOpen;
      }}
    >
      <img class="w-8 m-auto" src="/hamburgermeny.svg" alt="hamburgermeny" />
    </button>
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
  {#if navOpen}
    <MobileMenu
      {routes}
      on:clicked={() => {
        navOpen = false;
      }}
    />
  {/if}
</header>

<script lang="ts">
  import { page } from '$app/stores';

  import MobileMenu from '$lib/components/MobileMenu.svelte';

  import logo from '$lib/assets/logo_inverted.svg';
  import hamburgerMenuPic from '$lib/assets/hamburgermeny.svg';

  let username: string | undefined;

  let currentRoute = '';
  $: {
    currentRoute = $page.route.id || '';
  }

  const routes = [
    { label: 'Hjem', link: '/admin' },
    { label: 'Brukere', link: '/admin/users' },
    { label: 'Bedrifter', link: '/admin/companies' }
  ].map((route) => ({ ...route, linkNoLang: route.link }));

  let navOpen = false;
</script>

<header id="header" class="px-25 sticky top-0 left-0 z-50 bg-red">
  <div class="flex h-16 justify-between px-6 text-white md:justify-evenly">
    <a class="color-white flex items-center text-lg text-white lg:w-40" href={'/'}>
      <img class="mr-1" src={logo} alt="logo" width="40" />
      <span class="hidden lg:inline">Kjemidagen-admin</span>
    </a>
    <ul class="mx-4 hidden max-w-5xl flex-grow list-none overflow-hidden md:block">
      {#each routes as route}
        <li
          class="float-left flex h-full flex-col px-2"
          class:bg-red-light={currentRoute === route.link}
        >
          <a class="m-auto justify-self-center text-white" href={route.link}>{route.label}</a>
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
    {#if username !== undefined}
      <div>
        {username}
      </div>
    {/if}
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

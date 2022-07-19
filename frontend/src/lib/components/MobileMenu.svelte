<script lang="ts">
  import { t, locale } from '$lib/translations/translations';
  import { page } from '$app/stores';
  import { slide, fade } from 'svelte/transition';
  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher();

  $: ({ route } = $page.stuff);
  export let routes: string[];
</script>

<div
  class="absolute bg-black/20 h-screen w-full backdrop-blur-sm"
  on:click={() => {
    dispatch('closemenu');
  }}
  in:fade|local={{ duration: 200 }}
  out:fade|local={{ duration: 50 }}
/>
<ul
  class="absolute w-full bg-red border-red-light border-y-8 text-white"
  in:slide|local={{ duration: 200 }}
  out:slide|local={{ duration: 50 }}
>
  {#each routes as routeName}
    <li
      class:bg-red-light={route === routeName}
      on:click={() => {
        dispatch('closemenu');
      }}
    >
      <a class="block px-2 py-4 " href="/{$locale}{routeName}">
        {#if routeName === ''}
          {$t('common.home')}
        {:else}
          {$t('common.' + routeName.replace('/', ''))}
        {/if}
      </a>
    </li>
  {/each}
</ul>

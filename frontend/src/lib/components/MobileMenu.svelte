<script lang="ts">
  import { t, locale } from '$lib/translations/translations';
  import { page } from '$app/stores';

  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();

  $: ({ route } = $page.stuff);
  export let routes: string[];
</script>

<ul class="absolute w-full bg-red border-red-light border-y-8 text-white">
  {#each routes as routeName}
    <li
      class={route === routeName ? 'bg-red-light' : ''}
      on:click={() => {
        dispatch('clicked');
      }}
    >
      <a class="block px-2 py-2 " href="/{$locale}{routeName}">
        {#if routeName === ''}
          {$t('common.home')}
        {:else}
          {$t('common.' + routeName.replace('/', ''))}
        {/if}
      </a>
    </li>
  {/each}
</ul>

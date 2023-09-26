<script lang="ts">
  import { slide, fade } from 'svelte/transition';
  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher();

  export let currentRoute = "";
  export let routes: { label: string; link: string; linkNoLang: string }[];
</script>

<div
  class="absolute bg-black/20 h-screen w-full backdrop-blur-sm"
  on:click={() => {
    dispatch('closemenu');
  }}
  in:fade={{ duration: 200 }}
  out:fade={{ duration: 50 }}
/>
<ul
  class="absolute w-full bg-red border-red-light border-y-8 text-white"
  in:slide={{ duration: 200 }}
  out:slide={{ duration: 50 }}
>
  {#each routes as route}
    <li
      class:bg-red-light={route.linkNoLang === currentRoute}
      on:click={() => {
        dispatch('closemenu');
      }}
    >
      <a class="block px-2 py-4 text-white" href={route.link}>
        {route.label}
      </a>
    </li>
  {/each}
</ul>

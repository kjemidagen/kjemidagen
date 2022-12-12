<script lang="ts">
  import { slide, fade } from 'svelte/transition';
  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher();

  export let currentRoute: string;
  export let routes: { label: string; link: string; linkNoLang: string }[];
</script>

<div
  class="absolute h-screen w-full bg-black/20 backdrop-blur-sm"
  on:click={() => {
    dispatch('closemenu');
  }}
  in:fade|local={{ duration: 200 }}
  out:fade|local={{ duration: 50 }}
/>
<ul
  class="absolute w-full border-y-8 border-red-light bg-red text-white"
  in:slide|local={{ duration: 200 }}
  out:slide|local={{ duration: 50 }}
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

<script lang="ts">
  import { slide, fade } from 'svelte/transition';
  import { createEventDispatcher } from 'svelte';
  import InfoPill from '$lib/components/InfoPill.svelte';

  const dispatch = createEventDispatcher();

  export let currentRoute = '';
  export let routes: { label: string; link: string; linkNoLang: string; new?: boolean }[];
</script>

<div 
  class="absolute h-screen w-full bg-black/20 backdrop-blur-sm" 
  on:click={() => dispatch('closemenu')}
  on:keydown={(e) => e.key === 'Escape' && dispatch('closemenu')}
  role="button"
  tabindex="0"
  aria-label="Close menu"
  in:fade={{ duration: 200 }}
  out:fade={{ duration: 50 }}
/>
<ul
  class="bg-red border-red-light absolute w-full border-y-8 text-white"
  in:slide={{ duration: 200 }}
  out:slide={{ duration: 50 }}
>
  {#each routes as route}
    <li class:bg-red-light={route.linkNoLang === currentRoute}>
      <a 
        class="block px-2 py-4 text-white" 
        href={route.link}
        on:click={() => {
          dispatch('closemenu');
        }}
      >
        {route.label}
        <InfoPill
          class="transistion-all ml-2 h-fit duration-500 {route.new
            ? 'visible'
            : 'hidden'} bg-blue-500 text-sm"
        ></InfoPill>
      </a>
    </li>
  {/each}
</ul>

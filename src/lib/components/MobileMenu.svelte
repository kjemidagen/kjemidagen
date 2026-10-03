<script lang="ts">
  import { slide, fade } from 'svelte/transition';
  import { createEventDispatcher } from 'svelte';
  import InfoPill from '#lib/components/InfoPill.svelte';

  const dispatch = createEventDispatcher();

  interface Props {
    currentRoute?: string;
    routes: { label: string; link: string; linkNoLang: string; new?: boolean }[];
  }

  let { currentRoute = '', routes }: Props = $props();
</script>

<div
  class="absolute h-screen w-full bg-black/20 backdrop-blur-sm"
  onclick={() => dispatch('closemenu')}
  onkeydown={(e) => e.key === 'Escape' && dispatch('closemenu')}
  role="button"
  tabindex="0"
  aria-label="Close menu"
  in:fade={{ duration: 200 }}
  out:fade={{ duration: 50 }}
></div>
<ul
  class="absolute w-full border-y-8 border-red-light bg-red text-white"
  in:slide={{ duration: 200 }}
  out:slide={{ duration: 50 }}
>
  {#each routes as route}
    <li class:bg-red-light={route.linkNoLang === currentRoute}>
      <a
        class="block px-2 py-4 text-white"
        href={route.link}
        onclick={() => {
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

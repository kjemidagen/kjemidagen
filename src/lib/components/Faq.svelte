<script lang="ts">
  import { Icon } from '@steeze-ui/svelte-icon';
  import { ChevronDown } from '@steeze-ui/heroicons';
  import { slide } from 'svelte/transition';

  export let question: string;
  export let answer: string;
  export let linkUrl: string | null = null;   // optional
  export let linkLabel: string | null = null; // optional

  let open = false;
</script>

<div class="bg-red text-white text-2xl font-medium p-5">
  <button
    class="w-full flex items-center justify-between text-left"
    on:click={() => (open = !open)}
    aria-expanded={open}
  >
    <span class="font-medium break-words whitespace-normal">{question}</span>
    <span
      class="transition-transform flex-shrink-0 duration-200"
      style:transform={`rotate(${open ? 180 : 0}deg)`}
    >
      <Icon src={ChevronDown} size="1.25em" theme="outline" />
    </span>
  </button>

  {#if open}
    <div class="mt-3 text-white/90 leading-7 text-base" transition:slide>
      {@html answer}
      
      {#if linkUrl && linkLabel}
        <a
          href={linkUrl}
          target="_blank"
          rel="noopener noreferrer"
          class="text-white underline hover:text-white/70 transition"
        >
          {linkLabel}
        </a>
      {/if}
    </div>
  {/if}
</div>

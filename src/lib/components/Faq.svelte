<script lang="ts">
  import { Icon } from '@steeze-ui/svelte-icon';
  import { ChevronDown } from '@steeze-ui/heroicons';
  import { slide } from 'svelte/transition';

  export let question: string;
  export let answer: string;

  let open = false;
</script>

<div class="bg-red text-white text-2xl font-medium p-5">
  <button
    class="w-full flex items-center justify-between text-left"
    on:click={() => (open = !open)}
    aria-expanded={open}
  >
    <span class="font-medium">{question}</span>
    <span
      class="transition-transform duration-200"
      style:transform={`rotate(${open ? 180 : 0}deg)`}
    >
      <Icon src={ChevronDown} size="1.25em" theme="outline" />
    </span>
  </button>

  {#if open}
    <div class="mt-3 text-white/90 leading-7 text-base" transition:slide>
      {@html answer}
    </div>
  {/if}
</div>

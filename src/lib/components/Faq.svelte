<script lang="ts">
  import { Icon } from '@steeze-ui/svelte-icon';
  import { ChevronDown } from '@steeze-ui/heroicons';
  import { slide } from 'svelte/transition';

  interface Props {
    question: string;
    answer: string;
    linkUrl?: string | null; // optional
    linkLabel?: string | null; // optional
  }

  let { question, answer, linkUrl = null, linkLabel = null }: Props = $props();

  let open = $state(false);
</script>

<div class="bg-red p-5 text-2xl font-medium text-white">
  <button
    class="flex w-full items-center justify-between text-left"
    onclick={() => (open = !open)}
    aria-expanded={open}
  >
    <span class="whitespace-normal break-words font-medium">{question}</span>
    <span
      class="flex-shrink-0 transition-transform duration-200"
      style:transform={`rotate(${open ? 180 : 0}deg)`}
    >
      <Icon src={ChevronDown} size="1.25em" theme="outline" />
    </span>
  </button>

  {#if open}
    <div class="mt-3 text-base leading-7 text-white/90" transition:slide>
      {@html answer}

      {#if linkUrl && linkLabel}
        <a
          href={linkUrl}
          target="_blank"
          rel="noopener noreferrer"
          class="text-white underline transition hover:text-white/70"
        >
          {linkLabel}
        </a>
      {/if}
    </div>
  {/if}
</div>

<script lang="ts">
  import { MapPin, Clock } from '@steeze-ui/heroicons';
  import { Icon } from '@steeze-ui/svelte-icon';

  export let title: string;
  export let time: string = "";
  export let location: string = "";
</script>

<div class="bg-red my-2 p-4 pb-6 text-white">
  <h3 class="mt-4 mb-2 text-2xl font-medium">
    {title}
  </h3>
  {#if (location || time)}
    <span class="inline-flex items-center justify-center">
      {#if time}
        <Icon
          src={Clock}
          size="1.5em"
          theme="solid"
          class="my-auto mr-2 inline leading-none text-white"
        />
        <strong class="leading-1 mr-8 block text-white">{time}</strong>
      {/if}
      {#if location}
        <Icon
          src={MapPin}
          size="1.5em"
          theme="solid"
          class="my-auto mr-2 inline leading-none text-white"
        />
        <strong class="leading-1 text-white">{location}</strong>
      {/if}
    </span>
  {/if}
  <slot />
</div>

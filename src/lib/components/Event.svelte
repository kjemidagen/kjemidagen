<script lang="ts">
  import { MapPin, Clock } from '@steeze-ui/heroicons';
  import { Icon } from '@steeze-ui/svelte-icon';

  export let title: string;
  export let time = '';
  export let location = '';
  export let loc_link = '';
  export let image = '';
</script>

<div class="bg-red p-4 text-white {image ? 'flex flex-col gap-4 lg:flex-row' : ''}">
  <div class="flex-1">
    <h3 class="mb-2 mt-4 text-2xl font-medium">
      {title}
    </h3>
    {#if location || time}
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
          {#if loc_link}
          <a href={loc_link} target="_blank" rel="noopener noreferrer"><strong class="leading-1 text-white">{location}</strong></a>
          {:else}
          <strong class="leading-1 text-white">{location}</strong>
          {/if}
        {/if}
      </span>
    {/if}
    <slot />
  </div>
  {#if image}
    <img
      src={image}
      alt="{title} image"
      class="order-first col-span-1 aspect-[3/1] content-center bg-white object-contain p-8 lg:order-last lg:aspect-square lg:w-1/5 lg:p-4"
    />
  {/if}
</div>

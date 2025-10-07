<script lang="ts">
  import { MapPin, Clock, Link, ArrowTopRightOnSquare } from '@steeze-ui/heroicons';
  import { Icon } from '@steeze-ui/svelte-icon';
  import {t, locale} from '$lib/translations/translations';

  export let title: string;
  export let deadline = '';
  export let location = '';
  export let image = '';
  export let link = '';
  export let company = '';
  export let slug = '';
  export let applicationLink = '';
</script>

<div class="bg-red grid grid-cols-1 gap-2 p-4 text-white md:grid-cols-5 md:gap-8">
  <img
    src={image}
    alt="{title} logo"
    class="aspect-video max-h-full w-full bg-white object-contain object-center p-4 md:col-span-1 md:aspect-square"
  />
  <div class="md:col-span-4 grid grid-cols-1 gap-1">
    <h3 class="text-2xl font-medium">
      {title}
    </h3>
    {#if company || location || deadline || link}
      <div class="grid grid-cols-1 gap-2 md:flex md:flex-wrap md:gap-12">
        {#if company}
          <div class="flex flex-inline items-center justify-center">
            {company}
          </div>
        {/if}
        {#if deadline}
          <div class="flex-inline flex items-center">
            <Icon
              src={Clock}
              size="1.5em"
              theme="solid"
              class="my-auto mr-2 inline leading-none text-white"
            />
            <strong class="text-white">{deadline}</strong>
          </div>
        {/if}
        {#if location}
          <div class="flex-inline flex items-center">
            <Icon
              src={MapPin}
              size="1.5em"
              theme="solid"
              class="my-auto mr-2 inline leading-none text-white"
            />
            <strong class="text-white">{location}</strong>
          </div>
        {/if}
        {#if link}
          <div class="flex-inline flex items-center">
            <Icon
              src={Link}
              size="1.5em"
              theme="solid"
              class="my-auto mr-2 inline leading-none text-white"
            />
            <strong class="text-white">{link}</strong>
          </div>
        {/if}
      </div>
    {/if}
    <slot />
    <div class="flex flex-row space-x-2">
      <a
        href="jobs/{slug}"
        class="flex-inline text-red flex items-center rounded-lg border-2 border-white bg-white px-4 py-2"
      >
        <strong>{$t(`jobs.read_more`)}</strong>
      </a>
      {#if applicationLink}
      <a
        href={applicationLink}
        target="_blank"
        class="flex-inline flex items-center space-x-2 rounded-lg border-2 border-white px-4 py-2"
      >
        <span class="text-white">{$t(`jobs.apply`)}</span>
        <Icon
          src={ArrowTopRightOnSquare}
          size="1.5em"
          theme="solid"
          class="my-auto inline text-white"
        />
      </a>
      {/if}
    </div>
  </div>
</div>

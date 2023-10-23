<script lang="ts">
  import { t} from '$lib/translations/translations';

  import kdLogo from '$lib/assets/logo.svg';
  
  import { page } from '$app/stores';

  import { jobsMap } from '../Jobs.svelte';
  import { error } from '@sveltejs/kit';

  import { MapPin, Clock, Link, ArrowTopRightOnSquare } from '@steeze-ui/heroicons';
  import { Icon } from '@steeze-ui/svelte-icon';

  if (jobsMap.filter((e) => e.slug == $page.params.slug).length === 0) {
    throw error(404, { message: 'Page not found' });
  }
  const job = jobsMap.filter((e) => e.slug == $page.params.slug)[0];
</script>

<svelte:head>
  <title>{$t('common.jobs')}</title>
</svelte:head>

<section class="jobs" id="jobs">
  <div class="content grid grid-cols-1 gap-4 md:grid-cols-6 content-start items-start">
    <div class="col-span-1 md:col-span-4">
      <h1 class="mb-8 text-3xl">{$t(`jobs.${job.slug}.title`)}</h1>

      {@html job.long_description}
    </div>
    <div class="bg-red order-last p-4 md:col-span-2 self-start sticky top-20">
      <img
        src={jobsMap.filter((e) => e.slug == job.slug)[0].image}
        alt="${$t(`jobs.${job.slug}.title`)} logo"
        class="aspect-[2/1] w-full bg-white object-contain object-center p-4"
      />
      <div class="md:col-span-4">
        {#if job.company || job.location || $t(`jobs.${job.slug}.deadline`) || job.link}
          <div class="mt-4 grid grid-cols-1 gap-2 text-white">
            {#if job.company}
              <div class="flex-inline items-center justify-center">
                {job.company}
              </div>
            {/if}
            {#if $t(`jobs.${job.slug}.deadline`)}
              <div class="flex-inline flex items-center">
                <Icon
                  src={Clock}
                  size="1.5em"
                  theme="solid"
                  class="my-auto mr-2 inline leading-none "
                />
                <strong class="">{$t(`jobs.${job.slug}.deadline`)}</strong>
              </div>
            {/if}
            {#if job.location}
              <div class="flex-inline flex items-center">
                <Icon
                  src={MapPin}
                  size="1.5em"
                  theme="solid"
                  class="my-auto mr-2 inline leading-none "
                />
                <strong class="">{job.location}</strong>
              </div>
            {/if}
            {#if job.link}
              <div class="flex-inline flex items-center">
                <Icon
                  src={Link}
                  size="1.5em"
                  theme="solid"
                  class="my-auto mr-2 inline leading-none "
                />
                <strong class="">{job.link}</strong>
              </div>
            {/if}
          </div>
        {/if}
        <a
          href={job.applicationLink}
          target="_blank"
          class="mt-4 flex-inline flex w-fit items-center space-x-2 rounded-lg border-2 border-white px-4 py-2"
        >
          <span class="text-white">Søk her</span>
          <Icon
            src={ArrowTopRightOnSquare}
            size="1.5em"
            theme="solid"
            class="my-auto inline text-white"
          />
        </a>
      </div>
    </div>
  </div>
</section>

<style>
</style>

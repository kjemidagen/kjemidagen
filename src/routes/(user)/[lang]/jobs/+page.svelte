<script lang="ts">
  import { t } from '$lib/translations/translations';
  import Advert from '$lib/components/Advert.svelte';
  import kdlogo from '$lib/assets/logo.svg';
  import { jobsMap } from './Jobs.svelte';
</script>

<svelte:head>
  <title>{$t('common.jobs')}</title>
</svelte:head>

<section class="jobs" id="jobs">
  <div class="content">
    <div id="description">
      <h1 class="mb-8 text-3xl">{$t('jobs.title')}</h1>
      <p>
        {$t('jobs.description')}
      </p>
    </div>
    <div class="mt-4 grid grid-cols-1 gap-4">
      {#each jobsMap as job}
        <Advert
          title={$t(`jobs.${job.slug}.title`)}
          company={job.company}
          image={job.image}
          deadline={$t(`jobs.${job.slug}.deadline`)}
          location={job.location}
          link={job.link}
          slug={job.slug}
          applicationLink={job.applicationLink}
        >
            {job.short_description}
        </Advert>
      {/each}
    </div>
  </div>
</section>

<style>
</style>

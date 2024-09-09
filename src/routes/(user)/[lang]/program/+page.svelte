<script lang="ts">
  import { t } from '$lib/translations/translations';
  import Event from '$lib/components/Event.svelte';
  import presenterImg from '$lib/assets/presenter.jpg';
  import cambiLogo from '$lib/assets/cambi.svg';
  import norconsultLogo from '$lib/assets/norconsult.svg';
  import reinertsenLogo from '$lib/assets/reinertsen.svg';
  import carboncircleLogo from '$lib/assets/carbon_circle.svg';
  import bcsLogo from '$lib/assets/bcs.png';
</script>

<svelte:head>
  <title>{$t('common.program')}</title>
</svelte:head>

<section class="program" id="program">
  <div class="content">
    <h1 class="mb-8 text-3xl">{$t('program.title')}</h1>
    <p>
      {$t('program.description')}
    </p>
    <h3 class="mb-2 mt-8 text-2xl">{$t('program.day')}</h3>
    <div class="flex flex-col gap-2">
      <Event
        title="{$t('program.opening')}"
        time="10:00"
        location="{$t('program.opening_loc')}"
        loc_link="https://link.mazemap.com/DsnEdMUa"
        />
      <Event
        title="{$t('program.stands')}"
        time="10:15-15:00"
        location="{$t('program.stands_loc')}"
        loc_link="https://link.mazemap.com/DsnEdMUa"
        />
      <Event
        title="{$t('program.cv_check')}"
        time="10:15-15:00"
        location="{$t('program.cv_check_loc')}"
        loc_link="https://link.mazemap.com/DsnEdMUa"
        />
      <Event
        title="{$t('program.summerjob_marathon')}"
        time="11:15-12:00"
        location="{$t('program.summerjob_marathon_loc')}"
        loc_link="https://link.mazemap.com/DsnEdMUa"
        >
          <p class="mt-3 leading-7">
            {$t('program.summerjob_marathon_desc')}
          </p>
      </Event>
      <Event
        title="{$t('program.job_marathon')}"
        time="13:15-14:00"
        location="{$t('program.job_marathon_loc')}"
        loc_link="https://link.mazemap.com/DsnEdMUa"
        >
          <p class="mt-3 leading-7">
            {$t('program.job_marathon_desc')}
          </p>
      </Event>
      <Event
        title="{$t('program.banquet')}"
        time="18:30"
        location="{$t('program.banquet_loc')}"
        loc_link="https://www.google.no/maps/place/Frimurerlogen+Trondhjem+Selskapslokaler/@63.4300014,10.397319,17z/data=!3m1!4b1!4m6!3m5!1s0x466d319bd29d55b3:0xe0e4e3fdf8991cd1!8m2!3d63.4300014!4d10.3998939!16s%2Fg%2F1tgnvvrm?entry=ttu&g_ep=EgoyMDI0MDkwNC4wIKXMDSoASAFQAw%3D%3D"
        >
          <p class="mt-3 leading-7">
            {$t('program.banquet_desc')}
          </p>
      </Event>
    </div>

  </div>
</section>

<style>
</style>

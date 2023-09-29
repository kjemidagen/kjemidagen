<script lang="ts">
  import { t } from '$lib/translations/translations';
  import Event from '$lib/components/Event.svelte';
  import presenterImg from '$lib/assets/presenter.jpg';
  import cambiLogo from '$lib/assets/cambi.svg';
  import norconsultLogo from '$lib/assets/norconsult.svg';
  import reinertsenLogo from '$lib/assets/reinertsen.svg';
  import carboncircleLogo from '$lib/assets/carbon_circle.svg';
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
    <h3 class="mt-8 mb-2 text-2xl">{$t('frontpage.when')}</h3>
    <div class="flex flex-col gap-2">
      <Event title={$t('program.opening')} time="10:00" location={$t('program.opening_loc')} />
      <Event title={$t('program.stands')} time="10:15 - 15:00" location="Realfagbygget" />
      <Event
        title="{$t('program.speedinterview')} Cambi"
        time="10:30 - 13:00"
        location="BU1-108"
        image={cambiLogo}
      >
        <p class="mt-3 leading-7">
          {$t('program.speedinterview_cambi')}
        </p>
      </Event>
      <Event title={$t('program.cvphoto')} time="11:00 - 13:00" location="R21"></Event>
      <Event title={$t('program.summerjob')} time="11:15 - 12:00" location="R5">
        <p class="mt-3 leading-7">
          {$t('program.summerjob_p')}
        </p>
      </Event>
      <Event
        title="{$t('program.speedinterview')} Norconsult"
        time="12:00 - 16:00"
        location="K4-173"
        image={norconsultLogo}
      >
        <p class="mt-3 leading-7">
          {$t('program.speedinterview_norconsult')}
        </p>
      </Event>
      <Event title={$t('program.motivationalspeaking')} time="12:30 - 13:15" location="R5">
        <div class="grid grid-cols-1 gap-8 lg:-mb-8 lg:mr-8 lg:grid-cols-3">
          <p class="mt-3 leading-7 lg:col-span-2">
            {$t('program.motivationalspeaking_p')}
          </p>
          <img
            src={presenterImg}
            alt="Foredragsholder"
            class="order-first aspect-square h-auto w-full rounded-full object-cover object-top lg:order-last lg:-translate-y-8"
          />
        </div>
      </Event>
      <Event
        title="{$t('program.speedinterview')} Reinertsen"
        time="13:00 - 15:00"
        location="K4-172"
        image={reinertsenLogo}
      >
        <p class="mt-3 leading-7">
          {$t('program.speedinterview_reinertsen')}
        </p>
      </Event>
      <Event title={$t('program.jobmarathon')} time="13:15 - 14:00" location="R8">
        <p class="mt-3 leading-7">
          {$t('program.jobmarathon_p')}
        </p>
      </Event>
      <Event title={$t('program.banquet')} time="18:30" location={$t('program.banquet_loc')}>
        <p class="mt-3 leading-7">
          {$t('program.banquet_p')}
        </p>
      </Event>
    </div>
    <h3 class="mt-8 mb-2 text-2xl">{$t('program.day_after')}</h3>
    <div class="flex flex-col gap-2">
      <Event
        title="{$t('program.speedinterview')} Carbon Circle"
        time="10:00 - 15:00"
        location="K4-173"
        image={carboncircleLogo}
      >
        <p class="mt-3 leading-7">
          {$t('program.speedinterview_carboncircle')}
        </p>
      </Event>
    </div>
  </div>
</section>

<style>
</style>

<script lang="ts">
  import { t } from '$lib/translations/translations';
  import Event from '$lib/components/Event.svelte';
  import presenterImg from '$lib/assets/presenter.jpg';
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
    <h3 class="mt-8 text-2xl">{$t('frontpage.when')}</h3>
    <div class="">
      <Event title={$t('program.opening')} time="10:00" location={$t('program.opening_loc')} loc_link="https://link.mazemap.com/Z9qjgaJT" />
      <Event title={$t('program.stands')} time="10:15 - 15:00" location="Realfagbygget" loc_link="https://maps.app.goo.gl/wuCwKedeZXWjpbH56" />
      <Event title={$t('program.speedinterview')} time="10:15 - 15:00">
        <p class="mt-3 leading-7">
          {$t('program.speedinterview_p')}
        </p>
      </Event>
      <Event title={$t('program.cvphoto')} time="11:00 - 13:00" location="R21" loc_link="https://link.mazemap.com/Qw6ZzVYJ"></Event>
      <Event title={$t('program.summerjob')} time="11:15 - 12:00" location="R5" loc_link="https://link.mazemap.com/TFErG7Yc">
        <p class="mt-3 leading-7">
          {$t('program.summerjob_p')}
        </p>
      </Event>
      <Event title={$t('program.motivationalspeaking')} time="12:30 - 13:15" location="R5" loc_link="https://link.mazemap.com/TFErG7Yc">
        <div class="grid grid-cols-1 gap-8 lg:-mb-8 lg:mr-8 lg:grid-cols-3">
          <p class="mt-3 leading-7 lg:col-span-2">
            {$t('program.motivationalspeaking_p')}
          </p>
          <img
            src={presenterImg}
            alt="Foredragsholder"
            class="aspect-square h-auto w-full rounded-full object-cover object-top lg:-translate-y-8"
          />
        </div>
      </Event>
      <Event title={$t('program.jobmarathon')} time="13:15 - 14:00" location="R8" loc_link="https://link.mazemap.com/3r8RBH45">
        <p class="mt-3 leading-7">
          {$t('program.jobmarathon_p')}
        </p>
      </Event>
      <Event title={$t('program.banquet')} time="18:30" location={$t('program.banquet_loc')} loc_link="https://maps.app.goo.gl/MfvfL1mPSe1oVTQJ8">
        <p class="mt-3 leading-7">
          {$t('program.banquet_p')}
        </p>
      </Event>
    </div>
  </div>
</section>

<style>
</style>

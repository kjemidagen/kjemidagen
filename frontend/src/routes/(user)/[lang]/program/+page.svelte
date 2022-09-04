

<script lang="ts">
  import { t } from '$lib/translations/translations';
</script>

<svelte:head>
  <title>{$t('common.program')}</title>
</svelte:head>

<section class="program" id="program">
  <div class="content">
    <h1 class="text-3xl mb-8">{$t('program.title')}</h1>
    <figure class="table grid max-w-lg mb-16 text-lg mx-auto font-medium ">
      <div>10:00</div>
      <div>{$t('program.opening')}</div>
      <div>10:15 - 15:00</div>
      <div>{$t('program.stands')}</div>
      <div>10:15 - 15:00</div>
      <div>{$t('program.speedinterview')}</div>
      <div>10:30 - 13:00</div>
      <div>{$t('program.cvphoto')}</div>
      <div>11:15</div>
      <div>{$t('program.motivationalspeaking')}</div>
      <div>13:15</div>
      <div>{$t('program.summerjob')}</div>
      <div>14:00</div>
      <div>{$t('program.jobmarathon')}</div>
      <div>18:30</div>
      <div>{$t('program.banquet')}</div>
    </figure>
    <div class="my-8">
      <h3 class="font-medium text-xl my-4">{$t('program.speedinterview')}</h3>
      <p>
        {$t('program.speedinterview_p')}
      </p>
      <h3 class="font-medium text-xl my-4">{$t('program.summerjob')}</h3>
      <p>
        {$t('program.summerjob_p')}
      </p>
      <h3 class="font-medium text-xl my-4">{$t('program.jobmarathon')}</h3>
      <p>
        {$t('program.jobmarathon_p')}
      </p>
      <h3 class="font-medium text-xl my-4">{$t('program.banquet')}</h3>
      <p>
        {$t('program.banquet_p')}
      </p>
    </div>
  </div>
</section>

<style>
  .table {
    grid-template-columns: minmax(auto, 1fr) 1fr;
  }
</style>

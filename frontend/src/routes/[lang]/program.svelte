<script lang="ts">
  import { browser } from '$app/env';
  export const hydrate = true;
  export const router = browser;
  export const prerender = true;
  import { t } from '$lib/translations/translations';
</script>

<svelte:head>
  <title>{$t('common.program')}</title>
</svelte:head>

<section class="program" id="program">
  <div class="content">
    <h1 class="text-3xl mb-8">{$t('program.title')}</h1>
    <table class="grid max-w-lg mb-16 text-lg mx-auto font-medium ">
      <td>10:00</td> <td>{$t('program.opening')}</td>
      <td>10:15 - 15:00</td> <td>{$t('program.stands')}</td>
      <td>10:15 - 15:00</td> <td> {$t('program.speedinterview')} </td>
      <td>10:30 - 13:00</td> <td> {$t('program.cvphoto')} </td>
      <td>11:15</td> <td> {$t('program.motivationalspeaking')} </td>
      <td>13:15</td> <td> {$t('program.summerjob')} </td>
      <td>14:00</td> <td>{$t('program.jobmarathon')} </td>
      <td>18:30</td> <td>{$t('program.banquet')} </td>
    </table>
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
  table {
    grid-template-columns: minmax(auto, 1fr) 1fr;
  }
</style>

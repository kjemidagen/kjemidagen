<script lang="ts">
  import { t } from '$lib/translations/translations';
  import companyMap1 from '$lib/assets/standkart/standkart_tirsdag_14_oktober.jpeg';
  import companyMap2 from '$lib/assets/standkart/standkart_onsdag_15_oktober.jpeg';

  // Get today's date
  const today = new Date();

  // Set the cutoff date (October 15)
  const cutoffDate = new Date(today.getFullYear(), 9, 15); // Month is 0-indexed, so 9 = October

  // Default selectedDay based on date, cutoff date is given as October 15 00:00:00, so on the 15th it should show day 2.
  let selectedDay = today > cutoffDate ? 2 : 1;
</script>

<svelte:head>
  <title>{$t('common.map')}</title>
</svelte:head>

<section class="map">
  <div class="content" id="map">
    <h1 class="text-3xl mb-8">{$t('map.title')}</h1>
    <div class="flex mt-6 w-full px-2 gap-6 overflow-visible">
      <button
      class="folder-tab flex-1 px-6 py-3 rounded-t-lg border-b-2 transition-colors duration-200 font-semibold flex items-center justify-center
        {selectedDay === 1 ? 'bg-red text-white border-red-800 shadow-[0_10px_15px_rgba(0,0,0,0.7)]' : 'bg-red-light text-white border-red-700 opacity-60 shadow-[0_3px_6px_rgba(0,0,0,0.2)]'}"
      on:click={() => selectedDay = 1}
      type="button"
      >
      {$t('map.day1')}
      </button>
      <button
      class="folder-tab flex-1 px-6 py-3 rounded-t-lg border-b-2 transition-colors duration-200 font-semibold flex items-center justify-center
        {selectedDay === 2 ? 'bg-red text-white border-red-800 shadow-[0_10px_15px_rgba(0,0,0,0.7)]' : 'bg-red-light text-white border-red-700 opacity-60 shadow-[0_3px_6px_rgba(0,0,0,0.2)]'}"
      on:click={() => selectedDay = 2}
      type="button"
      >
      {$t('map.day2')}
      </button>
    </div>

    <div class="folder-content w-full relative aspect-[1.414/1]">
  <img
    src={companyMap1}
    alt="Map of the stands in Realfagsbygget, first day"
    class="w-full absolute top-0 left-0 transition-opacity duration-150
           {selectedDay === 1 ? 'opacity-100 z-10' : 'opacity-0 z-0'}"
  />
  <img
    src={companyMap2}
    alt="Map of the stands in Realfagsbygget, second day"
    class="w-full absolute top-0 left-0 transition-opacity duration-150
           {selectedDay === 2 ? 'opacity-100 z-10' : 'opacity-0 z-0'}"
  />
</div>
  </div>
</section>

<script lang="ts">
  import { t } from '$lib/translations/translations';
  import companyMap1 from '$lib/assets/standkart/1.jpg';
  import companyMapU1 from '$lib/assets/standkart/u1.jpg';
</script>

<svelte:head>
  <title>{$t('common.map')} • {$t('common.chemday')}</title>
</svelte:head>

<section class="map">
  <div class="content" id="map">
    <h1 class="mb-8 text-3xl">{$t('common.map')}</h1>
    <p class="text-lg">{$t('map.intro')}</p>
    <div class="flex flex-col lg:-mx-20 lg:flex-row lg:gap-2">
      <div class="my-1">
        <img src={companyMap1} alt="Map of the stands in etg 1" />
      </div>
      <div class="my-1">
        <img src={companyMapU1} alt="Map of the stands in etg u1" />
      </div>
    </div>
  </div>
</section>

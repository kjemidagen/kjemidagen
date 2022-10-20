<script lang="ts">
  import { t } from '$lib/translations/translations';
  import companyMap from '$lib/assets/map.jpg';
</script>

<svelte:head>
  <title>{$t('common.map')}</title>
</svelte:head>

<section class="map">
  <div class="content" id="map">
    <h1 class="text-3xl mb-8">{$t('common.map')}</h1>
    <p class="text-lg">{$t('map.intro')}</p>
    <img src={companyMap} alt="Map of the stands" />
  </div>
</section>

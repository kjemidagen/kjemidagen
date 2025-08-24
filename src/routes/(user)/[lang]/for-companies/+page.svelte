<script lang="ts">
  import { t } from '$lib/translations/translations';
</script>

<svelte:head>
  <title>{$t('common.for-companies')}</title>
</svelte:head>

<section class="for-companies">
  <div class="content" id="for-companies">
    <h1 class="text-3xl mb-8">{$t('for-companies.information_header')}</h1>
    <p class="text-lg mb-8">
      {$t('for-companies.information_description')}
    </p>
    <h2 class="text-2xl mb-4">{$t('for-companies.equipment_header')}</h2>
    <p class="text-lg">
      {$t('for-companies.equipment_description')}
      <a href="https://dtms.aiutrix.com/reg/kd/exhibitorstand" target="_blank" rel="noopener" class="text-blue-600 underline hover:text-blue-800">{$t('for-companies.equipment_link')}</a>
    </p>
  </div>
</section>

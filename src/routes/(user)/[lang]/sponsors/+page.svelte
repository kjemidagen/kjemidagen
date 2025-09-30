<script lang="ts">
  import { t } from '$lib/translations/translations';
</script>

<svelte:head>
  <title>{$t('common.sponsors')}</title>
</svelte:head>

<section class="sponsors">
  <div class="content" id="sponsors">
    <h1 class="text-3xl mb-8">{$t('sponsors.sponsors')}</h1>
    <p class="text-lg">{$t('sponsors.intro')}</p>
    <br>
    <br>
    <p class="text-lg">
      {$t('sponsors.institutes')}
    </p>
    <ul class="text-lg list-disc list-inside">
      <li>{$t('sponsors.kjemiskprostek')}</li>
      <li>{$t('sponsors.materialtek')}</li>
      <li>{$t('sponsors.biotek_og_matvit')}</li>      
    </ul>
  </div>
</section>

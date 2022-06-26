<script lang="ts">
  import { t } from '$lib/translations/translations';
</script>

<section class="banner" id="banner">
  <div class="grid grid-cols-3 mx-64 my-24">
    <img class="w-60" src="/logo.svg" alt="logo" />
    <div class="font-bold text-red col-span-2">
      <h1 class="text-7xl">{$t('common.chemday')}</h1>
      <h2 class="text-4xl">{$t('frontpage.when')}</h2>
      <h2 class="text-4xl">{$t('frontpage.where')}</h2>
    </div>
  </div>
</section>

<script lang="ts">
  import { t } from '$lib/translations/translations';
  import jotunImage from '$lib/assets/jotun.jpg';
  import samarbeidsForumImage from '$lib/assets/samarbeidsforum.jpg';
</script>

<svelte:head>
  <title>{$t('common.sponsors')}</title>
</svelte:head>

<section class="sponsors">
  <div class="content" id="sponsors">
    <h1 class="text-3xl mb-8">{$t('sponsors.sponsors')}</h1>
    <p class="text-lg">{$t('sponsors.intro')}</p>
    <!--<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 my-4">
      <img src={jotunImage} alt="Jotun logo" class="w-full h-full object-contain object-center" />
      <img src={samarbeidsForumImage} alt="Samarbeidsforum logo" class="w-full h-full object-contain object-center" />
    </div>
  -->
    <p class="text-lg">
      {$t('sponsors.institutes')}
    </p>
    <ul class="text-lg list-disc list-inside">
      <li>{$t('sponsors.ikp')}</li>
      <li>{$t('sponsors.ima')}</li>
    </ul>
  </div>
</section>

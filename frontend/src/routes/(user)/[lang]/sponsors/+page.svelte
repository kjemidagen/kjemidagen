<script lang="ts">
  import { t } from '$lib/translations/translations';
  import jotunImage from '$lib/assets/jotun.jpg';
  import samarbeidsForumImage from '$lib/assets/samarbeidsforum.jpg';
</script>

<svelte:head>
  <title>{$t('common.sponsors')} • {$t('common.chemday')}</title>
</svelte:head>

<section class="sponsors">
  <div class="content" id="sponsors">
    <h1 class="mb-8 text-3xl">{$t('sponsors.sponsors')}</h1>
    <p class="text-lg">{$t('sponsors.intro')}</p>
    <img src={jotunImage} alt="jotun logo" class="w-4/5 md:w-2/4" />
    <img src={samarbeidsForumImage} alt="samarbeidsforum logo" class="w-4/5 md:w-2/4" />
    <p class="text-lg">
      {$t('sponsors.institutes')}
    </p>
    <ul class="list-inside list-disc text-lg">
      <li>{$t('sponsors.ibt')}</li>
      <li>{$t('sponsors.ikp')}</li>
      <li>{$t('sponsors.ima')}</li>
    </ul>
  </div>
</section>

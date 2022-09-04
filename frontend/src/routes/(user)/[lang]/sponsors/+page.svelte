

<script lang="ts">
  import { t } from '$lib/translations/translations';
</script>

<svelte:head>
  <title>{$t('common.sponsors')}</title>
</svelte:head>

<section class="sponsors">
  <div class="content" id="sponsors">
    <h1 class="text-3xl mb-8">{$t('sponsors.sponsors')}</h1>
    <p class="text-lg">{$t('sponsors.moreinfo')}</p>
    <!-- <img src="/sponsors_22.png" alt="bedriftene som er med på kjemidagen" /> -->
  </div>
</section>

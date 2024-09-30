<script lang="ts">
  import { t } from '$lib/translations/translations';
  import companyImage from '$lib/assets/participant-logos.jpg';
</script>

<svelte:head>
  <title>{$t('common.companies')}</title>
</svelte:head>

<section class="companies">
  <div class="content" id="companies">
    <h1 class="text-3xl mb-8">{$t('companies.companies')}</h1>
    <p class="text-lg">{$t('companies.paragraph')}</p>
    <img src={companyImage} alt="Collage of companies participating" />
  </div>
</section>

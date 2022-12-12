<script lang="ts">
  import { t } from '$lib/translations/translations';
  import companyImage from '$lib/assets/bedrifter.jpg';
</script>

<svelte:head>
  <title>{$t('common.companies')} • {$t('common.chemday')}</title>
</svelte:head>

<section class="companies">
  <div class="content" id="companies">
    <h1 class="mb-8 text-3xl">{$t('companies.companies')}</h1>
    <p class="text-lg">{$t('companies.paragraph')}</p>
    <img src={companyImage} alt="Collage of companies participating" />
  </div>
</section>

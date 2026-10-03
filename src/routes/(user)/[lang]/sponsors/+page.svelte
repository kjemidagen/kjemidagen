<script lang="ts">
  import { t } from '#lib/translations/translations.js';
  import CompanyBox from './CompanyBox.svelte';
  import { companiesMap } from './Sponsors.svelte';
</script>

<svelte:head>
  <title>{$t('common.sponsors')}</title>
</svelte:head>

<section class="sponsors">
  <div class="content" id="sponsors">
    <h1 class="mb-8 text-3xl">{$t('sponsors.sponsors')}</h1>
    <p class="text-lg">{$t('sponsors.intro')}</p>
    <br />
  </div>
</section>

<div class="company-grid">
  {#each companiesMap as company}
    <CompanyBox picture={company.picture} border={company.border} link={company.link} />
  {/each}
</div>

<style>
  .company-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;

    max-width: 1000px;
    margin: 0 auto;
    padding: 24px;
  }

  @media (max-width: 900px) {
    .company-grid {
      grid-template-columns: repeat(3, 1fr);
    }
  }

  @media (max-width: 700px) {
    .company-grid {
      grid-template-columns: repeat(2, 1fr);
    }
  }

  @media (max-width: 450px) {
    .company-grid {
      grid-template-columns: 1fr;
    }
  }
</style>

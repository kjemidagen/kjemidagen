<script lang="ts">
  import { t } from '#lib/translations/translations.js';
  import CompanyBox from './CompanyBox.svelte';
  import { companiesMap } from './companiesMap.svelte';

  const companiesByDay = $derived(
    [
      { date: 1, label: $t('companies.date_1') },
      { date: 2, label: $t('companies.date_2') }
    ].map((day) => ({
      ...day,
      companies: companiesMap.filter((company) => company.days.includes(day.date))
    }))
  );
</script>

<svelte:head>
  <title>{$t('common.companies')}</title>
</svelte:head>

<section class="companies">
  <div class="content" id="companies">
    <h1 class="mb-8 text-3xl">{$t('companies.companies')}</h1>
    <p class="text-lg">{$t('companies.paragraph')}</p>
  </div>
</section>

{#each companiesByDay as day}
  <h2 class="day-heading">{day.label}</h2>

  <div class="company-grid">
    {#each day.companies as company}
      <CompanyBox picture={company.picture} border={company.border} link={company.link} />
    {/each}
  </div>
{/each}

<style>
  .day-heading {
    max-width: 1000px;
    margin: 32px auto 0;
    padding: 0 24px;
    font-size: 1.75rem;
  }

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

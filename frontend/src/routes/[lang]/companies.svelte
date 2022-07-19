<script lang="ts" context="module">
  export const hydrate = true;
  export const prerender = true;
</script>

<script lang="ts">
  import { t } from '$lib/translations/translations';
</script>

<svelte:head>
  <title>{$t('common.companies')}</title>
</svelte:head>

<section class="companies">
  <div class="content" id="companies">
    <h1 class="text-3xl mb-8">{$t('companies.companies')}</h1>
    <p class="text-lg">{$t('companies.moreinfo')}</p>
  </div>
</section>

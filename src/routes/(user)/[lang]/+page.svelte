<script lang="ts">
  import { t } from '$lib/translations/translations';
  import Hero from '$lib/3D/Hero.svelte';
  import logo from '$lib/3D/logo.svg';
</script>

<svelte:head>
  <title>{$t('common.chemday')}</title>
</svelte:head>

<section class="text-center py-20 bg-white">
  <img src="{logo}" alt="Halden Pharma Logo" class="mx-auto mb-8 w-32 md:w-48" />

  <h1 class="text-red text-5xl md:text-7xl font-[YourFontName] mb-4">
    Kjemidagen
  </h1>
  
  <h2 class="text-red text-3xl md:text-5xl font-[YourFontName] mb-2">
    14.-15. oktober 2025
  </h2>

  <h3 class="text-red text-2xl md:text-4xl font-[YourFontName]">
    Gløshaugen - Realfagbygget
  </h3>
</section>

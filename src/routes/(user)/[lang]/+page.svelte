<script lang="ts">
  import { t, locale } from '$lib/translations/translations';
  import Hero from '$lib/3D/Hero.svelte';
  import bg_image from '$lib/assets/Kjemidagen_bakgrunn_potensiell.png';
  import logo from '$lib/3D/logo.svg';
</script>

<svelte:head>
  <title>{$t('common.chemday')}</title>
</svelte:head>

<div
  class="absolute inset-0 -z-10 w-full h-full bg-white bg-center bg-cover md:bg-[url('$lib/assets/Kjemidagen_bakgrunn_potensiell.png')]"
></div>

<section class="py-20 bg-transparent">
  <div class="max-w-2xl mx-auto px-4 text-center">
    <img src={logo} alt="Kjemidagen logo" class="mx-auto mb-8 w-32 md:w-48 drop-shadow-[0_2px_4px_rgba(0,0,0,0.15)]" />

    <h1 class="text-red text-5xl md:text-7xl mb-4 drop-shadow-2xl font-semibold">
      Kjemidagen
    </h1>
    
    <h2 class="text-red text-2xl md:text-4xl mb-2 drop-shadow-md">
      13.-14. oktober 2026
    </h2>

    <h3 class="text-red text-lg md:text-2xl mb-6 drop-shadow-md">
      Gløshaugen - Realfagbygget
    </h3>

    <hr class="my-8 border-red/30 mx-auto w-4/6" />
<section class="hero" id="hero">
  <!-- fake border top -->
  <div class="relative -top-2 left-0 z-30 border-t-8 -mx-2 border-red-light" />
  <Hero />
  <div class="force-space flex flex-col h-[80vh] mx-auto max-w-3xl pointer-events-none">
    <div class="m-auto flex flex-col items-center">
    <div
        class="px-6 py-8 md:p-16 bg-black/60 backdrop-blur-md rounded-xl border-red/20 border z-10 pointer-events-auto"
      >
        <h1 class="mb-4 font-bold text-red text-4xl md:text-7xl">{$t('common.chemday')}</h1>
        <h2 class="mb-2 text-lg text-white md:text-3xl">{$t('frontpage.when')}</h2>
        <h2 class="mb-1 text-lg text-white md:text-3xl">{$t('frontpage.where')}</h2>
      </div>
      <a href="/{$locale}/interest">
      <button class="py-3 px-5 m-2 mx-auto bg-black/60 backdrop-blur-md hover:bg-black/50 rounded-xl border-red/20 border z-10 pointer-events-auto">
        <span class="mb-1 text-lg text-white md:text-xl">{$t('frontpage.interest')}</span>
      </button>
      </a>
    </div>
  </div>
</section>

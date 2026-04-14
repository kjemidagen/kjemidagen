<script lang="ts">
  import { t, locale } from '$lib/translations/translations';
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
  </div>
 <div class="flex justify-center">
  <a href="/{$locale}/interest">
    <button
      class="py-3 px-8 mt-4 
             bg-red hover:bg-red/90
             text-white text-lg md:text-xl font-medium
             rounded-xl 
             shadow-lg hover:shadow-red/30
             transition-all duration-300
             border border-red/30">
      {$t('frontpage.interest')}
    </button>
  </a>
</div>
</section>

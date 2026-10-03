<script lang="ts">
  import { t, locale } from '#lib/translations/translations.js';
  import logo from '#lib/3D/logo.svg';
</script>

<svelte:head>
  <title>{$t('common.chemday')}</title>
</svelte:head>

<div
  class="absolute inset-0 -z-10 h-full w-full bg-white bg-cover bg-center md:bg-[url('#lib/assets/Kjemidagen_bakgrunn_potensiell.png')]"
></div>

<section class="bg-transparent py-20">
  <div class="mx-auto max-w-2xl px-4 text-center">
    <img
      src={logo}
      alt="Kjemidagen logo"
      class="mx-auto mb-8 w-32 drop-shadow-[0_2px_4px_rgba(0,0,0,0.15)] md:w-48"
    />

    <h1 class="mb-4 text-5xl font-semibold text-red drop-shadow-2xl md:text-7xl">Kjemidagen</h1>

    <h2 class="mb-2 text-2xl text-red drop-shadow-md md:text-4xl">13.-14. oktober 2026</h2>

    <h3 class="mb-6 text-lg text-red drop-shadow-md md:text-2xl">Gløshaugen - Realfagbygget</h3>

    <hr class="mx-auto my-8 w-4/6 border-red/30" />
  </div>
  <div class="flex justify-center">
    <a href="/{$locale}/interest">
      <button
        class="mt-4 rounded-xl border
             border-red/30 bg-red
             px-8 py-3 text-lg font-medium
             text-white
             shadow-lg transition-all
             duration-300 hover:bg-red/90
             hover:shadow-red/30 md:text-xl"
      >
        {$t('frontpage.interest')}
      </button>
    </a>
  </div>
</section>

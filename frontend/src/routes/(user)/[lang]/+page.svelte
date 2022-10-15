<script lang="ts">
  import { t } from '$lib/translations/translations';
  import Hero from '$lib/3D/Hero.svelte';
</script>

<svelte:head>
  <title>{$t('common.chemday')}</title>
</svelte:head>

<section class="hero" id="hero">
  <!-- fake border top -->
  <div class="relative -top-2 left-0 z-30 border-t-8 -mx-2 border-red-light" />
  <Hero />
  <div class="force-space flex h-[80vh] mx-auto max-w-3xl pointer-events-none">
    <div
      class="px-6 py-8 m-auto md:p-16 bg-black/60 backdrop-blur-md rounded-xl border-red/20 border z-10 pointer-events-auto"
    >
      <h1 class="mb-4 font-bold text-red text-4xl md:text-7xl">{$t('common.chemday')}</h1>
      <h2 class="mb-2 text-lg text-white md:text-3xl">{$t('frontpage.when')}</h2>
      <h2 class="mb-1 text-lg text-white md:text-3xl">{$t('frontpage.where')}</h2>
    </div>
  </div>
  <!-- fake border bottom -->
  <div class="relative -bottom-2 left-0 z-30 border-b-8 -mx-2 border-red-light" />
</section>

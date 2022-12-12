<script lang="ts">
  import { t } from '$lib/translations/translations';
  import Hero from '$lib/3D/Hero.svelte';
</script>

<svelte:head>
  <title>{$t('common.chemday')}</title>
</svelte:head>

<section class="hero" id="hero">
  <!-- fake border top -->
  <div class="relative -top-2 left-0 z-30 -mx-2 border-t-8 border-red-light" />
  <Hero />
  <div class="force-space pointer-events-none mx-auto flex h-[80vh] max-w-3xl">
    <div
      class="pointer-events-auto z-10 m-auto rounded-xl border border-red/20 bg-black/60 px-6 py-8 backdrop-blur-md md:p-16"
    >
      <h1 class="mb-4 text-4xl font-bold text-red md:text-7xl">{$t('common.chemday')}</h1>
      <h2 class="mb-2 text-lg text-white md:text-3xl">{$t('frontpage.when')}</h2>
      <h2 class="mb-1 text-lg text-white md:text-3xl">{$t('frontpage.where')}</h2>
    </div>
  </div>
  <!-- fake border bottom -->
  <div class="relative -bottom-2 left-0 z-30 -mx-2 border-b-8 border-red-light" />
</section>

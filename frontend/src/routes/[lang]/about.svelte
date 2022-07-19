<script lang="ts" context="module">
  export const hydrate = true;
  export const prerender = true;
</script>

<script lang="ts">
  import AboutCard from '$lib/components/AboutCard.svelte';
  import { t } from '$lib/translations/translations';
</script>

<svelte:head>
  <title>{$t('common.about')}</title>
</svelte:head>

<section class="about" id="about">
  <div class="flex flex-col">
    <div class="content m-auto">
      <h1 class="text-3xl mb-8">{$t('common.about')}</h1>
      <p class="text-md mb-2">{$t('about.paragraph')}</p>
      <h3 class="mt-5 mb-5 text-2xl">{$t('about.theboard')}</h3>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-2 m-auto">
        <AboutCard
          imgSrc="leder.jpg"
          name="Pia Nedreås"
          title={$t('about.leader')}
          email="leder@kjemidagen.no"
        />
        <AboutCard
          imgSrc="nestleder.jpg"
          name="Celina Ryholt"
          title={$t('about.deputy')}
          email="nestleder@kjemidagen.no"
        />
        <AboutCard
          imgSrc="okonomisjef.jpg"
          name="Herman Berggren"
          title={$t('about.economist')}
          email="økonomisjef@kjemidagen.no"
        />
        <AboutCard
          imgSrc="pr-sjef.jpg"
          name="Vivi Gunnarsrud"
          title={$t('about.prboss')}
          email="pr-sjef@kjemidagen.no"
        />
        <AboutCard
          imgSrc="rigg-sjef.jpg"
          name="Cecilie Bakketun"
          title={$t('about.rigg')}
          email="riggeansvarlig@kjemidagen.no"
        />
      </div>
    </div>
  </div>
</section>

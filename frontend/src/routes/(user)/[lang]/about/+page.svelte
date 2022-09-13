<script lang="ts">
  import AboutCard from '$lib/components/AboutCard.svelte';
  import { t } from '$lib/translations/translations';
  import lederSrc from '$lib/assets/styret/leder.jpg';
  import nestlederSrc from '$lib/assets/styret/nestleder.jpg';
  import okonomisjefSrc from '$lib/assets/styret/okonomisjef.jpg';
  import prsjefSrc from '$lib/assets/styret/pr-sjef.jpg';
  import riggsjefSrc from '$lib/assets/styret/rigg-sjef.jpg';
  // import riggsjefSrc from '$lib/assets/styret/default.jpg';
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
      <div class="m-auto gap-2 grid grid-cols-1 md:grid-cols-3 xl:grid-cols-5 xl:-mx-20">
        <AboutCard
          imgSrc={lederSrc}
          name="Pia Nedreås"
          title={$t('about.leader')}
          email="leder@kjemidagen.no"
        />
        <AboutCard
          imgSrc={nestlederSrc}
          name="Celina Ryholt"
          title={$t('about.deputy')}
          email="nestleder@kjemidagen.no"
        />
        <AboutCard
          imgSrc={okonomisjefSrc}
          name="Herman Berggren"
          title={$t('about.economist')}
          email="okonomisjef@kjemidagen.no"
        />
        <AboutCard
          imgSrc={prsjefSrc}
          name="Vivi Gunnarsrud"
          title={$t('about.prboss')}
          email="pr-sjef@kjemidagen.no"
        />
        <AboutCard
          imgSrc={riggsjefSrc}
          name="Cecilie Bakketun"
          title={$t('about.rigg')}
          email="riggeansvarlig@kjemidagen.no"
        />
      </div>
    </div>
  </div>
</section>

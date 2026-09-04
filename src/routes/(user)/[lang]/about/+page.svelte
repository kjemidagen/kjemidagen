<script lang="ts">
  import AboutCard from '$lib/components/AboutCard.svelte';
  import { t } from '$lib/translations/translations';

  import heroSrc from '$lib/assets/styret/hero.jpg';
  import headSrc from '$lib/assets/styret/head.jpg';
  import deputyHeadSrc from '$lib/assets/styret/deputy_head.jpg';
  import cfoSrc from '$lib/assets/styret/cfo.jpg';
  import prOfficerSrc from '$lib/assets/styret/pr_officer.jpg';
  import chiefRiggerSrc from '$lib/assets/styret/chief_rigger.jpg';
  import eventManagerSrc from '$lib/assets/styret/event_manager.jpg';
</script>

<svelte:head>
  <title>{$t('common.about')}</title>
</svelte:head>

<section class="about" id="about">
  <div class="flex flex-col">
    <div class="content m-auto">
      <div class="hero-image-wrapper">
        <img src={heroSrc} alt="Kjemidagen" class="hero-image" />
        <div class="hero-overlay">
          <h1>Om Kjemidagen</h1>
        </div>
      </div>
      <p class="text-md mb-2">{$t('about.paragraph')}</p>
      <h3 class="mt-5 mb-5 text-2xl">{$t('about.theboard')}</h3>
      <div class="m-auto gap-2 grid grid-cols-1 md:grid-cols-3 xl:grid-cols-3">
        <AboutCard
          imgSrc={headSrc}
          name="Stine Sagmyr"
          title={$t('about.leader')}
          email="leder@kjemidagen.no"
        />
        <AboutCard
          imgSrc={deputyHeadSrc}
          name="Astrid Fjeldstad Nerland"
          title={$t('about.deputy')}
          email="nestleder@kjemidagen.no"
        />
        <AboutCard
          imgSrc={cfoSrc}
          name="Thea Marøy Haugland"
          title={$t('about.cfo')}
          email="okonomiansvarlig@kjemidagen.no"
        />
      </div>
      <div class="m-auto gap-2 grid grid-cols-1 md:grid-cols-3 xl:grid-cols-3">
        <AboutCard
          imgSrc={prOfficerSrc}
          name="Celina Klefstad Storaker"
          title={$t('about.pr_officer')}
          email="pr-sjef@kjemidagen.no"
        />
        <AboutCard
          imgSrc={chiefRiggerSrc}
          name="Sivert Haga"
          title={$t('about.rigger')}
          email="riggeansvarlig@kjemidagen.no"
        />
        <AboutCard
          imgSrc={eventManagerSrc}
          name="Anna Horrigmoe"
          title={$t('about.event')}
          email="arrangement@kjemidagen.no"
        />
      </div>
    </div>
  </div>
</section>

<style>
  .content {
    max-width: 1100px;
  }

  .hero-image-wrapper {
    position: relative;
    width: 100%;
    margin-bottom: 2rem;
    border-radius: 1.5rem;
    overflow: hidden;
    box-shadow: 0 18px 35px rgba(0, 0, 0, 0.08);
  }

  .hero-image {
    display: block;
    width: 100%;
    height: clamp(220px, 32vw, 420px);
    object-fit: cover;
    object-position: center center;
    filter: saturate(0.95) contrast(1.02);
  }

  .hero-overlay {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: flex-end;
    justify-content: center;
    padding-bottom: 1.25rem;
    background: linear-gradient(to top, rgba(0, 0, 0, 0.36), rgba(0, 0, 0, 0.08));
  }

  .hero-overlay h1 {
    margin: 0;
    color: white;
    font-size: clamp(2rem, 4vw, 4rem);
    line-height: 1;
    font-weight: 800;
    letter-spacing: 0.02em;
    text-shadow: 0 2px 12px rgba(0, 0, 0, 0.35);
  }

  @media (max-width: 768px) {
    .hero-image {
      height: 220px;
    }

    .hero-overlay h1 {
      font-size: 2.25rem;
    }
  }
</style>

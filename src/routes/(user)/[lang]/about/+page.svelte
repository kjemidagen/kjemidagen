<script lang="ts">
  import AboutCard from '$lib/components/AboutCard.svelte';
  import { t } from '$lib/translations/translations';
  import headSrc from '$lib/assets/styret/head.jpg';
  import deputyHeadSrc from '$lib/assets/styret/deputy_head.jpg';
  import cfoSrc from '$lib/assets/styret/default.jpg';
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
      <h1 class="text-3xl mb-8">{$t('common.about')}</h1>
      <p class="text-md mb-2">{$t('about.paragraph')}</p>
      <h3 class="mt-5 mb-5 text-2xl">{$t('about.theboard')}</h3>
      <div class="m-auto gap-2 grid grid-cols-1 md:grid-cols-3 xl:grid-cols-3">
        <AboutCard
          imgSrc={headSrc}
          name="Emilie Hewitt"
          title={$t('about.leader')}
          email="leder@kjemidagen.no"
        />
        <AboutCard
          imgSrc={deputyHeadSrc}
          name="Stine Ødegård"
          title={$t('about.deputy')}
          email="nestleder@kjemidagen.no"
        />
        <AboutCard
          imgSrc={cfoSrc}
          name="Marcus Feruglio Tokvam"
          title={$t('about.cfo')}
          email="okonomiansvarlig@kjemidagen.no"
        />
      </div>
      <div class="m-auto gap-2 grid grid-cols-1 md:grid-cols-3 xl:grid-cols-3">
        <AboutCard
          imgSrc={prOfficerSrc}
          name="Sofie Sponberg Gundersen"
          title={$t('about.pr_officer')}
          email="pr-sjef@kjemidagen.no"
        />
        <AboutCard
          imgSrc={chiefRiggerSrc}
          name="Linus Backen"
          title={$t('about.rigger')}
          email="riggeansvarlig@kjemidagen.no"
        />
        <AboutCard
          imgSrc={eventManagerSrc}
          name="Maja Christine Stahl"
          title={$t('about.event')}
          email="arrangement@kjemidagen.no"
        />
      </div>
    </div>
  </div>
</section>

<script lang="ts">
  import { t } from '$lib/translations/translations';
  import Event from '$lib/components/Event.svelte';
  import presenterImg from '$lib/assets/presenter.jpg';
  import cambiLogo from '$lib/assets/cambi.svg';
  import norconsultLogo from '$lib/assets/norconsult.svg';
  import reinertsenLogo from '$lib/assets/reinertsen.svg';
  import carboncircleLogo from '$lib/assets/carbon_circle.svg';
  import bcsLogo from '$lib/assets/bcs.png';
</script>

<svelte:head>
  <title>{$t('common.program')}</title>
</svelte:head>

<section class="program" id="program">
  <div class="content">
    <h1 class="mb-8 text-3xl">{$t('program.title')}</h1>
    <p>
      {$t('program.description')}
    </p>
    

  </div>
</section>

<style>
</style>

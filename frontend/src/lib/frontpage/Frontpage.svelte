<script lang="ts">
  import { t } from 'svelte-intl-precompile';
</script>

<section class="frontpage" id="frontpage">
  <div class="content">
    <nav class="navigation">
      <ul>
        <li><a href="#about">{$t('nav.about')}</a></li>
        <li><a href="#program">{$t('nav.program')}</a></li>
        <li><a href="#companies">{$t('nav.companies')}</a></li>
        <li><a href="#contact">{$t('nav.contact')}</a></li>
        <!--<li><a href="challenge.html">Kjemidagen Challenge</a></li> -->
      </ul>
    </nav>
    <div class="frontpage-content">
      <p class="bigger">{$t('index.start')}</p>
      <p>{@html $t('index.text')}</p>
      <p>{$t('index.seeingyou')}</p>
    </div>
  </div>
  <img alt="jotun" src="/jotun.jpg" />
</section>

<style>
  .content {
    max-width: var(--document-width);
    margin: auto;
    display: grid;
    grid-template-columns: 1fr 1fr 2fr 1fr;
    grid-gap: 2rem;
    padding: 4rem 0;
  }
  .navigation {
    grid-column-start: 2;
  }

  p {
    margin-bottom: 1rem;
  }
  img {
    z-index: -1;
    object-fit: cover;
    height: 35rem;
    width: 100%;
  }
</style>

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
      <p>{$t('index.text')}</p>
      <p>{$t('index.seeingyou')}</p>
    </div>
  </div>
</section>

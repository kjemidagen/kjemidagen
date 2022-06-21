<script lang="ts">
  import { t } from '$lib/translations/translations';
</script>

<section class="about" id="about">
  <div class="content">
    <div class="about-intro">
      <h3>{$t('about.theboard')}</h3>
    </div>

    <div class="about-content">
      <article>
        <h4>Pia Nedreås</h4>
        <h5>{$t('about.leader')}</h5>
        <h5><a href="mailto:leder@kjemidagen.no">leder@kjemidagen.no</a></h5>
      </article>

      <article>
        <h4>Celina Ryholt</h4>
        <h5>{$t('about.deputy')}</h5>
        <h5><a href="mailto:nestleder@kjemidagen.no">nestleder@kjemidagen.no</a></h5>
      </article>

      <article>
        <h4>Herman Berggren</h4>
        <h5>{$t('about.economist')}</h5>
        <h5><a href="mailto:okonomiansvarlig@kjemidagen.no">okonomiansvarlig@kjemidagen.no</a></h5>
      </article>

      <article>
        <h4>Vivi Gunnarsrud</h4>
        <h5>{$t('prboss')}</h5>
        <h5><a href="mailto:pr-sjef@kjemidagen.no">pr-sjef@kjemidagen.no</a></h5>
      </article>

      <article>
        <h4>Cecilie Bakketun</h4>
        <h5>{$t('rigg')}</h5>
        <h5><a href="mailto:riggeansvarlig@kjemidagen.no">riggeansvarlig@kjemidagen.no</a></h5>
      </article>
    </div>
  </div>
</section>

<style>
  .content {
    max-width: var(--document-width);
    align-items: center;
    margin: auto;
    padding: 3rem 0;
  }
  h3,
  h4 {
    color: var(--color-text-base);
  }
  h3 {
    margin-bottom: 2rem;
  }
  p {
    color: #000;
  }
  .about-content {
    padding-top: 2rem;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-gap: 2rem;
  }
  img {
    z-index: -1;
    object-fit: cover;
    height: 35rem;
    width: 100%;
  }
</style>

<script lang="ts">
  import { t } from 'svelte-intl-precompile';
</script>

<section class="about" id="about">
  <div class="content">
    <div class="about-intro">
      <h3>{$t('about.header')}</h3>

      <p>{@html $t('about.intro')}</p>
    </div>

    <div class="about-content">
      <article>
        <h4>{$t('about.head1')}</h4>
        <p>{$t('about.par1')}</p>
      </article>

      <article>
        <h4>{$t('about.head2')}</h4>
        <p>{$t('about.par2')}</p>
      </article>

      <article>
        <h4>{$t('about.head3')}</h4>
        <p>{$t('about.par3')}</p>
      </article>
    </div>
  </div>
  <img src="exxon.jpg" alt="exxon" />
</section>

<style>
  .about {
    background: var(--color-bg-secondary);
  }
  .content {
    max-width: var(--document-width);
    align-items: center;
    margin: auto;
    padding: 3rem 0;
  }
  h3,
  h4 {
    color: var(--color-text-brand);
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

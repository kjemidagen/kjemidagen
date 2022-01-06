<script lang="ts">
  import { t } from 'svelte-intl-precompile';
</script>

<section class="about" id="about">
  <div class="content">
    <div class="about-intro">
      <h3>{$t('about.header')}</h3>

      <p>{$t('about.intro')}</p>
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
</section>

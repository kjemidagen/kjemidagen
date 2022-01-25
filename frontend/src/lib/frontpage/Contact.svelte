<script lang="ts">
  import { t } from 'svelte-intl-precompile';
</script>

<section class="contact" id="contact">
  <div class="content">
    <h3>{$t('contact.header')}</h3>

    <figure class="contact-image">
      <img src="/styret21.jpg" alt="styret 2021" />
    </figure>

    <p>{$t('contact.text')}</p>
    <p class="contact-email"><a href="mailto:kontakt@kjemidagen.no">kontakt@kjemidagen.no</a></p>
    <p>{$t('contact.footer')}</p>
  </div>
</section>

<style>
  .contact {
    background: var(--color-bg-secondary);
    color: var(--color-text-brand);
    padding: 40px 0;
  }
  .content {
    max-width: var(--document-width);
    margin: auto;
  }
  p {
    color: var(--color-text-base);
    text-align: center;
  }

  img {
    display: block;
    margin: 10px auto;
    max-width: 100%;
  }
  .contact-email {
    font-size: 2rem;
  }
  a {
    color: var(--color-text-base);
  }
</style>

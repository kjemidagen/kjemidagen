<script lang="ts">
  import { t } from 'svelte-intl-precompile';
</script>

<section class="companies">
  <div class="content" id="companies">
    <h3>{$t('companies.header')}</h3>
    <p>{$t('companies.text')}</p>
    <img src="companies_21.png" alt="bedriftene som er med på kjemidagen" />
  </div>
</section>

<style>
  .companies {
    background: var(--color-text-loud);
    color: var(--color-text-brand);
    padding: 40px 0;
  }
  .content {
    max-width: var(--document-width);
    margin: auto;
  }

  p {
    color: var(--color-text-base);
    padding: 0 1rem;
  }
  img {
    display: block;
    margin: 30px auto;
    max-width: 100%;
  }
</style>

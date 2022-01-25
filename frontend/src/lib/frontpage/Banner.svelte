<script lang="ts">
  import { t } from 'svelte-intl-precompile';
</script>

<section class="banner" id="banner">
  <div class="title">
    <h1>{$t('Kjemidagen')}</h1>
    <h2>{$t('date')}</h2>
  </div>
</section>

<style>
  section {
    position: relative;
    max-width: 100%;
    background: url('/header.jpg') no-repeat center center;
    background-size: cover;
    height: 600px;
  }
  .title {
    position: relative;
    top: 100px;
    left: 30px;
    max-width: var(--document-width);
    margin: 0 auto;
    padding: 65px 0 0 260px;
    background: url('/logo250.png') no-repeat;
  }

  h1 {
    text-decoration: none;
    color: var(--color-text-brand);
    font-size: 5rem;
  }
  h1:hover {
    text-decoration: none;
  }
  h2 {
    color: #fff;
    font-size: 6rem;
    line-height: 1;
  }
</style>

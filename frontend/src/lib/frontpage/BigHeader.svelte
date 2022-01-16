<script lang="ts">
  import { t } from 'svelte-intl-precompile';
</script>

<header class="header" id="header">
  <div class="title">
    <h1><a href="/">{$t('Kjemidagen')}</a></h1>
    <h2>{$t('date')}</h2>
  </div>
</header>

<style>
  header {
    position: relative;
    max-width: 100%;
    background: url('header.jpg') no-repeat center center;
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
    background: url('logo250.png') no-repeat;
  }

  h1 a {
    text-decoration: none;
    color: var(--color-text-brand);
    font-size: 5rem;
  }
  h1 a:hover {
    text-decoration: none;
  }
  h2 {
    color: #fff;
    font-size: 6rem;
    line-height: 1;
  }
</style>

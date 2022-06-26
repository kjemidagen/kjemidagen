<script lang="ts">
  import { t } from '$lib/translations/translations';
</script>

<section class="banner" id="banner">
  <div class="title">
    <h1>{$t('common.chemday')}</h1>
    <h2>{$t('frontpage.when')}</h2>
    <h2>{$t('frontpage.where')}</h2>
  </div>
</section>

<style>
  section {
    position: relative;
    max-width: 100%;
    background-size: cover;
    box-sizing: border-box;
  }
  .title {
    position: relative;
    top: 100px;
    left: 30px;
    max-width: 88rem;
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
    color: var(--color-text-brand);
    font-size: 6rem;
    line-height: 1;
  }
</style>

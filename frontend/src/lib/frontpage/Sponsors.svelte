<script lang="ts">
  import { t } from '$lib/translations/translations';
</script>

<section class="sponsors">
  <div class="content" id="sponsors">
    <h3>{$t('sponsors.sponsors')}</h3>
    <p>{$t('sponsors.moreinfo')}</p>
    <!-- <img src="/sponsors_22.png" alt="bedriftene som er med på kjemidagen" /> -->
  </div>
</section>

<style>
  .sponsors {
    background: var(--color-text-loud);
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

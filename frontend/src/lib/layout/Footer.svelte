<script lang="ts">
  import { t } from '$lib/translations/translations';
</script>

<footer>
  <div class="center">
    <div class="footer-about">
      Kjemidagen 2022<br />
      Org.nr 992 641 231<br />&nbsp;<br />

      Realfagbygget (NTNU)<br />
      Høgskoleringen 5<br />
      7034 Trondheim<br />&nbsp;<br />&nbsp;<br />

      <a class="back-to-top" href="#banner">Tilbake til toppen</a>
    </div>
    <div>
      {$t('common.contactus')} <br />
      <a href="mailto:kontakt@kjemidagen.no">kontakt@kjemidagen.no</a>
    </div>
    <div class="footer-collaborators">
      <h6>SoMe</h6>
      LinkedIn-link<br />
      Facebook-link<br />
      Insta-link<br />
    </div>
  </div>
</footer>

<style>
  footer {
    background-color: var(--color-bg-brand);
    color: var(--color-text-muted);
  }
  .center {
    align-items: center;
    max-width: var(--document-width);
    display: flex;
    justify-content: space-between;
    margin: auto;
    padding: 1rem;
  }
  .footer-collaborators {
    padding: 16px 40px;
    float: left;
  }

  .back-to-top {
    color: var(--color-text-muted);
  }
</style>

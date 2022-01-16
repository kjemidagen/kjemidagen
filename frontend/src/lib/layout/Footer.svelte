<script lang="ts">
  import { t } from 'svelte-intl-precompile';
</script>

<footer>
  <div class="center">
    <div class="footer-collaborators">
      I samarbeid med:
      <ul class="list-collaborators">
        <li>Institutt for materialteknologi</li>
        <li>Institutt for kjemisk prosessteknologi</li>
        <li>Institutt for kjemi</li>
        <li>Institutt for bioteknologi</li>
        <li>Samarbeidsforum</li>
      </ul>
      <br />
      <img src="sf_logo.png" alt="Samarbeidsforum logo" />
    </div>

    <div class="footer-about">
      &copy; {$t('year')}
      {$t('Kjemidagen')} <br />
      {$t('orgnr')} 992 641 231<br />&nbsp;<br />

      {$t('address')}:<br />
      Institutt for kjemisk prosessteknologi<br />
      Sem Sælands vei 4<br />
      7491 Trondheim<br />&nbsp;<br />&nbsp;<br />

      <a class="back-to-top" href="#header">{$t('backtotop')}</a>
    </div>
  </div>
</footer>

<style>
  footer {
    background-color: var(--color-bg-primary);
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
  img {
    max-width: 100%;
  }
  .list-collaborators {
    padding-left: 16px;
  }
</style>

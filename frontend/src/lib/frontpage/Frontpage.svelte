<script lang="ts">
</script>

<section class="frontpage" id="frontpage">
  <div class="content">
    <nav class="navigation">
      <ul>
        <li><a href="#about">Om Kjemidagen</a></li>
        <li><a href="#program">Program</a></li>
        <li><a href="#companies">Bedrifter</a></li>
        <li><a href="#contact">Ta kontakt</a></li>
      </ul>
    </nav>
    <div class="frontpage-content">
      <p class="bigger">Vi ser frem til å ta dere imot 19. oktober 2021!</p>
      <p>
        Disse sidene oppdateres fortløpende og inneholder blant annet generell informasjon om dagen,
        program for hele arrangementet og en oversikt over hvilke bedrifter som kommer. Informasjon
        vil også bli delt på vår facebookgruppe: <a href="https://facebook.com/kjemidagen\"
          >facebook.com/kjemidagen</a
        >
        og Instagram <a href="https://instagram.com/kjemidagen\">Kjemidagen</a>.
      </p>
      <p>Ta gjerne kontakt med styret hvis du har spørsmål."</p>
      <p>Vi gleder oss til å se dere på Kjemidagen!</p>
    </div>
  </div>
  <img alt="jotun" src="/jotun.jpg" />
</section>

<style>
  .content {
    max-width: var(--document-width);
    margin: auto;
    display: grid;
    grid-template-columns: 1fr 1fr 2fr 1fr;
    grid-gap: 2rem;
    padding: 4rem 0;
  }
  .navigation {
    grid-column-start: 2;
  }

  p {
    margin-bottom: 1rem;
  }
  img {
    z-index: -1;
    object-fit: cover;
    height: 35rem;
    width: 100%;
  }
</style>

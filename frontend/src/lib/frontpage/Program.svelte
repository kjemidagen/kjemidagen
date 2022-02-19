<script lang="ts">
</script>

<section class="program" id="program">
  <div class="content">
    <h3>Årets program</h3>
    <p class="program-ingress">
      Kjemidagen har som mål å bidra til god kontakt mellom studentene vi representerer og faglig
      relevante bedrifter. Som en følge av dette sørger vi for å tilby et bredest mulig utvalg av
      arenaer hvor bedrifter og studenter kan møtes og bli bedre kjent.
    </p>
    <div class="program-body">
      <img src="/raworth-lecture.jpg" alt="lecture room" width="400px" height="400px" object-fit />
      <div class="program-text">
        <table class="program-table">
          <tr><th class="left-col"><b>19. oktober</b></th></tr>
          <tr><td class="left-col">10:00</td> <td>Åpning og utdeling av goodiebags </td></tr>
          <tr><td class="left-col">10:15 - 15:00</td> <td>Bedriftsstands </td></tr>
          <tr><td class="left-col">10:15 - 15:00</td> <td>Speedintervju </td></tr>
          <tr><td class="left-col">10:30 - 13:00</td> <td>CV-fotografering </td></tr>
          <tr><td class="left-col">11:15 - 12:00</td> <td>Motivasjonsforedrag </td></tr>
          <tr><td class="left-col">13:15 - 14:00</td> <td>Sommerjobbmaraton </td></tr>
          <tr><td class="left-col">18:30</td> <td>Bankett </td></tr>
        </table>
        <div>
          <p>
            Dette året har vi invitert Ragnhild Sofie Ragnhildstveit Sætra og Jacob Hadler-Jacobsen,
            som er tidligere studenter ved MTNANO og MTKJ, til Kjemidagen.
          </p>
          <p>
            Ragnhild forsker på molekylærmekanismer i tuberkulose, mens Jacob jobber med modellering
            av katodematerialer for magnesiumbatterier. Sammen skal de diskutere seg gjennom hvordan
            hverdagen etter endt studie ser ut, og hvilken nytte de fikk av studiet.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>

<style>
  .program {
    padding: 40px 0;
  }
  .content {
    max-width: var(--document-width);
    margin: auto;
  }
  .program-body {
    display: flex;
  }
  h3 {
    grid-column: span 2;
  }
  table {
    margin-bottom: 1rem;
  }
  .left-col {
    padding-right: min(4vw, 2rem);
  }
  img {
    border: 0px solid;
    border-radius: 1000px;
    object-fit: cover;
    object-position: 0 50%;
    margin: 2rem;
  }
  @media only screen and (min-width: 768px) {
    .program-body {
      flex-direction: row;
      justify-content: center;
    }
    .program-text {
      max-width: 50%;
    }
  }
</style>

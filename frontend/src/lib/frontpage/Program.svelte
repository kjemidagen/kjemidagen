<script lang="ts">
</script>

<section class="program" id="program">
  <div class="content">
    <h3>Årets program</h3>
    <div class="program-body">
      <img src="/raworth-lecture.jpg" alt="lecture room" width="400px" height="400px" object-fit />
      <div class="program-text">
        <table class="program-table">
          <tr><th class="left-col"><b>19. oktober</b></th></tr>
          <tr><td class="left-col">10:00</td> <td>Åpning med ballongslipp </td></tr>
          <tr><td class="left-col">10:15 - 15:00</td> <td>Bedriftsstands </td></tr>
          <tr><td class="left-col">10:15 - 15:00</td> <td>Speedintervju </td></tr>
          <tr><td class="left-col">10:30 - 13:00</td> <td>CV-fotografering </td></tr>
          <tr><td class="left-col">11:15</td> <td>Motivasjonsforedrag </td></tr>
          <tr><td class="left-col">13:15</td> <td>Sommerjobbmaraton </td></tr>
          <tr><td class="left-col">14:00</td> <td>Jobbmaraton </td></tr>
          <tr><td class="left-col">18:30</td> <td>Bankett </td></tr>
        </table>
        <div>
          <h3>Speedintervju</h3>
          <p>
            Alle bedriftene vil på forhånd ha mulighet til å reservere et eget rom for speedintervju
            i løpet av dagen. Dette er en spennende mulighet for studenter og bedrifter, og en fin
            mulighet for deltakende bedrift å finne sin neste kollega.
          </p>
          <h3>Sommerjobbmaraton</h3>
          <p>
            Sommerjobbmaraton er et event hvor alle bedrifter som deltar på Kjemidagen får to
            minutter til rådighet for å presentere sine sommerjobber og sommerprogram. Dette er et
            meget populært arrangement med gode tilbakemeldinger fra både bedrifter og studenter.
          </p>
          <h3>Jobbmaraton</h3>
          <p>
            Jobbmaraton er et liknende event som sommerjobbmaraton, men istedenfor sommerjobber får
            deltakende bedrifter mulighet til å kort presentere sine graduate- program,
            traineestillinger, internships, masteroppgaver, Ph.d.-stillinger, og fulltidsstillinger.
          </p>
          <h3>Bankett</h3>
          <p>
            På kvelden vil det arrangeres en bankett med bedriftsrepresentanter og 4. og 5.
            årsstudenter. Banketten er en viktig del av Kjemidagen, og en fin mulighet for
            bedriftene til å bli bedre kjent med våre studenter.
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

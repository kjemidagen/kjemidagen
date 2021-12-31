<script context="module">
  import { browser, dev } from '$app/env';

  // we don't need any JS on this page, though we'll load
  // it in dev so that we get hot module replacement...
  export const hydrate = dev;

  // ...but if the client-side router is already loaded
  // (i.e. we came here from elsewhere in the app), use it
  export const router = browser;

  // since there's no dynamic data here, we can prerender
  // it so that it gets served as a static asset in prod
  export const prerender = true;
</script>

<svelte:head>
  <title>About</title>
</svelte:head>

<div class="content">
  <section class="frontpage" id="frontpage">
    <div class="content">
      <nav class="navigation">
        <ul>
          <li><a href="#about">Om Kjemidagen</a></li>
          <li><a href="#program">Program</a></li>
          <li><a href="#companies">Bedrifter</a></li>
          <li><a href="#contact">Kontakt</a></li>
          <!--<li><a href="challenge.html">Kjemidagen Challenge</a></li> -->
        </ul>
      </nav>
      <div class="frontpage-content">
        <p class="bigger">Vi ser frem til å ta dere imot 19. oktober 2021!</p>
        <p>
          Disse sidene oppdateres fortløpende og inneholder blant annet generell informasjon om
          dagen, program for hele arrangementet og en oversikt over hvilke bedrifter som kommer.
          Informasjon vil også bli delt på vår facebookgruppe: <a
            href="https://facebook.com/kjemidagen">facebook.com/kjemidagen</a
          >
          og Instagram (<a href="https://instagram.com/kjemidagen">Kjemidagen</a>).
        </p>
        <p>Ta gjerne <a href="#contact"> kontakt med styret</a> hvis du har spørsmål.</p>
        <p>Vi gleder oss til å se dere på Kjemidagen!</p>
      </div>
    </div>
  </section>

  <section class="about" id="about">
    <div class="content">
      <div class="about-intro">
        <h3>Om Kjemidagen</h3>

        <p>
          Kjemidagen er en unik bedriftsdag på NTNU for sivilingeniørstudenter på linjene
          Nanoteknologi, og Industriell Kjemi og Bioteknologi. Dette er en dag for og av studenter,
          noe som skaper et stort engasjement rundt arrangementet. Vi er opptatt av å skape god
          kontakt mellom studentene ved våre linjer og aktører i næringslivet. Derfor tilbyr vi
          Kjemidagen som et helhetlig arrangement hvor bedriftene får anledning til å komme i
          kontakt med studentene på flere arenaer i løpet av dagen. Kjemidagen er en populær
          begivenhet for studentene og derfor er oppmøtet og oppslutningen alltid stor. Dagen
          trekker studenter på alle årstrinn og fra alle studieretninger.
        </p>
      </div>

      <div class="about-content">
        <article>
          <h4>Engasjement</h4>
          <p>
            Kjemidagens aller sterkeste side er studentenes engasjement rundt selve dagen. Dette er
            en bedriftsdag for og av studenter. Det er den store dugnadsånden, og ikke minst et
            brennende engasjement, som gjør at Kjemidagen har blitt en stor suksess i løpet av sine
            få år. Dagen engasjerer hele 3. klasse, i tillegg til flere frivillige, som bruker mye
            av tiden sin på å gjøre Kjemidagen til NTNUs beste bedriftsdag. Vi ønsker at Kjemidagen
            skal være en begivenhet som studentene ser frem til og ikke kun en vanlig bedriftsdag.
          </p>
        </article>

        <article>
          <h4>Interaksjon</h4>
          <p>
            På Kjemidagen i 2019, som var forrige gang karrieredagen ble gjennomført på fysisk på
            campus, deltok 23 bedrifter samt flere av instituttene ved NTNU. Dette er en størrelse
            vi ønsker å beholde slik at både bedrifter og studenter skal føle seg sett. I tillegg
            til dette mener vi at rekruttering strekker seg langt utover kombinasjonen stand og
            bedriftspresentasjon. For å gi bedrifter muligheten til å bli kjent med studentene,
            arrangerer vi bankett med lett underholdning på kvelden.
          </p>
        </article>

        <article>
          <h4>Relevans</h4>
          <p>
            Kjemidagen er en spesialisert bedriftsdag som hovedsakelig inviterer bedrifter innen
            nøkkelområdene kjemi, materialteknologi, prosessindustri, nanoteknologi og bioteknologi.
            Et slikt spesialisert interesseområde gjør dette til en unik bedriftsdag for både
            bedriftene og våre studenter. Dere vil som bedrift møte interesserte studenter som er
            relevant for deres firma, og studentene vil møte et bredt utvalg av bedrifter innen sine
            nøkkelområder.
          </p>
        </article>
      </div>
    </div>
  </section>

  <section class="pictures" id="pictures">
    <!-- GIEF PIX -->
  </section>

  <section class="program" id="program">
    <div class="content">
      <h3>Årets program</h3>

      <p class="program-desc">
        Kjemidagen har som mål å bidra til god kontakt mellom studentene vi representerer og faglig
        relevante bedrifter. Som en følge av dette sørger vi for å tilby et bredest mulig utvalg av
        arenaer hvor bedrifter og studenter kan møtes og bli bedre kjent.
      </p>

      <div class="program-table">
        <table>
          <tbody>
            <tr><td class="left-col"><b>19. oktober</b></td> </tr><tr
              ><td class="left-col">10:00</td><td>Åpning og utdeling av goodiebags </td></tr
            ><tr><td class="left-col">10:15 - 15:00</td><td>Bedriftsstands </td></tr><tr
              ><td class="left-col">10:15 - 15:00<br /></td><td>Speedintervju </td></tr
            ><tr><td class="left-col">10:30 - 13:00</td><td>CV-fotografering </td></tr><tr
              ><td class="left-col">11:15 - 12:00</td><td>Motivasjonsforedrag </td></tr
            ><tr><td class="left-col">13:15 - 14:00</td><td>Sommerjobbmaraton </td></tr><tr
              ><td class="left-col">18:30</td><td>Bankett </td></tr
            ></tbody
          >
        </table>
      </div>

      <p>
        Dette året har vi invitert Ragnhild Sofie Ragnhildstveit Sætra og Jacob Hadler-Jacobsen, som
        er tidligere studenter ved MTNANO og MTKJ, til Kjemidagen.
      </p>
      <p>
        Ragnhild forsker på molekylærmekanismer i tuberkulose, mens Jacob jobber med modellering av
        katodematerialer for magnesiumbatterier. Sammen skal de diskutere seg gjennom hvordan
        hverdagen etter endt studie ser ut, og hvilken nytte de fikk av studiet.
      </p>
    </div>
  </section>

  <section class="companies">
    <div class="content" id="companies">
      <h3>Bedrifter</h3>

      <p>Følgende bedrifter kommer på Kjemidagen i høst:</p>

      <img src="companies_21.png" alt="Logoene til bedriftene som kommer på kjemidagen." />
    </div>
  </section>

  <section class="contact" id="contact">
    <div class="content">
      <h3>Ta kontakt</h3>
      5
      <figure class="contact-image">
        <img src="styret21.jpg" alt="Styret 2021, Ida, Cornelia, Kristian og Andrea" />
      </figure>

      <p>Skulle du ha noen spørsmål om arrangementet, ikke nøl med å ta kontakt på e-post:</p>
      <p class="contact-email"><a href="mailto:kontakt@kjemidagen.no">kontakt@kjemidagen.no</a></p>
      <p>Styret i Kjemidagen ønsker alle studenter hjertelig velkommen!</p>
    </div>
  </section>
</div>

<style>
</style>

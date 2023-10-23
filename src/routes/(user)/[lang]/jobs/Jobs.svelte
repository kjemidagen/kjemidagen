<script lang="ts" context="module">
  import sintefLogo from '$lib/assets/sintef.svg';
  import yaraLogo from '$lib/assets/yara.svg';
  import borregaardLogo from '$lib/assets/borregaard.svg'
  import hydroLogo from '$lib/assets/hydro.svg';
  import { t } from '$lib/translations/translations';

  export const jobsMap = [
    {
      slug: 'sintef',
      image: sintefLogo,
      company: 'SINTEF',
      location: 'Oslo',
      link: 'https://www.sintef.no/',
      applicationLink: 'https://www.sintef.no/sintef-energi/sommerjobb_i_sintef_energi/',
      short_description:
        'SINTEF Energi tilbyr spennende sommerjobbmuligheter for studenter. Bli en del av vårt team og utvikle bærekraftig energiteknologi med veiledning fra våre erfarne forskere. Grip sjansen til å gjøre en reell innvirkning og søk nå!',
      long_description:
        "Vil du være med å forme fremtiden? <br/><br/><br/><br/>\n\nNå kan du prøve deg som forsker for en sommer hos SINTEF, et av Europas største uavhengige forskningsinstitutt! <br/><br/><br/><br/>\n\n <p>SINTEF Energi utvikler fremtidens bærekraftige energiløsninger. I tett samarbeid med NTNU, industri og næringsliv, forsker vi fram ny teknologi med visjonen<strong>&nbsp;teknologi for et bedre samfunn</strong>.</p><br/><br/><p>Hver sommer ansetter vi studenter for å forske sammen med oss på våre prosjekter, med tilgang til verdensledende laboratorier og veiledning fra våre forskere. Nå vil vi at du skal bli en av dem, og få mulighet til å utvikle bærekraftig energiteknologi som skal bidra til å redde verden.</p><br/><br/><p><strong>I år lyser vi ut totalt 38 sommerjobber fordelt på disse avdelingene: </strong></p><ul><li><strong>Elkraftteknologi (ET) 7 jobber</strong></li><li><strong>Gassteknologi (GT) 10 jobber</strong></li><li><strong>Termisk Energi (TE) 9 jobber </strong></li><li><strong>Energisystemer (ES) 12 jobber</strong></li></ul>"
    },
    {
      slug: 'yara-cfd',
      image: yaraLogo,
      company: 'Yara',
      location: 'Porsgrunn',
      link: 'https://jobs.yara.com/',
      applicationLink:
        'https://jobs.yara.com/job/Porsgrunn-Summer-Intern-Computational-Fluid-Dynamics-%28CFD%29/976262801/',
      short_description:
        "Spend your summer in a meaningful internship at Yara's Technology Center in Porsgrunn, Norway. Join their CFD (Computational Fluid Dynamics) simulation project to enhance Yara's production processes, design complex 3D geometries, and communicate your findings in English, all while making a valuable impact.",
      long_description:
        "Mastering technology and development has always been a key to the commercial success of Yara’s products. Yara Technology Center, located in Porsgrunn, Norway, is a vital contributor to this success working to improve existing processes and technologies as well as to develop new and innovative solutions for processes and products. <br> We are now looking for students to work on an interesting project during this summer: CFD Simulation of Yara 's production process. <br> During the internship, Computational Fluid Dynamics (CFD) will be used to simulate one of Yara's production processes. The simulations can be used in developing new process technology for Yara or connected to Yara factory troubleshooting."
    },
    {
      slug: 'yara-cdf',
      image: yaraLogo,
      company: 'Yara',
      location: 'Porsgrunn',
      link: 'https://jobs.yara.com/',
      applicationLink:
        'https://jobs.yara.com/job/Porsgrunn-Summer-Intern-Coating-Development-for-fertilizer/976272701/',
      short_description:
        "Embark on an enriching summer journey at Yara Technology Center in Porsgrunn, Norway, by participating in their Coating Development for Fertilizer project. As a student pursuing a master’s degree in chemistry or related fields, you'll engage in vital tasks such as literature review, laboratory tests, and statistical analyses, contributing to the enhancement of fertilizer preservation techniques and product quality.",
      long_description:
        'Mastering technology and development have always been a key to the commercial success of Yara’s products. Yara Technology Center (YTC), located in Porsgrunn, Norway, is a vital contributor to this success working to improve existing processes and technologies as well as to develop new and innovative solutions for processes and products.<br>We are now looking for students to work on an interesting project during this summer. The work will be connected to ongoing projects in the Product Quality and Development Department, related to Coating Development for Fertilizer.<br>Fertilizers are usually coated before shipment to preserve the quality of product during handling and transport. In this project different coatings will be tested and evaluated in respect to quality of products and performance of coatings in protecting the fertilizers in different climate conditions.'
    },
    {
      slug: 'yara-prilling',
      image: yaraLogo,
      company: 'Yara',
      location: 'Porsgrunn',
      link: 'https://jobs.yara.com/',
      applicationLink:
        'https://jobs.yara.com/job/Porsgrunn-Summer-Intern-Prilling-optimization/976269501/',
      short_description:
        "Become a part of Yara's mission to responsibly feed the world and protect the planet by joining their Prilling Optimization summer project in Porsgrunn, Norway. As a student pursuing a master's degree in chemistry or related fields, you'll delve into tasks such as method development, laboratory work, and process optimization, contributing to Yara's innovative solutions and sustainable fertilizer production.",
      long_description:
        "Yara’s mission is to responsibly feed the world and protect the planet. To convert this into action, Yara Technology located in Porsgrunn, Norway, works to optimize utilization of assets and identify solutions for long-term competitive advantage, including technologies for emission free production of fertilizers based on renewable energy.<br/><br/> Our focus is to improve existing processes and technologies as well as to develop new and innovative solutions for processes and products. We work together with plants and the market organization on product development, problem solving and advisory to support production of high-quality fertilizers. Our aim is to contribute to maintain Yara's leading position in sustainable fertilizer production.<br/><br/>We are now looking for students to work on an interesting project during this summer: Prilling optimization, Optimize mass and energy balance model for prilling tower. Build on the existing mass and energy balance model for prilling tower in NPK3. The student will focus on optimizing the prilling process and reducing emissions.<br/><br/>This internship is an opportunity to experience and influence the industrial scale production of fertilizers in Porsgrunn. In close connection to an industrial plant the technical support and innovative solutions of tomorrow are investigated. The work will be connected to ongoing projects in the NPK & Environmental Technologies Department."
    },
    {
      slug: 'yara-pm',
      image: yaraLogo,
      company: 'Yara',
      location: 'Porsgrunn',
      link: 'https://jobs.yara.com/',
      applicationLink:
        'https://jobs.yara.com/job/Porsgrunn-Summer-Intern-Process-Modeling/976261301/',
      short_description:
        "Embark on a transformative journey with Yara's Process Modeling summer internship in Porsgrunn, Norway. If you're a master's degree student in chemical engineering passionate about process simulation, this opportunity offers hands-on experience in utilizing various software tools, such as ProSimPlus and Aspen Plus, to model and optimize Yara's production processes, contributing to innovative solutions and best practices.",
      long_description:
        "Mastering technology and development has always been a key to the commercial success of Yara’s products. Yara Technology Center, located in Porsgrunn, Norway, is a vital contributor to this success working to improve existing processes and technologies as well as to develop new and innovative solutions for processes and products.<br/><br/>We are now looking for students to work on an interesting project during this summer: Process Modeling<br/><br/>During the internship, different process simulation software will be used to model parts of Yara's production processes. The work will be connected to tasks in the Process Modeling and Control department.   "
    },
    {
      slug: 'yara-tdd',
      image: yaraLogo,
      company: 'Yara',
      location: 'Porsgrunn',
      link: 'https://jobs.yara.com/',
      applicationLink:
        'https://jobs.yara.com/job/Porsgrunn-Summer-Intern-Technology-Development-Department/976291101/',
      short_description:
        "Join Yara's Technology Development Department this summer in Porsgrunn, Norway, and contribute to the future of engineering data management. As a summer intern, you'll engage in shaping Digital Twin solutions for production sites, focusing on collecting, organizing, and enhancing as-built design data for Nitric Acid plants. This hands-on experience is ideal for Chemical/Process Engineering students passionate about simulation tools and data analysis, providing a unique opportunity to make a meaningful impact on Yara's innovative initiatives.",
      long_description:
        "Mastering technology and development has always been a key to the commercial success of Yara’s products. Yara Technology Center, located in Porsgrunn, Norway, is a vital contributor to this success working to improve existing processes and technologies as well as to develop new and innovative solutions for processes and products.<br/><br/>We are now looking for students to work on an interesting project during this summer: Process Design Data and Digital Twin Solutions. <br/><br/>We are introducing a Digital Twin solution for our production sites, that will secure a structured way of storing and sharing our design data. The Digital Twin provides an intuitive and user-friendly way of working with engineering data throughout the life-cycle. Data access and data quality are essential for the efficiency of all business processes and decision-making."
    },
    {
      slug: 'yara-napc',
      image: yaraLogo,
      company: 'Yara',
      location: 'Porsgrunn',
      link: 'https://jobs.yara.com/',
      applicationLink:
        'https://jobs.yara.com/job/Porsgrunn-Summer-Intern-Nitric-Acid-Process-Catalysts/976256101/',
      short_description:
        "Embark on a hands-on research journey this summer with Yara's Nitric Acid Process Catalysts project in Porsgrunn, Norway. As a summer intern, you'll delve into the world of catalyst materials, conducting comprehensive tests and characterizations. This opportunity is ideal for students in their 3rd or 4th year, specializing in chemical or materials science, who possess strong laboratory skills and a passion for innovation. Join us in shaping the future of nitric acid production.",
      long_description:
        "Mastering technology and development have always been a key to the commercial success of Yara’s products. Yara Technology Center, located in Porsgrunn, Norway, is a vital contributor to this success working to improve existing processes and technologies as well as to develop new and innovative solutions for processes and products.<br/><br/>We are now looking for students to work on an interesting project during this summer: Nitric Acid Process Catalysts<br/><br/>Yara utilize several catalysts in the production of nitric acid. The aim of the internship project to perform a test program of several potential catalysts in the nitric acid process and make an evaluation of their potentials and limitations."
    },
    {
      slug: 'yara-phosphate',
      image: yaraLogo,
      company: 'Yara',
      location: 'Porsgrunn',
      link: 'https://jobs.yara.com/',
      applicationLink:
        'https://jobs.yara.com/job/Porsgrunn-Summer-Intern-Phosphate-flexiblity/976266701/',
      short_description:
        "Dive into innovative solutions for fertilizer production this summer with Yara's Phosphate Flexibility project in Porsgrunn, Norway. As an intern, you'll explore methods to prevent the sudden thickening of process liquor during neutralization, conducting experiments and gaining hands-on experience in a laboratory-scale pilot plant. This opportunity is ideal for students pursuing a master’s degree in chemistry, chemical engineering, or related fields, offering a chance to contribute to cutting-edge research in a diverse and multicultural industrial environment.",
      long_description:
        "Mastering technology and development has always been a key to the commercial success of Yara’s products. Yara Technology Center is located in Porsgrunn, Norway. <br/><br/>The focus is to improve existing processes and technologies as well as to develop new and innovative solutions for processes and products. <br/><br/>One of the key challenges faced during the production of compound (NPK) fertilizers using the nitrophosphate process is a sudden change in the rheology of the process liquor during the neutralization of the acidic liquor with ammonia. The resulting increase in viscosity, or thickening, of the liquor can result in several issues, such as clogging of various process units, decreased production, or poor final product quality. In the worst cases, thickening can lead to a complete stop in the plant, which is both costly and time-consuming. <br/><br/>This summer project will explore methods to mitigate or prevent thickening, with experiments carried out in a laboratory-scale neutralization pilot plant. The key elements in the composition of the raw materials that influence the thickening are believed to be Mg and F, as well as Al and Fe. The summer student will perform experiments to remove Mg and/or F from the liquor prior to neutralization and study the subsequent effect on the thickening behavior of the liquor. <br/><br/>The student will be involved in the design of the experiments and be introduced to practical applications of industrial R&D, as well as gain new skills in operating laboratory-scale pilot plants. The student will also gain insight into the chemistry of the nitrophosphate process, and the experience of working in a diverse and multicultural environment in an established research center that is part of a large industry."
    },
    {
      slug: 'yara-summer-project',
      image: yaraLogo,
      company: 'Yara',
      location: 'Porsgrunn',
      link: 'https://jobs.yara.com/',
      applicationLink:
        'https://jobs.yara.com/job/Porsgrunn-Summer-Intern-Sommerprosjektet-Yara/976288201/',
      short_description:
        "Bli en del av Yara sitt sommerprosjekt 2024 i Porsgrunn, hvor du som student får sjansen til å bidra til løsninger på verdens matvaremangel. Dette tverrfaglige prosjektet gir deg muligheten til å jobbe tett sammen med andre studenter i et internasjonalt miljø, løse utfordrende problemstillinger og utvikle både faglige og personlige ferdigheter. Søk nå og vær med på å forme en mer bærekraftig fremtid med Yara Porsgrunn. For Sommerprosjektet Yara søkes det etter inntil 6 studenter som skal jobbe tverrfagleg på eit prosjekt i fabrikken i Porsgrunn",
      long_description:
        "Vil du være med på å utgjøre en forskjell ved å bidra til å løse et av verdens største problemer: matvaremangel? <br/><br/>Å være sommerstudent i Yara Porsgrunn 2024 kan være en god mulighet til å gjøre nettopp det!<br/><br/>Yara sin misjon er å sørge for mat til verdens befolkning og samtidig verne jordkloden på en ansvarlig måte. Yara Porsgrunn produserer og leverer høykvalitetsprodukter til landbruk og industrielle formål over hele verden. Vi er en av verdens største produsenter innen plantenæring og en stor aktør innenfor produksjonssystemet til Yara International ASA. Produksjonen av gjødsel ved Yara Porsgrunn bidrar til mat på bordet til 50 millioner mennesker hvert år.<br/><br/>I år vil Yara Porsgrunn tilby studenter «Sommerprosjektet 2024». Vi ønsker at fremtidens arbeidskraft skal få blir kjent med Yara Porsgrunn - og gjennom et tverrfaglig samarbeid bli med på å løse en av våre viktige problemstillinger.<br/><br/>Verden endrer seg raskt, og det gjør vi også. Yara jobber for å bli naturpositiv og klimanøytral innen 2050. Ved å bygge på vår misjon, vitenskap og mer enn 100 år med agronomisk kunnskap, skal vi gi tilbake til jorden mer enn vi tar. Vi kutter utslipp i vår egen produksjon, utvikler verktøy for å kutte utslipp i felt og beskytte biologisk mangfold, og bidrar til et grønt skifte i skipsfart og annen energikrevende industri.<br/><br/>Gjødselproduksjon er en kompleks  prosess og ved Yara Porsgrunn jobber vi kontinuerlig med hvordan vi kan bidra til en bærekraftig og effektiv verdikjede. Gjennom sommerprosjekt 2024 ønsker vi dere studenters innspill på hvordan vi kan jobbe med ytterligere optimalisering på tvers av våre fabrikker i Porsgrunn – gjennom virkemidler som prosessoptimalisering, styring og digitalisering. <br/><br/>Vi ser etter motiverte, ambisiøse studenter som er nysgjerrige på å jobbe i et internasjonalt selskap. Du får samarbeide med andre studenter og du vil få et ansvar for både en utfordrende og meningsfull oppgave.<br/><br/>Gjennomføring: <br/><br/>Vi ønsker å samle inntil 6 studenter som skal jobbe tett sammen om en problemstilling.<br/><br/>Arbeidet vil foregå i vårt fabrikkmiljø i Yara Porsgrunn<br/><br/>Prosjektet vil ha en varighet på ca 9 uker, inkludert 2 ukers ferie.<br/><br/>Oppstart medio juni, avslutning medio august.<br/><br/>Prosjektet avleveres en av de siste dagene i perioden med en presentasjon av løsning på gitt problemstilling for Yara Porsgrunn sin ledergruppe"
    },
    {
      slug: 'borregaard-summer-intern',
      image: borregaardLogo,
      company: 'Borregaard',
      location: 'Sarpsborg',
      link: 'https://www.borregaard.com',
      applicationLink:
        'https://www.borregaard.com/no/karriere/ledige-stillinger/vi-soker-engasjerte-sommerstudenter-innen-kjemi-prosess/?rmpage=apply&rmjob=318',
      short_description:
        "Bli med på spennende sommerprosjekter hos Borregaard, verdens mest avanserte bioraffineri! Vi søker engasjerte ingeniørstudenter i kjemi/prosess fra 2. til 5. klasse for å utforske bærekraftige løsninger og utvikle dine faglige ferdigheter i et inspirerende arbeidsmiljø. Søk nå og bli en del av vårt dedikerte team!",
      long_description:
        "Har du lyst til å jobbe med spennende prosjekter i verdens mest avanserte bioraffineri? Borregaard tilbyr relevant og utfordrende prosjektarbeid for ingeniørstudenter i 2. til 5. klasse kjemi/prosess.<br/><br/>Borregaards produkter er alternativer til oljebaserte alternativer og møter dermed langsiktige, globale utfordringer knyttet til befolkningsvekst, ressurstilgang og miljø- og klimabelastninger. I løpet av 8 uker blir du kjent  med hvordan det er å jobbe ved verdens mest avanserte bioraffineri.<br/><br/>Gjennom relevante og spennende oppgaver får du både brukt din kompetanse fra studiene og videreutviklet dine faglige ferdigheter. I tillegg til faglig utvikling, arrangeres det felles aktiviteter der du blir kjent med andre studenter og får bygget nettverk.<br/><br/>Prosjektene vil bli definert når det nærmer seg oppstart, basert på din bakgrunn og Borregaards behov."
    },
    {
      slug: 'borregaard-summer-research',
      image: borregaardLogo,
      company: 'Borregaard',
      location: 'Sarpsborg',
      link: 'https://www.borregaard.com',
      applicationLink:
        'https://www.borregaard.com/no/karriere/ledige-stillinger/vi-soker-engasjerte-studenter-innenfor-kjemi-og-bioteknologi-til-sommerjobber-i-forskningsavdelingen/?rmpage=apply&rmjob=316',
      short_description:
        "Borregaard søker engasjerte masterstudenter i kjemi og bioteknologi (3. og 4. klasse) til sommerprosjekter ved deres innovative forskningssenter. Utforsk bærekraftige løsninger i verdens ledende bioraffineri og bli en del av et dyktig og tverrfaglig team. Søk nå for en mulighet til å forme fremtiden innen forskning og innovasjon!",
      long_description:
        "Å opprettholde en sterk innovasjonsinnsats er en av Borregaards strategiske prioriteringer, og bærekraft er avgjørende i våre innovasjonsprosesser. Forskning og utvikling har over tid resultert i bærekraftige løsninger som svarer på langsiktige globale utfordringer. Vi er overbevist om at denne sterke trenden representerer en stor mulighet for oss som selskap. <br/><br/>Har du lyst til å jobbe med spennende innovasjonsprosjekter i verdens mest avanserte bioraffineri? Borregaards forskningssenter i Sarpsborg har rundt 70 ansatte med stor kjemifaglig bredde, mye spisskompetanse og stort engasjement. Borregaards forskningsavdeling tilbyr relevant og utfordrende prosjektarbeid for mastergradsstudenter i 3. og 4. klasse ved kjemi og bioteknologi.<br/><br/>Borregaards produkter er alternativer til oljebaserte alternativer og møter dermed langsiktige, globale utfordringer knyttet til befolkningsvekst, ressurstilgang og miljø- og klimabelastninger. I løpet av 8 uker blir du kjent med hvordan det er å jobbe ved verdens mest avanserte bioraffineri.<br/><br/>Gjennom relevante og spennende oppgaver får du både brukt din kompetanse fra studiene og videreutviklet dine faglige ferdigheter. I tillegg til faglig utvikling, arrangeres det felles aktiviteter der du blir kjent med andre studenter og får bygget nettverk.<br/><br/>Hvilket av våre forskningsprosjekter du skal jobbe med blir avgjort når det nærmer seg oppstart, basert på Borregaards behov og din bakgrunn."
    },
    {
      slug: 'hydro',
      image: hydroLogo,
      company: 'Hydro',
      location: "Norway",
      link: 'https://jobs.hydro.com',
      applicationLink:
        'https://jobs.hydro.com/job/Oslo-Hydro-Summer-internship-2024-0283/977933801/',
      short_description:
        "Join Hydro's Summer Internship 2024 and dive into a world of innovation and sustainability. With over 50 diverse positions in Norway, this program offers real challenges, mentorship, and a chance to shape the future of metal technologies. Apply now to be part of this transformative experience!",
      long_description:
        "Hydro offers various internship positions across business areas in Norway. This year we are recruiting over 50 interns for the summer of 2024.<br/><br/>An internship in Hydro is a great way for you to try out and learn more about your field of study. You will be obtaining a valuable experience and you get to tackle relevant tasks and real challenges, with support from experienced colleagues. You will also get to participate in a joint program with all the Hydro interns, allowing you to learn more about our business and acquire interdisciplinary knowledge. All the while, we expect and want you to have a fun experience during the summer.<br/><br/>The positions: <br\><ul><li>Aluminium Metal Commercial Logistics, Karmøy</li>  <li>Aluminium Metal Commercial Logistics, Oslo</li>  <li>Batteries, Oslo</li>  <li>Business Systems and Safety Management, Oslo</li>  <li>Carbon, Årdal</li>  <li>Commercial Technology Laboratories, Karmøy eller Sunndalsøra</li>  <li>Communication & Public Affairs, Energy, Oslo</li>  <li>Electrolysis, Årdal</li>  <li>Electrolysis/Wire Rod Casthouse/HSE, Karmøy </li>  <li>Energy Power Operation, Nesflaten, Rjukan, Stavanger & Sogn</li>  <li>Energy Strategy & Policy, Oslo</li>  <li>Enterprise Risk Management, Oslo</li>  <li>GBS Finance - Global Process Design and Improvements, Oslo</li>  <li>GBS HR - Gobal Learning Center, Oslo</li>  <li>Group Information & Technology, Oslo</li>  <li>Group Performance, Planning and Controlling (GPPC), Oslo</li>  <li>Havrand, Oslo</li>  <li>Hydro Rein, Projects & Operations, Oslo</li>  <li>Hydro Rein, Strategy and Transactions, Oslo</li>  <li>Investor Relations, Oslo</li>  <li>Metal Sourcing & Trading, Oslo</li>  <li>Projects Electrolyse, Husnes </li>  <li>Recycling, Operational Performance - Oslo</li>  <li>Technology – Hycast, Sunndal</li>  <li>TOS - Asset Management, Oslo</li>  <li>TOS - Digital Production Support - Årdal</li>  <li>TOS - IOS Carbon, Årdal</li>  <li>TOS - IOS Sustainability, Oslo</li>  <li>TOS - New Technologies, Årdal</li>  <li>TOS - Technology and Operational Support, Porsgrunn</li>  <li>TOS - Technology Development - Cell Technology, Årdal</li>  <li>TOS - IOS Electrolysis, Products & Analytics, Årdal</li></ul>"
    }

  ];
</script>

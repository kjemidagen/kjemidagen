<script context="module">
  import { browser, dev } from '$app/env';
  import Banner from '$lib/frontpage/Banner.svelte';
  import Frontpage from '$lib/frontpage/Frontpage.svelte';
  import About from '$lib/frontpage/About.svelte';
  import Program from '$lib/frontpage/Program.svelte';
  import Companies from '$lib/frontpage/Companies.svelte';
  import Contact from '$lib/frontpage/Contact.svelte';

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
  <title>DEV Kjemidagen</title>
</svelte:head>

<Banner />
<Frontpage />
<About />
<Program />
<Companies />
<Contact />

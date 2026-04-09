<script lang="ts">
  import { onMount } from "svelte";
  import { t, locale } from '$lib/translations/translations';
  
  $: other_lang = $locale === "en" ? "no" : "en";
  let formUrl = "https://forms.office.com/Pages/ResponsePage.aspx?id=cgahCS-CZ0SluluzdZZ8BWRw7RWtPeFLoYPXAOQ4SHJUREpPT0NSMkNIN05ZNVNOUkhHUklaVVdWOC4u"
  onMount(() => {
    const mainElement = document.getElementById('main');
    if (mainElement) {
      mainElement.classList.add('px-0');
    }
  });
</script>

<svelte:head>
  <title>{$t('common.companies')}</title>
</svelte:head>

<div class="flex flex-col h-screen">
  <iframe 
    title="interest-form"
    src={formUrl} 
    class="flex-grow w-full"
    frameborder="0" 
    allowfullscreen>
  </iframe>
</div>

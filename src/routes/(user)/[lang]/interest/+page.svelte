<script lang="ts">
  import { onMount, onDestroy } from "svelte";
  import { t } from '$lib/translations/translations';
  
  let formUrl = "https://docs.google.com/forms/d/e/1FAIpQLSfCrVdfxMUP9sTf_DZLrL9NT_dHbCVD4QwB7mQCFFqdlN92yg/viewform?usp=header"
  onMount(() => {
    const mainElement = document.getElementById('main');
    if (mainElement) {
      mainElement.classList.remove('px-2');
    }
  });
  onDestroy(() => {
    const mainElement = document.getElementById('main');
    if (mainElement) {
      mainElement.classList.add('px-2');
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
    class="flex-grow h-full w-full"
    frameborder="0" 
    allowfullscreen>
  </iframe>
</div>

<script lang="ts">
  import { t, locale, locales } from 'svelte-intl-precompile';
</script>

<header
  id="header"
  class="text-skin-inverted mb-8 p-3 pb-4
   bg-skin-primary sticky top-0 left-0 flex flex-col justify-between lg:flex-row lg:items-start"
>
  <div>
    <a href="/"
      ><img src="logo_inverted.svg" alt="logo" width="20" class="inline-block mr-2" />Kjemidagen</a
    >
    <aside class="language-selector">
      {#each $locales as loc}
        <button
          type="button"
          class={loc === $locale && 'current-locale'}
          on:click={() => ($locale = loc)}>{loc}</button
        >
      {/each}
    </aside>
  </div>
</header>

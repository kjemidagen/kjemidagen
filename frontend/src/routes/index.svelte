<script lang="ts">
  import { goto } from '$app/navigation';
  import { onMount } from 'svelte';
  import { locale } from 'svelte-intl-precompile';
  onMount(() => {
    goto('./' + $locale, { replaceState: true });
  });
</script>

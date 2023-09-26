<script context="module" lang="ts">
  import Error from '../../+error.svelte';
</script>

<script lang="ts">
  import type { PageData } from './$types';
  export let data: PageData;
  const status: number = data.status;
</script>

<Error {status} />

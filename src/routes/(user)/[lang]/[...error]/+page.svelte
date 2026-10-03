<script module lang="ts">
  import Error from '../../+error.svelte';
</script>

<script lang="ts">
  import type { PageData } from './$types';
  interface Props {
    data: PageData;
  }

  let { data }: Props = $props();
  const status: number = data.status;
</script>

<Error {status} />

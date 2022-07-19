<script lang="ts" context="module">
  import type { Load } from '@sveltejs/kit';
  import { refresh } from '$lib/auth';

  export const load: Load = async ({ fetch }) => {
    refresh(fetch);
    return {
      status: 200
    };
  };
</script>

<script lang="ts">
  import Header from '$lib/layout/Header.svelte';
  import Footer from '$lib/layout/Footer.svelte';
</script>

<Header />

<div class="h-96 mb-auto">
  <slot />
</div>

<Footer />

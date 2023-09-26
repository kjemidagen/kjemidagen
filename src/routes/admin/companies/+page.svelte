<script lang="ts">
  export let data: {
    companies: string[];
  };
</script>

<div>company admin</div>
{#each data.companies as company}
  <div>{company}</div>
{:else}
  <div>No companies</div>
{/each}

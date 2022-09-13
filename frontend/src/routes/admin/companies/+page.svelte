<script lang="ts">
  export let companies: string[];
</script>

<div>company admin</div>
{#each companies as company}
  <div>{company}</div>
{/each}

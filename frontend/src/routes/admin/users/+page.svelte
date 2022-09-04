<script lang="ts">
  export let users: string[];
</script>

<div>user admin</div>
{#each users as user}
  <div>{user}</div>
{/each}

<script lang="ts">
  import type { User } from '$lib/user';

  export let data: {
    users: User[];
  };
  console.log(data);
</script>

<div>user admin</div>
{#each data.users as user}
  <div>
    <span>
      {user.username}
    </span>
    <span>
      {user.isAdmin}
    </span>
    <span>
      {user.id}
    </span>
  </div>
{/each}

<script lang="ts">
  import type { User } from '$lib/user';

  export let data: {
    users: User[];
  };
</script>

<div class="grid grid-cols-3 content">
  <div class=" col-span-2">
    <h1 class="text-lg">user admin</h1>
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
    {:else}
      <div>No users</div>
    {/each}
  </div>
  <div>
    <a href="/admin/users/create">create user</a>
  </div>
</div>

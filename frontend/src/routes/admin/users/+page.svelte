<script lang="ts">
  import type { User } from '$lib/user';

  export let data: {
    users: User[];
  };
</script>

<div class="content grid grid-cols-3">
  <div class=" col-span-2">
    <h1 class="text-lg">User admin</h1>
    {#each data.users as user}
      <div>
        <a href="/admin/users/{user.id}" class="decoration-black hover:underline">
          {#if user.isAdmin}
            <span class="text-red">admin</span>
          {:else}
            <span class="text-red">company</span>
          {/if}
          <span class="text-black">
            {user.username}
          </span>
        </a>
      </div>
    {:else}
      <div>No users</div>
    {/each}
  </div>
  <div>
    <a href="/admin/users/create" class="text-bold border-red bg-red-light px-2 py-1 text-white"
      >create user</a
    >
  </div>
</div>

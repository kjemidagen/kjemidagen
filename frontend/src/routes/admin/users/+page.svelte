<script lang="ts">
  import type { User } from '$lib/user';

  export let data: {
    users: User[];
  };
</script>

<div class="grid grid-cols-3 content">
  <div class=" col-span-2">
    <h1 class="text-lg">User admin</h1>
    {#each data.users as user}
      <div>
        <a href="/admin/users/{user.id}" class="hover:underline decoration-black">
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
    <a href="/admin/users/create" class="border-red bg-red-light px-2 py-1 text-white text-bold"
      >create user</a
    >
  </div>
</div>

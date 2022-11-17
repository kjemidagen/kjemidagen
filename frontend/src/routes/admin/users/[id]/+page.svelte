<script lang="ts">
  import type { User } from '$lib/user';

  export let data: {
    user: User;
    id: string;
  };

  let editing = false;
</script>

<div class="grid grid-cols-3 content">
  <div class=" col-span-2">
    <h1 class="text-lg">user admin</h1>
    {#if data.user}
      <div>
        <span>
          {data.user.username}
        </span>
        <span>
          {data.user.isAdmin}
        </span>
        <span>
          {data.user.id}
        </span>
      </div>
    {:else}
      <div>No user with id {data.id}</div>
    {/if}
  </div>
  {#if data.user}
    <div>
      <a
        href="/admin/users{data.id}/edit"
        class="border-red bg-red-light px-2 py-1 text-white text-bold">create user</a
      >
    </div>
  {/if}
</div>

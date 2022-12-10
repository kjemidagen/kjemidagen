<script lang="ts">
  import type { User } from '$lib/user';

  export let user: User;
</script>

<div class="grid grid-cols-3 content">
  <h1 class="text-lg">Edit {user.username}</h1>
  <div>
    <span>
      {user.username}
    </span>
    <span>
      {user.isAdmin ? 'Admin' : 'Not admin'}
    </span>
    <span>
      {user.id}
    </span>
  </div>
</div>

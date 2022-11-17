<script lang="ts">
  import type { User } from '$lib/user';

  export let user: User;
</script>

<div class="grid grid-cols-3 content">
  <h1 class="text-lg">user admin</h1>
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
</div>

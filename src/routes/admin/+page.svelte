<script lang="ts">
  import { userData } from '$lib/stores';
  import { refresh, logout } from '$lib/auth';
</script>

<div><p>Logged in</p></div>
<div>{$userData !== undefined ? $userData.email : ''}</div>
<div class="break-all">{$userData !== undefined ? $userData.accessToken : ''}</div>
<button on:click={() => refresh(fetch)}>Refresh</button>
<button on:click={() => logout(fetch)}>Logout</button>

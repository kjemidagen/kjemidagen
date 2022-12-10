<script lang="ts">
  // import { refresh, logout } from '$lib/auth';

  import { userData } from '$lib/stores';
</script>

<div class="content">
  <div><p>Logged in</p></div>
  <div>{$userData?.email ?? 'Not logged in'}</div>
  <form action="/logout">
    <button type="submit">Logg ut</button>
  </form>

  <div><a href="admin/users">Brukeradmin</a></div>
  <div><a href="admin/companies">Bedriftsadmin</a></div>
</div>

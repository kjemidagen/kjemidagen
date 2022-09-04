<script lang="ts">
  import { goto } from '$app/navigation';
  import { login } from '$lib/auth';
  let email: string;
  let password: string;
  async function onSubmit() {
    await login(fetch, email, password);
    goto(`/admin`);
  }
</script>

<svelte:head>
  <title>Login</title>
</svelte:head>

<section class="content">
  <div>Login</div>
  <form on:submit|preventDefault={onSubmit}>
    <input type="email" name="username" placeholder="email" bind:value={email} />
    <input type="password" name="password" placeholder="password" bind:value={password} />
    <input type="submit" value="Logg Inn" />
  </form>
</section>

<style>
</style>

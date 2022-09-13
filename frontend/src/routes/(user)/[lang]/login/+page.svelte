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

<section class="content grid grid-cols-2">
  <form class="flex flex-col pr-6" on:submit|preventDefault={onSubmit}>
    <h1 class="text-3xl mb-8">Login</h1>
    <div class="mb-6">
      <input
        class="form-control block w-full px-4 py-2 text-xl font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-red focus:outline-none"
        type="email"
        name="username"
        placeholder="email"
        id="email"
        bind:value={email}
      />
    </div>
    <div class="mb-6">
      <input
        class="form-control block w-full px-4 py-2 text-xl font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-red focus:outline-none"
        type="password"
        name="password"
        placeholder="password"
        id="email"
        bind:value={password}
      />
    </div>
    <div>
      <input
        class="inline-block px-7 py-3 bg-red text-white font-medium text-sm leading-snug uppercase rounded shadow-md hover:bg-red-dark hover:shadow-lg focus:bg-red-dark focus:shadow-lg focus:outline-none focus:ring-0 active:bg-red-darker active:shadow-lg transition duration-150 ease-in-out"
        type="submit"
        value="Logg Inn"
      />
    </div>
  </form>
  <div class="h-full">
    <h2 class="text-xl mb-8">Informasjon om innlogging</h2>
    <p class="">Kommer senere</p>
  </div>
</section>

<style>
</style>

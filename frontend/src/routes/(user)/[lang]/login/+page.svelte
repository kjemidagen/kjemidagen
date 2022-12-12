<script lang="ts">
  import { goto } from '$app/navigation';
  import { login } from '$lib/auth';
  let email: string;
  let password: string;
  let feedback: string = '';
  async function onSubmit() {
    const res = await login(fetch, email, password);
    const status = res.status;
    if (status === 200) {
      goto(`/admin`);
    } else {
      feedback = 'Wrong password or email';
    }
  }
</script>

<svelte:head>
  <title>Login • Kjemidagen</title>
</svelte:head>

<section class="content grid grid-cols-2">
  <form class="flex flex-col pr-6" on:submit|preventDefault={onSubmit}>
    <h1 class="mb-8 text-3xl">Login</h1>
    <div class="mb-6">
      <input
        class="form-control m-0 block w-full rounded border border-solid border-gray-300 bg-white bg-clip-padding px-4 py-2 text-xl font-normal text-gray-700 transition ease-in-out focus:border-red focus:bg-white focus:text-gray-700 focus:outline-none"
        type="email"
        name="username"
        placeholder="email"
        id="email"
        bind:value={email}
      />
    </div>
    <div class="mb-6">
      <input
        class="form-control m-0 block w-full rounded border border-solid border-gray-300 bg-white bg-clip-padding px-4 py-2 text-xl font-normal text-gray-700 transition ease-in-out focus:border-red focus:bg-white focus:text-gray-700 focus:outline-none"
        type="password"
        name="password"
        placeholder="password"
        id="password"
        bind:value={password}
      />
    </div>
    <div>
      <input
        class="inline-block rounded bg-red px-7 py-3 text-sm font-medium uppercase leading-snug text-white shadow-md transition duration-150 ease-in-out hover:bg-red-dark hover:shadow-lg focus:bg-red-dark focus:shadow-lg focus:outline-none focus:ring-0 active:bg-red-darker active:shadow-lg"
        type="submit"
        value="Logg Inn"
      />
    </div>
    {#if feedback}
      <div>
        <p>{feedback}</p>
      </div>
    {/if}
  </form>
  <div class="h-full">
    <h2 class="mb-8 text-xl">Informasjon om innlogging</h2>
    <p class="">Kommer senere</p>
  </div>
</section>

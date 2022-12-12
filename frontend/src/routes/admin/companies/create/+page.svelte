<script lang="ts">
  import { createCompany } from '$lib/company';
  import { goto } from '$app/navigation';
  let email: string = '';
  let password: string = '';
  let repeatpass: string = '';
  let feedback: string | undefined;
  let emailField: HTMLInputElement;
  let repeatpassField: HTMLInputElement;

  async function onSubmit() {
    if (feedback === 'creating company') {
    }
    feedback = undefined;
    if (password !== repeatpass || password === '') {
      repeatpassField.setCustomValidity('Does not match password field');
      repeatpassField.reportValidity();
      return;
    }
    feedback = 'creating user';
    const response = await createCompany(email, password);
    if (response.status === 200) {
      goto(`/admin/companies/${response.message}`);
    }
  }

  function onTextChange() {
    repeatpassField.setCustomValidity('');
    repeatpassField.reportValidity();
  }
</script>

<div class="content">
  <h1 class="text-2xl text-red">Create company</h1>
  <form on:submit|preventDefault={onSubmit} on:change={onTextChange} class="flex flex-col">
    <div>
      <label for="email">Email</label>
      <input
        class="rounded border-2 border-red-light px-2"
        type="email"
        label="email"
        placeholder="email"
        bind:value={email}
        bind:this={emailField}
        required
      />
    </div>
    <div>
      <label for="password">Password</label>
      <input
        class="rounded border-2 border-red-light px-2"
        type="password"
        label="password"
        placeholder="password"
        bind:value={password}
        required
      />
    </div>
    <div>
      <label for="repeatpass">Repeat password</label>
      <input
        class="rounded border-2 border-red-light px-2"
        type="password"
        label="repeat password"
        placeholder="repeat password"
        bind:value={repeatpass}
        bind:this={repeatpassField}
        required
      />
    </div>
    <div>
      <button
        type="submit"
        class="rounded border-2 border-red bg-red-light px-2 py-1 font-extrabold text-white"
        >Create</button
      >
    </div>
  </form>
</div>

{#if feedback !== undefined}
  <div>{feedback}</div>
{/if}

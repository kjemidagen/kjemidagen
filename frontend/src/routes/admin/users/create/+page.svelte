<script lang="ts">
  import { createUser } from '$lib/user';
  let email: string = '';
  let password: string = '';
  let repeatpass: string = '';
  let feedback: string | undefined;
  let emailField: HTMLInputElement;
  let repeatpassField: HTMLInputElement;

  async function onSubmit() {
    if (feedback === 'creating user') {
    }
    feedback = undefined;
    if (password === repeatpass && password !== '') {
      feedback = 'creating user';
      const response = await createUser(email, password);
      console.log(response);
      repeatpassField.setCustomValidity('');
    } else {
      repeatpassField.setCustomValidity('Does not match password field');
      repeatpassField.reportValidity();
    }
  }
</script>

<div class="content">
  <h1 class="text-2xl text-red">Create user</h1>
  <form on:submit|preventDefault={onSubmit} class="flex flex-col">
    <div>
      <label for="email">Email</label>
      <input
        class="border-2 border-red-light rounded px-2"
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
        class="border-2 border-red-light rounded px-2"
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
        class="border-2 border-red-light rounded px-2"
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
        class="border-2 border-red rounded px-2 py-1 text-white font-extrabold bg-red-light"
        >Create</button
      >
    </div>
  </form>
</div>

{#if feedback !== undefined}
  <div>{feedback}</div>
{/if}

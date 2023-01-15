<script lang="ts">
  import { goto } from '$app/navigation';
  import { editUser, type User } from '$lib/user';

  export let data: {
    user: User;
    id: string;
    accessToken: string;
  };
  let new_is_admin: boolean = data.user.isAdmin;
  let new_password: string = '';
  let repeat_password: string = '';
  let feedback: string = '';

  async function onSubmit() {
    let send_password: string | undefined = undefined;
    if (new_password !== '' && repeat_password !== '') {
      if (new_password === repeat_password) {
        send_password = new_password;
      }
    }
    const res = await editUser(data.user.id, send_password, new_is_admin, data.accessToken);
    if (res.status === 200) {
      goto(`/admin/users/${res.message}`);
    }
    feedback = 'Something failed';
  }
</script>

<div class="content grid grid-cols-3">
  <div class="col-span-2">
    <h1 class="text-lg">Edit {data.user.username}</h1>
    <form on:submit={onSubmit}>
      <div>
        <label for="password">Password</label>
        <input
          name="password"
          type="password"
          placeholder="new password"
          bind:value={new_password}
        />
      </div>
      <div>
        <label for="repeatpass">Repeat password</label>
        <input
          name="repeatpass"
          type="password"
          placeholder="repeat password"
          bind:value={repeat_password}
        />
      </div>
      <label class="relative mt-4 inline-flex cursor-pointer items-center">
        <input name="is-admin" type="checkbox" class="peer sr-only" bind:checked={new_is_admin} />
        <div
          class="peer h-6 w-11 rounded-full bg-gray-200 after:absolute after:top-[2px] after:left-[2px] after:h-5 after:w-5 after:rounded-full after:border after:border-gray-300 after:bg-white after:transition-all after:content-[''] peer-checked:bg-red peer-checked:after:translate-x-full peer-checked:after:border-white peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-red-light"
        />
        <span class="ml-3">Admin?</span>
      </label>
      <div>
        <button
          type="submit"
          class="rounded border-2 border-red bg-red-light px-2 py-1 font-extrabold text-white"
          >Lagre endringer</button
        >
      </div>
      {#if feedback}
        <p>{feedback}</p>
      {/if}
    </form>
  </div>
</div>

<script lang="ts">
  import { isLoginOpen } from '$lib/stores';
  import { env } from '$lib/envVars';

  let email: string;
  let password: string;

  async function handleLogin(event: SubmitEvent) {
    const formData = {
      username: email,
      password: password
    };
    const response = await fetch(env.apiUrl + '/v1/auth/login', {
      method: 'POST',
      body: JSON.stringify(formData)
    });
    const responseData = await response.json();
    alert(responseData);
  }
</script>

<div class="background" on:click={() => ($isLoginOpen = false)} />
<div class="modal">
  <form on:submit|preventDefault={handleLogin}>
    <h1>Logg inn</h1>
    <label for="email">Epost-adresse: </label><input
      type="email"
      name="email"
      placeholder="ola@nordmann.no"
      bind:value={email}
    />
    <label for="password">Passord: </label><input
      type="password"
      name="password"
      placeholder="Passord"
      bind:value={password}
    />
    <button type="submit" name="login" value="1">Logg inn</button>
  </form>
</div>

<style>
  .background {
    position: fixed;
    z-index: 1000;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: #10090970;
  }

  .modal {
    position: fixed;
    z-index: 1001;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    filter: drop-shadow(0 0 20px #333);
    padding: 1rem 2rem 2rem 2rem;
    border-radius: 0.2rem;
    background: var(--color-bg-primary);
  }
</style>

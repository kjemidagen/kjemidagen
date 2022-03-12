<script>
  import { isLoginOpen } from '$lib/stores';
</script>

<header id="header">
  <div class="center">
    <a class="home" href={'/'}>
      <img class="logo" src="/logo_inverted.svg" alt="logo" width="40" />
      <span>Kjemidagen</span>
    </a>
    <ul>
      <li><a href="/">Hjem</a></li>
      <li><a href="/about">Om kjemidagen</a></li>
      <li><a href="/program">Program</a></li>
      <li><a href="/contact">Ta kontakt</a></li>
      <li><a href="/companies">Bedrifter</a></li>
      <li><a href="/english">English</a></li>
      <li>
        <button
          class="login"
          href="/login"
          on:click={(event) => {
            event.preventDefault;
            $isLoginOpen = true;
            return false;
          }}>Logg inn</button
        >
      </li>
    </ul>
  </div>
</header>

<style>
  header {
    display: block;
    width: 100%;
    justify-content: right;
    position: sticky;
    top: 0;
    left: 0;
    background-color: var(--color-bg-brand);
    z-index: 1000;
  }
  .center {
    align-items: center;
    max-width: var(--document-width);
    display: flex;
    justify-content: space-between;
    margin: auto;
    padding: 1rem;
  }
  .home {
    display: flex;
    text-decoration: none;
    font-size: larger;
    color: var(--color-text-loud);
    align-items: center;
  }
  .logo {
    margin-right: 0.5rem;
  }

  .login {
    border: 1px solid var(--color-text-inverted);
    border-radius: 3px;
    background-color: inherit;
    color: var(--color-text-inverted);
    cursor: pointer;
  }

  ul {
    list-style: none;
  }
  li {
    display: inline-block;
    margin: auto 0.3rem;
  }

  a {
    color: var(--color-text-loud);
  }
</style>

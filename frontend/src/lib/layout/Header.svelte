<header id="header">
  <div class="center">
    <a class="home" href={'/'}>
      <img class="logo" src="/logo_inverted.svg" alt="logo" width="40" />
      <span>Kjemidagen</span>
    </a>
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
    background-color: var(--color-bg-primary);
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
</style>

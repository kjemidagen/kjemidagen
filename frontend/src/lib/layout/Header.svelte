<script lang="ts">
  import { isLoginOpen } from '$lib/stores';

  import { t, locales, locale } from '$lib/translations/translations';
  import { page } from '$app/stores';
  import { goto } from '$app/navigation';

  $: ({ route } = $page.stuff);
  const handleLanguageSwitch: svelte.JSX.ChangeEventHandler<HTMLSelectElement> = ({ target }) => {
    const target2 = target as HTMLOptionElement; // This is ugly
    console.log(target2.value);
    goto(target2.value);
  };
</script>

<header id="header">
  <div class="center">
    <a class="home" href={'/'}>
      <img class="logo" src="/logo_inverted.svg" alt="logo" width="40" />
      <span>{$t('common.chemday')}</span>
    </a>
    <ul class="navigation">
      <li><a href="/">{$t('common.home')}</a></li>
      <li><a href="/about">{$t('common.about')}</a></li>
      <li><a href="/program">{$t('common.program')}</a></li>
      <li><a href="/companies">{$t('common.companies')}</a></li>
      <li><a href="/sponsors">{$t('common.sponsors')}</a></li>
    </ul>
    <button>
      <img src="hamburgermeny.svg" alt="hamburgermeny" />
    </button>
    <select on:change={handleLanguageSwitch}>
      {#each $locales as lc}
        <option value="/{lc}{route}" selected={lc === $locale}>{$t(`lang.${lc}`)}</option>
      {/each}
    </select>
    <button
      class="login"
      href="/login"
      on:click={(event) => {
        event.preventDefault;
        $isLoginOpen = true;
        return false;
      }}>{$t('common.login')}</button
    >
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

  li {
    display: inline-block;
    margin: auto 0.3rem;
  }

  a {
    color: var(--color-text-loud);
  }

  .navigation {
    list-style: none;
  }

  @media screen and (max-width: 768px) {
    .navigation {
      visibility: hidden;
    }
  }
</style>

<script context="module">
  import { loadTranslations } from '$lib/translations/translations';

  import favicon from '$lib/assets/favicon.ico';

  /** @type {import('@sveltejs/kit').Load} */
  export const load = async ({ url }) => {
    const { pathname } = url;

    const lang = `${pathname.match(/[^/]+?(?=\/|$)/) || ''}`;

    const route = pathname.replace(new RegExp(`^/${lang}`), '');

    await loadTranslations(lang, route);

    return { stuff: { route, lang } };
  };
</script>

<svelte:head>
  <link rel="icon" href={favicon} />
</svelte:head>

<slot />

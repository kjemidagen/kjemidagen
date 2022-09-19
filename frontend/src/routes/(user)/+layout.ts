
import { loadTranslations } from '$lib/translations/translations';
import type { LayoutLoad } from "../../../.svelte-kit/types/src/routes/$types";

export const load: LayoutLoad = async ({ url }) => {
  const { pathname } = url;
  const defaultLocale = "no";

  const lang = `${pathname.match(/[^/]+?(?=\/|$)/) || defaultLocale}`;

  const route = pathname.replace(new RegExp(`^/${lang}`), '');

  await loadTranslations(lang, route);

  return { route, lang };
};

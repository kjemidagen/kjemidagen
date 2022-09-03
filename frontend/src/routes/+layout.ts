
import { loadTranslations } from '$lib/translations/translations';
import type { LayoutLoad } from "./$types";

export const load: LayoutLoad = async ({ url }) => {
  const { pathname } = url;

  const lang = `${pathname.match(/[^/]+?(?=\/|$)/) || ''}`;

  const route = pathname.replace(new RegExp(`^/${lang}`), '');

  await loadTranslations(lang, route);

  return { route, lang };
};

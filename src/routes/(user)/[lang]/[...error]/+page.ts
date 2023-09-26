import { dev } from '$app/environment';
import { loadTranslations } from '$lib/translations/translations';

import type { PageLoad } from './$types';

export const load: PageLoad = async ({ params }) => {
  const { error, lang } = params;

  let status = parseInt(error);

  if (Number.isNaN(status)) status = 404;

  await loadTranslations(lang, 'error');

  return {
    props: { status },
    /**
     * NOTE: The `status` prop redirects us to `__error.svelte` in dev mode with correct error code,
     * but for build returns 200 and renders this page (imported `__error.svelte` with status prop).
     */
    status: dev ? status : 200,
    stuff: { status }
  };
};

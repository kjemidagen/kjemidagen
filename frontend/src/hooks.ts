import type { Handle, ExternalFetch } from '@sveltejs/kit';
import { defaultLocale, locales } from '$lib/translations/translations';

const routeRegex = new RegExp(/^\/[^.]*([?#].*)?$/);

export const handle: Handle = async ({ event, resolve }) => {
  const { url, request } = event;
  const { pathname } = url;

  // If this request is a route request
  if (routeRegex.test(pathname)) {
    // Get defined locales
    const supportedLocales = locales.get();

    // Try to get locale from `pathname`.
    let locale = supportedLocales.find(
      (l) => `${l}`.toLowerCase() === `${pathname.match(/[^/]+?(?=\/|$)/)}`.toLowerCase()
    );

    // If route locale is not supported
    if (!locale) {
      // Get user preferred locale
      locale = `${`${request.headers.get('accept-language')}`.match(
        /[a-zA-Z]+?(?=-|_|,|;)/
      )}`.toLowerCase();

      // Set default locale if user preferred locale does not match
      if (!supportedLocales.includes(locale)) locale = defaultLocale;

      // 301 redirect
      return new Response(undefined, {
        headers: { location: `/${locale}${pathname}` },
        status: 301
      });
    }

    // Add html `lang` attribute
    return resolve(event, {
      transformPage: ({ html }) => html.replace(/<html.*>/, `<html lang="${locale}">`)
    });
  }

  return resolve(event);
};

const publicApiUrl: string = import.meta.env.VITE_PUBLIC_API_URL; // https://www.kjemidagen.com
const localApiUrl: string = import.meta.env.VITE_SSR_API_URL; // https://backend:8000

export const externalFetch: ExternalFetch = async (request) => {
  if (request.url.startsWith(publicApiUrl)) {
    request = new Request(request.url.replace(publicApiUrl, localApiUrl), request);
  }
  return fetch(request);
};

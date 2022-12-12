import type { Handle, HandleFetch } from '@sveltejs/kit';
import { defaultLocale, locales } from '$lib/translations/translations';

const routeRegex = new RegExp(/^\/[^.]*([?#].*)?$/);

export const handle: Handle = async ({ event, resolve }) => {
  const { url } = event; // request is in this object if you need it
  const { pathname } = url;

  // If this request is a route request
  if (routeRegex.test(pathname)) {
    // Admin requests dont need lang data
    if (pathname.slice(0, 6) === '/admin') {
      return resolve(event);
    }
    // All other requests need lang data

    // Get defined locales
    const supportedLocales = locales.get();

    // Try to get locale from `pathname`.
    let locale = supportedLocales.find(
      (l) => `${l}`.toLowerCase() === `${pathname.match(/[^/]+?(?=\/|$)/)}`.toLowerCase()
    );

    // If route locale is not supported
    if (!locale) {
      locale = defaultLocale;

      // 301 redirect
      return new Response(undefined, {
        headers: { location: `/${locale}${pathname}` },
        status: 301
      });
    }

    // Add html `lang` attribute
    return resolve(event, {
      transformPageChunk: ({ html }) => html.replace(/<html.*>/, `<html lang="${locale}">`)
    });
  }
  return resolve(event);
};

const publicApiUrl: string = import.meta.env.VITE_PUBLIC_API_URL; // https://www.kjemidagen.com
const localApiUrl: string = import.meta.env.VITE_SSR_API_URL; // https://backend:8000

export const handleFetch: HandleFetch = async ({ request }) => {
  if (request.url.startsWith(publicApiUrl)) {
    request = new Request(request.url.replace(publicApiUrl, localApiUrl), request);
  }
  return fetch(request);
};

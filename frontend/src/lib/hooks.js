/* eslint-disable @typescript-eslint/explicit-module-boundary-types */
import cookie from 'cookie';
import { v4 as uuid } from '@lukeed/uuid';

export const handle = async ({ request, resolve }) => {
  const cookies = cookie.parse(request.headers.cookie || '');
  request.locals.userid = cookies.userid || uuid();

  // TODO https://github.com/sveltejs/kit/issues/1046
  if (request.query.has('_method')) {
    request.method = request.query.get('_method').toUpperCase();
  }

  const response = await resolve(request);

  if (!cookies.userid) {
    // if this is the first time the user has visited this app,
    // set a cookie so that we recognise them when they return
    response.headers['set-cookie'] = `userid=${request.locals.userid}; Path=/; HttpOnly`;
  }

  return response;
};

export function getSession(request) {
  console.log('request.headers["accept-language"]', request.headers['accept-language']);
  let acceptedLanguage =
    request.headers['accept-language'] && request.headers['accept-language'].split(',')[0];
  console.log('aracceptedLanguage', acceptedLanguage);
  return { acceptedLanguage };
}

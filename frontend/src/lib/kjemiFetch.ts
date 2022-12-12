import { userData } from './stores';
import { get } from 'svelte/store';
import { refresh } from '$lib/auth';

// const apiUrl: string = import.meta.env.VITE_PUBLIC_API_URL;

export interface fetchOptions {
  headers?: Headers;
  method?: 'GET' | 'POST' | 'PATCH' | 'PUT' | 'DELETE';
  data?: BodyInit;
}

export type fetchFunc =
  | ((input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>)
  | ((info: RequestInfo, init?: RequestInit | undefined) => Promise<Response>);

export async function kjemiFetch(
  fetch: fetchFunc,
  url: string,
  options?: fetchOptions
): Promise<Response> {
  let user = get(userData);
  if (user === undefined || user?.accessTokenExp < Date.now()) {
    await refresh(fetch);
    user = get(userData);
  }
  const headers = options?.headers || new Headers();
  headers.append('Authorization', 'Bearer ' + user?.accessToken || '');
  headers.append('Content-Type', 'application/json');
  return await fetch(url, {
    headers: headers,
    method: options?.method,
    body: options?.data
  });
}

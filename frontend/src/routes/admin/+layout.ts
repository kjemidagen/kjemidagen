import type { LayoutLoad } from './$types';
import { refresh } from '$lib/auth';
import { redirect } from '@sveltejs/kit';

export const ssr = false;

export const load: LayoutLoad = async ({ fetch }) => {
  const res = await refresh(fetch);
  if (res.status === 401) {
    // Credentials exception
    console.log(typeof window);
    throw redirect(302, '/no/login');
  }
  return;
};

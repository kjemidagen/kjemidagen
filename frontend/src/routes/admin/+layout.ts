import type { LayoutLoad } from './$types';
import { refresh } from '$lib/auth';
import { redirect } from '@sveltejs/kit';

// export const ssr = false;

export const load: LayoutLoad = async ({ fetch }) => {
  const { res, data } = await refresh(fetch);
  if (res.status === 401) {
    // Credentials exception
    throw redirect(307, '/no/login');
  } else if (res.status !== 200) {
    console.error('Refresh failed with', res.status);
  }

  return { accessToken: data.accessToken, email: data.email };
};

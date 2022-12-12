import type { PageLoad } from './$types';
import { kjemiFetch } from '$lib/kjemiFetch';

const apiUrl: string = import.meta.env.VITE_PUBLIC_API_URL;

export const load: PageLoad = async ({ fetch }) => {
  // TODO: Pagination?
  const res = await kjemiFetch(fetch, apiUrl + '/v1/companies/');
  const data = await res.json();
  return { companies: data };
};

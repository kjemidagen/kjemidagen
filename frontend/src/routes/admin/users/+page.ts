import type { PageLoad } from './$types';
import { kjemiFetch } from '$lib/kjemiFetch';

const apiUrl: string = import.meta.env.VITE_PUBLIC_API_URL;

export const load: PageLoad = async ({ fetch, parent }) => {
  // TODO: pagination, ta insp fra gmail tenker jeg
  const { accessToken } = await parent();
  const res = await kjemiFetch(fetch, apiUrl + '/v1/users/', accessToken);
  const data = await res.json();
  return { users: data };
};

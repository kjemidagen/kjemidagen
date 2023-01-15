import type { LayoutLoad } from './$types';
import type { User } from '$lib/user';
import { kjemiFetch } from '$lib/kjemiFetch';

const apiUrl: string = import.meta.env.VITE_PUBLIC_API_URL;

export const load: LayoutLoad = async ({ fetch, params, parent }) => {
  const { accessToken } = await parent();
  const res = await kjemiFetch(fetch, apiUrl + '/v1/users/' + params.id, accessToken);
  const data: User = await res.json();
  return { user: data, id: params.id };
};

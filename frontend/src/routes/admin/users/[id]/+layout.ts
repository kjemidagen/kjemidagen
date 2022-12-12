import type { LayoutLoad } from './$types';
import type { User } from '$lib/user';
import { kjemiFetch } from '$lib/kjemiFetch';

const apiUrl: string = import.meta.env.VITE_PUBLIC_API_URL;

export const load: LayoutLoad = async ({ fetch, params }) => {
  const res = await kjemiFetch(fetch, apiUrl + '/v1/users/' + params.id);
  const data: User = await res.json();
  return { user: data, id: params.id };
};

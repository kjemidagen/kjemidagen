import type { LayoutLoad } from './$types';
import type { Company } from '$lib/company';
import { kjemiFetch } from '$lib/kjemiFetch';

const apiUrl: string = import.meta.env.VITE_PUBLIC_API_URL;

export const load: LayoutLoad = async ({ fetch, params }) => {
  const res = await kjemiFetch(fetch, apiUrl + '/v1/companies/' + params.id);
  const data: Company = await res.json();
  return { company: data, id: params.id };
};

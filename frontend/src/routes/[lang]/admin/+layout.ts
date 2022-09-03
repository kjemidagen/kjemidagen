
import type { LayoutLoad } from './$types';
import { refresh } from '$lib/auth';

export const load: LayoutLoad = async ({ fetch }) => {
  refresh(fetch);
  return;
};


import type { LayoutLoad } from './$types';
import { refresh } from '$lib/auth';
import { userData } from '$lib/stores';
import { get } from "svelte/store";

export const load: LayoutLoad = async ({ fetch, setHeaders }) => {
  const user = get(userData);
  if (user === undefined || user.accessTokenExp < Date.now()) {
    const refreshHeaders = await refresh(fetch);
    setHeaders({ 'set-cookie': refreshHeaders.get('set-cookie') });
  }
  return;
};

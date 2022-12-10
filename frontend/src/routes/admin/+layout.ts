import type { LayoutLoad } from "./$types";
import { refresh } from "$lib/auth";

export const ssr = false;

export const load: LayoutLoad = async ({ fetch }) => {

  await refresh(fetch);

  return;
};

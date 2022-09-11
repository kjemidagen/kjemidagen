import { userData } from "./stores";
import { get } from "svelte/store";

export interface fetchOptions {
  headers?: Headers;
}

export type fetchFunc =
  ((input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>)
  | ((info: RequestInfo, init?: RequestInit | undefined) => Promise<Response>);


export async function kjemiFetch(
  fetch: fetchFunc,
  url: string,
  options?: fetchOptions
): Promise<Response> {
  // TODO: refresh token middleware
  const user = get(userData);
  if (user === undefined) {
    console.error("Error, not logged in.");
  }
  const headers = options?.headers || new Headers();
  headers.append("Authorization", "Bearer " + user?.accessToken || "");
  return await fetch(url, {
    headers: headers
  });
}

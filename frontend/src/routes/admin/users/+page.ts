import type { PageLoad } from "./$types";
import { kjemiFetch } from "$lib/kjemiFetch";

const apiUrl: string = import.meta.env.VITE_PUBLIC_API_URL;

export const load: PageLoad = async ({ fetch }) => {
  console.log("loading users");
  const res = await kjemiFetch(fetch, apiUrl + "/v1/users/");
  const data = await res.json();
  console.log("users", data);
  return { users: ["user 1"] };
};

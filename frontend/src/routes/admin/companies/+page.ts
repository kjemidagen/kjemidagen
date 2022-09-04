import type { PageLoad } from "./$types";
import { kjemiFetch } from "$lib/kjemiFetch";

const apiUrl: string = import.meta.env.VITE_PUBLIC_API_URL;


export const load: PageLoad = ({ fetch }) => {
  console.log("loading companies");
  kjemiFetch(fetch, apiUrl + "/v1/", {});
  return { companies: "company 1" };
};

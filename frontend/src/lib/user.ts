import { kjemiFetch } from "./kjemiFetch";

const apiUrl: string = import.meta.env.VITE_PUBLIC_API_URL;


export interface User {
  id: string;
  username: string;
  isAdmin: boolean;
}

export async function createUser(email: string, password: string) {
  console.log(email, password);
  const res = await kjemiFetch(
    fetch,
    apiUrl + "/v1/users/",
    {
      method: "POST",
      data: JSON.stringify({ username: email, password: password })
    }
  );
  const data = await res.json();
  return data;
}

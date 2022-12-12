import { kjemiFetch } from './kjemiFetch';

const apiUrl: string = import.meta.env.VITE_PUBLIC_API_URL;

export interface User {
  id: number;
  username: string;
  isAdmin: boolean;
}

export async function createUser(
  email: string,
  password: string
): Promise<{ status: number; message: string }> {
  const res = await kjemiFetch(fetch, apiUrl + '/v1/users/', {
    method: 'POST',
    data: JSON.stringify({ username: email, password: password })
  });
  const data = await res.json();
  return { status: res.status, message: data['id'] };
}

export async function editUser(
  id: number,
  password: string | undefined,
  isAdmin: boolean | undefined
): Promise<{ status: number; message: string }> {
  const res = await kjemiFetch(fetch, apiUrl + `/v1/users/${id}`, {
    method: 'PATCH',
    data: JSON.stringify({ password: password, isAdmin: isAdmin })
  });
  const data = await res.json();
  return { status: res.status, message: data['id'] };
}

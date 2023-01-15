import { invalidate } from '$app/navigation';
import { kjemiFetch } from './kjemiFetch';

const apiUrl: string = import.meta.env.VITE_PUBLIC_API_URL;

export interface User {
  id: number;
  username: string;
  isAdmin: boolean;
}

export async function createUser(
  email: string,
  password: string,
  accessToken: string
): Promise<{ status: number; message: string }> {
  const res = await kjemiFetch(fetch, apiUrl + '/v1/users/', accessToken, {
    method: 'POST',
    data: JSON.stringify({ username: email, password: password })
  });
  const data = await res.json();
  return { status: res.status, message: data['id'] };
}

export async function editUser(
  id: number,
  password: string | undefined,
  isAdmin: boolean | undefined,
  accessToken: string
): Promise<{ status: number; message: string }> {
  const res = await kjemiFetch(fetch, apiUrl + `/v1/users/${id}`, accessToken, {
    method: 'PATCH',
    data: JSON.stringify({ password: password, isAdmin: isAdmin })
  });
  invalidate(apiUrl + '/v1/users/' + id);
  const data = await res.json();
  return { status: res.status, message: data['id'] };
}

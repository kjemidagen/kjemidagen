import { kjemiFetch } from './kjemiFetch';

const apiUrl: string = import.meta.env.VITE_PUBLIC_API_URL;

export interface Company {
  id: number;
  user_id: number;
  title: string;
  public_email: string;
  additional_data: string | undefined;
}

export async function createCompany(
  email: string,
  title: string,
  numberOfRepresentatives: number,
  publicEmail: string,
  additionalData: string,
  accessToken: string
): Promise<{ status: number; message: string }> {
  const res = await kjemiFetch(fetch, apiUrl + '/v1/companies/', accessToken, {
    method: 'POST',
    data: JSON.stringify({
      username: email,
      title: title,
      numberOfRepresentatives: numberOfRepresentatives,
      publicEmail: publicEmail,
      additionalData: additionalData
    })
  });
  const data = await res.json();
  return { status: res.status, message: data['id'] };
}

export async function editCompany(
  password: string | undefined,
  isAdmin: boolean | undefined,
  accessToken: string
): Promise<{ status: number; message: string }> {
  const res = await kjemiFetch(fetch, apiUrl + '/v1/companies/', accessToken, {
    method: 'PATCH',
    data: JSON.stringify({ password: password, isAdmin: isAdmin })
  });
  const data = await res.json();
  return { status: res.status, message: data['id'] };
}

import { userData } from '$lib/stores';

const apiUrl: string = import.meta.env.VITE_PUBLIC_API_URL;

type fetchFunc = (input: RequestInfo, init?: RequestInit) => Promise<Response>;

export async function login(fetch: fetchFunc, email: string, password: string) {
  const formData = new FormData();
  formData.append('username', email);
  formData.append('password', password);
  // Note: this is the only fetch using formData because it adheres to
  // Oauth2 standards
  const res = await fetch(apiUrl + '/v1/auth/login', {
    method: 'POST',
    body: formData,
    credentials: 'include' //'same-origin'
  });
  // TODO: handle bad credidentials
  const data = await res.json();
  userData.set(data);
}

export async function refresh(fetch: fetchFunc) {
  // Note: this is the only fetch using formData because it adheres to
  // Oauth2 standards
  const res = await fetch(apiUrl + '/v1/auth/token', {
    method: 'POST',
    credentials: 'include' // 'same-origin'
  });
  const data = await res.json();
  userData.set(data);
  return res.headers;
}

export async function logout(fetch: fetchFunc) {
  const res = await fetch(apiUrl + '/v1/auth/logout', {
    method: 'POST',
    credentials: 'include' // 'same-origin'
  });
  if (res.status === 200) {
    userData.set(undefined);
  } else {
    console.error(res.status);
  }
}

export interface fetchOptions {
  headers?: Headers;
  method?: 'GET' | 'POST' | 'PATCH' | 'PUT' | 'DELETE';
  data?: BodyInit;
}

export type fetchFunc =
  | ((input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>)
  | ((info: RequestInfo, init?: RequestInit | undefined) => Promise<Response>);

export async function kjemiFetch(
  fetch: fetchFunc,
  url: string,
  accessToken: string,
  options?: fetchOptions
): Promise<Response> {
  const headers = options?.headers || new Headers();
  headers.append('Authorization', 'Bearer ' + accessToken || '');
  headers.append('Content-Type', 'application/json');
  return await fetch(url, {
    headers: headers,
    method: options?.method,
    body: options?.data
  });
}

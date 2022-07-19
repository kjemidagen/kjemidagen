export async function kjemiFetch(
  fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
  input: RequestInfo | URL,
  init?: RequestInit | undefined
): Promise<Response> {
  // TODO: refresh token middleware
  return await fetch(input, init);
}

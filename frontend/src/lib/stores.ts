import { writable } from 'svelte/store';

interface UserData {
  accessToken: string;
  refreshToken: string;
  email: string;
}

export const userData = writable<UserData | undefined>();

import { writable } from 'svelte/store';

interface UserData {
  accessToken: string;
  accessTokenExp: number;
  email: string;
}

export const userData = writable<UserData | undefined>();

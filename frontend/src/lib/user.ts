
export interface User {
  id: string;
  username: string;
  isAdmin: boolean;
}

export function createUser(email: string, password: string) {
  console.log(email, password);
}

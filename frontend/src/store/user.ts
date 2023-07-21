import { defineStore } from 'pinia';

export interface User {
  id: number;
  username: string;
  email: string;
  display_name: string;
  // Add more properties as needed
}

export const useUserStore = defineStore('user', {
  state() {
    return {
      accessToken: '',
      user: null as User | null, // Define user as User type or null
    };
  },
  getters: {
    isLoggedIn: (state) => !!state.accessToken,
  },
  actions: {
    setAccessToken(token: string) {
      this.accessToken = token;
    },
    setUser(user: User) {
      this.user = user;
    },
    logout() {
      this.accessToken = '';
      this.user = null;
    },
  },
  persist: true,
});

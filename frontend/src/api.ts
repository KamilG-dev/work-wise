import axios from 'axios';
import { useUserStore } from '@/store/user';
import { API_ENDPOINT } from './constants';
// Create an instance of Axios
const api = axios.create({
  baseURL: API_ENDPOINT, // Replace with your API base URL
});

// api.interceptors.request.use((config) => {
//   const userStore = useUserStore();
//   if (userStore.accessToken) {
//     // Add the authorization header with the access token
//     config.headers.Authorization = `Bearer ${userStore.accessToken}`;
//   }
//   return config;
// });

api.interceptors.request.use((config) => {
    config.headers.Authorization = `Bearer ${useUserStore().accessToken}`;
    return config;
});
export function setAuthHeader(token: string) {
    api.defaults.headers.Authorization = `Bearer ${token}`;
}

export default api;

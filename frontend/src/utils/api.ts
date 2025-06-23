import axios from 'axios';
import jwtDecode from 'jwt-decode';

let tokenGetter: () => string | null = () => null;
let logoutHandler: (() => void) | null = null;

export const setTokenGetter = (getter: () => string | null) => {
  tokenGetter = getter;
};

export const setLogoutHandler = (handler: () => void) => {
  logoutHandler = handler;
};

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
});

api.interceptors.request.use((config) => {
  const token = tokenGetter();
  if (token) {
    try {
      const decoded: { exp: number } = jwtDecode(token);
      if (Date.now() >= decoded.exp * 1000) {
        logoutHandler?.();
        return config;
      }
    } catch {}
    config.headers = config.headers || {};
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      logoutHandler?.();
    }
    return Promise.reject(error);
  },
);

export default api;

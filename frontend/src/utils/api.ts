import axios from 'axios';

let tokenGetter: () => string | null = () => null;

export const setTokenGetter = (getter: () => string | null) => {
  tokenGetter = getter;
};

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
});

api.interceptors.request.use((config) => {
  const token = tokenGetter();
  if (token) {
    config.headers = config.headers || {};
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
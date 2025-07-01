import axios from 'axios';
import { useAuth } from './AuthProvider';

const instance = axios.create({
  baseURL: 'http://localhost:8000',
  withCredentials: true,
});

export const attachToken = (token) => {
  instance.defaults.headers.common['Authorization'] = `Bearer ${token}`;
};

export default instance;

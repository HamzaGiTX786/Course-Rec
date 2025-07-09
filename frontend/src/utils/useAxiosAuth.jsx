import { useEffect } from 'react';
import api from './axiosInstance';
import { useAuth } from './AuthProvider';
import { useNavigate } from 'react-router-dom';

export default function useAxiosAuth() {
  const { accessToken, setAccessToken, logout } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    const requestInterceptor = api.interceptors.request.use(
      (config) => {
        if (accessToken) {
          config.headers.Authorization = `Bearer ${accessToken}`;
        }
        return config;
      },
      (error) => Promise.reject(error)
    );

    const responseInterceptor = api.interceptors.response.use(
      (response) => response,
      async (error) => {
        const originalRequest = error.config;

        if (
          error.response?.status === 401 &&
          !originalRequest._retry
        ) {
          originalRequest._retry = true;

          try {
            const res = await api.get('/users/refresh/', {
              withCredentials: true,
            });

            const newToken = res.data.access_token;
            setAccessToken(newToken);

            originalRequest.headers.Authorization = `Bearer ${newToken}`;
            return api(originalRequest);
          } catch (refreshErr) {
            console.error('Token refresh failed after 401', refreshErr);
            logout(); // clears state and sends logout request
            navigate('/login');
            return Promise.reject(refreshErr);
          }
        }

        return Promise.reject(error);
      }
    );

    return () => {
      api.interceptors.request.eject(requestInterceptor);
      api.interceptors.response.eject(responseInterceptor);
    };
  }, [accessToken, setAccessToken, logout, navigate]);

  return api;
}

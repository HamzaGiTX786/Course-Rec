import { createContext, useContext, useEffect, useState } from 'react';
import axios from 'axios';

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [accessToken, setAccessToken] = useState(null);
  const [loading, setLoading] = useState(true);

  // Refresh once on mount
  useEffect(() => {
    const fetchToken = async () => {
      try {
        const res = await axios.get('/users/refresh/', {
          withCredentials: true,
        });
        setAccessToken(res.data.access_token);
      } catch (err) {
        console.error('Initial token refresh failed:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchToken();
  }, []);

  // Refresh token periodically
  useEffect(() => {
    if (!accessToken) return;

    const interval = setInterval(async () => {
      try {
        const res = await axios.get('/users/refresh/', {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
          withCredentials: true,
        });
        setAccessToken(res.data.access_token);
      } catch (err) {
        console.error('Periodic refresh failed:', err);
        setAccessToken(null);
      }
    }, 4.5 * 60 * 1000); // every 4.5 minutes

    return () => clearInterval(interval);
  }, [accessToken]);

  const logout = () => {
    axios.get('http://localhost:8000/users/logout/', 
      { withCredentials: true,
       headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    }).catch((err) => {
      console.error('Logout request failed', err);
    });

    setAccessToken(null);
  };

  return (
    <AuthContext.Provider value={{ accessToken, setAccessToken, logout }}>
      {!loading && children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}

import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import { useAuth } from '../utils/AuthProvider';
import api from '../utils/axiosInstance';
import { FaEye, FaEyeSlash } from 'react-icons/fa';

export default function Login() {
  const [formData, setFormData] = useState({ email: '', password: '' });
  const [errors, setErrors] = useState({});
  const [serverError, setServerError] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const navigate = useNavigate();
  const { setAccessToken } = useAuth();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
    setErrors({ ...errors, [e.target.name]: '' });
    setServerError('');
  };

  const validate = () => {
    const newErrors = {};
    if (!formData.email.trim()) {
      newErrors.email = 'Email is required';
    } else if (!/\S+@\S+\.\S+/.test(formData.email)) {
      newErrors.email = 'Please enter a valid email address';
    }

    if (!formData.password) {
      newErrors.password = 'Password is required';
    }

    return newErrors;
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    const validationErrors = validate();

    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors);
      return;
    }

    try {
      const response = await api.post(
        '/users/login/',
        {
          email: formData.email,
          password: formData.password,
        },
        {
          withCredentials: true,
        }
      );

      setAccessToken(response.data.access_token);
      navigate('/dashboard');
    } catch (err) {
      setServerError('Invalid email or password');
    }
  };

  return (
    <div className="min-h-screen bg-gray-900 flex flex-col">
      {/* Logo */}
      <div className="px-6 py-6">
        <a href="/" className="text-3xl font-bold text-purple-500 font-poppins">
          CourseRec<span className="text-white">.</span>
        </a>
      </div>

      <div className="flex flex-1 items-center justify-center px-6 py-12">
        <motion.div
          initial={{ opacity: 0, y: -40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="bg-gray-800 p-8 sm:p-10 rounded-2xl shadow-2xl max-w-md w-full"
        >
          <h2 className="text-3xl font-bold text-white mb-6 text-center">
            Log in to CourseRec
          </h2>

          <form onSubmit={handleLogin} className="space-y-5">
            <div>
              <input
                type="email"
                name="email"
                placeholder="Email"
                value={formData.email}
                onChange={handleChange}
                className={`w-full p-3 rounded-lg bg-gray-700 text-white focus:outline-none focus:ring-2 ${
                  errors.email
                    ? 'border border-red-500 focus:ring-red-500'
                    : 'focus:ring-purple-500'
                }`}
              />
              {errors.email && (
                <p className="text-red-500 text-sm mt-1">{errors.email}</p>
              )}
            </div>

            <div className="relative">
              <input
                type={showPassword ? 'text' : 'password'}
                name="password"
                placeholder="Password"
                value={formData.password}
                onChange={handleChange}
                className={`w-full p-3 rounded-lg bg-gray-700 text-white focus:outline-none focus:ring-2 ${
                  errors.password
                    ? 'border border-red-500 focus:ring-red-500'
                    : 'focus:ring-purple-500'
                } pr-10`}
              />
              <button
                type="button"
                onClick={() => setShowPassword((prev) => !prev)}
                className="absolute top-1/2 right-3 -translate-y-1/2 text-gray-400 hover:text-purple-500 focus:outline-none cursor-pointer"
                tabIndex={-1}
              >
                {showPassword ? <FaEyeSlash /> : <FaEye />}
              </button>
              {errors.password && (
                <p className="text-red-500 text-sm mt-1">{errors.password}</p>
              )}
            </div>

            {serverError && (
              <p className="text-red-500 text-sm text-center">{serverError}</p>
            )}

            <button
              type="submit"
              className="w-full bg-purple-600 hover:bg-purple-700 text-white py-3 rounded-lg transition-colors"
            >
              Login
            </button>
          </form>

          {/* Links */}
          <div className="mt-6 text-sm text-center text-gray-400 space-y-3">
            <p>
              Don't have an account?
              <a href="/signup" className="text-purple-500 hover:text-purple-400 ml-1">
                Sign Up
              </a>
            </p>
            <p>
              <a href="/forgot-password" className="text-purple-500 hover:text-purple-400">
                Forgot Password?
              </a>
            </p>
            <p>
              <a href="/terms" className="text-purple-500 hover:text-purple-400">Terms</a>
              {' '}|{' '}
              <a href="/privacy" className="text-purple-500 hover:text-purple-400">Privacy</a>
            </p>
            <p className="text-xs text-gray-500 pt-2">
              &copy; {new Date().getFullYear()} CourseRec. All rights reserved.
            </p>
          </div>
        </motion.div>
      </div>
    </div>
  );
}

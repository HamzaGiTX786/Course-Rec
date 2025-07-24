import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import { FaEye, FaEyeSlash } from 'react-icons/fa';

import api from '../utils/axiosInstance';
import { useAuth } from '../utils/AuthProvider';

export default function Signup() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    email: '',
    password: '',
    confirmPassword: '',
  });

  const [errors, setErrors] = useState({});
  const [serverError, setServerError] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);
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
    } else if (
      !/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?#&])[A-Za-z\d@$!%*?#&]{8,}$/.test(formData.password)
    ) {
      newErrors.password =
        'Password must be at least 8 characters and include uppercase, lowercase, number, and special character.';
    }

    if (formData.confirmPassword !== formData.password) {
      newErrors.confirmPassword = 'Passwords do not match';
    }

    return newErrors;
  };

  const handleSignup = async (e) => {
    e.preventDefault();
    const validationErrors = validate();

    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors);
      return;
    }

    try {
      const response = await api.post('/users/create/', {
        email: formData.email,
        password: formData.password,
        is_superuser: false,
      });
      
      setAccessToken(response.data.access_token);
      navigate('/dashboard');
    } catch (err) {
      if (err.response?.data?.message?.includes('already')) {
        setServerError('Email already exists');
      } else {
        setServerError('Something went wrong. Please try again.');
        console.log(err);
      }
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
            Sign Up for CourseRec
          </h2>

          <form onSubmit={handleSignup} className="space-y-5">
            {/* Email */}
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

            {/* Password */}
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
                className="absolute top-1/2 right-3 -translate-y-1/2 text-gray-400 hover:text-purple-500 cursor-pointer"
                tabIndex={-1}
              >
                {showPassword ? <FaEyeSlash /> : <FaEye />}
              </button>
              {errors.password && (
                <p className="text-red-500 text-sm mt-1">{errors.password}</p>
              )}
            </div>

            {/* Confirm Password */}
            <div className="relative">
              <input
                type={showConfirmPassword ? 'text' : 'password'}
                name="confirmPassword"
                placeholder="Confirm Password"
                value={formData.confirmPassword}
                onChange={handleChange}
                className={`w-full p-3 rounded-lg bg-gray-700 text-white focus:outline-none focus:ring-2 ${
                  errors.confirmPassword
                    ? 'border border-red-500 focus:ring-red-500'
                    : 'focus:ring-purple-500'
                } pr-10`}
              />
              <button
                type="button"
                onClick={() => setShowConfirmPassword((prev) => !prev)}
                className="absolute top-1/2 right-3 -translate-y-1/2 text-gray-400 hover:text-purple-500 cursor-pointer"
                tabIndex={-1}
              >
                {showConfirmPassword ? <FaEyeSlash /> : <FaEye />}
              </button>
              {errors.confirmPassword && (
                <p className="text-red-500 text-sm mt-1">{errors.confirmPassword}</p>
              )}
            </div>

            {/* Server error */}
            {serverError && (
              <p className="text-red-500 text-sm text-center">{serverError}</p>
            )}

            <button
              type="submit"
              className="w-full bg-purple-600 hover:bg-purple-700 text-white py-3 rounded-lg transition-colors cursor-pointer"
            >
              Sign Up
            </button>
          </form>

          {/* Footer links */}
          <div className="mt-6 text-sm text-center text-gray-400 space-y-3">
            <p>
              Already have an account?
              <a href="/login" className="text-purple-500 hover:text-purple-400 ml-1 cursor-pointer">
                Login
              </a>
            </p>
            <p>
              <a href="/terms" className="text-purple-500 hover:text-purple-400 cursor-pointer">Terms</a>
              {' '}|{' '}
              <a href="/privacy" className="text-purple-500 hover:text-purple-400 cursor-pointer">Privacy</a>
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

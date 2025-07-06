import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import api from '../utils/axiosInstance';

const validatePassword = (password) => {
  const regex =
    /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?#&_])[A-Za-z\d@$!%*?#&_]{8,}$/;
  return regex.test(password);
};

const Signup = () => {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    confirmPassword: '',
  });

  const [errors, setErrors] = useState({});
  const [serverError, setServerError] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData((prev) => ({ ...prev, [e.target.name]: e.target.value }));
    setErrors((prev) => ({ ...prev, [e.target.name]: '' }));
    setServerError('');
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors({});
    setServerError('');

    const newErrors = {};

    if (!formData.email.trim()) newErrors.email = 'Email is required';
    else if (!/\S+@\S+\.\S+/.test(formData.email))
      newErrors.email = 'Please enter a valid email address';

    if (!formData.password) newErrors.password = 'Password is required';
    else if (!validatePassword(formData.password))
      newErrors.password =
        'Password must be at least 8 characters, include uppercase, lowercase, number, and symbol';

    if (formData.password !== formData.confirmPassword)
      newErrors.confirmPassword = 'Passwords do not match';

    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }

    try {
      await api.post('/users/signup', {
        email: formData.email,
        password: formData.password,
      });

      navigate('/login');
    } catch (err) {
      if (err.response?.data?.message?.toLowerCase().includes('email')) {
        setErrors((prev) => ({
          ...prev,
          email: 'This email is already registered',
        }));
      } else {
        setServerError('Signup failed. Please try again later.');
      }
    }
  };

  return (
    <div className="min-h-screen bg-gray-900 flex flex-col">
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
            Create an Account
          </h2>

          <form onSubmit={handleSubmit} className="space-y-5">
            <div>
              <input
                name="email"
                type="email"
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

            <div>
              <input
                name="password"
                type="password"
                placeholder="Password"
                value={formData.password}
                onChange={handleChange}
                className={`w-full p-3 rounded-lg bg-gray-700 text-white focus:outline-none focus:ring-2 ${
                  errors.password
                    ? 'border border-red-500 focus:ring-red-500'
                    : 'focus:ring-purple-500'
                }`}
              />
              {errors.password && (
                <p className="text-red-500 text-sm mt-1">{errors.password}</p>
              )}
            </div>

            <div>
              <input
                name="confirmPassword"
                type="password"
                placeholder="Confirm Password"
                value={formData.confirmPassword}
                onChange={handleChange}
                className={`w-full p-3 rounded-lg bg-gray-700 text-white focus:outline-none focus:ring-2 ${
                  errors.confirmPassword
                    ? 'border border-red-500 focus:ring-red-500'
                    : 'focus:ring-purple-500'
                }`}
              />
              {errors.confirmPassword && (
                <p className="text-red-500 text-sm mt-1">
                  {errors.confirmPassword}
                </p>
              )}
            </div>

            {serverError && (
              <p className="text-red-500 text-sm text-center">{serverError}</p>
            )}

            <button
              type="submit"
              className="w-full bg-purple-600 hover:bg-purple-700 text-white py-3 rounded-lg transition-colors"
            >
              Sign Up
            </button>
          </form>

          <div className="mt-6 text-sm text-center text-gray-400 space-y-3">
            <p>
              Already have an account?
              <a href="/login" className="text-purple-500 hover:text-purple-400 ml-1">
                Log in
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
};

export default Signup;

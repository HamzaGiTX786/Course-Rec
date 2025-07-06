import React, { useState, useEffect } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { FaArrowRight, FaBars, FaTimes } from 'react-icons/fa';
import FadeInSection from '../components/FadeInSection';

const Navbar = () => {
  const navigate = useNavigate();
  const [scrolled, setScrolled] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  // Scroll behavior
  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const toggleMobileMenu = () => setIsMobileMenuOpen(!isMobileMenuOpen);
  const closeMobileMenu = () => setIsMobileMenuOpen(false);

  return (
    <nav
      className={`fixed top-0 left-0 w-full z-50 transition-all duration-300 ${
        scrolled ? 'bg-gray-900 shadow-md' : 'bg-transparent'
      }`}
    >
      <div className="container mx-auto flex justify-between items-center py-4 px-6">
        {/* Logo */}
        <a
          href="/"
          className="text-2xl sm:text-3xl font-bold text-purple-500 font-poppins"
        >
          CourseRec<span className="text-white">.</span>
        </a>

        {/* Desktop Menu */}
        <div className="hidden md:flex items-center space-x-6 lg:space-x-8">
          <a
            href="#how-it-works"
            className="text-base lg:text-lg font-roboto hover:text-purple-500 transition duration-300"
          >
            How it works
          </a>
          <a
            href="#why-use-course-rec"
            className="text-base lg:text-lg font-roboto hover:text-purple-500 transition duration-300"
          >
            Why use CourseRec.
          </a>

          <a
            href="/signup"
            className="bg-purple-600 hover:bg-purple-700 text-white px-4 lg:px-6 py-2 lg:py-3 rounded-lg inline-flex items-center transition-colors duration-300 font-roboto cursor-pointer"
          >
            Get Started
            <FaArrowRight className="ml-2" />
          </a>

          <button
            onClick={() => navigate('/login')}
            className="text-base border border-purple-500 text-purple-500 px-4 lg:px-6 py-2 lg:py-3 rounded-lg hover:bg-purple-500 hover:text-white transition-colors duration-300 font-roboto cursor-pointer"
          >
            Login
          </button>
        </div>

        {/* Hamburger Icon - Mobile Only */}
        <div className="md:hidden">
          <button
            onClick={toggleMobileMenu}
            className="text-white text-2xl focus:outline-none"
            aria-label="Toggle mobile menu"
          >
            {isMobileMenuOpen ? <FaTimes /> : <FaBars />}
          </button>
        </div>
      </div>

      {/* Mobile Slide-down Menu */}
      {isMobileMenuOpen && (
        <div className="md:hidden bg-gray-900 text-white px-6 pt-4 pb-6 space-y-4 shadow-md">
          <a
            href="#how-it-works"
            onClick={closeMobileMenu}
            className="block text-lg hover:text-purple-400 transition"
          >
            How it works
          </a>
          <a
            href="#why-use-course-rec"
            onClick={closeMobileMenu}
            className="block text-lg hover:text-purple-400 transition"
          >
            Why use CourseRec.
          </a>
          <a
            href="/signup"
            onClick={closeMobileMenu}
            className="block bg-purple-600 hover:bg-purple-700 text-white px-4 py-2 rounded-md text-center transition-colors"
          >
            Get Started <FaArrowRight className="inline ml-2" />
          </a>
          <button
            onClick={() => {
              closeMobileMenu();
              navigate('/login');
            }}
            className="block w-full border border-purple-500 text-purple-500 px-4 py-2 rounded-md hover:bg-purple-500 hover:text-white transition-colors text-center"
          >
            Login
          </button>
        </div>
      )}
    </nav>
  );
};

export default Navbar;

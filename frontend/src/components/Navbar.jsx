import React, { useState, useEffect } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import FadeInSection from '../components/FadeInSection';
import { FaArrowRight } from 'react-icons/fa';

const Navbar = () => {
  const navigate = useNavigate();
  const [scrolled, setScrolled] = useState(false);

  // Detecting scroll position
  useEffect(() => {
    const handleScroll = () => {
      // Update the navbar style on scroll
      if (window.scrollY > 50) {
        setScrolled(true);
      } else {
        setScrolled(false);
      }
    };

    window.addEventListener('scroll', handleScroll);

    // Cleanup the event listener
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <nav
      className={`${
        scrolled ? 'bg-gray-900 shadow-md' : 'bg-transparent'
      } text-white fixed top-0 left-0 w-full z-50 transition-all duration-300`}
    >
      <div className="container mx-auto flex justify-between items-center py-4 px-6">
        {/* Logo */}
        <FadeInSection className="flex justify-start">
          <a href="/" className="text-3xl font-bold text-purple-500 font-poppins">
            CourseRec<span className="text-white">.</span>
          </a>
        </FadeInSection>

        {/* Links and Buttons */}
        <div className="flex items-center space-x-8">
          {/* Link to "How it works" */}
          <FadeInSection>
            <a
              href="#how-it-works"
              className="text-lg font-roboto hover:text-purple-500 transition duration-300"
            >
              How it works
            </a>
          </FadeInSection>

          {/* Link to "Why use CourseRec." */}
          <FadeInSection>
            <a
              href="#why-use-course-rec"
              className="text-lg font-roboto hover:text-purple-500 transition duration-300"
            >
              Why use CourseRec.
            </a>
          </FadeInSection>

          {/* Get Started Button */}
          <FadeInSection>
            <a
              href="/signup"
              className="bg-purple-600 hover:bg-purple-700 text-white px-6 py-3 rounded-lg inline-flex items-center transition-colors duration-300 w-40 text-center font-roboto"
            >
              Get Started
              <FaArrowRight className="ml-2" />
            </a>
          </FadeInSection>

          {/* Login Button */}
          <FadeInSection>
            <a
              onClick={() => navigate('/login')}
              className="text-lg border border-purple-500 text-purple-500 px-6 py-3 rounded-lg hover:bg-purple-500 hover:text-white transition-colors duration-300 w-40 text-center font-roboto cursor-pointer"
            >
              Login
            </a>
          </FadeInSection>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;

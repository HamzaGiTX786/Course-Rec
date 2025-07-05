import React, { useRef } from 'react';
import { motion } from 'framer-motion';
import { Link } from 'react-router-dom';

// Motion variants for animation
const fadeInUp = {
  hidden: { opacity: 0, y: 30 },
  visible: (i = 0) => ({
    opacity: 1,
    y: 0,
    transition: {
      delay: i * 0.15,
      duration: 0.6,
      ease: 'easeOut',
    },
  }),
};

const Footer = () => {
  const footerRef = useRef();

  return (
    <motion.footer
      ref={footerRef}
      initial="hidden"
      animate="visible"
      variants={fadeInUp}
      className="bg-gray-800 text-white py-10"
    >
      <div className="max-w-6xl mx-auto px-6">
        {/* Copyright Section */}
        <motion.div
          className="text-center text-sm text-gray-400"
          variants={fadeInUp}
          initial="hidden"
          animate="visible"
        >
          <p>&copy; 2025 CourseRec. All rights reserved.</p>
        </motion.div>

        {/* Links Section */}
        <motion.div
          className="flex justify-center space-x-8 mt-4"
          variants={fadeInUp}
          initial="hidden"
          animate="visible"
        >
          <Link
            to="/terms"
            className="text-purple-500 hover:text-purple-400 transition duration-300"
          >
            Terms
          </Link>
          <Link
            to="/privacy"
            className="text-purple-500 hover:text-purple-400 transition duration-300"
          >
            Privacy
          </Link>
        </motion.div>

        {/* Email for inquiries */}
        <motion.div
          className="text-center mt-6"
          variants={fadeInUp}
          initial="hidden"
          animate="visible"
        >
          <p className="text-sm text-gray-400">
            For questions, support, or inquiries, email{' '}
            <a
              href="mailto:support@courserec.com"
              className="text-purple-500 hover:text-purple-400 transition duration-300"
            >
              support@courserec.com
            </a>
          </p>
        </motion.div>
      </div>
    </motion.footer>
  );
};

export default Footer;

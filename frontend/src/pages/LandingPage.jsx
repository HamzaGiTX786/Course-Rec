import { useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import {
  FaArrowRight, FaUserFriends, FaRobot, FaClock,
  FaChartLine, FaCalendarAlt, FaShieldAlt, FaSearch,
  FaRegClock, FaQuestionCircle
} from 'react-icons/fa';

import FadeInSection from '../components/FadeInSection';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

import TrentUniversityLogo from '../assets/TrentU_logo.webp';
import HeroGif from '../assets/Hero_Gif.gif' 
import ChatNow from '../assets/Chat_Now.gif'

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

export default function LandingPage() {
  const navigate = useNavigate();
  const features = [
    {
      icon: <FaRobot />,
      title: "AI-Powered Guidance",
      desc: "Get personalized recommendations based on your academic history and interests.",
    },
    {
      icon: <FaUserFriends />,
      title: "Student-Centric Design",
      desc: "Built by students, for students — intuitive and hassle-free.",
    },
    {
      icon: <FaCalendarAlt />,
      title: "Plan Ahead with Ease",
      desc: "Map your degree and prerequisites smartly, semester by semester.",
    },
    {
      icon: <FaClock />,
      title: "Available Anytime",
      desc: "No appointments needed. Get help whenever you need it.",
    },
    {
      icon: <FaChartLine />,
      title: "Data-Backed Choices",
      desc: "Recommendations are grounded in real course data and trends.",
    },
    {
      icon: <FaShieldAlt />,
      title: "Confidence, Not Guesswork",
      desc: "Eliminate confusion and plan your next steps with clarity.",
    },
  ];

  return (
    <div className="bg-gray-900 text-white">
      <Navbar />

            {/* HERO SECTION */}
      <section className="mb-50 bmin-h-screen flex flex-col justify-center items-center px-4 sm:px-6 text-center bg-gray-900">
        <motion.h1
          className="text-4xl sm:text-5xl md:text-6xl font-bold mt-50 mb-4 text-purple-500 animate__animated animate__fadeIn"
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2, duration: 0.8 }}
        >
          CourseRec<span className="text-white">.</span>
        </motion.h1>
        <p className="text-lg sm:text-xl md:text-2xl text-gray-300 max-w-xl sm:max-w-2xl mb-8 animate__animated animate__fadeIn animate__delay-1s">
          Your AI-Powered Course Recommender — anytime, anywhere.
        </p>

        <a
          href="/signup"
          className="mt-6 inline-block bg-purple-600 hover:bg-purple-700 text-white px-6 py-3 rounded-lg transition-all duration-300 transform hover:scale-105 hover:shadow-lg"
        >
          Get Started
          <FaArrowRight className="inline ml-2" />
        </a>

        <div className="relative mt-10 w-full max-w-4xl h-auto mx-auto">
          <img
            src={HeroGif}
            alt="A gif showing the working of CourseRec"
            className="w-full h-auto mx-auto rounded-2xl transform hover:scale-105 transition-all duration-500"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black opacity-40 rounded-2xl"></div>
        </div>
      </section>

      {/* PROBLEM SECTION */}
      <section className="py-20 px-4 sm:px-6 bg-gray-800 text-white text-center">
        <div className="max-w-4xl mx-auto">
          <FadeInSection>
            <h2 className="text-3xl sm:text-4xl font-bold mb-4 text-purple-500">
              Feeling Lost Picking Courses?
            </h2>
            <p className="text-md sm:text-lg text-white mb-12">
              You're not alone - students face real challenges planning their academic journey. Sound familiar?
            </p>
          </FadeInSection>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 sm:gap-8 text-left">
            {[
              {
                icon: <FaSearch className="text-white text-4xl mb-4" />,
                title: "Too Many Options",
                desc: "Hundreds of courses, unclear which one fits your path or goals.",
              },
              {
                icon: <FaRegClock className="text-white text-4xl mb-4" />,
                title: "No Time for Advising",
                desc: "Academic advisors aren't always available when you need help.",
              },
              {
                icon: <FaQuestionCircle className="text-white text-4xl mb-4" />,
                title: "What Comes Next?",
                desc: "Confused about prerequisites, major requirements, or future semesters?",
              },
            ].map((problem, idx) => (
              <FadeInSection key={idx}>
                <div className="bg-gray-900 rounded-xl p-6 shadow hover:ring-2 hover:ring-purple-500 transition-all h-full">
                  {problem.icon}
                  <h3 className="text-lg sm:text-xl font-semibold text-purple-400 mb-2">{problem.title}</h3>
                  <p className="text-gray-400">{problem.desc}</p>
                </div>
              </FadeInSection>
            ))}
          </div>
        </div>
      </section>

      {/* HOW IT WORKS SECTION */}
      <section className="py-20 px-4 sm:px-6 bg-gray-900" id="how-it-works">
        <h2 className="text-3xl sm:text-4xl font-bold mb-8 text-purple-500 text-center">How It Works</h2>
        <div className="max-w-6xl mx-auto flex flex-col-reverse md:flex-row gap-10 items-center">
          {/* Text Steps */}
          <div className="flex-1 space-y-6 w-full">
            {[
              {
                title: '1. Create an Account',
                desc: 'Sign up quickly using your email to get started.',
              },
              {
                title: '2. Ask Questions',
                desc: 'Chat with our AI to get personalized course recommendations.',
              },
              {
                title: '3. Plan with Confidence',
                desc: 'Make informed decisions anytime, on your own.',
              },
            ].map((step, idx) => (
              <FadeInSection key={idx}>
                <div className="bg-gray-800 p-6 rounded-xl shadow-lg hover:ring-2 hover:ring-purple-500 transition-all duration-200">
                  <h3 className="text-lg sm:text-xl font-semibold mb-2 text-purple-400">{step.title}</h3>
                  <p className="text-gray-300">{step.desc}</p>
                </div>
              </FadeInSection>
            ))}
          </div>

          {/* Chat Demo */}
          <div className="max-w-4xl h-auto mx-auto flex-1 w-full sm:max-w-full sm:h-[400px] flex items-center justify-center">
            <img
            src={ChatNow}
            alt="A gif showing the sign up process of CourseRec"
            className="w-full h-auto mx-auto rounded-2xl transform hover:scale-105 transition-all duration-500"
          />
          </div>
        </div>
      </section>

      {/* WHY USE COURSEREC SECTION */}
      <section className="py-20 px-4 sm:px-6 bg-gray-800 text-center" id="why-use-course-rec">
        <h2 className="text-3xl sm:text-4xl font-bold mb-4 text-purple-500">
          Why Use CourseRec<span className="text-white">.</span>
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 sm:gap-8 max-w-6xl mx-auto text-left">
          {features.map((item, idx) => (
            <FadeInSection key={idx}>
              <div className="bg-gray-900 p-6 rounded-xl shadow hover:ring-2 hover:ring-purple-500 transition-all duration-300">
                <div className="text-3xl mb-4">{item.icon}</div>
                <h3 className="text-lg sm:text-xl font-semibold text-purple-400 mb-2">{item.title}</h3>
                <p className="text-gray-300">{item.desc}</p>
              </div>
            </FadeInSection>
          ))}
        </div>
      </section>

      {/* SUPPORTED UNIVERSITIES SECTION */}
      <section className="py-20 px-4 sm:px-6 bg-gray-900 text-center">
        <h2 className="text-3xl sm:text-4xl font-bold mb-4 text-purple-500">Currently Supports</h2>
       
        <div className="mb-6">
          <img
            src={TrentUniversityLogo}
            alt="Trent University Logo"
            className="mx-auto h-16 sm:h-20 object-contain"
          />
        </div>
        <p className="text-white text-base sm:text-lg mb-4 sm:mb-6">
          Department of Computing & Information Systems, Trent University
        </p>
        <p className="text-purple-400 text-sm">More universities coming soon...</p>
      </section>

      <Footer />
    </div>
  );
}

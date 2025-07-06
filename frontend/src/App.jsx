import { useState } from 'react'
import { Navigate, Route, Routes } from "react-router-dom";

import LandingPage from './pages/LandingPage';
import Signup from './pages/SignUp';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';





function App() {

  return (
    <>
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/signup" element={<Signup />} />
      <Route path="/login" element={<Login />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="*" element={<Navigate to="/login" replace />} />
    </Routes>
    </>
  )
}

export default App

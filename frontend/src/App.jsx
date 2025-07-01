import { useState } from 'react'
import { Navigate, Route, Routes } from "react-router-dom";

import Login from './pages/Login';
import Dashboard from './pages/Dashboard';




function App() {

  return (
    <>
    <Routes>
      <Route path="/" element={<Navigate to="/login" replace />} />
      <Route path="/login" element={<Login />} />
      <Route path="/dashboard" element={<Dashboard />} />
      {/*
      <Route path="/courses" element={<Courses />} />
      <Route path="/profile" element={<Profile />} /> */}
      <Route path="*" element={<Navigate to="/login" replace />} />
    </Routes>
    </>
  )
}

export default App

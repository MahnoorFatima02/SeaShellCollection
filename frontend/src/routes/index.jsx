import React from 'react';
import { Routes, Route } from 'react-router-dom';
import ShellForm from '../components/ShellForm.jsx';
import SeashellList from '../components/SeaShellList.jsx';
import LandingPage from '../components/LandingPage.jsx';
import NotFound from '../components/NotFound.jsx';
import SignupPage from '../components/SignupPage.jsx';
import LoginPage from '../components/LoginPage.jsx';
import FindShellPage from '../components/FindShellPage.jsx';

const Router = () => {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/shells" element={<SeashellList />} />
      <Route path="/shell/add" element={<ShellForm />} />
      <Route path="/shell/edit/:id" element={<ShellForm />} />
      <Route path="/signup" element={<SignupPage />}/>
      <Route path="/login" element={<LoginPage />} />
      <Route path="*" element={<NotFound />} />
      <Route path="/find-shell" element={<FindShellPage />} />
    </Routes>
  );
};

export default Router;

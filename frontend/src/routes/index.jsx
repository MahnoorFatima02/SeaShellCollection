import React from 'react';
import { Routes, Route } from 'react-router-dom';
import ShellForm from '../components/ShellForm.jsx';
import SeashellList from '../components/SeaShellList.jsx';
import LandingPage from '../components/LandingPage.jsx';

const Router = () => {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/collection" element={<SeashellList />} />
      <Route path="/add" element={<ShellForm />} />
      <Route path="/edit/:id" element={<ShellForm />} />
    </Routes>
  );
};

export default Router;

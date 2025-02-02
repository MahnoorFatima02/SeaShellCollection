import React from 'react';
import { Routes, Route } from 'react-router-dom';
import ShellForm from '../components/ShellForm.jsx';
import SeashellList from '../components/SeaShellList.jsx';
import LandingPage from '../components/LandingPage.jsx';
import NotFound from '../components/NotFound.jsx';

const Router = () => {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/shells" element={<SeashellList />} />
      <Route path="/shell/add" element={<ShellForm />} />
      <Route path="/shell/edit/:id" element={<ShellForm />} />
      <Route path="*" element={<NotFound />} />
    </Routes>
  );
};

export default Router;

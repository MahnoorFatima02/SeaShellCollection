import React from 'react';
import { Link } from 'react-router-dom';

const LandingPage = () => {
  return (
    <div className="landing-page">
        <div className="welcome-container">
      <h1 className="welcome-title">Welcome to Shell Luxe</h1>
      <div className="landing-buttons">
        <Link to="/shells" className="nav-button">SeaShell Collection</Link>
        <Link to="/shell/add" className="nav-button">Add Seashell</Link>
        </div>
      </div>
    </div>
  );
};

export default LandingPage;

import React from 'react';

const NotFound = () => {
  return (
    <div className="not-found-container">
      <h1 className="not-found-heading">404 - Page Not Found</h1>
      <p className="not-found-paragraph">The page you are looking for does not exist.</p>
      <a href="/" className="not-found-link">Go back to the homepage</a>
    </div>
  );
};

export default NotFound;
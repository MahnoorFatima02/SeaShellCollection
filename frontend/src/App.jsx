import React from "react";
import Router from "./routes";
import { Provider, useDispatch } from "react-redux";
import store from "./redux/store";
import './App.css'; 
import NavBar from "./components/NavBar";
import { useNavigate } from "react-router-dom";
import { LOGOUT } from "./redux/user/actionTypes";

const AppContent = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleLogout = () => {
    dispatch({ type: LOGOUT });
    navigate("/");
  };

  return (
    <>
      <NavBar onLogout={handleLogout} />
      <div className="main-content">
        <Router />
      </div>
    </>
  );
};

const App = () => (
  <Provider store={store}>
    <AppContent />
  </Provider>
);

export default App;
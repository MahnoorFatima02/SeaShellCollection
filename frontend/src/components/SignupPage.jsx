import { useState } from "react";
import { useNavigate } from 'react-router-dom';
import { signup } from "../redux/user/actions";
import { useDispatch } from "react-redux";

const SignupPage = () => {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const [form, setForm] = useState({ username: "", password: "" });
  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage("");
    try {
      const res = await dispatch(signup(form)).unwrap();
      setMessage(res?.msg || "Signup successful!");
      navigate('/')
    } catch (err) {
      setMessage(err.response?.data?.detail || "Signup failed.");
    }
  };

  return (
    <div>
  <div className="auth-center-wrapper">
    <div className="authContainer">
      <h2>Sign Up</h2>
      <form className="authForm" onSubmit={handleSubmit}>
        <input
          name="username"
          placeholder="Username"
          value={form.username}
          onChange={handleChange}
          required
        />
        <input
          name="password"
          type="password"
          placeholder="Password"
          value={form.password}
          onChange={handleChange}
          required
        />
        <button type="submit">Sign Up</button>
      </form>
      {message && <div className="message">{message}</div>}
    </div>
    </div>
    
           <button className="back-button-fixed-bottom" onClick={() => navigate("/")}>
        Back
      </button>
    </div>
  );
};

export default SignupPage;
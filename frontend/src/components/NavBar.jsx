import { Link, useNavigate } from "react-router-dom";
import { useSelector } from "react-redux";
import PropTypes from "prop-types";


const NavBar = ({ onLogout }) => {

const navigate = useNavigate();
const username = useSelector(state => state.user.userInfo?.username);
  return (
    <nav className="navbar">
      <Link to="/" className="nav-logo">Prompt. Generate. Collect. Shell done.</Link>
      <div className="nav-links">
        {!username ? (
          <>
            <button className="navigation-button" onClick={() => navigate("/login")}>Login</button>
            <button className="navigation-button" onClick={() => navigate("/signup")}>Sign Up</button>
          </>
        ) : (
          <>
            <span className="nav-user">Hello, {username}</span>
            <button className="navigation-button" onClick={onLogout}>Logout</button>
          </>
        )}
      </div>
    </nav>
  );
};

NavBar.propTypes = {
  onLogout: PropTypes.func.isRequired,
};


export default NavBar;
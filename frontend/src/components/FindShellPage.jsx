import ShellSuggester from "./ShellSuggester";
import { useNavigate } from "react-router-dom";

const FindShellPage = () => {
  const navigate = useNavigate();
  return (
    <div className="find-shell-page">
      <h1>Prompt the Ocean!</h1>
      <ShellSuggester />
      <button className="back-button-fixed-bottom" onClick={() => navigate('/')}>
        Back
      </button>
    </div>
  );
};

export default FindShellPage;
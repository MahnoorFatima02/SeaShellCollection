import { useState, useEffect } from 'react';
import { useParams, useNavigate, useLocation } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { addShell, editShell } from '../redux/seaShell/actions';

function ShellForm() {
  const { id } = useParams();
  const navigate = useNavigate();
  const location = useLocation();
  const dispatch = useDispatch();
  const [formData, setFormData] = useState({
    name: '',
    species: '',
    description: '',
    location: '',
    size: ''
  });
    const [warning, setWarning] = useState("");

  useEffect(() => {
    if (id && location.state?.shell) {
      setFormData(location.state.shell);
    }
  }, [id, location.state]);
  

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!formData.name.trim() || !formData.species.trim() || !formData.description.trim()) {
      return;
    }

      try {
      if (id) {
        await dispatch(editShell(id, formData));
      } else {
        await dispatch(addShell(formData));
      }
      setWarning("");
      navigate('/shells');
    } catch (error) {
      if (error.response && error.response.status === 401) {
        setWarning("⚠️ Please login to continue!");
      } else {
        setWarning("Something went wrong.");
      }
    }
  };

  return (
      <div className="shell-form-wrapper">
      <div className="form-container">
      <h1>{id ? 'Edit Seashell' : 'Add New Seashell'}</h1>
          <div className="form-content-wrapper">
      {warning && <div className="login-warning">{warning}</div>}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Name"
          value={formData.name}
          onChange={(e) => setFormData({...formData, name: e.target.value})}
          required
        />
        <input
          type="text"
          placeholder="Species"
          value={formData.species}
          onChange={(e) => setFormData({...formData, species: e.target.value})}
          required
        />
        <textarea
          placeholder="Description"
          value={formData.description}
          onChange={(e) => setFormData({...formData, description: e.target.value})}
          required
        />
        <input
          type="text"
          placeholder="Location"
          value={formData.location}
          onChange={(e) => setFormData({...formData, location: e.target.value})}
        />
        <input
          type="text"
          placeholder="Size"
          value={formData.size}
          onChange={(e) => setFormData({...formData, size: e.target.value})}
        />
        <button type="submit">{id ? 'Save Changes' : 'Add Seashell'}</button>
      </form>
    </div>
    </div>
        <button className="back-button-fixed-bottom" onClick={() => navigate("/")}>
      Back
    </button>
    </div>
  );
}

export default ShellForm;

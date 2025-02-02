

import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, useLocation } from 'react-router-dom';
import axiosInstance from '../redux/axiosInstance';

function ShellForm() {
  const { id } = useParams();
  const navigate = useNavigate();
  const location = useLocation();
  const shellToEdit = location.state?.shell; 
  const [formData, setFormData] = useState({
    name: '',
    species: '',
    description: '',
    location: '',
    size: ''
  });

  // useEffect(() => {
  //   if (id) {
  //     // Fetch the specific shell data for editing
  //     axiosInstance.get(`/shells/${id}`)
  //       .then(response => {
  //         setFormData(response.data);
  //       })
  //       .catch(error => console.error('Error fetching shell:', error));
  //   }
  // }, [id]);
  useEffect(() => {
    if (id && location.state?.shell) {
      setFormData(location.state.shell);
    }
  }, [id, location.state]);
  

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!formData.name.trim() || !formData.species.trim() || !formData.description.trim()) {
      return;
    }

    console.log('Submitting form data:', formData); 

    const apiCall = id
      ? axiosInstance.put(`/shells/${id}`, formData)
      : axiosInstance.post('/shells', formData);

    apiCall
      .then(() => {
        navigate('/shells');
      })
      .catch(error => {
        console.error('Error:', error);
      });
  };

  return (
      <div className="form-container">
    <button 
      className="back-button" 
      onClick={() => navigate('/')}
    >
      Back to Home
    </button>

      <h1>{id ? 'Edit Seashell' : 'Add New Seashell'}</h1>
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
  );
}

export default ShellForm;

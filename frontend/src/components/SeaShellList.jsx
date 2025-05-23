
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { fetchShells, deleteShell } from '../redux/seaShell/actions';
import './SeaShell.css';

const SeaShellList = () => {
    const navigate = useNavigate();
    const dispatch = useDispatch();
    // const state = useSelector(state => state);
    const [warning, setWarning] = useState("");

    // Select only the shells array from state
    const seashells = useSelector(state => state.shells.shells) || [];

    useEffect(() => {
        dispatch(fetchShells());
    }, [dispatch]);

 const handleRemoveSeashell = async (id) => {
  try {
    await dispatch(deleteShell(id));
    setWarning("");
  } catch (error) {
    if (error.response && error.response.status === 401) {
      setWarning("⚠️ Please login to continue!");
    } else {
      setWarning("Something went wrong.");
    }
  }
};

    const handleEdit = (shell) => {
        navigate(`/shell/edit/${shell.id}`, { state: { shell } });
    };

    return (
        <div className="seashell-container">
        {warning && <div className="login-warning">{warning}</div>}
            <h1>SEASHELL COLLECTION</h1>
            <div className="seashell-list">
                    {Array.isArray(seashells) && seashells.length > 0 ? (
                        seashells.map(shell => (
                            <div key={shell.id} className="seashell-card">
                                <h3>{shell.name}</h3>
                                <p>Species: {shell.species}</p>
                                <p>Description: {shell.description}</p>
                                <p>Location: {shell.location}</p>
                                <p>Size: {shell.size}</p>
                                <button onClick={() => handleRemoveSeashell(shell.id)}>Remove</button>
                                <button onClick={() => handleEdit(shell)}>Edit</button>
                            </div>
                        ))
                    ) : (
                        <div className="empty-collection">
                            <h2>Your collection is empty</h2>
                            <p>Start adding beautiful seashells to your collection!</p>
                        </div>
                    )}
                </div>
                   <button className="back-button-fixed-bottom" onClick={() => navigate('/')}>
                Back
            </button>
        </div>
    );
};

export default SeaShellList;



import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { fetchShells, deleteShell } from '../redux/actions';

const SeaShellList = () => {
    const navigate = useNavigate();
    const dispatch = useDispatch();
    // const state = useSelector(state => state);

    // Select only the shells array from state
    const seashells = useSelector(state => state.shells.shells) || [];

    useEffect(() => {
        dispatch(fetchShells());
    }, [dispatch]);

    const handleRemoveSeashell = (id) => {
        dispatch(deleteShell(id));
    };

    const handleEdit = (shell) => {
        navigate(`/edit/${shell.id}`, { state: { shell } });
    };

    return (
        <div className="seashell-container">
            <button className="back-button" onClick={() => navigate('/')}>
                Back to Home
            </button>
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
        </div>
    );
};

export default SeaShellList;


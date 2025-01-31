import { ADD_SHELL, DELETE_SHELL, FETCH_SHELLS } from './actionTypes';
import axiosInstance from './axiosInstance';

// Action Creators
const addShellSuccess = (shell) => ({
    type: ADD_SHELL,
    payload: shell,
});

const deleteShellSuccess = (id) => ({
    type: DELETE_SHELL,
    payload: id,
});

const fetchShellsSuccess = (shells) => ({
    type: FETCH_SHELLS,
    payload: shells,
});

// Thunk Actions
export const fetchShells = () => async (dispatch) => {
    try {
        const response = await axiosInstance.get('/shells');
        dispatch(fetchShellsSuccess(response.data));
    } catch (error) {
        console.log('Error fetching shells:', error);
    }
};

export const addShell = (shellData) => async (dispatch) => {
    try {
        const response = await axiosInstance.post('/shells', shellData);
        console.log('Added shell:', response.data);
        dispatch(addShellSuccess(response.data));
    } catch (error) {
        console.log('Error adding shell:', error);
    }
};

export const deleteShell = (id) => async (dispatch) => {
    try {
        await axiosInstance.delete(`/shells/${id}`);
        console.log('Deleted shell:', id);
        dispatch(deleteShellSuccess(id));
    } catch (error) {
        console.log('Error deleting shell:', error);
    }
};
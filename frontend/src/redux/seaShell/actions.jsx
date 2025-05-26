import { ADD_SHELL, DELETE_SHELL, FETCH_SHELLS, EDIT_SHELL } from './actionTypes';
import axiosInstance from '../axiosInstance';

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

const editShellSuccess = (shell) => ({
    type: EDIT_SHELL,
    payload: shell,
})

export const fetchShells = () => async (dispatch) => {
    try {
        const response = await axiosInstance.get('/shells');
        dispatch(fetchShellsSuccess(response.data));
    } catch (error) {
        console.log('Error fetching shells:', error);
    }
};

export const addShell = (shellData) => async (dispatch, getState) => {
    try {
        const token = getState().user.accessToken;
        const response = await axiosInstance.post('/shells', shellData, {
            headers: { Authorization: `Bearer ${token}` }
        });
        dispatch(addShellSuccess(response.data));
    } catch (error) {
        throw error;
    }
};

export const deleteShell = (id) => async (dispatch, getState) => {
    try {
        const token = getState().user.accessToken;
        await axiosInstance.delete(`/shells/${id}`, {
            headers: { Authorization: `Bearer ${token}` }
        });
        dispatch(deleteShellSuccess(id));
    } catch (error) {
        throw error;
    }
};

export const editShell = (id, shellData) => async (dispatch, getState) => {
    try {
        const token = getState().user.accessToken;
        const response = await axiosInstance.put(`/shells/${id}`, shellData, {
            headers: { Authorization: `Bearer ${token}` }
        });
        dispatch(editShellSuccess(response.data));
    } catch (error) {
        throw error;
    }
};


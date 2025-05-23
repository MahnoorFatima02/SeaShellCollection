import { ADD_SHELL, DELETE_SHELL, EDIT_SHELL, FETCH_SHELLS } from './actionTypes';
// seashellReducer.js
const initialState = { shells: [] };

export const seashellReducer = (state = initialState, action) => {
  switch (action.type) {
    case ADD_SHELL:
      return { 
        ...state, 
        shells: [...state.shells, action.payload] };
    case DELETE_SHELL:
      return { 
        ...state, 
        shells: state.shells.filter(shell => shell.id !== action.payload) };
    case FETCH_SHELLS:
      return {
         ...state, 
         shells: action.payload };
      case EDIT_SHELL:
          return {
        ...state,
        shells: state.shells.map(shell =>
          shell.id === action.payload.id ? action.payload : shell
        ),
      };
    default:
      return state;
  }
};

export default seashellReducer;
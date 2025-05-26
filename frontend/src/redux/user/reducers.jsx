import {
  LOGIN_PENDING,
  LOGIN_FULFILLED,
  LOGIN_REJECTED,
  SIGNUP_PENDING,
  SIGNUP_FULFILLED,
  SIGNUP_REJECTED,
  LOGOUT,
} from "./actionTypes";

const initialState = {
  accessToken: null,
//   refreshToken: null,
  loading: false,
  userInfo: null,
  error: null,
};

const userReducer = (state = initialState, action) => {
  switch (action.type) {
    case LOGIN_PENDING:
    case SIGNUP_PENDING:
      return {
        ...state,
        loading: true,
        error: null,
      };
    case LOGIN_FULFILLED:
      return {
        ...state,
        loading: false,
        accessToken: action.payload.accessToken,
        userInfo: action.payload.userInfo,
      };
    case SIGNUP_FULFILLED:
      return {
        ...state,
        loading: false,
        accessToken: action.payload.accessToken,
        userInfo: action.payload.userInfo,
      };

    case LOGIN_REJECTED:
    case SIGNUP_REJECTED:
      return {
        ...state,
        loading: false,
        error: action.error.message,
      };
    case LOGOUT:
      return {
        ...initialState,
      };

    default:
      return state;
  }
};

export default userReducer;
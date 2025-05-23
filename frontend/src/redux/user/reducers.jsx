import {
  LOGIN_PENDING,
  LOGIN_FULFILLED,
  LOGIN_REJECTED,
  SIGNUP_PENDING,
  SIGNUP_FULFILLED,
  SIGNUP_REJECTED,
//   REFRESH_ACCESS_TOKEN_PENDING,
//   REFRESH_ACCESS_TOKEN_FULFILLED,
//   REFRESH_ACCESS_TOKEN_REJECTED,
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
    // case UPDATE_USER_PENDING:
    // case REFRESH_ACCESS_TOKEN_PENDING:
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
        // refreshToken: action.payload.refreshToken,
        userInfo: action.payload.userInfo,
      };
    case SIGNUP_FULFILLED:
      return {
        ...state,
        loading: false,
        accessToken: action.payload.accessToken,
        // refreshToken: action.payload.refreshToken,
        userInfo: action.payload.userInfo,
      };

    // case REFRESH_ACCESS_TOKEN_FULFILLED:
    //   return {
    //     ...state,
    //     loading: false,
    //     accessToken: action.payload.accessToken,
    //     refreshToken: action.payload.refreshToken,
    //   };
    case LOGIN_REJECTED:
    case SIGNUP_REJECTED:
    // case FETCH_USER_REJECTED:
    // case UPDATE_USER_REJECTED:
    // case REFRESH_ACCESS_TOKEN_REJECTED:
      return {
        ...state,
        loading: false,
        error: action.error.message,
      };
    case LOGOUT:
      return {
        ...initialState,
      };

    //   case SET_ACCESS_TOKEN:
    //     console.log("LOGGING OIT")
    //     return {
    //         ...state,
    //         loading: false,
    //         error: action.error.message,
    //       };
    default:
      return state;
  }
};

export default userReducer;
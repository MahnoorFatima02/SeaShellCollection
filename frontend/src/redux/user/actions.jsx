import { createAsyncThunk } from "@reduxjs/toolkit";
import { jwtDecode } from "jwt-decode";

import {
  LOGIN,
  SIGNUP,
  LOGOUT,
} from "./actionTypes";

import axiosInstance from "../axiosInstance";

// Async thunk for login
export const login = createAsyncThunk(LOGIN, async ({ username, password }) => {
  const params = new URLSearchParams();
  params.append("username", username);
  params.append("password", password);

  const response = await axiosInstance.post(
    "/login",
    params, // send as form data
    { headers: { "Content-Type": "application/x-www-form-urlencoded" } }
  );
  if (!response.data) {
    throw new Error("Network response was not ok");
  }
  const decoded = jwtDecode(response.data.access_token);
  return {
    accessToken: response.data.access_token,
    userInfo: { username: decoded.sub }
  };
});

// Async thunk for signup
export const signup = createAsyncThunk(
  SIGNUP,
  async ({ username, password }) => {
    const response = await axiosInstance.post(
      "/signup",
     { username, password }
    );

    if (!response.data) {
      throw new Error("Failed to sign up");
    }
  const decoded = jwtDecode(response.data.access_token);
  return {
    accessToken: response.data.access_token,
    userInfo: { username: decoded.sub }
  };
  }
);

export const logout = () => ({
  type: LOGOUT,
});

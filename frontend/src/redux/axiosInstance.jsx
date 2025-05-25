import axios from "axios";
import store from "./store";

const axiosInstance = axios.create({
  baseURL: "https://seashellcollection-backend.onrender.com/api/v1",
  timeout: 5000,
  headers: {
    "Content-Type": "application/json",
  },
});

// Add request interceptor
axiosInstance.interceptors.request.use(
  (config) => {
    const state = store.getState();
    const accessToken = state.user.accessToken;
    if (accessToken) {
      config.headers["Authorization"] = `Bearer ${accessToken}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

export default axiosInstance;

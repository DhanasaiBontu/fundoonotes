import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000/api/v1",
  headers: {
    "Content-Type": "application/json",
  },
});

export const registerUser = (data) =>
  API.post("/users/register", data);

export const loginUser = (data) =>
  API.post("/users/login", data);

export const forgotPassword = (data) =>
  API.post("/users/forgot-password", data);

import axios from "axios";


export const resetPassword = (data) =>
  API.post("/auth/reset-password", data);


export const getNotes = (token) =>
  API.get("/notes", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

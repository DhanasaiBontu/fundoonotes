import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000/api/v1",
  headers: {
    "Content-Type": "application/json",
  },
});

export const registerUser = async (data) => {
  return await API.post("/users/register", data);
};

export const loginUser = async (data) => {
  return await API.post("/auth/login", data);
};

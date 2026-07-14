import axios from "axios";

export const BASE_URL = "http://127.0.0.1:5000";

const api = axios.create({
    baseURL: "http://127.0.0.1:5000/api",
    headers: {
        "Content-Type": "application/json",
    },
    
});

api.interceptors.request.use((config) => {
    const token = localStorage.getItem("auth_token");

    if (token) {
        config.headers["Authentication-Token"] = token;
    }

    return config;
});

api.interceptors.response.use(

    (response) => response,

    (error) => {

        if (error.response?.status === 401 || error.response?.status === 403) {

            localStorage.removeItem("auth_token");
            localStorage.removeItem("user");

            window.location.href = "/login";
        }

        return Promise.reject(error);
    }

);

export default api;
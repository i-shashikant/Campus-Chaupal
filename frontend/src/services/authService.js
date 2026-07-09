import api from "./api";

const login = (credentials) => {
    return api.post("/auth/login", credentials);
};

const registerStudent = (data) => {
    return api.post("/auth/register/student", data);
};

const registerCompany = (data) => {
    return api.post("/auth/register/company", data);
};

export default {
    login,
    registerStudent,
    registerCompany,
};
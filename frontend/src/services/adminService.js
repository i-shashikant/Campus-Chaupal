import api from "@/services/api";

export default {

    getDashboard() {
        return api.get("/admin/dashboard");
    },

    getPendingCompanies() {
        return api.get("/admin/companies/pending");
    },

    approveCompany(companyId) {
        return api.put(`/admin/company/${companyId}/approve`);
    },

    rejectCompany(companyId) {
        return api.put(`/admin/company/${companyId}/reject`);
    },

    getUsers() {
        return api.get("/admin/users");
    },

    getJobs() {
        return api.get("/admin/jobs");
    },

    getApplications() {
        return api.get("/admin/applications");
    }

};
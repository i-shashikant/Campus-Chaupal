import api from "@/services/api";

export default {

    getDashboard() {
        return api.get("/admin/dashboard");
    },

    getPendingCompanies() {
        return api.get("/admin/companies/pending");
    },

    getCompanies() {
        return api.get("/admin/companies");
    },

    approveCompany(companyId) {
        return api.put(`/admin/company/${companyId}/approve`);
    },

    rejectCompany(companyId) {
        return api.put(`/admin/company/${companyId}/reject`);
    },

    blacklistCompany(companyId) {
        return api.put(`/admin/company/${companyId}/blacklist`);
    },

    unblockCompany(companyId) {
        return api.put(`/admin/company/${companyId}/unblock`);
    },

    getUsers() {
        return api.get("/admin/users");
    },

    blacklistStudent(studentId) {
        return api.put(`/admin/student/${studentId}/blacklist`);
    },

    unblockStudent(studentId) {
        return api.put(`/admin/student/${studentId}/unblock`);
    },

    getJobs() {
        return api.get("/admin/jobs");
    },

    getPendingJobs() {
        return api.get("/admin/jobs/pending");
    },

    approveJob(jobId) {
        return api.put(`/admin/job/${jobId}/approve`);
    },

    rejectJob(jobId, reason) {
        return api.put(`/admin/job/${jobId}/reject`, { reason });
    },

    getApplications() {
        return api.get("/admin/applications");
    }

};
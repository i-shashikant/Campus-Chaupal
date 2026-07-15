import api from "@/services/api";

export default {

    getJobs() {
        return api.get("/company/jobs");
    },

    createJob(data) {
        return api.post("/company/jobs", data);
    },

    updateJob(id, data) {
        return api.put(`/company/jobs/${id}`, data);
    },

    deleteJob(id) {
        return api.delete(`/company/jobs/${id}`);
    },
    closeJob(id) {

    return api.put(`/company/jobs/${id}/close`);

},

    
};
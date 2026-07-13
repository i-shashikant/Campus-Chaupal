import api from "@/services/api";

export default {

    apply(jobId) {
        return api.post(`/applications/apply/${jobId}`);
    },

    getStudentApplications() {
        return api.get("/applications/student");
    },

    getCompanyApplications() {
        return api.get("/applications/company");
    },
    
    updateStatus(applicationId, status) {
        return api.put(
            `/company/applications/${applicationId}/status`,
            { status }
        );
    }

};
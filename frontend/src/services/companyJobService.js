import api from "@/services/api";

export default {

    createJob(data) {
        return api.post("/company/jobs", data);
    }

};
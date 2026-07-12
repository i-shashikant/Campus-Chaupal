import api from "@/services/api";

export default {

    getJobs() {
        return api.get("/jobs");
    }

};
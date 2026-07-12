import api from "@/services/api";

export default {

    getProfile() {
        return api.get("/student/profile");
    },

    updateProfile(data) {
        return api.put("/student/profile", data);
    }

};
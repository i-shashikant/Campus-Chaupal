import { defineStore } from "pinia";
import api from "@/services/api";

export const useCompanyProfileStore = defineStore("companyProfile", {

    state: () => ({
        profile: {},
        loading: false,
    }),

    actions: {

        async fetchProfile() {

            this.loading = true;

            try {

                const res = await api.get("/company/profile");

                this.profile = res.data.data;

            } finally {

                this.loading = false;

            }

        },

        async updateProfile(data) {

            await api.put("/company/profile", data);

            await this.fetchProfile();

        },

        async uploadLogo(file){

            const form = new FormData();

            form.append("logo", file);

            const res = await api.post(
                "/company/logo",
                form,
                {
                    headers:{
                        "Content-Type":
                        "multipart/form-data"
                    }
                }
            );

            this.profile.logo = res.data.data.logo;

        }
    

    }

});
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

        }

    }

});
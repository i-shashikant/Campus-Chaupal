import { defineStore } from "pinia";
import studentProfileService from "@/services/studentProfileService";

export const useStudentProfileStore = defineStore("studentProfile", {

    state: () => ({

        profile: {

            full_name: "",
            gender: "",
            phone: "",
            address: "",
            roll_number: "",
            branch: "",
            year: "",
            cgpa: "",
            graduation_year: "",
            skills: "",
            github: "",
            linkedin: "",
            portfolio: "",
            resume: ""

        },

        loading: false

    }),

    actions: {

        async loadProfile() {

            this.loading = true;

            try {

                const response =
                    await studentProfileService.getProfile();

                this.profile = response.data.data;

            } finally {

                this.loading = false;

            }

        },

        async saveProfile() {

            this.loading = true;

            try {

                await studentProfileService.updateProfile(
                    this.profile
                );

                alert("Profile updated successfully!");

            } finally {

                this.loading = false;

            }

        }

    }

});
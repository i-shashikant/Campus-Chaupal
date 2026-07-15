import { defineStore } from "pinia";
import studentProfileService from "@/services/studentProfileService";
import api from "@/services/api";
import toast from "@/utils/toast";
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

                toast.success("Profile updated successfully!");

            } finally {

                this.loading = false;

            }

        },

        async uploadResume(file){

            const formData = new FormData();

            formData.append("resume", file);

            await api.post("/student/resume", formData,{
                headers:{
                    "Content-Type":"multipart/form-data"
                }
            });

            await this.loadProfile();

        }

    }

});
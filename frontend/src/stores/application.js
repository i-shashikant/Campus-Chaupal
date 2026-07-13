import { defineStore } from "pinia";
import applicationService from "@/services/applicationService";

export const useApplicationStore = defineStore("application", {

    state: () => ({

        applications: [],
        loading: false

    }),

    actions: {

        async apply(jobId) {

            try {

                await applicationService.apply(jobId);

                alert("Application submitted successfully.");

                return true;

            } catch (error) {

                return false;

            }

        },

        async loadStudentApplications() {

            const response =
                await applicationService.getStudentApplications();

            this.applications = response.data.data;

        },

        async loadCompanyApplications() {

            const response =
                await applicationService.getCompanyApplications();

            this.applications = response.data.data;

        }

    }

});
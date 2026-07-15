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

        },

        async updateStatus(id, status) {

            this.loading = true;

            try {

                await applicationService.updateStatus(id, status);

                const application = this.applications.find(
                    app => app.id === id
                );

                if (application) {
                    application.status = status;
                }

            } finally {

                this.loading = false;

            }

        },

        async scheduleInterview(id, data) {

            this.loading = true;

            try {

                await applicationService.scheduleInterview(id, data);

                const application = this.applications.find(
                    app => app.id === id
                );

                if (application) {

                    application.status = "Interview Scheduled";

                    application.interview_date = data.interview_date;
                    application.interview_time = data.interview_time;
                    application.interview_mode = data.interview_mode;
                    application.interview_link = data.interview_link;

                }

            } finally {

                this.loading = false;

            }

        },

        

        

    }

});
import { defineStore } from "pinia";
import companyJobService from "@/services/companyJobService";

export const useCompanyJobsStore = defineStore("companyJobs", {

    state: () => ({
        loading: false
    }),

    actions: {

        async createJob(job) {

            this.loading = true;

            try {

                await companyJobService.createJob(job);

                alert("Job Posted Successfully!");

            } finally {

                this.loading = false;

            }

        }

    }

});
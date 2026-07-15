import { defineStore } from "pinia";
import jobService from "@/services/jobService";

export const useJobStore = defineStore("job", {

    state: () => ({
        jobs: [],
        loading: false
    }),

    actions: {

        async loadJobs() {

            this.loading = true;

            try {

                const response =
                    await jobService.getJobs();

                this.jobs = response.data.data;

            } finally {

                this.loading = false;

            }

        },
        

    }

});
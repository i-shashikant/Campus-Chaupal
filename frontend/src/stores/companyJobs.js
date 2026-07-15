import { defineStore } from "pinia";
import companyJobService from "@/services/companyJobService";

export const useCompanyJobsStore = defineStore("companyJob", {

    state: () => ({

        jobs: [],

        job: {

            title: "",
            description: "",
            location: "",
            job_type: "",
            salary_package: "",
            eligibility_cgpa: "",
            deadline: ""

        },

        loading: false

    }),

    actions: {

        async loadJobs() {

            this.loading = true;

            try {

                const response =
                    await companyJobService.getJobs();

                this.jobs = response.data.data;

            } finally {

                this.loading = false;

            }

        },

        async createJob(job) {

            this.loading = true;

            try {

                await companyJobService.createJob(job);
                await this.loadJobs();

                console.log("Job created successfully.");

                this.job = {

                    title: "",
                    description: "",
                    location: "",
                    job_type: "",
                    salary_package: "",
                    eligibility_cgpa: "",
                    deadline: ""

                };

            } finally {

                this.loading = false;

            }

        },

        async closeJob(id) {

            await companyJobService.closeJob(id);

            const job = this.jobs.find(j => j.id === id);

            if (job) {

                job.status = "Closed";
                job.is_active = false;

            }

        },

        async deleteJob(id) {

            await companyJobService.deleteJob(id);

            this.loadJobs();

        }

    }

});
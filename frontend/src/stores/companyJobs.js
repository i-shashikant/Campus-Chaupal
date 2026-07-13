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

        async createJob() {

            this.loading = true;

            try {

                await companyJobService.createJob(this.job);

                alert("Job created successfully.");

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

        async deleteJob(id) {

            await companyJobService.deleteJob(id);

            this.loadJobs();

        }

    }

});
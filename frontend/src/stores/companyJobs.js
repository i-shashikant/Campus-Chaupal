import { defineStore } from "pinia";
import companyJobService from "@/services/companyJobService";
import toast from "@/utils/toast";
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

                return true;

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

    const response = await companyJobService.closeJob(id);

    const updated = response.data.data;

    this.jobs = this.jobs.map(job => {

        if (job.id === id) {

            return {
                ...job,
                status: updated.status,
                is_active: updated.is_active
            };

        }

        return job;

    });

},
        async deleteJob(id) {

            await companyJobService.deleteJob(id);

            this.jobs = this.jobs.filter(job => job.id !== id);

        }

    }

});
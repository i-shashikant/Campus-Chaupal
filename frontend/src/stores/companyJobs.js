import { defineStore } from "pinia";
import companyJobService from "@/services/companyJobService";

export const useCompanyJobsStore = defineStore("companyJobs", {

    actions: {

        async createJob(job) {

            await companyJobService.createJob(job);

            alert("Job Posted Successfully!");

        }

    }

});
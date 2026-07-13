<template>
    <DashboardLayout>

        <div class="container-fluid">

            <h2 class="fw-bold mb-4">
                Post New Job
            </h2>

            <div class="card shadow-sm">

                <div class="card-body">

                    <div class="row">

                        <div class="col-md-6 mb-3">
                            <label class="form-label">Job Title</label>
                            <input
                                class="form-control"
                                v-model="job.title"
                                placeholder="Software Engineer"
                            >
                        </div>

                        <div class="col-md-6 mb-3">
                            <label class="form-label">Location</label>
                            <input
                                class="form-control"
                                v-model="job.location"
                                placeholder="Bangalore"
                            >
                        </div>

                    </div>

                    <div class="mb-3">
                        <label class="form-label">Description</label>

                        <textarea
                            rows="5"
                            class="form-control"
                            v-model="job.description"
                            placeholder="Describe the role..."
                        ></textarea>
                    </div>

                    <div class="row">

                        <div class="col-md-4 mb-3">
                            <label class="form-label">Package</label>

                            <input
                                class="form-control"
                                v-model="job.salary_package"
                                placeholder="12 LPA"
                            >
                        </div>

                        <div class="col-md-4 mb-3">

                            <label class="form-label">Job Type</label>

                            <select
                                class="form-select"
                                v-model="job.job_type"
                            >

                                <option value="">Select</option>
                                <option>Full Time</option>
                                <option>Internship</option>
                                <option>Part Time</option>

                            </select>

                        </div>

                        <div class="col-md-4 mb-3">

                            <label class="form-label">Minimum CGPA</label>

                            <input
                                type="number"
                                step="0.01"
                                class="form-control"
                                v-model="job.eligibility_cgpa"
                            >

                        </div>

                    </div>

                    <div class="row">

                        <div class="col-md-4 mb-3">

                            <label class="form-label">Application Deadline</label>

                            <input
                                type="date"
                                class="form-control"
                                v-model="job.deadline"
                            >

                        </div>

                    </div>

                    <div class="text-end">

                        <button
                            class="btn btn-primary px-5"
                            @click="submit"
                            :disabled="companyStore.loading"
                        >

                            {{
                                companyStore.loading
                                    ? "Posting..."
                                    : "Post Job"
                            }}

                        </button>

                    </div>

                </div>

            </div>

        </div>

    </DashboardLayout>
</template>

<script setup>
import { reactive } from "vue";

import DashboardLayout from "@/layouts/DashboardLayout.vue";

import { useCompanyJobsStore } from "@/stores/companyJobs";

const companyStore = useCompanyJobsStore();

const job = reactive({

    title: "",
    description: "",
    location: "",
    salary_package: "",
    job_type: "",
    eligibility_cgpa: "",
    deadline: ""

});

async function submit() {

    await companyStore.createJob(job);

    Object.assign(job, {
        title: "",
        description: "",
        location: "",
        salary_package: "",
        job_type: "",
        eligibility_cgpa: "",
        deadline: ""
    });

}
</script>
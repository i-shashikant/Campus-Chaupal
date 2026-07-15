<template>
    <DashboardLayout>
        <div class="ppa-company">

            <div class="page-header">
                <h2 class="page-title">Post New Job</h2>
                <p class="page-sub">Fill in the details of the placement drive you're opening.</p>
            </div>

            <div class="ledger-card">
                <div class="row">
                    <div class="col-md-6 mb-3">
                        <label class="form-label">Job Title</label>
                        <input class="form-control" v-model="job.title" placeholder="Software Engineer">
                    </div>
                    <div class="col-md-6 mb-3">
                        <label class="form-label">Location</label>
                        <input class="form-control" v-model="job.location" placeholder="Bangalore">
                    </div>
                </div>

                <div class="mb-3">
                    <label class="form-label">Description</label>
                    <textarea rows="5" class="form-control" v-model="job.description" placeholder="Describe the role..."></textarea>
                </div>

                <div class="row">
                    <div class="col-md-4 mb-3">
                        <label class="form-label">Package</label>
                        <input class="form-control" v-model="job.salary_package" placeholder="12 LPA">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label class="form-label">Job Type</label>
                        <select class="form-select" v-model="job.job_type">
                            <option value="">Select</option>
                            <option>Full Time</option>
                            <option>Internship</option>
                            <option>Part Time</option>
                        </select>
                    </div>
                    <div class="col-md-4 mb-3">
                        <label class="form-label">Minimum CGPA</label>
                        <input type="number" step="0.01" class="form-control" v-model="job.eligibility_cgpa">
                    </div>
                </div>

                <div class="row">

                    <div class="col-md-4 mb-3">
                        <label class="form-label">Eligible Branch</label>
                        <select
                            class="form-control"
                            v-model="job.eligibility_branch"
                            placeholder="CSE"
                        >

                            <option value="">Select Branch</option>
                            <option>CSE</option>
                            <option>IT</option>
                            <option>ECE</option>
                            <option>EEE</option>
                            <option>Mechanical</option>
                            <option>Civil</option>
                            <option>Biotechnology</option>
                        </select>


                    </div>

                    <div class="col-md-4 mb-3">
                        <label class="form-label">Eligible Year</label>
                        <select
                            type="number"
                            class="form-control"
                            v-model="job.eligibility_year"
                            placeholder="2027"
                        >
                            <option value="">Eligibility Year</option>
                            <option>2021</option>
                            <option>2022</option>
                            <option>2023</option>
                            <option>2024</option>
                            <option>2025</option>
                            <option>2026</option>
                            <option>2027</option>
                            <option>2028</option>
                        </select>
                    </div>
                </div>

                <div class="row">
                    <div class="col-md-4 mb-3">
                        <label class="form-label">Application Deadline</label>
                        <input type="date" class="form-control" v-model="job.deadline">
                    </div>
                </div>

                <div class="text-end">
                    <button class="btn-ledger btn-ledger-navy" @click="submit" :disabled="companyStore.loading">
                        {{ companyStore.loading ? "Posting..." : "Post Job" }}
                    </button>
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
    eligibility_branch: "",
    eligibility_year: "",
    deadline: ""
});



import toast from "@/utils/toast";
import { useRouter } from "vue-router";

const router = useRouter();

const submit = async () => {

    const success = await companyStore.createJob(job);
    if(success){

        toast.success("Placement drive created successfully.");

        router.push("/company/jobs");

    }

    if (success) {

        toast.success("Placement drive created successfully!");

        router.push("/company/jobs");

    }

};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=JetBrains+Mono:wght@500&display=swap');

.ppa-company {
    --ink: #1b2a4a;
    --slate: #5b6478;
    --brass: #c89b3c;
    --emerald: #2f855a;
    --paper: #fbfaf7;
    --line: #e4e1d8;
    color: var(--ink);
}

.page-header { margin-bottom: 1.5rem; }
.page-title { font-family: "Fraunces", serif; font-weight: 600; margin-bottom: 0.15rem; }
.page-sub { color: var(--slate); margin: 0; }

.ledger-card {
    background: #fff;
    border: 1px solid var(--line);
    border-radius: 1rem;
    padding: 1.75rem;
}

.btn-ledger {
    font-size: 0.9rem;
    padding: 0.6rem 2rem;
    border-radius: 0.5rem;
    border: none;
    font-weight: 500;
    cursor: pointer;
}

.btn-ledger:disabled { opacity: 0.7; cursor: not-allowed; }
.btn-ledger-navy { background: var(--ink); color: #fff; }
</style>
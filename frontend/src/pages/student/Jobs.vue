<template>

<DashboardLayout>

    <div class="card card-job shadow-sm h-100">

        <div class="card-body">

            <div class="row g-3">

                <div class="col-md-8">

                    <div class="input-group">

                        <span class="input-group-text bg-white">

                            <i class="bi bi-search"></i>

                        </span>

                        <input
                            type="text"
                            class="form-control"
                            placeholder="Search by job title, company or location..."
                            v-model="search"
                        >

                    </div>

                </div>

                <div class="col-md-4">

                    <button
                        class="btn btn-primary w-100"
                    >

                        <i class="bi bi-funnel me-2"></i>

                        Filters

                    </button>

                </div>

            </div>

        </div>

    </div>

    <div class="container-fluid">

        <div class="card border-0 bg-primary text-white rounded-4 mb-4">

            <div class="card-body">

                <h2 class="fw-bold">

                    Find Your Dream Job 🚀

                </h2>

                <p class="mb-0">

                    Browse the latest opportunities posted by top recruiters.

                </p>

            </div>

        </div>

        <div
            class="row"
            v-if="store.jobs.length"
        >

            <div
                class="col-md-6 mb-4"
                v-for="job in store.jobs"
                :key="job.id">

                <div class="card-body">

                    <div class="d-flex justify-content-between">

                        <div>

                            <h4 class="fw-bold mb-1">

                                {{ job.title }}

                            </h4>

                            <h6 class="text-primary mb-3">

                                {{ job.company }}

                            </h6>

                        </div>

                        <div>

                            <span class="badge bg-success">

                                {{ job.salary_package }}

                            </span>

                        </div>

                    </div>

                    <p class="text-muted">

                        {{ job.description }}

                    </p>

                    <div class="row mt-3">

                        <div class="col-md-6 mb-2">

                            <i class="bi bi-geo-alt-fill text-danger me-2"></i>

                            {{ job.location }}

                        </div>

                        <div class="col-md-6 mb-2">

                            <i class="bi bi-briefcase-fill text-primary me-2"></i>

                            {{ job.job_type }}

                        </div>

                        <div class="col-md-6 mb-2">

                            <i class="bi bi-mortarboard-fill text-warning me-2"></i>

                            CGPA :

                            {{ job.eligibility_cgpa }}

                        </div>

                        <div class="col-md-6 mb-2">

                            <i class="bi bi-calendar-event me-2"></i>

                            {{ job.application_deadline }}

                        </div>

                    </div>

                    <hr>

                    <div class="d-flex justify-content-between">

                        <button
                            class="btn btn-outline-primary"
                        >

                            <i class="bi bi-eye me-2"></i>

                            View

                        </button>

                        <button
                            class="btn"
                            :class="job.applied ? 'btn-success' : 'btn-primary'"
                            :disabled="job.applied || applying.includes(job.id)"
                            @click="applyJob(job.id)"
                        >

                            <template v-if="applying.includes(job.id)">

                                <span
                                    class="spinner-border spinner-border-sm me-2"
                                ></span>

                                Applying...

                            </template>

                            <template v-else-if="job.applied">

                                <i class="bi bi-check-circle-fill me-2"></i>

                                Applied

                            </template>

                            <template v-else>

                                <i class="bi bi-send-check me-2"></i>

                                Apply Now

                            </template>

                        </button>

                    </div>

                </div>

            </div>

        </div>

        <div class="text-center py-5">

            <i class="bi bi-search fs-1 text-muted"></i>

            <h4 class="mt-3">

                No Jobs Found

            </h4>

            <p class="text-muted">

                Check back later for new placement opportunities.

            </p>

        </div>

    </div>

</DashboardLayout>

</template>

<script setup>

import { onMounted } from "vue";

import DashboardLayout from "@/layouts/DashboardLayout.vue";

import { useJobStore } from "@/stores/jobs";
import { useApplicationStore } from "@/stores/application";

const applicationStore = useApplicationStore();
import { ref } from "vue";

const applying = ref([]);

const store = useJobStore();

onMounted(() => {

    store.loadJobs();

});

const applyJob = async (jobId) => {

    applying.value.push(jobId);

    const success = await applicationStore.apply(jobId);

    if (success) {

        const job = store.jobs.find(
            j => j.id === jobId
        );

        if (job) {

            job.applied = true;

        }

    }

    applying.value = applying.value.filter(
        id => id !== jobId
    );

};

</script>
<template>

<DashboardLayout>

<div class="container-fluid">

    <h2 class="fw-bold mb-4">

        Available Jobs

    </h2>

    <div
        class="row"
        v-if="store.jobs.length"
    >

        <div
            class="col-md-6 mb-4"
            v-for="job in store.jobs"
            :key="job.id"
        >

            <div class="card shadow-sm h-100">

                <div class="card-body">

                    <h4>

                        {{ job.title }}

                    </h4>

                    <h6 class="text-primary">

                        {{ job.company }}

                    </h6>

                    <p>

                        {{ job.description }}

                    </p>

                    <div class="mb-2">

                        📍 {{ job.location }}

                    </div>

                    <div class="mb-2">

                        💼 {{ job.job_type }}

                    </div>

                    <div class="mb-2">

                        💰 {{ job.salary_package }}

                    </div>

                    <div class="mb-2">

                        🎓 Min CGPA :
                        {{ job.eligibility_cgpa }}

                    </div>

                    <button
                        class="btn btn-success mt-3" @click="applicationStore.apply(job.id)"
                    >

                        Apply Now

                    </button>

                </div>

            </div>

        </div>

    </div>

    <div
        v-else
        class="text-center text-muted mt-5"
    >

        No jobs available.

    </div>

</div>

</DashboardLayout>

</template>

<script setup>

import { onMounted } from "vue";

import DashboardLayout from "@/layouts/DashboardLayout.vue";

import { useJobStore } from "@/stores/job";
import { useApplicationStore } from "@/stores/application";

const applicationStore = useApplicationStore();

const store = useJobStore();

onMounted(() => {

    store.loadJobs();

});

</script>
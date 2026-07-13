<template>

<DashboardLayout>

<div class="container-fluid">

    <div class="d-flex justify-content-between align-items-center mb-4">

        <h2 class="fw-bold">
            Manage Jobs
        </h2>

        <RouterLink
            to="/company/jobs/create"
            class="btn btn-primary"
        >
            <i class="bi bi-plus-circle"></i>
            New Job
        </RouterLink>

    </div>

    <div class="card shadow-sm">

        <div class="card-body p-0">

            <table class="table table-hover align-middle mb-0">

                <thead class="table-light">

                    <tr>

                        <th>Title</th>
                        <th>Location</th>
                        <th>Type</th>
                        <th>Package</th>
                        <th>CGPA</th>
                        <th>Deadline</th>
                        <th width="170">Actions</th>

                    </tr>

                </thead>

                <tbody>

                    <tr
                        v-for="job in store.jobs"
                        :key="job.id"
                    >

                        <td>{{ job.title }}</td>

                        <td>{{ job.location }}</td>

                        <td>{{ job.job_type }}</td>

                        <td>{{ job.salary_package }}</td>

                        <td>{{ job.eligibility_cgpa }}</td>

                        <td>{{ job.deadline }}</td>

                        <td>

                            <button
                                class="btn btn-warning btn-sm me-2"
                            >
                                Edit
                            </button>

                            <button
                                class="btn btn-danger btn-sm"
                                @click="removeJob(job.id)"
                            >
                                Delete
                            </button>

                        </td>

                    </tr>

                    <tr
                        v-if="store.jobs.length===0"
                    >

                        <td
                            colspan="7"
                            class="text-center py-5 text-muted"
                        >

                            No jobs posted yet.

                        </td>

                    </tr>

                </tbody>

            </table>

        </div>

    </div>

</div>

</DashboardLayout>

</template>

<script setup>

import { onMounted } from "vue";

import DashboardLayout from "@/layouts/DashboardLayout.vue";

import { useCompanyJobStore } from "@/stores/companyJob";

const store = useCompanyJobStore();

onMounted(() => {

    store.loadJobs();

});

const removeJob = async(id)=>{

    if(confirm("Delete this job?")){

        await store.deleteJob(id);

    }

}

</script>
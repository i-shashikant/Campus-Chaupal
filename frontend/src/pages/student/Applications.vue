<template>

<DashboardLayout>

    <div class="container-fluid">

        <!-- Header -->

        <div class="d-flex justify-content-between align-items-center mb-4">

            <div>

                <h2 class="fw-bold mb-1">
                    Placement History
                </h2>

                <p class="text-muted mb-0">
                    Track all your placement applications and their current status.
                </p>

            </div>

            <button
                class="btn btn-success rounded-pill" @click="exportCSV">
                <i class="bi bi-download me-2"></i>
                Export CSV
            </button>

        </div>

        <!-- Search -->

        <div class="card border-0 shadow-sm rounded-4 mb-4">

            <div class="card-body">

                <div class="input-group">

                    <span class="input-group-text bg-white">
                        <i class="bi bi-search"></i>
                    </span>

                    <input
                        v-model="search"
                        class="form-control"
                        placeholder="Search by company or job title..."
                    >

                </div>

            </div>

        </div>

        <!-- Table -->

        <div
            v-if="filteredApplications.length"
            class="card border-0 shadow-sm rounded-4"
        >

            <div class="table-responsive">

                <table class="table table-hover align-middle mb-0">

                    <thead class="table-light">

                        <tr>

                            <th>Company</th>
                            <th>Job Role</th>
                            <th>Status</th>
                            <th>Applied On</th>

                        </tr>

                    </thead>

                    <tbody>

                        <tr
                            v-for="app in filteredApplications"
                            :key="app.id"
                        >

                            <td>

                                <strong>
                                    {{ app.company }}
                                </strong>

                            </td>

                            <td>

                                {{ app.title }}

                            </td>

                            <td>

                                <span
                                    class="badge rounded-pill px-3 py-2"
                                    :class="{

                                        'bg-warning': app.status === 'Applied',

                                        'bg-primary': app.status === 'Shortlisted',

                                        'bg-success': app.status === 'Selected',

                                        'bg-danger': app.status === 'Rejected'

                                    }"
                                >

                                    {{ app.status }}

                                </span>

                            </td>

                            <td>

                                {{ app.applied_at }}

                            </td>

                        </tr>

                    </tbody>

                </table>

            </div>

        </div>

        <!-- Empty State -->

        <div
            v-else
            class="text-center py-5"
        >

            <i class="bi bi-file-earmark-text fs-1 text-muted"></i>

            <h4 class="mt-3">

                No Applications Yet

            </h4>

            <p class="text-muted">

                Apply for your first job to start your placement journey.

            </p>

        </div>

    </div>

</DashboardLayout>

</template>

<script setup>

import { ref, computed, onMounted } from "vue";

import DashboardLayout from "@/layouts/DashboardLayout.vue";

import { useApplicationStore } from "@/stores/application";

const store = useApplicationStore();

const search = ref("");

const exportCSV = () => {

    const headers = [
        "Company",
        "Job Role",
        "Status",
        "Applied On"
    ];

    const rows = filteredApplications.value.map(app => [

        app.company,
        app.title,
        app.status,
        app.applied_at

    ]);

    const csvContent = [

        headers.join(","),

        ...rows.map(row => row.join(","))

    ].join("\n");

    const blob = new Blob(

        [csvContent],

        { type: "text/csv;charset=utf-8;" }

    );

    const url = window.URL.createObjectURL(blob);

    const link = document.createElement("a");

    link.href = url;

    link.setAttribute(
        "download",
        "placement_history.csv"
    );

    document.body.appendChild(link);

    link.click();

    document.body.removeChild(link);

};

onMounted(() => {

    store.loadStudentApplications();

});

const filteredApplications = computed(() => {

    if (!search.value.trim()) {

        return store.applications;

    }

    const keyword = search.value.toLowerCase();

    return store.applications.filter(app =>

        app.company.toLowerCase().includes(keyword) ||

        app.title.toLowerCase().includes(keyword)

    );

});

</script>
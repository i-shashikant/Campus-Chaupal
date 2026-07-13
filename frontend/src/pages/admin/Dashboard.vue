<template>
    <DashboardLayout>

        <div class="container-fluid">

            <div class="d-flex justify-content-between align-items-center mb-4">

                <div>
                    <h2 class="fw-bold mb-1">
                        Admin Dashboard
                    </h2>

                    <p class="text-muted">
                        Welcome back, Administrator.
                    </p>
                </div>

            </div>

            <div class="row g-4">

                <div class="col-md-4">
                    <div class="card shadow-sm border-0">
                        <div class="card-body">
                            <h6 class="text-muted">Students</h6>
                            <h2>{{ admin.dashboard.students }}</h2>
                        </div>
                    </div>
                </div>

                <div class="col-md-4">
                    <div class="card shadow-sm border-0">
                        <div class="card-body">
                            <h6 class="text-muted">Companies</h6>
                            <h2>{{ admin.dashboard.companies }}</h2>
                        </div>
                    </div>
                </div>

                <div class="col-md-4">
                    <div class="card shadow-sm border-0">
                        <div class="card-body">
                            <h6 class="text-muted">Pending Companies</h6>
                            <h2>{{ admin.dashboard.pending_companies }}</h2>
                        </div>
                    </div>
                </div>

                <div class="col-md-4">
                    <div class="card shadow-sm border-0">
                        <div class="card-body">
                            <h6 class="text-muted">Jobs</h6>
                            <h2>{{ admin.dashboard.jobs }}</h2>
                        </div>
                    </div>
                </div>

                <div class="col-md-4">
                    <div class="card shadow-sm border-0">
                        <div class="card-body">
                            <h6 class="text-muted">Applications</h6>
                            <h2>{{ admin.dashboard.applications }}</h2>
                        </div>
                    </div>
                </div>

                <div class="col-md-4">
                    <div class="card shadow-sm border-0">
                        <div class="card-body">
                            <h6 class="text-muted">Active Jobs</h6>
                            <h2>{{ admin.dashboard.active_jobs }}</h2>
                        </div>
                    </div>
                </div>

            </div>

        </div>

    </DashboardLayout>
</template>

<script setup>
import { onMounted } from "vue";

import DashboardLayout from "@/layouts/DashboardLayout.vue";
import { useAdminStore } from "@/stores/admin";

const admin = useAdminStore();

onMounted(() => {
    admin.loadDashboard();
});
</script>
<template>
    <DashboardLayout>

        <div class="container-fluid">

            <div class="card border-0 bg-primary text-white rounded-4 mb-4">

                <div class="card-body d-flex justify-content-between align-items-center">

                    <div>

                        <h2 class="fw-bold">

                            Welcome back, Administrator 👋

                        </h2>

                        <p class="mb-0">

                            Manage students, companies and placement activities from one dashboard.

                        </p>

                    </div>

                    <i class="bi bi-speedometer2 display-3 opacity-50"></i>

                </div>

            </div>

            <div class="card border-0 shadow-sm rounded-4 mt-4">

                <div class="card-body">

                    <div class="d-flex justify-content-between mb-3">

                        <h5 class="fw-bold">

                            Pending Company Approvals

                        </h5>

                        <RouterLink
                            to="/admin/companies"
                        >

                            View All

                        </RouterLink>

                    </div>

                    <div
                        class="alert alert-light border"
                        v-if="admin.dashboard.pending_companies"
                    >

                        <i class="bi bi-hourglass-split text-warning me-2"></i>

                        There are

                        <strong>

                            {{ admin.dashboard.pending_companies }}

                        </strong>

                        companies waiting for approval.

                    </div>

                    <div
                        v-else
                        class="text-center text-muted py-3"
                    >

                        <i class="bi bi-check-circle-fill text-success fs-2"></i>

                        <p class="mt-2">

                            No pending approvals.

                        </p>

                    </div>

                </div>

            </div>







                <div class="card border-0 shadow-sm rounded-4 mt-4">

                    <div class="card-body">

                        <h5 class="fw-bold mb-4">

                            Quick Actions

                        </h5>

                        <div class="row g-4">

                            <div class="col-md-3">

                                <RouterLink
                                    to="/admin/users"
                                    class="text-decoration-none"
                                >

                                    <div class="card border-0 bg-light h-100 text-center">

                                        <div class="card-body">

                                            <i class="bi bi-people-fill fs-1 text-primary"></i>

                                            <h6 class="mt-3">

                                                Students

                                            </h6>

                                        </div>

                                    </div>

                                </RouterLink>

                            </div>

                            <div class="col-md-3">

                                <RouterLink
                                    to="/admin/companies"
                                    class="text-decoration-none"
                                >

                                    <div class="card border-0 bg-light h-100 text-center">

                                        <div class="card-body">

                                            <i class="bi bi-buildings fs-1 text-success"></i>

                                            <h6 class="mt-3">

                                                Companies

                                            </h6>

                                        </div>

                                    </div>

                                </RouterLink>

                            </div>

                            <div class="col-md-3">

                                <RouterLink
                                    to="/admin/jobs"
                                    class="text-decoration-none"
                                >

                                    <div class="card border-0 bg-light h-100 text-center">

                                        <div class="card-body">

                                            <i class="bi bi-briefcase-fill fs-1 text-warning"></i>

                                            <h6 class="mt-3">

                                                Jobs

                                            </h6>

                                        </div>

                                    </div>

                                </RouterLink>

                            </div>

                            <div class="col-md-3">

                                <RouterLink
                                    to="/admin/applications"
                                    class="text-decoration-none"
                                >

                                    <div class="card border-0 bg-light h-100 text-center">

                                        <div class="card-body">

                                            <i class="bi bi-file-earmark-text-fill fs-1 text-danger"></i>

                                            <h6 class="mt-3">

                                                Applications

                                            </h6>

                                        </div>

                                    </div>

                                </RouterLink>

                            </div>

                        </div>

                    </div>

                </div>



            <div class="row g-4">

                <div class="col-lg-4 col-md-6">

                    <div class="card border-0 shadow-sm rounded-4 h-100">

                        <div class="card-body d-flex align-items-center">

                            <div class="rounded-circle bg-primary-subtle p-3 me-3">

                                <i class="bi bi-mortarboard-fill fs-3 text-primary"></i>

                            </div>

                            <div>

                                <small class="text-muted">
                                    Students
                                </small>

                                <h3 class="fw-bold mb-0">
                                    {{ admin.dashboard.students }}
                                </h3>

                            </div>

                        </div>

                    </div>

                </div>

                <div class="col-lg-4 col-md-6">

                    <div class="card border-0 shadow-sm rounded-4 h-100">

                        <div class="card-body d-flex align-items-center">

                            <div class="rounded-circle bg-success-subtle p-3 me-3">

                                <i class="bi bi-buildings-fill fs-3 text-success"></i>

                            </div>

                            <div>

                                <small class="text-muted">
                                    Companies
                                </small>

                                <h3 class="fw-bold mb-0">
                                    {{ admin.dashboard.companies }}
                                </h3>

                            </div>

                        </div>

                    </div>

                </div>

                <div class="col-lg-4 col-md-6">

                    <div class="card border-0 shadow-sm rounded-4 h-100">

                        <div class="card-body d-flex align-items-center">

                            <div class="rounded-circle bg-warning-subtle p-3 me-3">

                                <i class="bi bi-hourglass-split fs-3 text-warning"></i>

                            </div>

                            <div>

                                <small class="text-muted">
                                    Pending Companies
                                </small>

                                <h3 class="fw-bold mb-0">
                                    {{ admin.dashboard.pending_companies }}
                                </h3>

                            </div>

                        </div>

                    </div>

                </div>

                <div class="col-lg-4 col-md-6">

                    <div class="card border-0 shadow-sm rounded-4 h-100">

                        <div class="card-body d-flex align-items-center">

                            <div class="rounded-circle bg-info-subtle p-3 me-3">

                                <i class="bi bi-briefcase-fill fs-3 text-info"></i>

                            </div>

                            <div>

                                <small class="text-muted">
                                    Jobs
                                </small>

                                <h3 class="fw-bold mb-0">
                                    {{ admin.dashboard.jobs }}
                                </h3>

                            </div>

                        </div>

                    </div>

                </div>

                <div class="col-lg-4 col-md-6">

                    <div class="card border-0 shadow-sm rounded-4 h-100">

                        <div class="card-body d-flex align-items-center">

                            <div class="rounded-circle bg-danger-subtle p-3 me-3">

                                <i class="bi bi-file-earmark-text-fill fs-3 text-danger"></i>

                            </div>

                            <div>

                                <small class="text-muted">
                                    Applications
                                </small>

                                <h3 class="fw-bold mb-0">
                                    {{ admin.dashboard.applications }}
                                </h3>

                            </div>

                        </div>

                    </div>

                </div>

                <div class="col-lg-4 col-md-6">

                    <div class="card border-0 shadow-sm rounded-4 h-100">

                        <div class="card-body d-flex align-items-center">

                            <div class="rounded-circle bg-secondary-subtle p-3 me-3">

                                <i class="bi bi-check-circle-fill fs-3 text-secondary"></i>

                            </div>

                            <div>

                                <small class="text-muted">
                                    Active Jobs
                                </small>

                                <h3 class="fw-bold mb-0">
                                    {{ admin.dashboard.active_jobs }}
                                </h3>

                            </div>

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
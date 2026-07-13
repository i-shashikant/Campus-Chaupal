<template>
    <DashboardLayout>

        <div class="container-fluid">

            <div class="d-flex justify-content-between align-items-center mb-4">

                <div>
                    <h2 class="fw-bold">Pending Companies</h2>
                    <p class="text-muted">
                        Review and approve company registrations.
                    </p>
                </div>

            </div>

            <div class="card shadow-sm border-0">

                <div class="card-body">

                    <div
                        v-if="admin.pendingCompanies.length === 0"
                        class="text-center py-5 text-muted"
                    >
                        No pending companies.
                    </div>

                    <table
                        v-else
                        class="table align-middle"
                    >

                        <thead>

                            <tr>
                                <th>Company</th>
                                <th>Email</th>
                                <th>Industry</th>
                                <th>Location</th>
                                <th>Status</th>
                                <th class="text-end">
                                    Actions
                                </th>
                            </tr>

                        </thead>

                        <tbody>

                            <tr
                                v-for="company in admin.pendingCompanies"
                                :key="company.id"
                            >

                                <td>{{ company.company_name }}</td>

                                <td>{{ company.email }}</td>

                                <td>{{ company.industry }}</td>

                                <td>{{ company.location }}</td>

                                <td>

                                    <span class="badge bg-warning text-dark">
                                        {{ company.status }}
                                    </span>

                                </td>

                                <td class="text-end">

                                    <button
                                        class="btn btn-success btn-sm me-2"
                                        @click="approve(company.id)"
                                    >
                                        Approve
                                    </button>

                                    <button
                                        class="btn btn-danger btn-sm"
                                        @click="reject(company.id)"
                                    >
                                        Reject
                                    </button>

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
import { useAdminStore } from "@/stores/admin";

const admin = useAdminStore();

onMounted(() => {
    admin.loadPendingCompanies();
});

async function approve(id) {
    await admin.approveCompany(id);
}

async function reject(id) {
    await admin.rejectCompany(id);
}
</script>
<template>
    <DashboardLayout>

        <div class="container-fluid">

            <div class="d-flex justify-content-between align-items-center mb-4">

                <div>
                    <h2 class="fw-bold">Companies</h2>
                    <p class="text-muted">
                        Review registrations and manage company access.
                    </p>
                </div>

            </div>

            <div class="card shadow-sm border-0">

                <div class="card-body">

                    <div
                        v-if="admin.companies.length === 0"
                        class="text-center py-5 text-muted"
                    >
                        No companies found.
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
                                v-for="company in admin.companies"
                                :key="company.id"
                            >

                                <td>{{ company.company_name }}</td>

                                <td>{{ company.email }}</td>

                                <td>{{ company.industry }}</td>

                                <td>{{ company.location }}</td>

                                <td>

                                    <span
                                        class="badge"
                                        :class="{
                                            'bg-success': company.status === 'Approved',
                                            'bg-warning text-dark': company.status === 'Pending',
                                            'bg-danger': company.status === 'Rejected',
                                            'bg-dark': company.status === 'Blacklisted'
                                        }"
                                    >

                                        {{ company.status }}

                                    </span>

                                </td>

                                <td class="text-end">

                                    <span v-if="company.status === 'Pending'">

                                        <button
                                            class="btn btn-sm btn-success me-1"
                                            @click="approve(company.id)"
                                        >
                                            Approve
                                        </button>

                                        <button
                                            class="btn btn-sm btn-outline-danger"
                                            @click="reject(company.id)"
                                        >
                                            Reject
                                        </button>

                                    </span>

                                    <span v-else-if="company.status === 'Approved'">

                                        <button
                                            class="btn btn-sm btn-outline-dark"
                                            @click="blacklist(company.id)"
                                        >
                                            Blacklist
                                        </button>

                                    </span>

                                    <span v-else-if="company.status === 'Blacklisted'">

                                        <button
                                            class="btn btn-sm btn-outline-success"
                                            @click="unblock(company.id)"
                                        >
                                            Unblock
                                        </button>

                                    </span>

                                    <span v-else>

                                        <button
                                            class="btn btn-sm btn-outline-success"
                                            @click="approve(company.id)"
                                        >
                                            Approve
                                        </button>

                                    </span>

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
    admin.loadCompanies();
});

async function approve(id) {
    if (confirm("Approve this company?")) {
        await admin.approveCompany(id);
    }
}

async function reject(id) {
    if (confirm("Reject this company?")) {
        await admin.rejectCompany(id);
    }
}

async function blacklist(id) {
    if (confirm("Blacklist this company? Their active drives will be closed.")) {
        await admin.blacklistCompany(id);
    }
}

async function unblock(id) {
    await admin.unblockCompany(id);
}
</script>
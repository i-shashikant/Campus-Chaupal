<template>
    <DashboardLayout>
        <div class="container-fluid ppa-admin">

            <div class="page-header">
                <div>
                    <h2 class="page-title">Jobs</h2>
                    <p class="page-sub">All placement drives posted across companies.</p>
                </div>
                <div class="search-box">
                    <i class="bi bi-search"></i>
                    <input v-model="query" type="text" placeholder="Search title, company, location..." />
                </div>
            </div>

            <div class="ledger-card">
                <div class="ledger-card-header">
                    <h5>All Jobs</h5>
                    <div class="filter-tabs">
                        <button
                            v-for="tab in tabs"
                            :key="tab.value"
                            class="filter-tab"
                            :class="{ active: activeTab === tab.value }"
                            @click="activeTab = tab.value"
                        >
                            {{ tab.label }}
                        </button>
                    </div>
                </div>

                <div v-if="admin.jobs.length === 0" class="empty-state">
                    <i class="bi bi-briefcase"></i>
                    <p>No jobs found.</p>
                </div>

                <div v-else-if="filteredJobs.length === 0" class="empty-state">
                    <i class="bi bi-search"></i>
                    <p>No jobs match your filters.</p>
                </div>

                <table v-else class="ledger-table">
                    <thead>
                        <tr>
                            <th>Title</th>
                            <th>Company</th>
                            <th>Location</th>
                            <th>Deadline</th>
                            <th>Applications</th>
                            <th>Status</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="job in filteredJobs" :key="job.id">
                            <td class="fw-cell">{{ job.title }}</td>
                            <td>{{ job.company }}</td>
                            <td>{{ job.location }}</td>
                            <td>{{ job.deadline }}</td>
                            <td>{{ job.applications }}</td>
                            <td>
                                <span
                                    class="status-badge"
                                    :class="{
                                        pending: job.status === 'Pending',
                                        approved: job.status === 'Approved',
                                        rejected: job.status === 'Rejected',
                                        closed: job.status === 'Closed'
                                    }"
                                >
                                    {{ job.status }}
                                </span>
                            </td>
                            <td>

                                <template v-if="job.status === 'Pending'">

                                    <button
                                        class="btn-ledger btn-ledger-outline-emerald"
                                        @click="approve(job.id)"
                                    >
                                        <i class="bi bi-check-lg"></i>
                                        Approve
                                    </button>

                                    <button
                                        class="btn-ledger btn-ledger-outline-crimson"
                                        @click="reject(job.id)"
                                    >
                                        <i class="bi bi-x-lg"></i>
                                        Reject
                                    </button>

                                </template>

                                <span
                                    v-else
                                    class="text-muted"
                                >
                                    —
                                </span>

                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>

        </div>
    </DashboardLayout>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";

import DashboardLayout from "@/layouts/DashboardLayout.vue";
import { useAdminStore } from "@/stores/admin";

const admin = useAdminStore();
const query = ref("");
const activeTab = ref("all");

const tabs = [
    { label: "All", value: "all" },
    { label: "Pending", value: "pending" },
    { label: "Approved", value: "approved" },
    { label: "Closed", value: "closed" },
    { label: "Rejected", value: "rejected" }
];

onMounted(async () => {

    await admin.loadJobs();

});


const filteredJobs = computed(() => {

    let jobs = [...admin.jobs];

    switch (activeTab.value) {

        case "pending":
            jobs = jobs.filter(j => j.status === "Pending");
            break;

        case "approved":
            jobs = jobs.filter(j => j.status === "Approved");
            break;

        case "closed":
            jobs = jobs.filter(j => j.status === "Closed");
            break;

        case "rejected":
            jobs = jobs.filter(j => j.status === "Rejected");
            break;

        default:
            break;
    }

    const q = query.value.trim().toLowerCase();

    if (!q)
        return jobs;

    return jobs.filter(job =>
        [job.title, job.company, job.location]
            .filter(Boolean)
            .some(field => field.toLowerCase().includes(q))
    );

});

async function approve(id) {

    await admin.approveJob(id);

    await admin.loadJobs();

}

async function reject(id) {

    const reason = prompt("Reason for rejection");

    if (reason === null) return;

    await admin.rejectJob(id, reason);

    await admin.loadJobs();

}

</script>

<style scoped>
@import "@/assets/css/admin.css";
</style>
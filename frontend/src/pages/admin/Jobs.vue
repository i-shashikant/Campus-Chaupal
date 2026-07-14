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
                                        class="btn-action btn-approve"
                                        @click="approve(job.id)"
                                    >
                                        <i class="bi bi-check-lg me-1"></i>
                                        Approve
                                    </button>

                                    <button
                                        class="btn-action btn-reject"
                                        @click="reject(job.id)"
                                    >
                                        <i class="bi bi-x-lg me-1"></i>
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
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=JetBrains+Mono:wght@500&display=swap');

.ppa-admin {
    --ink: #1b2a4a;
    --slate: #5b6478;
    --brass: #c89b3c;
    --emerald: #2f855a;
    --amber: #d97706;
    --crimson: #b4442e;
    --paper: #fbfaf7;
    --line: #e4e1d8;
    color: var(--ink);
}

.page-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 1.5rem;
    gap: 1rem;
    flex-wrap: wrap;
}

.page-title {
    font-family: "Fraunces", serif;
    font-weight: 600;
    margin-bottom: 0.15rem;
}

.page-sub {
    color: var(--slate);
    margin: 0;
}

.search-box {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    background: #fff;
    border: 1px solid var(--line);
    border-radius: 0.6rem;
    padding: 0.5rem 0.9rem;
    min-width: 280px;
}

.search-box i {
    color: var(--slate);
}

.search-box input {
    border: none;
    outline: none;
    flex: 1;
    font-size: 0.9rem;
}

.ledger-card {
    background: #fff;
    border: 1px solid var(--line);
    border-radius: 1rem;
    padding: 1.5rem 1.75rem;
}

.ledger-card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
    flex-wrap: wrap;
    gap: 0.75rem;
}

.ledger-card-header h5 {
    font-weight: 600;
    margin: 0;
}

.filter-tabs {
    display: flex;
    gap: 0.4rem;
    background: var(--paper);
    padding: 0.25rem;
    border-radius: 0.6rem;
}

.filter-tab {
    border: none;
    background: transparent;
    padding: 0.35rem 0.9rem;
    border-radius: 0.45rem;
    font-size: 0.82rem;
    color: var(--slate);
    cursor: pointer;
}

.filter-tab.active {
    background: var(--ink);
    color: #fff;
}

.empty-state {
    text-align: center;
    padding: 3rem 0;
    color: var(--slate);
}

.empty-state i {
    font-size: 2rem;
    margin-bottom: 0.5rem;
    display: block;
    color: var(--line);
}

.ledger-table {
    width: 100%;
    border-collapse: collapse;
}

.ledger-table thead th {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--slate);
    border-bottom: 1px solid var(--line);
    padding: 0.6rem 0.5rem;
    text-align: left;
}

.ledger-table tbody td {
    padding: 0.85rem 0.5rem;
    border-bottom: 1px solid var(--paper);
    vertical-align: middle;
}

.ledger-table tbody tr:hover {
    background: var(--paper);
}

.fw-cell {
    font-weight: 600;
}

.tone-badge {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.72rem;
    padding: 0.25rem 0.65rem;
    border-radius: 1rem;
    text-transform: capitalize;
}

.status-badge{

    display:inline-block;

    padding:.35rem .8rem;

    border-radius:10px;

    font-size:.8rem;

    border:1px solid;

    font-weight:500;

}

.pending{

    color:#d97706;

    border-color:#d97706;

    background:white;

}

.approved{

    color:#198754;

    border-color:#198754;

    background:white;

}

.rejected{

    color:#dc3545;

    border-color:#dc3545;

    background:white;

}

.closed{

    color:#6c757d;

    border-color:#6c757d;

    background:white;

}

.btn-action{

    background:white;

    border:1px solid;

    border-radius:10px;

    padding:.45rem .9rem;

    transition:.2s;

    margin-right:.4rem;

}

.btn-approve{

    color:#198754;

    border-color:#198754;

}

.btn-approve:hover{

    background:#198754;

    color:white;

}

.btn-reject{

    color:#dc3545;

    border-color:#dc3545;

}

.btn-reject:hover{

    background:#dc3545;

    color:white;

}



.tone-emerald { background: #e7f3ec; color: var(--emerald); }
.tone-slate { background: #eef0f3; color: var(--slate); }
</style>
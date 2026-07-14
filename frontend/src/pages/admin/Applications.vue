<!-- <template>

<DashboardLayout>

<div class="container-fluid">

<h2 class="fw-bold mb-4">

Applications

</h2>

<div class="card shadow-sm">

<div class="card-body">

<table class="table">

<thead>

<tr>

<th>Student</th>

<th>Company</th>

<th>Job</th>

<th>Status</th>

<th>Applied On</th>

</tr>

</thead>

<tbody>

<tr
v-for="application in admin.applications"
:key="application.id"
>

<td>

{{ application.student }}

</td>

<td>

{{ application.company }}

</td>

<td>

{{ application.job }}

</td>

<td>

<span class="badge bg-info">

{{ application.status }}

</span>

</td>

<td>

{{ application.applied_at }}

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

admin.loadApplications();

});

</script> -->

<template>
    <DashboardLayout>
        <div class="container-fluid ppa-admin">

            <div class="page-header">
                <div>
                    <h2 class="page-title">Applications</h2>
                    <p class="page-sub">Every student application across all placement drives.</p>
                </div>
                <div class="search-box">
                    <i class="bi bi-search"></i>
                    <input v-model="query" type="text" placeholder="Search student, company, job..." />
                </div>
            </div>

            <div class="ledger-card">
                <div class="ledger-card-header">
                    <h5>All Applications</h5>
                    <span class="count-pill">{{ filteredApplications.length }} of {{ admin.applications.length }}</span>
                </div>

                <div v-if="admin.applications.length === 0" class="empty-state">
                    <i class="bi bi-file-earmark-text"></i>
                    <p>No applications found.</p>
                </div>

                <div v-else-if="filteredApplications.length === 0" class="empty-state">
                    <i class="bi bi-search"></i>
                    <p>No applications match "{{ query }}".</p>
                </div>

                <table v-else class="ledger-table">
                    <thead>
                        <tr>
                            <th>Student</th>
                            <th>Company</th>
                            <th>Job</th>
                            <th>Status</th>
                            <th>Applied On</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="application in filteredApplications" :key="application.id">
                            <td class="fw-cell">{{ application.student }}</td>
                            <td>{{ application.company }}</td>
                            <td>{{ application.job }}</td>
                            <td>
                                <span class="tone-badge" :class="badgeTone(application.status)">
                                    {{ application.status }}
                                </span>
                            </td>
                            <td>{{ application.applied_at }}</td>
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

onMounted(() => {
    admin.loadApplications();
});

const filteredApplications = computed(() => {
    const q = query.value.trim().toLowerCase();
    if (!q) return admin.applications;
    return admin.applications.filter((a) => {
        return [a.student, a.company, a.job]
            .filter(Boolean)
            .some((field) => field.toLowerCase().includes(q));
    });
});

function badgeTone(status) {
    const s = (status || "").toLowerCase();
    if (["selected", "placed", "hired"].includes(s)) return "tone-emerald";
    if (["shortlisted", "in review", "in-review", "pending"].includes(s)) return "tone-amber";
    if (["rejected", "not selected"].includes(s)) return "tone-crimson";
    if (["withdrawn"].includes(s)) return "tone-ink";
    return "tone-slate";
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
}

.ledger-card-header h5 {
    font-weight: 600;
    margin: 0;
}

.count-pill {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.75rem;
    color: var(--slate);
    background: var(--paper);
    border: 1px solid var(--line);
    padding: 0.2rem 0.6rem;
    border-radius: 1rem;
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

.tone-emerald { background: #e7f3ec; color: var(--emerald); }
.tone-amber { background: #fdf1de; color: var(--amber); }
.tone-crimson { background: #fbe9e5; color: var(--crimson); }
.tone-ink { background: #e6e9f0; color: var(--ink); }
.tone-slate { background: #eef0f3; color: var(--slate); }
</style>
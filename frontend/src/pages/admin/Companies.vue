<!-- <template>
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
</script> -->


<template>
    <DashboardLayout>
        <div class="container-fluid ppa-admin">

            <div class="page-header">
                <div>
                    <h2 class="page-title">Companies</h2>
                    <p class="page-sub">Review registrations and manage company access.</p>
                </div>
                <div class="search-box">
                    <i class="bi bi-search"></i>
                    <input v-model="query" type="text" placeholder="Search company, email, industry..." />
                </div>
            </div>

            <div class="ledger-card">
                <div class="ledger-card-header">
                    <h5>All Companies</h5>
                    <span class="count-pill">{{ filteredCompanies.length }} of {{ admin.companies.length }}</span>
                </div>

                <div v-if="admin.companies.length === 0" class="empty-state">
                    <i class="bi bi-buildings"></i>
                    <p>No companies found.</p>
                </div>

                <div v-else-if="filteredCompanies.length === 0" class="empty-state">
                    <i class="bi bi-search"></i>
                    <p>No companies match "{{ query }}".</p>
                </div>

                <table v-else class="ledger-table">
                    <thead>
                        <tr>
                            <th>Company</th>
                            <th>Email</th>
                            <th>Industry</th>
                            <th>Location</th>
                            <th>Status</th>
                            <th class="text-end">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="company in filteredCompanies" :key="company.id">
                            <td class="fw-cell">{{ company.company_name }}</td>
                            <td>{{ company.email }}</td>
                            <td>{{ company.industry }}</td>
                            <td>{{ company.location }}</td>
                            <td>
                                <span class="tone-badge" :class="badgeTone(company.status)">
                                    {{ company.status }}
                                </span>
                            </td>
                            <td class="text-end">
                                <span v-if="company.status === 'Pending'">
                                    <button class="btn-ledger btn-ledger-emerald" @click="approve(company.id)">Approve</button>
                                    <button class="btn-ledger btn-ledger-outline-crimson" @click="reject(company.id)">Reject</button>
                                </span>
                                <span v-else-if="company.status === 'Approved'">
                                    <button class="btn-ledger btn-ledger-outline-ink" @click="blacklist(company.id)">Blacklist</button>
                                </span>
                                <span v-else-if="company.status === 'Blacklisted'">
                                    <button class="btn-ledger btn-ledger-outline-emerald" @click="unblock(company.id)">Unblock</button>
                                </span>
                                <span v-else>
                                    <button class="btn-ledger btn-ledger-outline-emerald" @click="approve(company.id)">Approve</button>
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

onMounted(() => {
    admin.loadCompanies();
});

const filteredCompanies = computed(() => {
    const q = query.value.trim().toLowerCase();
    if (!q) return admin.companies;
    return admin.companies.filter((c) => {
        return [c.company_name, c.email, c.industry, c.location]
            .filter(Boolean)
            .some((field) => field.toLowerCase().includes(q));
    });
});

function badgeTone(status) {
    const s = (status || "").toLowerCase();
    if (["approved"].includes(s)) return "tone-emerald";
    if (["pending"].includes(s)) return "tone-amber";
    if (["rejected"].includes(s)) return "tone-crimson";
    if (["blacklisted"].includes(s)) return "tone-ink";
    return "tone-slate";
}

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

.btn-ledger {
    font-size: 0.8rem;
    padding: 0.35rem 0.8rem;
    border-radius: 0.5rem;
    border: 1px solid transparent;
    margin-left: 0.4rem;
    font-weight: 500;
    cursor: pointer;
}

.btn-ledger-emerald { background: var(--emerald); color: #fff; }
.btn-ledger-outline-crimson { background: transparent; color: var(--crimson); border-color: var(--crimson); }
.btn-ledger-outline-ink { background: transparent; color: var(--ink); border-color: var(--ink); }
.btn-ledger-outline-emerald { background: transparent; color: var(--emerald); border-color: var(--emerald); }
</style>
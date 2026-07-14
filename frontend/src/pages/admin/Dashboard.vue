<!-- <template>
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

                <div class="card border-0 shadow-sm rounded-4 mt-4">

                    <div class="card-body">

                        <h5 class="fw-bold mb-4">

                            Reports & Placement Statistics

                        </h5>

                        <div class="row g-4">

                            <div class="col-md-3">

                                <div class="border rounded-4 p-3 text-center h-100">

                                    <i class="bi bi-trophy-fill text-success fs-2"></i>

                                    <h4 class="fw-bold mt-2">

                                        {{ admin.dashboard.selected }}

                                    </h4>

                                    <small class="text-muted">

                                        Selected Students

                                    </small>

                                </div>

                            </div>

                            <div class="col-md-3">

                                <div class="border rounded-4 p-3 text-center h-100">

                                    <i class="bi bi-graph-up-arrow text-primary fs-2"></i>

                                    <h4 class="fw-bold mt-2">

                                        {{ admin.dashboard.placement_rate }}%

                                    </h4>

                                    <small class="text-muted">

                                        Placement Rate

                                    </small>

                                </div>

                            </div>

                            <div class="col-md-3">

                                <div class="border rounded-4 p-3 text-center h-100">

                                    <i class="bi bi-buildings-fill text-warning fs-2"></i>

                                    <h6 class="fw-bold mt-2">

                                        {{ admin.dashboard.most_active_company }}

                                    </h6>

                                    <small class="text-muted">

                                        {{ admin.dashboard.most_active_company_jobs }}

                                        Jobs Posted

                                    </small>

                                </div>

                            </div>

                            <div class="col-md-3">

                                <div class="border rounded-4 p-3 text-center h-100">

                                    <i class="bi bi-mortarboard-fill text-info fs-2"></i>

                                    <h4 class="fw-bold mt-2">

                                        {{ admin.dashboard.average_cgpa }}

                                    </h4>

                                    <small class="text-muted">

                                        Average CGPA

                                    </small>

                                </div>

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
</script> -->


<template>
    <DashboardLayout>
        <div class="container-fluid ppa-admin">

            <div class="hero-card mb-4">
                <div class="hero-emblem">
                    <i class="bi bi-award-fill"></i>
                </div>
                <div class="hero-content">
                    <span class="eyebrow">Campus Chaupal Placement Cell</span>
                    <h2 class="hero-title">Welcome back, Administrator</h2>
                    <p class="hero-sub">Manage students, companies and placement activities from one dashboard.</p>
                </div>
            </div>

            <div class="ledger-card mb-4">
                <div class="ledger-card-header">
                    <h5>Pending Company Approvals</h5>
                    <RouterLink to="/admin/companies" class="ledger-link">
                        View all <i class="bi bi-arrow-right"></i>
                    </RouterLink>
                </div>

                <div v-if="hasData" class="approval-row" :class="{ 'is-clear': !admin.dashboard.pending_companies }">
                    <template v-if="admin.dashboard.pending_companies">
                        <i class="bi bi-hourglass-split"></i>
                        <span>
                            <strong>{{ admin.dashboard.pending_companies }}</strong>
                            {{ admin.dashboard.pending_companies === 1 ? 'company is' : 'companies are' }} waiting for approval.
                        </span>
                    </template>
                    <template v-else>
                        <i class="bi bi-check-circle-fill"></i>
                        <span>No pending approvals. The register is clear.</span>
                    </template>
                </div>
                <div v-else class="skeleton-line"></div>
            </div>

            <div class="ledger-card mb-4">
                <h5 class="mb-4">Quick Actions</h5>
                <div class="quick-actions">
                    <RouterLink to="/admin/users" class="quick-action">
                        <div class="quick-icon quick-icon-navy"><i class="bi bi-people-fill"></i></div>
                        <span>Students</span>
                    </RouterLink>
                    <RouterLink to="/admin/companies" class="quick-action">
                        <div class="quick-icon quick-icon-emerald"><i class="bi bi-buildings"></i></div>
                        <span>Companies</span>
                    </RouterLink>
                    <RouterLink to="/admin/jobs" class="quick-action">
                        <div class="quick-icon quick-icon-brass"><i class="bi bi-briefcase-fill"></i></div>
                        <span>Jobs</span>
                    </RouterLink>
                    <RouterLink to="/admin/applications" class="quick-action">
                        <div class="quick-icon quick-icon-crimson"><i class="bi bi-file-earmark-text-fill"></i></div>
                        <span>Applications</span>
                    </RouterLink>
                </div>
            </div>

            <div class="ledger-card mb-4">
                <h5 class="mb-4">Reports &amp; Placement Statistics</h5>

                <div v-if="hasData" class="stats-ledger">
                    <div class="seal-wrap">
                        <div class="seal-ring" :style="{ '--pct': admin.dashboard.placement_rate ?? 0 }">
                            <div class="seal-inner">
                                <span class="seal-number">{{ admin.dashboard.placement_rate ?? 0 }}%</span>
                                <span class="seal-label">Placed</span>
                            </div>
                        </div>
                    </div>

                    <div class="ledger-lines">
                        <div class="ledger-line">
                            <span class="ledger-label"><i class="bi bi-trophy-fill"></i> Selected Students</span>
                            <span class="ledger-fill"></span>
                            <span class="ledger-value">{{ admin.dashboard.selected ?? 0 }}</span>
                        </div>
                        <div class="ledger-line">
                            <span class="ledger-label"><i class="bi bi-mortarboard-fill"></i> Average CGPA</span>
                            <span class="ledger-fill"></span>
                            <span class="ledger-value">{{ admin.dashboard.average_cgpa ?? '—' }}</span>
                        </div>
                        <div class="ledger-line">
                            <span class="ledger-label"><i class="bi bi-buildings-fill"></i> Most Active Company</span>
                            <span class="ledger-fill"></span>
                            <span class="ledger-value">
                                {{ admin.dashboard.most_active_company ?? '—' }}
                                <small v-if="admin.dashboard.most_active_company_jobs">
                                    ({{ admin.dashboard.most_active_company_jobs }} jobs)
                                </small>
                            </span>
                        </div>
                    </div>
                </div>
                <div v-else class="skeleton-block"></div>
            </div>

            <div class="row g-4">
                <div class="col-lg-4 col-md-6" v-for="card in summaryCards" :key="card.key">
                    <div class="count-card" :class="`count-card-${card.tone}`">
                        <div class="count-icon"><i :class="card.icon"></i></div>
                        <div>
                            <small>{{ card.label }}</small>
                            <h3>{{ hasData ? (admin.dashboard[card.key] ?? 0) : '—' }}</h3>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </DashboardLayout>
</template>

<script setup>
import { computed, onMounted } from "vue";

import DashboardLayout from "@/layouts/DashboardLayout.vue";
import { useAdminStore } from "@/stores/admin";

const admin = useAdminStore();

const hasData = computed(() => {
    return admin.dashboard && Object.keys(admin.dashboard).length > 0;
});

const summaryCards = [
    { key: "students", label: "Students", icon: "bi bi-mortarboard-fill", tone: "navy" },
    { key: "companies", label: "Companies", icon: "bi bi-buildings-fill", tone: "emerald" },
    { key: "pending_companies", label: "Pending Companies", icon: "bi bi-hourglass-split", tone: "amber" },
    { key: "jobs", label: "Jobs", icon: "bi bi-briefcase-fill", tone: "slate" },
    { key: "applications", label: "Applications", icon: "bi bi-file-earmark-text-fill", tone: "crimson" },
    { key: "active_jobs", label: "Active Jobs", icon: "bi bi-check-circle-fill", tone: "brass" },
];

onMounted(() => {
    admin.loadDashboard();
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=JetBrains+Mono:wght@500&display=swap');

.ppa-admin {
    --ink: #1b2a4a;
    --ink-soft: #2e3e63;
    --slate: #5b6478;
    --brass: #c89b3c;
    --brass-soft: #e8d9b5;
    --emerald: #2f855a;
    --amber: #d97706;
    --crimson: #b4442e;
    --paper: #fbfaf7;
    --line: #e4e1d8;
    color: var(--ink);
}

.hero-card {
    position: relative;
    overflow: hidden;
    border-radius: 1.25rem;
    padding: 2.25rem 2.5rem;
    background: linear-gradient(135deg, var(--ink) 0%, var(--ink-soft) 100%);
    color: #fff;
}

.hero-emblem {
    position: absolute;
    right: 1.5rem;
    top: 50%;
    transform: translateY(-50%);
    font-size: 6rem;
    opacity: 0.12;
}

.eyebrow {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.72rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--brass-soft);
}

.hero-title {
    font-family: "Fraunces", serif;
    font-weight: 600;
    margin: 0.35rem 0 0.5rem;
}

.hero-sub {
    margin: 0;
    opacity: 0.85;
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

.ledger-card h5 {
    font-weight: 600;
    margin: 0;
}

.ledger-link {
    font-size: 0.85rem;
    color: var(--ink);
    text-decoration: none;
    font-weight: 500;
}

.ledger-link:hover {
    color: var(--brass);
}

.approval-row {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.9rem 1.1rem;
    border-radius: 0.6rem;
    background: #fef8ec;
    border-left: 3px solid var(--amber);
    color: #8a5a00;
}

.approval-row.is-clear {
    background: #f0f7f3;
    border-left-color: var(--emerald);
    color: #1e5c3f;
}

.approval-row i {
    font-size: 1.3rem;
}

.quick-actions {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
}

.quick-action {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.6rem;
    padding: 1.25rem 0.5rem;
    border-radius: 0.85rem;
    background: var(--paper);
    text-decoration: none;
    color: var(--ink);
    font-weight: 500;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}

.quick-action:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(27, 42, 74, 0.1);
}

.quick-icon {
    width: 3rem;
    height: 3rem;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.35rem;
    color: #fff;
}

.quick-icon-navy { background: var(--ink); }
.quick-icon-emerald { background: var(--emerald); }
.quick-icon-brass { background: var(--brass); }
.quick-icon-crimson { background: var(--crimson); }

.stats-ledger {
    display: flex;
    gap: 2.5rem;
    align-items: center;
}

.seal-wrap {
    flex-shrink: 0;
}

.seal-ring {
    width: 140px;
    height: 140px;
    border-radius: 50%;
    background: conic-gradient(var(--brass) calc(var(--pct) * 3.6deg), var(--line) 0deg);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 8px;
}

.seal-inner {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: #fff;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    box-shadow: inset 0 0 0 1px var(--line);
}

.seal-number {
    font-family: "Fraunces", serif;
    font-weight: 600;
    font-size: 1.7rem;
    color: var(--ink);
}

.seal-label {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.65rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--slate);
}

.ledger-lines {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.ledger-line {
    display: flex;
    align-items: baseline;
}

.ledger-label {
    color: var(--slate);
    font-size: 0.92rem;
    white-space: nowrap;
}

.ledger-label i {
    margin-right: 0.4rem;
    color: var(--brass);
}

.ledger-fill {
    flex: 1;
    margin: 0 0.6rem;
    border-bottom: 2px dotted var(--line);
    height: 0.6em;
}

.ledger-value {
    font-family: "JetBrains Mono", monospace;
    font-weight: 500;
    white-space: nowrap;
}

.ledger-value small {
    color: var(--slate);
    font-weight: 400;
}

.count-card {
    display: flex;
    align-items: center;
    gap: 1rem;
    background: #fff;
    border: 1px solid var(--line);
    border-left-width: 4px;
    border-radius: 0.85rem;
    padding: 1.25rem 1.5rem;
    height: 100%;
}

.count-card small {
    color: var(--slate);
    font-size: 0.8rem;
}

.count-card h3 {
    font-family: "Fraunces", serif;
    font-weight: 600;
    margin: 0.15rem 0 0;
}

.count-icon {
    width: 2.75rem;
    height: 2.75rem;
    border-radius: 0.6rem;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    color: #fff;
    flex-shrink: 0;
}

.count-card-navy { border-left-color: var(--ink); }
.count-card-navy .count-icon { background: var(--ink); }
.count-card-emerald { border-left-color: var(--emerald); }
.count-card-emerald .count-icon { background: var(--emerald); }
.count-card-amber { border-left-color: var(--amber); }
.count-card-amber .count-icon { background: var(--amber); }
.count-card-slate { border-left-color: var(--slate); }
.count-card-slate .count-icon { background: var(--slate); }
.count-card-crimson { border-left-color: var(--crimson); }
.count-card-crimson .count-icon { background: var(--crimson); }
.count-card-brass { border-left-color: var(--brass); }
.count-card-brass .count-icon { background: var(--brass); }

.skeleton-line,
.skeleton-block {
    background: linear-gradient(90deg, var(--paper) 25%, var(--line) 50%, var(--paper) 75%);
    background-size: 200% 100%;
    animation: shimmer 1.4s infinite;
    border-radius: 0.6rem;
}

.skeleton-line { height: 48px; }
.skeleton-block { height: 140px; }

@keyframes shimmer {
    0% { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}

@media (max-width: 767px) {
    .quick-actions { grid-template-columns: repeat(2, 1fr); }
    .stats-ledger { flex-direction: column; }
    .hero-emblem { display: none; }
}

@media (prefers-reduced-motion: reduce) {
    .skeleton-line, .skeleton-block { animation: none; }
    .quick-action { transition: none; }
}
</style>
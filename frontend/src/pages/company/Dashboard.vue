<template>

    <DashboardLayout>

        <div class="container-fluid">

            <h2 class="fw-bold mb-4">
            Company Dashboard
            </h2>

            <div class="row">

                <div class="col-md-4">

                    <div class="card">
                        <div class="card-body">

                            <h5>Total Jobs</h5>

                            <h2>0</h2>

                        </div>
                    </div>

                </div>

                <div class="col-md-4">

                    <div class="card">
                        <div class="card-body">

                            <h5>Total Applications</h5>

                            <h2>0</h2>

                        </div>
                    </div>

                </div>

            </div>

        </div>

    </DashboardLayout>

</template> -->

<!-- <script setup>
import DashboardLayout from "@/layouts/DashboardLayout.vue";
</script> 

<!-- <template>
    <DashboardLayout>
        <div class="ppa-company">

            <div class="hero-card mb-4">
                <div class="hero-emblem"><i class="bi bi-buildings"></i></div>
                <div class="hero-content">
                    <span class="eyebrow">Company Portal</span>
                    <h2 class="hero-title">Welcome back, {{ profile.company_name || "Recruiter" }}</h2>
                    <p class="hero-sub">Post drives, track applicants, and manage your hiring pipeline.</p>
                </div>
                <RouterLink to="/company/jobs/create" class="hero-cta">
                    <i class="bi bi-plus-circle me-2"></i>
                    New Job
                </RouterLink>
            </div>

            <div class="row g-4 mb-4">
                <div class="col-md-3 col-sm-6">
                    <div class="count-card count-card-navy">
                        <div class="count-icon"><i class="bi bi-briefcase-fill"></i></div>
                        <div>
                            <h3>{{ stats.totalJobs }}</h3>
                            <small>Total Jobs</small>
                        </div>
                    </div>
                </div>
                <div class="col-md-3 col-sm-6">
                    <div class="count-card count-card-emerald">
                        <div class="count-icon"><i class="bi bi-check-circle-fill"></i></div>
                        <div>
                            <h3>{{ stats.activeJobs }}</h3>
                            <small>Active Jobs</small>
                        </div>
                    </div>
                </div>
                <div class="col-md-3 col-sm-6">
                    <div class="count-card count-card-brass">
                        <div class="count-icon"><i class="bi bi-file-earmark-text-fill"></i></div>
                        <div>
                            <h3>{{ stats.totalApplications }}</h3>
                            <small>Total Applications</small>
                        </div>
                    </div>
                </div>
                <div class="col-md-3 col-sm-6">
                    <div class="count-card count-card-amber">
                        <div class="count-icon"><i class="bi bi-trophy-fill"></i></div>
                        <div>
                            <h3>{{ stats.selected }}</h3>
                            <small>Selected</small>
                        </div>
                    </div>
                </div>
            </div>

            <div class="ledger-card">
                <h5 class="mb-4">Quick Actions</h5>
                <div class="quick-actions">
                    <RouterLink to="/company/jobs/create" class="quick-action">
                        <div class="quick-icon quick-icon-navy"><i class="bi bi-plus-circle"></i></div>
                        <span>Post Job</span>
                    </RouterLink>
                    <RouterLink to="/company/jobs" class="quick-action">
                        <div class="quick-icon quick-icon-brass"><i class="bi bi-briefcase-fill"></i></div>
                        <span>Manage Jobs</span>
                    </RouterLink>
                    <RouterLink to="/company/applications" class="quick-action">
                        <div class="quick-icon quick-icon-crimson"><i class="bi bi-file-earmark-text-fill"></i></div>
                        <span>Applications</span>
                    </RouterLink>
                    <RouterLink to="/company/profile" class="quick-action">
                        <div class="quick-icon quick-icon-emerald"><i class="bi bi-building-gear"></i></div>
                        <span>Company Profile</span>
                    </RouterLink>
                </div>
            </div>

        </div>
    </DashboardLayout>
</template>

<script setup>
import { computed, onMounted } from "vue";

import DashboardLayout from "@/layouts/DashboardLayout.vue";
import { useCompanyJobsStore } from "@/stores/companyJobs";
import { useApplicationStore } from "@/stores/application";
import { useCompanyProfileStore } from "@/stores/companyProfile";

const jobStore = useCompanyJobsStore();
const applicationStore = useApplicationStore();
const profileStore = useCompanyProfileStore();

onMounted(async () => {
    await jobStore.loadJobs();
    await applicationStore.loadCompanyApplications();
    await profileStore.loadProfile();
});

const profile = computed(() => profileStore.profile);

const stats = computed(() => ({
    totalJobs: jobStore.jobs.length,
    activeJobs: jobStore.jobs.filter(job => job.active !== false).length,
    totalApplications: applicationStore.applications.length,
    selected: applicationStore.applications.filter(a => a.status === "Selected").length,
}));
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=JetBrains+Mono:wght@500&display=swap');

.ppa-company {
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

.hero-card {
    position: relative;
    overflow: hidden;
    border-radius: 1.25rem;
    padding: 2.25rem 2.5rem;
    background: linear-gradient(135deg, var(--ink) 0%, #2e3e63 100%);
    color: #fff;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 1.5rem;
    flex-wrap: wrap;
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
    color: #e8d9b5;
}

.hero-title { font-family: "Fraunces", serif; font-weight: 600; margin: 0.35rem 0 0.5rem; }
.hero-sub { margin: 0; opacity: 0.85; }

.hero-cta {
    background: var(--brass);
    color: #1b2a4a;
    font-weight: 600;
    padding: 0.65rem 1.4rem;
    border-radius: 2rem;
    text-decoration: none;
    white-space: nowrap;
    z-index: 1;
    display: flex;
    align-items: center;
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

.count-card small { color: var(--slate); font-size: 0.8rem; }
.count-card h3 { font-family: "Fraunces", serif; font-weight: 600; margin: 0.15rem 0 0; }

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
.count-card-brass { border-left-color: var(--brass); }
.count-card-brass .count-icon { background: var(--brass); }
.count-card-amber { border-left-color: var(--amber); }
.count-card-amber .count-icon { background: var(--amber); }

.ledger-card {
    background: #fff;
    border: 1px solid var(--line);
    border-radius: 1rem;
    padding: 1.5rem 1.75rem;
}

.ledger-card h5 { font-weight: 600; margin: 0; }

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

.quick-action:hover { transform: translateY(-3px); box-shadow: 0 8px 20px rgba(27, 42, 74, 0.1); }

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

@media (max-width: 767px) {
    .quick-actions { grid-template-columns: repeat(2, 1fr); }
    .hero-emblem { display: none; }
}
</style> -->
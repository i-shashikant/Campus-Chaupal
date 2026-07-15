<template>
    <DashboardLayout>
        <div class="ppa-student">

            <div class="hero-card mb-4">
                <div class="hero-emblem"><i class="bi bi-mortarboard-fill"></i></div>
                <div class="hero-content">
                    <span class="eyebrow">Student Portal</span>
                    <h2 class="hero-title">Welcome back, {{ student.full_name || "Student" }}</h2>
                    <p class="hero-sub">Complete your profile and start applying for your dream placements.</p>
                </div>
                <RouterLink
                    to="/student/profile"
                    class="hero-cta"
                >
                    {{
                        completion < 100
                            ? "Complete Profile"
                            : "View Profile"
                    }}
                </RouterLink>
            </div>

            <div class="row g-4 mb-4">
                <div class="col-md-4">
                    <div class="count-card count-card-navy">
                        <div class="count-icon"><i class="bi bi-briefcase-fill"></i></div>
                        <div>
                            <h3>{{ stats.jobs }}</h3>
                            <small>Available Jobs</small>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="count-card count-card-emerald">
                        <div class="count-icon"><i class="bi bi-file-earmark-check-fill"></i></div>
                        <div>
                            <h3>{{ stats.applications }}</h3>
                            <small>Applications</small>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="count-card count-card-brass">
                        <div class="count-icon"><i class="bi bi-trophy-fill"></i></div>
                        <div>
                            <h3>{{ stats.selected }}</h3>
                            <small>Selected</small>
                        </div>
                    </div>
                </div>
            </div>

            <div class="row g-4">
                <div class="col-lg-4">
                    <ProfileCard :student="student" />
                </div>
                <div class="col-lg-8">
                    <ProfileCompletionCard :completion="completion" />
                </div>
            </div>

            <div class="row g-4 mt-1">
                <div class="col-lg-6">
                    <AcademicCard :student="student" />
                </div>
                <div class="col-lg-6">
                    <ProfessionalCard :student="student" />
                </div>
            </div>

            <div class="ledger-card mt-4">
                <div class="ledger-card-header">
                    <h5>Latest Opportunities</h5>
                    <RouterLink to="/student/jobs" class="ledger-link">
                        View all <i class="bi bi-arrow-right"></i>
                    </RouterLink>
                </div>

                <div v-if="latestJobs.length" class="opportunity-list">
                    <div class="opportunity-row" v-for="job in latestJobs" :key="job.id">
                        <div>
                            <h6>{{ job.title }}</h6>
                            <small>{{ job.company }}</small>
                        </div>
                        <RouterLink to="/student/jobs" class="btn-ledger btn-ledger-outline-ink">View</RouterLink>
                    </div>
                </div>

                <div v-else class="empty-state">
                    <i class="bi bi-search"></i>
                    <h5>No Jobs Available</h5>
                    <p>Check back later for new opportunities.</p>
                </div>
            </div>

            <div class="ledger-card mt-4">
                <h5 class="mb-3">Recent Placement Activity</h5>

                <div v-if="recentApplications.length" class="activity-list">
                    <div class="activity-row" v-for="application in recentApplications" :key="application.id">
                        <div>
                            <strong>{{ application.job_title }}</strong>
                            <div class="activity-company">{{ application.company }}</div>
                        </div>
                        <span class="tone-badge" :class="badgeTone(application.status)">
                            {{ application.status }}
                        </span>
                    </div>
                </div>

                <div v-else class="empty-state">
                    <i class="bi bi-file-earmark-text"></i>
                    <h5>Apply to your first placement drive to start tracking your placement journey.</h5>
                    <p>Your placement applications will show up here.</p>
                </div>
            </div>

        </div>
    </DashboardLayout>
</template>

<script setup>
import { onMounted, computed } from "vue";

import DashboardLayout from "@/layouts/DashboardLayout.vue";
import { useStudentProfileStore } from "@/stores/studentProfile";
import { useJobStore } from "@/stores/jobs";
import { useApplicationStore } from "@/stores/application";
import ProfileCard from "@/components/student/ProfileCard.vue";
import ProfileCompletionCard from "@/components/student/ProfileCompletionCard.vue";
import AcademicCard from "@/components/student/AcademicCard.vue";
import ProfessionalCard from "@/components/student/ProfessionalCard.vue";

const profileStore = useStudentProfileStore();
const jobStore = useJobStore();
const applicationStore = useApplicationStore();

onMounted(async () => {
    await profileStore.loadProfile();
    await jobStore.loadJobs();
    await applicationStore.loadStudentApplications();
});

const student = computed(() => profileStore.profile);

const latestJobs = computed(() =>
    jobStore.jobs
        .filter(j => j.is_active)
        .slice(0,3)
);

const recentApplications = computed(() =>
    applicationStore.applications.slice(0, 5)
);

const stats = computed(() => ({
    jobs: jobStore.jobs.length,
    applications: applicationStore.applications.length,
    selected: applicationStore.applications.filter(
        a => a.status === "Selected"
    ).length
}));

const completion = computed(() => {
    const profile = student.value || {};
    const fields = [
        profile.full_name,
        profile.gender,
        profile.phone,
        profile.address,
        profile.roll_number,
        profile.branch,
        profile.year,
        profile.cgpa,
        profile.graduation_year,
        profile.skills,
        profile.github,
        profile.linkedin,
        profile.portfolio,
    ];
    const filled = fields.filter(f => f !== null && f !== undefined && f !== "").length;
    return Math.round((filled / fields.length) * 100);
});

function badgeTone(status) {
    const s = (status || "").toLowerCase();
    if (["selected"].includes(s)) return "tone-emerald";
    if (["shortlisted", "applied"].includes(s)) return "tone-amber";
    if (s === "interview scheduled") return "tone-info";
    if (["rejected"].includes(s)) return "tone-crimson";
    return "tone-slate";
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=JetBrains+Mono:wght@500&display=swap');

.ppa-student {
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

.hero-title {
    font-family: "Fraunces", serif;
    font-weight: 600;
    margin: 0.35rem 0 0.5rem;
}

.hero-sub {
    margin: 0;
    opacity: 0.85;
}

.hero-cta {
    background: var(--brass);
    color: #1b2a4a;
    font-weight: 600;
    padding: 0.65rem 1.4rem;
    border-radius: 2rem;
    text-decoration: none;
    white-space: nowrap;
    z-index: 1;
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

.ledger-card-header h5, .ledger-card h5 { font-weight: 600; margin: 0; }

.ledger-link {
    font-size: 0.85rem;
    color: var(--ink);
    text-decoration: none;
    font-weight: 500;
}

.ledger-link:hover { color: var(--brass); }

.opportunity-list, .activity-list {
    display: flex;
    flex-direction: column;
}

.opportunity-row, .activity-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.9rem 0;
    border-bottom: 1px solid var(--paper);
}

.opportunity-row:last-child, .activity-row:last-child { border-bottom: none; }

.opportunity-row h6 { margin: 0 0 0.15rem; font-weight: 600; }
.opportunity-row small { color: var(--slate); }
.activity-company { color: var(--slate); font-size: 0.85rem; }

.btn-ledger {
    font-size: 0.8rem;
    padding: 0.35rem 0.9rem;
    border-radius: 0.5rem;
    border: 1px solid transparent;
    font-weight: 500;
    cursor: pointer;
    text-decoration: none;
}

.btn-ledger-outline-ink { background: transparent; color: var(--ink); border-color: var(--ink); }

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
.tone-slate { background: #eef0f3; color: var(--slate); }

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
.tone-info {
    background: #e8f2ff;
    color: #2563eb;
}
</style>
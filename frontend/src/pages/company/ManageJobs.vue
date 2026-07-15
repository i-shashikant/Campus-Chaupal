<template>
    <DashboardLayout>
        <div class="ppa-company">

            <div class="page-header">
                <div>
                    <h2 class="page-title">Manage Jobs</h2>
                    <p class="page-sub">Every drive you've posted, in one place.</p>
                </div>
                <RouterLink to="/company/jobs/create" class="btn-ledger btn-ledger-navy">
                    <i class="bi bi-plus-circle me-2"></i>
                    New Job
                </RouterLink>
            </div>

            <div class="search-box mb-3">
                <i class="bi bi-search"></i>
                <input v-model="query" type="text" placeholder="Search title or location..." />
            </div>

            <div class="ledger-card">
                <div v-if="store.jobs.length === 0" class="empty-state">
                    <i class="bi bi-briefcase"></i>
                    <p>No jobs posted yet.</p>
                </div>

                <div v-else-if="filteredJobs.length === 0" class="empty-state">
                    <i class="bi bi-search"></i>
                    <p>No jobs match "{{ query }}".</p>
                </div>

                <table v-else class="ledger-table">
                    <thead>
                        <tr>
                            <th>Title</th>
                            <th>Location</th>
                            <th>Type</th>
                            <th>Package</th>
                            <th>CGPA</th>
                            <th>Deadline</th>
                            <th>Status</th>
                            <th>Applicants</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="job in filteredJobs" :key="job.id">
                            <td class="fw-cell">{{ job.title }}</td>
                            <td>{{ job.location }}</td>
                            <td>{{ job.job_type }}</td>
                            <td>{{ job.salary_package }}</td>
                            <td>{{ job.eligibility_cgpa }}</td>
                            <td>{{ job.deadline }}</td>
                            <td> <span
                                class="status-pill"
                                :class="statusClass(job.status)"
                            >
                                {{ job.status }}
                            </span></td>
                            <td>
                                {{ job.applicant_count }}
                            </td>
                            <td>
                                <!-- <RouterLink :to="`/company/jobs/${job.id}/edit`" class="btn-ledger btn-ledger-outline-brass">
                                    Edit
                                </RouterLink> -->
                                <button class="btn-ledger btn-ledger-outline-crimson" @click="removeJob(job.id)">
                                    Delete
                                </button>
                                <button
                                    v-if="job.status !== 'Closed'"
                                    class="btn-ledger btn-ledger-outline-crimson"
                                    @click="closeJob(job.id)"
                                >
                                    Close
                                </button>

                                <span
                                    v-else
                                    class="status-pill closed"
                                >
                                    Closed
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
import { useCompanyJobsStore } from "@/stores/companyJobs";

const store = useCompanyJobsStore();
const query = ref("");

onMounted(() => {
    store.loadJobs();
});

const filteredJobs = computed(() => {
    const q = query.value.trim().toLowerCase();
    if (!q) return store.jobs;
    return store.jobs.filter(job => {
        return [job.title, job.location]
            .filter(Boolean)
            .some(field => field.toLowerCase().includes(q));
    });
});

const removeJob = async (id) => {
    if (confirm("Delete this job?")) {
        await store.deleteJob(id);
    }
};

const closeJob = async (id) => {

    if (!confirm("Close this placement drive?")) {
        return;
    }

    await store.closeJob(id);

};
function statusClass(status) {

    switch ((status || "").toLowerCase()) {

        case "approved":
            return "approved";

        case "pending":
            return "pending";

        case "rejected":
            return "rejected";

        case "closed":
            return "closed";

        default:
            return "";
    }

}

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=JetBrains+Mono:wght@500&display=swap');

.ppa-company {
    --ink: #1b2a4a;
    --slate: #5b6478;
    --brass: #c89b3c;
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

.page-title { font-family: "Fraunces", serif; font-weight: 600; margin-bottom: 0.15rem; }
.page-sub { color: var(--slate); margin: 0; }

.search-box {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    background: #fff;
    border: 1px solid var(--line);
    border-radius: 0.6rem;
    padding: 0.5rem 0.9rem;
    max-width: 340px;
}

.search-box i { color: var(--slate); }
.search-box input { border: none; outline: none; flex: 1; font-size: 0.9rem; }

.ledger-card {
    background: #fff;
    border: 1px solid var(--line);
    border-radius: 1rem;
    padding: 1.5rem 1.75rem;
}

.empty-state { text-align: center; padding: 3rem 0; color: var(--slate); }
.empty-state i { font-size: 2rem; margin-bottom: 0.5rem; display: block; color: var(--line); }

.ledger-table { width: 100%; border-collapse: collapse; }

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

.ledger-table tbody tr:hover { background: var(--paper); }
.fw-cell { font-weight: 600; }

.btn-ledger {
    font-size: 0.8rem;
    padding: 0.35rem 0.8rem;
    border-radius: 0.5rem;
    border: 1px solid transparent;
    margin-left: 0.4rem;
    font-weight: 500;
    cursor: pointer;
    text-decoration: none;
    display: inline-block;
}
.status-pill {

    display: inline-block;
    padding: 5px 14px;

    border-radius: 999px;

    font-size: 12px;

    font-weight: 600;

    letter-spacing: .3px;

}

.status-pill.approved {

    background: #d1fae5;
    color: #065f46;

}

.status-pill.pending {

    background: #fef3c7;
    color: #92400e;

}

.status-pill.rejected {

    background: #fee2e2;
    color: #991b1b;

}

.status-pill.closed {

    background: #e5e7eb;
    color: #374151;

}
.btn-ledger-navy { background: var(--ink); color: #fff; margin-left: 0; }
.btn-ledger-outline-brass { background: transparent; color: var(--brass); border-color: var(--brass); }
.btn-ledger-outline-crimson { background: transparent; color: var(--crimson); border-color: var(--crimson); }
</style>
<template>
    <DashboardLayout>
        <div class="ppa-student">

            <div class="page-header">
                <div>
                    <h2 class="page-title">Placement History</h2>
                    <p class="page-sub">Track all your placement applications and their current status.</p>
                </div>
                <button class="btn-ledger btn-ledger-emerald" @click="exportCSV">
                    <i class="bi bi-download me-2"></i>
                    Export CSV
                </button>
            </div>

            <div class="search-panel mb-4">
                <div class="search-box">
                    <i class="bi bi-search"></i>
                    <input v-model="search" placeholder="Search by company or job title..." />
                </div>
            </div>

            <div v-if="filteredApplications.length" class="ledger-card">
                <table class="ledger-table">
                    <thead>
                        <tr>
                            <th>Company</th>
                            <th>Job Role</th>
                            <th>Status</th>
                            <th>Interview</th>
                            <th>Applied On</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="app in filteredApplications" :key="app.id">
                            <td class="fw-cell">{{ app.company }}</td>
                            <td>{{ app.title }}</td>
                            <td>
                                <span class="tone-badge" :class="badgeTone(app.status)">
                                    {{ app.status }}
                                </span>
                            </td>

                            <td>

                                <template v-if="app.status==='Interview Scheduled'">

                                    <div class="small">
                                        <strong>Date -</strong>{{ app.interview_date }}
                                    </div>

                                    <div class="small">
                                        <strong>Time -</strong>{{ app.interview_time }}
                                    </div>

                                    <div class="small">
                                        <Strong> Mode -</Strong>{{ app.interview_mode }}
                                    </div>

                                    <a
                                        v-if="app.interview_link"
                                        :href="app.interview_link"
                                        target="_blank"
                                    >
                                        Join
                                    </a>

                                </template>

                                <span v-else>-</span>

                            </td>
                            <td>{{ app.applied_at }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div v-else class="empty-state">
                <i class="bi bi-file-earmark-text"></i>
                <h4>No Applications Yet</h4>
                <p>Apply for your first job to start your placement journey.</p>
            </div>

        </div>
    </DashboardLayout>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";

import DashboardLayout from "@/layouts/DashboardLayout.vue";
import { useApplicationStore } from "@/stores/application";

const store = useApplicationStore();
const search = ref("");

onMounted(() => {
    store.loadStudentApplications();
});

const filteredApplications = computed(() => {
    if (!search.value.trim()) {
        return store.applications;
    }
    const keyword = search.value.toLowerCase();
    return store.applications.filter(app =>
        app.company.toLowerCase().includes(keyword) ||
        app.title.toLowerCase().includes(keyword)
    );
});

function badgeTone(status) {
    const s = (status || "").toLowerCase();
    if (["selected"].includes(s)) return "tone-emerald";
    if (
        [
            "shortlisted",
            "applied",
            "interview scheduled"
        ].includes(s)
    ) return "tone-amber";
    if (["rejected"].includes(s)) return "tone-crimson";
    return "tone-slate";
}

const exportCSV = () => {

    const headers = ["Company", "Job Role", "Status", "Applied On"];

    const rows = filteredApplications.value.map(app => [
        app.company,
        app.title,
        app.status,
        app.applied_at
    ]);

    const csvContent = [
        headers.join(","),
        ...rows.map(row => row.join(","))
    ].join("\n");

    const blob = new Blob(
        [csvContent],
        { type: "text/csv;charset=utf-8;" }
    );

    const url = window.URL.createObjectURL(blob);

    const link = document.createElement("a");

    link.href = url;

    link.setAttribute(
        "download",
        "placement_history.csv"
    );

    document.body.appendChild(link);

    link.click();

    document.body.removeChild(link);

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

.search-panel {
    background: #fff;
    border: 1px solid var(--line);
    border-radius: 1rem;
    padding: 1rem 1.5rem;
}

.search-box { display: flex; align-items: center; gap: 0.5rem; }
.search-box i { color: var(--slate); }
.search-box input { border: none; outline: none; flex: 1; font-size: 0.9rem; }

.ledger-card {
    background: #fff;
    border: 1px solid var(--line);
    border-radius: 1rem;
    padding: 0.5rem 1.5rem;
}

.ledger-table { width: 100%; border-collapse: collapse; }

.ledger-table thead th {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--slate);
    border-bottom: 1px solid var(--line);
    padding: 0.9rem 0.5rem;
    text-align: left;
}

.ledger-table tbody td {
    padding: 0.9rem 0.5rem;
    border-bottom: 1px solid var(--paper);
    vertical-align: middle;
}

.ledger-table tbody tr:hover { background: var(--paper); }
.fw-cell { font-weight: 600; }

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

.btn-ledger {
    font-size: 0.85rem;
    padding: 0.55rem 1.2rem;
    border-radius: 2rem;
    border: 1px solid transparent;
    font-weight: 500;
    cursor: pointer;
}

.btn-ledger-emerald { background: var(--emerald); color: #fff; }

.empty-state { text-align: center; padding: 4rem 0; color: var(--slate); }
.empty-state i { font-size: 2.5rem; margin-bottom: 0.75rem; display: block; color: var(--line); }
</style>
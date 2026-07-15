<template>
    <div
        class="modal fade"
        id="interviewModal"
        tabindex="-1"
    >
    <div class="modal-dialog">
    <div class="modal-content">

    <div class="modal-header">
    <h5>Schedule Interview</h5>
    <button class="btn-close" data-bs-dismiss="modal"></button>
    </div>

    <div class="modal-body">

    <label>Date</label>
    <input
    type="date"
    class="form-control mb-3"
    v-model="interviewDate"
    />

    <label>Time</label>
    <input
    type="time"
    class="form-control mb-3"
    v-model="interviewTime"
    />

    <label>Mode</label>
    <input
    class="form-control mb-3"
    v-model="interviewMode"
    />

    <label>Meeting Link</label>
    <input
    class="form-control"
    v-model="interviewLink"
    />

    </div>

    <div class="modal-footer">

    <button
    class="btn btn-secondary"
    data-bs-dismiss="modal"
    >
    Cancel
    </button>

    <button
    class="btn btn-primary"
    @click="saveInterview"
    >
    Save
    </button>

    </div>

    </div>
    </div>
    </div>
    <DashboardLayout>
        <div class="ppa-company">

            <div class="page-header">
                <div>
                    <h2 class="page-title">Received Applications</h2>
                    <p class="page-sub">Review and update the status of every applicant across your drives.</p>
                </div>
                <div class="search-box">
                    <i class="bi bi-search"></i>
                    <input v-model="query" type="text" placeholder="Search student or job..." />
                </div>
            </div>

            <div class="ledger-card">
                <div v-if="store.applications.length === 0" class="empty-state">
                    <i class="bi bi-file-earmark-text"></i>
                    <p>No applications received yet.</p>
                </div>

                <div v-else-if="filteredApplications.length === 0" class="empty-state">
                    <i class="bi bi-search"></i>
                    <p>No applications match "{{ query }}".</p>
                </div>

                <table v-else class="ledger-table">
                    <thead>
                        <tr>
                            <th>Student</th>
                            <th>Job</th>
                            <th>Status</th>
                            <th>Interview</th>
                            <th>Resume</th>
                            <th>Applied On</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="app in filteredApplications" :key="app.id">
                            <td class="fw-cell">{{ app.student }}</td>
                            <td>{{ app.job }}</td>
                            <td><div class="status-actions">

                                <select
                                    class="status-select"
                                    :class="badgeTone(app.status)"
                                    :value="app.status"
                                    @change="updateStatus(app.id, $event.target.value)"
                                >
                                    <option>Applied</option>
                                    <option>Shortlisted</option>
                                    <option>Interview Scheduled</option>
                                    <option>Selected</option>
                                    <option>Rejected</option>
                                </select>
                                
                                <button
                                    v-if="app.status === 'Shortlisted'"
                                    class="btn btn-sm btn-outline-primary"
                                    @click="scheduleInterview(app)"
                                > Schedule
                                </button></div>

                            </td>
                            <td>

                                <template v-if="app.interview_date">

                                    <div><strong>Date -</strong> {{ app.interview_date }}</div>

                                    <div> <strong>Time -</strong>{{ app.interview_time }}</div>

                                    <div><Strong> Mode -</Strong>{{ app.interview_mode }}</div>
                                    <div><a
    v-if="app.interview_link"
    :href="app.interview_link"
    target="_blank"
    class="text-decoration-none"
>
    Join Meeting
</a></div>

                                </template>

                                <span v-else>-</span>

                            </td>
                            <td>

    <a
        v-if="app.resume"
        :href="app.resume"
        target="_blank"
        class="btn btn-sm btn-outline-success"
    >
        <i class="bi bi-file-earmark-pdf me-1"></i>
        View Resume
    </a>

    <span v-else class="text-muted">
        Not Uploaded
    </span>

</td>
                            <td>{{ app.applied_at }}</td>
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
import { useApplicationStore } from "@/stores/application";
import * as bootstrap from "bootstrap";


const store = useApplicationStore();
const query = ref("");
const selectedApplication = ref(null);
const interviewDate = ref("");
const interviewTime = ref("");
const interviewMode = ref("Google Meet");
const interviewLink = ref("");


onMounted(() => {
    store.loadCompanyApplications();
});

const filteredApplications = computed(() => {
    const q = query.value.trim().toLowerCase();
    if (!q) return store.applications;
    return store.applications.filter(app => {
        return [app.student, app.job]
            .filter(Boolean)
            .some(field => field.toLowerCase().includes(q));
    });
});

function badgeTone(status) {
    const s = (status || "").toLowerCase();
    if (s === "selected") return "tone-emerald";
    if (s === "shortlisted" || s === "applied") return "tone-amber";
    if (s === "rejected") return "tone-crimson";
    return "tone-slate";
}

async function updateStatus(id, status) {

    if (
        status === "Selected" &&
        !confirm("Mark this student as Selected?")
    ) {
        return;
    }

    await store.updateStatus(id, status);

}

function scheduleInterview(app) {

    selectedApplication.value = app;

    interviewDate.value = "";
    interviewTime.value = "";
    interviewMode.value = "Google Meet";
    interviewLink.value = "";

    const modal = new bootstrap.Modal(
        document.getElementById("interviewModal")
    );

    modal.show();
}

async function saveInterview() {

    await store.scheduleInterview(
        selectedApplication.value.id,
        {
            interview_date: interviewDate.value,
            interview_time: interviewTime.value,
            interview_mode: interviewMode.value,
            interview_link: interviewLink.value
        }
    );

    bootstrap.Modal
        .getInstance(document.getElementById("interviewModal"))
        .hide();

    store.loadCompanyApplications();

}




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
    min-width: 280px;
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

.status-select {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.78rem;
    padding: 0.35rem 0.7rem;
    border-radius: 0.5rem;
    border: 1px solid var(--line);
    background: #fff;
    cursor: pointer;
}
.status-actions {
    display: flex;
    align-items: center;
    gap: 10px;
}
.tone-emerald { color: var(--emerald); border-color: var(--emerald); }
.tone-amber { color: var(--amber); border-color: var(--amber); }
.tone-crimson { color: var(--crimson); border-color: var(--crimson); }
.tone-slate { color: var(--slate); }
</style>
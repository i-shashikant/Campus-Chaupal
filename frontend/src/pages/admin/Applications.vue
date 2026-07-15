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
import toast from "@/utils/toast";

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
@import "@/assets/css/admin.css";
</style>
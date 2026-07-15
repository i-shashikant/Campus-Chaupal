<template>
    <DashboardLayout>
        <div class="container-fluid ppa-admin">

            <div class="page-header">
                <div>
                    <h2 class="page-title">Students</h2>
                    <p class="page-sub">See every student registered at your portal.</p>
                </div>
                <div class="search-box">
                    <i class="bi bi-search"></i>
                    <input v-model="query" type="text" placeholder="Search name, email, role..." />
                </div>
            </div>

            <div class="ledger-card">
                <div class="ledger-card-header">
                    <h5>All Users</h5>
                    <span class="count-pill">{{ filteredUsers.length }} of {{ admin.users.length }}</span>
                </div>

                <div v-if="admin.users.length === 0" class="empty-state">
                    <i class="bi bi-people"></i>
                    <p>No users found.</p>
                </div>

                <div v-else-if="filteredUsers.length === 0" class="empty-state">
                    <i class="bi bi-search"></i>
                    <p>No users match "{{ query }}".</p>
                </div>

                <table v-else class="ledger-table">
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Email</th>
                            <th>Role</th>
                            <th>Status</th>
                            <th class="text-end">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="user in filteredUsers" :key="user.id">
                            <td class="fw-cell">{{ user.name || "—" }}</td>
                            <td>{{ user.email }}</td>
                            <td>
                                <span class="tone-badge" :class="roleTone(user.role)">
                                    {{ user.role }}
                                </span>
                            </td>
                            <td>
                                <span class="tone-badge" :class="badgeTone(user.status)">
                                    {{ user.status }}
                                </span>
                            </td>
                            <td class="text-end">

                                <template v-if="user.role === 'student'">

                                    <button
                                        v-if="user.status !== 'Blacklisted'"
                                        class="btn-ledger btn-ledger-outline-crimson"
                                        @click="blacklist(user.id)"
                                    >
                                        <i class="bi bi-slash-circle me-1"></i>
                                        Blacklist
                                    </button>

                                    <button
                                        v-else
                                        class="btn-ledger btn-ledger-outline-emerald"
                                        @click="unblock(user.id)"
                                    >
                                        <i class="bi bi-arrow-clockwise me-1"></i>
                                        Activate
                                    </button>

                                </template>

                                <span v-else class="text-muted">
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
import toast from "@/utils/toast";

const admin = useAdminStore();
const query = ref("");

onMounted(() => {
    admin.loadUsers();
});

const filteredUsers = computed(() => {
    const q = query.value.trim().toLowerCase();
    if (!q) return admin.users;
    return admin.users.filter((u) => {
        return [u.name, u.email, u.role]
            .filter(Boolean)
            .some((field) => field.toLowerCase().includes(q));
    });
});

function roleTone(role) {
    const r = (role || "").toLowerCase();
    if (r === "student") return "tone-ink";
    if (r === "company") return "tone-brass";
    if (r === "admin") return "tone-crimson";
    return "tone-slate";
}

function badgeTone(status) {
    const s = (status || "").toLowerCase();
    if (["active", "approved"].includes(s)) return "tone-emerald";
    if (["pending"].includes(s)) return "tone-amber";
    if (["blocked", "blacklisted", "deactivated", "inactive"].includes(s)) return "tone-crimson";
    return "tone-slate";
}

async function blacklist(id){

    if(!confirm("Blacklist this student?"))
        return;

    await admin.blacklistStudent(id);

    await admin.loadUsers();
    toast.warning("Student blacklisted.");

}

async function unblock(id){

    await admin.unblockStudent(id);

    await admin.loadUsers();
    toast.warning("Student activated.");

}
</script>

<style scoped>
@import "@/assets/css/admin.css";
</style>
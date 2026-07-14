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

                    <h5>Companies</h5>

                    <div class="filter-tabs">

                        <button
                            v-for="tab in tabs"
                            :key="tab.value"
                            class="filter-tab"
                            :class="{ active: activeTab === tab.value }"
                            @click="activeTab = tab.value"
                        >
                            {{ tab.label }}
                        </button>

                    </div>

                </div>

                <div v-if="admin.companies.length === 0" class="empty-state">
                    <i class="bi bi-buildings"></i>
                    <p>No companies found.</p>
                </div>

                <div v-else-if="filteredCompanies.length === 0" class="empty-state">
                    <i class="bi bi-search"></i>

                    <p>
                        {{
                            query
                                ? `No companies match "${query}".`
                                : "No companies found."
                        }}
                    </p>
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
                                    <button class="btn-ledger btn-ledger-emerald" @click="approve(company.id)"><i class="bi bi-check-lg me-1"></i>Approve</button>
                                    <button class="btn-ledger btn-ledger-outline-crimson" @click="reject(company.id)"> <i class="bi bi-x-lg me-1"></i>Reject</button>
                                </span>
                                <span v-else-if="company.status === 'Approved'">
                                    <button class="btn-ledger btn-ledger-outline-ink" @click="blacklist(company.id)"> <i class="bi bi-slash-circle me-1"></i>Blacklist</button>
                                </span>
                                <span v-else-if="company.status === 'Blacklisted'">
                                    <button class="btn-ledger btn-ledger-outline-emerald" @click="unblock(company.id)"><i class="bi bi-arrow-clockwise me-1"></i>Unblock</button>
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
const activeTab = ref("all");

const tabs = [
    { label: "All", value: "all" },
    { label: "Pending", value: "pending" },
    { label: "Approved", value: "approved" },
    { label: "Rejected", value: "rejected" },
    { label: "Blacklisted", value: "blacklisted" }
];

onMounted(() => {
    admin.loadCompanies();
});

const filteredCompanies = computed(() => {

    let companies = [...admin.companies];

    switch (activeTab.value) {

        case "pending":
            companies = companies.filter(c => c.status === "Pending");
            break;

        case "approved":
            companies = companies.filter(c => c.status === "Approved");
            break;

        case "rejected":
            companies = companies.filter(c => c.status === "Rejected");
            break;

        case "blacklisted":
            companies = companies.filter(c => c.status === "Blacklisted");
            break;
    }

    const q = query.value.trim().toLowerCase();

    if (!q)
        return companies;

    return companies.filter(c =>
        [
            c.company_name,
            c.email,
            c.industry,
            c.location
        ]
            .filter(Boolean)
            .some(field =>
                field.toLowerCase().includes(q)
            )
    );

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

    if (!confirm("Approve this company?"))
        return;

    await admin.approveCompany(id);

    await admin.loadCompanies();

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
@import "@/assets/css/admin.css";

</style>
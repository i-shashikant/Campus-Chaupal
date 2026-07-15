<template>
    <DashboardLayout>
        <div class="ppa-company">

            <div class="page-header">
                <h2 class="page-title">Company Profile</h2>
                <p class="page-sub">This is what students see when they view your job postings.</p>
            </div>

            <div class="ledger-card mb-4">
                <div class="profile-summary">
                    <img
                        :src="
                            profileStore.profile.logo
                                ? BASE_URL + profileStore.profile.logo
                                : logoUrl
                        "
                        class="logo"
                        width="100"
                        height="100"
                    />
                    <div class="flex-grow-1">
                        <h3>{{ profileStore.profile.company_name || "Company Name" }}</h3>
                        <p class="summary-sub">{{ profileStore.profile.industry || "Industry" }}</p>
                        <span class="tone-badge tone-navy">{{ profileStore.profile.location || "Location not set" }}</span>
                    </div>
                    <label class="btn-ledger btn-ledger-outline-ink">
                        Upload Logo
                        <input type="file" accept="image/*" hidden @change="onLogoChange">
                    </label>
                </div>
            </div>

            <div class="row g-4 mb-4">
                <div class="col-lg-6">
                    <div class="ledger-card h-100">
                        <div class="section-header">
                            <i class="bi bi-building me-2"></i>
                            Company Details
                        </div>

                        <div class="mb-3">
                            <label class="form-label">Company Name</label>
                            <input class="form-control" v-model="profileStore.profile.company_name">
                        </div>

                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label class="form-label">Industry</label>
                                <input class="form-control" v-model="profileStore.profile.industry">
                            </div>
                            <div class="col-md-6 mb-3">
                                <label class="form-label">Location</label>
                                <input class="form-control" v-model="profileStore.profile.location">
                            </div>
                        </div>

                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label class="form-label">Website</label>
                                <input type="text" class="form-control" v-model="profileStore.profile.website">
                            </div>
                            <div class="col-md-6 mb-3">
                                <label class="form-label">Email</label>
                                <input class="form-control" :value="profileStore.profile.email" disabled>
                            </div>
                        </div>

                        <div class="mb-3">
                            <label class="form-label">About the Company</label>
                            <textarea rows="4" class="form-control" v-model="profileStore.profile.description"></textarea>
                        </div>
                    </div>
                </div>

                <div class="col-lg-6">
                    <div class="ledger-card h-100">
                        <div class="section-header">
                            <i class="bi bi-person-lines-fill me-2"></i>
                            Contact Person
                        </div>

                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label class="form-label">Contact Name</label>
                                <input class="form-control" v-model="profileStore.profile.hr_name">
                            </div>
                            <div class="col-md-6 mb-3">
                                <label class="form-label">Phone</label>
                                <input class="form-control" v-model="profileStore.profile.phone" pattern="[0-9]{10}" maxlength="10">
                            </div>
                        </div>

                        <div class="mb-3">
                            <label class="form-label">HR / Recruiter Email</label>
                            <input type="text" class="form-control" v-model="profileStore.profile.hr_email">
                        </div>

                        <div class="mb-3">
                            <label class="form-label">Address</label>
                            <textarea
                                rows="2"
                                class="form-control"
                                v-model="profileStore.profile.address">
                            </textarea>
                        </div>

                        <div class="row">

                            <div class="col-md-4 mb-3">
                                <label class="form-label">City</label>
                                <input
                                    class="form-control"
                                    v-model="profileStore.profile.city">
                            </div>

                            <div class="col-md-4 mb-3">
                                <label class="form-label">State</label>
                                <input
                                    class="form-control"
                                    v-model="profileStore.profile.state">
                            </div>

                            <div class="col-md-4 mb-3">
                                <label class="form-label">Country</label>
                                <input
                                    class="form-control"
                                    v-model="profileStore.profile.country">
                            </div>

                        </div>
                    </div>
                </div>
            </div>

            <div class="text-end mb-4">
                <button class="btn-ledger btn-ledger-navy btn-lg" @click="saveProfile">
                    <i class="bi bi-check-circle me-2"></i>
                    Save Changes
                </button>
            </div>

        </div>
    </DashboardLayout>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";

import DashboardLayout from "@/layouts/DashboardLayout.vue";
import { useCompanyProfileStore } from "@/stores/companyProfile";
import api, { BASE_URL } from "@/services/api";
import toast from "@/utils/toast";
const profileStore = useCompanyProfileStore();
const logoPreview = ref(null);

onMounted(() => {
    profileStore.fetchProfile();
});

const logoUrl = computed(() => {
    const name = profileStore.profile.company_name || "Company";
    return `https://ui-avatars.com/api/?name=${encodeURIComponent(name)}`;
});


async function onLogoChange(event) {

    const file = event.target.files[0];

    if (!file) return;

    await profileStore.uploadLogo(file);
    console.log(profileStore.profile.logo);

    await profileStore.fetchProfile();
    toast.success("Company profile updated.");

}

async function saveProfile() {

    await profileStore.updateProfile(profileStore.profile);

    toast.success("Company profile updated.");

}

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=JetBrains+Mono:wght@500&display=swap');

.ppa-company {
    --ink: #1b2a4a;
    --slate: #5b6478;
    --brass: #c89b3c;
    --paper: #fbfaf7;
    --line: #e4e1d8;
    color: var(--ink);
}

.page-header { margin-bottom: 1.5rem; }
.page-title { font-family: "Fraunces", serif; font-weight: 600; margin-bottom: 0.15rem; }
.page-sub { color: var(--slate); margin: 0; }

.ledger-card {
    background: #fff;
    border: 1px solid var(--line);
    border-radius: 1rem;
    padding: 1.5rem 1.75rem;
}

.profile-summary {
    display: flex;
    align-items: center;
    gap: 1.5rem;
    flex-wrap: wrap;
}

.logo {
    border-radius: 0.85rem;
    border: 1px solid var(--line);
    object-fit: cover;
}

.profile-summary h3 { font-family: "Fraunces", serif; font-weight: 600; margin-bottom: 0.2rem; }
.summary-sub { color: var(--slate); margin-bottom: 0.5rem; }

.section-header {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--slate);
    border-bottom: 1px solid var(--line);
    padding-bottom: 0.9rem;
    margin-bottom: 1.25rem;
}

.tone-badge {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.72rem;
    padding: 0.25rem 0.65rem;
    border-radius: 1rem;
    background: #e6e9f0;
    color: var(--ink);
}

.btn-ledger {
    font-size: 0.85rem;
    padding: 0.55rem 1.3rem;
    border-radius: 2rem;
    border: 1px solid transparent;
    font-weight: 500;
    cursor: pointer;
}

.btn-ledger-navy { background: var(--ink); color: #fff; }
.btn-ledger-outline-ink { background: transparent; color: var(--ink); border-color: var(--ink); cursor: pointer; }
.btn-lg { padding: 0.75rem 2.2rem; font-size: 0.95rem; }
</style>
<template>
    <DashboardLayout>
        <div class="ppa-student">

            <div class="page-header">
                <div>
                    <h2 class="page-title">My Profile</h2>
                    <p class="page-sub">Keep your details current so recruiters see the real you.</p>
                </div>
            </div>

            <div class="ledger-card mb-4">
                <div class="profile-summary">
                    <img :src="avatarUrl" class="avatar" width="110" height="110" />
                    <div class="flex-grow-1">
                        <h3>{{ profileStore.profile.full_name || "Student Name" }}</h3>
                        <p class="summary-sub">{{ profileStore.profile.branch || "Branch" }}</p>
                        <span class="tone-badge tone-navy me-2">CGPA {{ profileStore.profile.cgpa || "--" }}</span>
                        <span class="tone-badge tone-emerald">{{ profileStore.profile.year || "--" }} Year</span>
                    </div>
                    <button class="btn-ledger btn-ledger-navy" @click="scrollToForm">
                        <i class="bi bi-pencil-square me-2"></i>
                        Edit Profile
                    </button>
                </div>
            </div>

            <div class="row g-4 mb-4" ref="formSection">
                <div class="col-lg-6">
                    <div class="ledger-card h-100">
                        <div class="section-header">
                            <i class="bi bi-person-circle me-2"></i>
                            Personal Information
                        </div>

                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label class="form-label">Full Name</label>
                                <input class="form-control" v-model="profileStore.profile.full_name">
                            </div>
                            <div class="col-md-6 mb-3">
                                <label class="form-label">Gender</label>
                                <select class="form-select" v-model="profileStore.profile.gender">
                                    <option>Male</option>
                                    <option>Female</option>
                                    <option>Other</option>
                                </select>
                            </div>
                        </div>

                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label class="form-label">Phone</label>
                                <input class="form-control" v-model="profileStore.profile.phone"  maxlength="10", type="tel">
                            </div>
                            <div class="col-md-6 mb-3">
                                <label class="form-label">Email</label>
                                <input class="form-control" :value="profileStore.profile.email" disabled>
                            </div>
                        </div>

                        <div class="mb-3">
                            <label class="form-label">Address</label>
                            <textarea rows="3" class="form-control" v-model="profileStore.profile.address"></textarea>
                        </div>
                    </div>
                </div>

                <div class="col-lg-6">
                    <div class="ledger-card h-100">
                        <div class="section-header">
                            <i class="bi bi-mortarboard me-2"></i>
                            Academic Information
                        </div>

                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label class="form-label">Roll Number</label>
                                <input v-model="profileStore.profile.roll_number" class="form-control">
                            </div>
                        </div>

                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label class="form-label">Branch</label>
                                <select v-model="profileStore.profile.branch" class="form-select">
                                    <option value="">Select Branch</option>
                                    <option>CSE</option>
                                    <option>IT</option>
                                    <option>ECE</option>
                                    <option>EEE</option>
                                    <option>Mechanical</option>
                                    <option>Civil</option>
                                    <option>Biotechnology</option>
                                </select>
                            </div>
                            <div class="col-md-6 mb-3">
                                <label class="form-label">Year</label>
                                <select v-model="profileStore.profile.year" class="form-select">
                                    <option value="">Select Year</option>
                                    <option>1</option>
                                    <option>2</option>
                                    <option>3</option>
                                    <option>4</option>
                                </select>
                            </div>
                        </div>

                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label class="form-label">CGPA</label>
                                <input type="number" step="0.01" min="0" max="10" class="form-control" v-model="profileStore.profile.cgpa" />
                            </div>
                            <div class="col-md-6 mb-3">
                                <label class="form-label">Graduation Year</label>
                                <select type="number" class="form-control" v-model="profileStore.profile.graduation_year">
                
                                    <option value="">Select Year</option>
                                    <option>2021</option>
                                    <option>2022</option>
                                    <option>2023</option>
                                    <option>2024</option>
                                    <option>2025</option>
                                    <option>2026</option>
                                    <option>2027</option>
                                    <option>2028</option>
                                </select>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="ledger-card mb-4">
                <div class="section-header">
                    <i class="bi bi-briefcase me-2"></i>
                    Professional Information
                </div>

                <div class="row">
                    <div class="col-md-6 mb-3">
                        <label class="form-label">Skills</label>
                        <textarea rows="3" class="form-control" v-model="profileStore.profile.skills"></textarea>
                    </div>
                    <div class="col-md-6 mb-3">
                        <label class="form-label">Github URL</label>
                        <input type="text" class="form-control" v-model="profileStore.profile.github">
                    </div>
                    <div class="col-md-6 mb-3">
                        <label class="form-label"> <i class="bi bi-eye me-2"></i>LinkedIn URL</label>
                        <input type="text" class="form-control" v-model="profileStore.profile.linkedin">
                    </div>
                    <div class="col-md-6 mb-3">
                        <label class="form-label">Portfolio URL</label>
                        <input type="text" class="form-control" v-model="profileStore.profile.portfolio">
                    </div>

                    <div class="resume-drop">

                        <i class="bi bi-file-earmark-pdf-fill"></i>

                        <h6>Resume</h6>

                        <p v-if="profileStore.profile.resume">
                            Resume Uploaded ✅
                        </p>

                        <p v-else>
                            Upload your latest resume (PDF)
                        </p>

                        <input
                            type="file"
                            accept=".pdf"
                            class="form-control mt-3"
                            @change="uploadResume"
                        />
                        <br>
                        <a
                            v-if="resumeUrl"
                            :href="resumeUrl"
                            target="_blank"
                            class="btn-ledger btn-ledger-outline-navy"
                        >
                            <i class="bi bi-file-earmark-pdf"></i>
                            View Resume
                        </a>

                    </div>
                </div>
            </div>

            <div class="text-end mb-4">
                <button class="btn-ledger btn-ledger-navy btn-lg" @click="saveProfile()">
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
import { useStudentProfileStore } from "@/stores/studentProfile";
import toast from "@/utils/toast";

const profileStore = useStudentProfileStore();
const formSection = ref(null);
const photoPreview = ref(null);
const resumeFile = ref(null);

onMounted(async () => {
    await profileStore.loadProfile();
});

const avatarUrl = computed(() => {
    const name = profileStore.profile.full_name || "Student";
    return `https://ui-avatars.com/api/?name=${encodeURIComponent(name)}`;
});

function scrollToForm() {
    formSection.value?.scrollIntoView({ behavior: "smooth", block: "start" });
}


function onResumeChange(event) {
    resumeFile.value = event.target.files[0] || null;
}

async function uploadResume(e){

    const file = e.target.files[0];

    if(!file) return;

    await profileStore.uploadResume(file);
    toast.success("Resume updated successfully.");

}

const resumeUrl = computed(() => {

    if (!profileStore.profile.resume) return null;

    return "http://127.0.0.1:5000" + profileStore.profile.resume;

});


async function saveProfile() {

    const success = await profileStore.saveProfile();

    if (success) {

        router.push("/student/dashboard");

    }

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

.avatar, .avatar-lg {
    border-radius: 50%;
    border: 3px solid var(--paper);
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

.resume-drop {
    border: 1px dashed var(--line);
    border-radius: 0.85rem;
    padding: 1.5rem;
    text-align: center;
}

.resume-drop i { font-size: 2rem; color: var(--crimson); }
.resume-drop h6 { margin-top: 0.5rem; }
.resume-name { color: var(--emerald); font-size: 0.85rem; margin: 0.25rem 0 0; }

.tone-badge {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.72rem;
    padding: 0.25rem 0.65rem;
    border-radius: 1rem;
}

.tone-navy { background: #e6e9f0; color: var(--ink); }
.tone-emerald { background: #e7f3ec; color: var(--emerald); }

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
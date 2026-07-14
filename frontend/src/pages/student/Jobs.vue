<template>
    <div
    class="modal fade"
    id="jobModal"
    tabindex="-1">

        <div class="modal-dialog modal-lg">

            <div class="modal-content">

                <div class="modal-header">

                    <h5 class="modal-title">

                {{ selectedJob?.title }}

                    </h5>

                    <button
                        class="btn-close"
                        data-bs-dismiss="modal"
                    ></button>

                </div>

                <div class="modal-body">

                    <p>

                    <strong>Company</strong><br>

                    {{ selectedJob?.company }}

                    </p>

                    <p>

                    <strong>Location</strong><br>

                    {{ selectedJob?.location }}

                    </p>

                    <p>

                    <strong>Package</strong><br>

                    {{ selectedJob?.salary_package }}

                    </p>

                    <p>

                    <strong>Job Type</strong><br>

                    {{ selectedJob?.job_type }}

                    </p>

                    <p>

                    <strong>Description</strong><br>

                    {{ selectedJob?.description }}

                    </p>

                    <p>

                    <strong>Eligibility CGPA</strong><br>

                    {{ selectedJob?.eligibility_cgpa }}

                    </p>

                    <p>

                    <strong>Deadline</strong><br>

                    {{ selectedJob?.deadline }}

                    </p>
                    <p>

                    <strong>Deadline</strong><br>

                    {{ selectedJob?.deadline }}

                    </p> 

                </div>

            <div class="modal-footer">

                <button
                    class="btn btn-secondary"
                    data-bs-dismiss="modal"
                >

                Close

                </button>

            </div>

        </div>

    </div>

    </div>
    <DashboardLayout>
        <div class="ppa-student">

            <div class="hero-card mb-4">
                <div>
                    <h2 class="hero-title">Find Your Dream Job</h2>
                    <p class="hero-sub">Browse the latest opportunities posted by top recruiters.</p>
                </div>
            </div>

            <div class="search-panel mb-4">
                <div class="search-row">
                    <div class="search-box flex-grow-1">
                        <i class="bi bi-search"></i>
                        <input type="text" v-model="search" placeholder="Search by job title, company or location..." />
                    </div>
                    <button class="btn-ledger btn-ledger-navy" @click="showFilters = !showFilters">
                        <i class="bi bi-funnel me-2"></i>
                        Filters
                    </button>
                </div>

                <div v-if="showFilters" class="filter-row">
                    <select v-model="jobTypeFilter" class="filter-select">
                        <option value="">All Job Types</option>
                        <option v-for="type in jobTypes" :key="type" :value="type">{{ type }}</option>
                    </select>
                    <select v-model="locationFilter" class="filter-select">
                        <option value="">All Locations</option>
                        <option v-for="loc in locations" :key="loc" :value="loc">{{ loc }}</option>
                    </select>
                    <button
                        v-if="jobTypeFilter || locationFilter"
                        class="btn-ledger btn-ledger-outline-ink"
                        @click="jobTypeFilter = ''; locationFilter = ''"
                    >
                        Clear
                    </button>
                </div>
            </div>

            <div class="row" v-if="filteredJobs.length">
                <div class="col-md-6 mb-4" v-for="job in filteredJobs" :key="job.id">
                    <div class="job-card">
                        <div class="d-flex justify-content-between align-items-start">

                            <div class="d-flex">

                                <img
                                    :src="job.company_logo || '/company.png'"
                                    class="company-logo"
                                />

                                <div class="ms-3">

                                    <h4 class="mb-1">
                                        {{ job.title }}
                                    </h4>

                                    <h6 class="company-name">
                                        {{ job.company }}
                                    </h6>

                                </div>

                            </div>

                            <div class="salary-badge">

                                {{ job.salary_package }}

                            </div>

                        </div>

                        

                        <div class="job-info mt-3">

                            <div>

                                <i class="bi bi-geo-alt-fill text-danger me-2"></i>

                                {{ job.location }}

                            </div>

                            <div>

                                <i class="bi bi-briefcase-fill me-2"></i>

                                {{ job.job_type }}

                            </div>

                        </div>

                        <div class="eligibility mt-3">

                            <span class="chip">

                                CGPA {{ job.eligibility_cgpa }}

                            </span>

                            <span
                                class="chip"
                                v-if="job.eligibility_branch"
                            >

                                {{ job.eligibility_branch }}

                            </span>

                            <span
                                class="chip"
                                v-if="job.eligibility_year"
                            >

                                {{ job.eligibility_year }}

                            </span>

                        </div>

                        <div class="deadline mt-3">

                            <i class="bi bi-calendar-event me-2"></i>

                            Apply Before

                            <strong>

                                {{ job.deadline }}

                            </strong>

                        </div>

                        <hr>

                        <div class="d-flex justify-content-between align-items-center mt-4">

                            <button
                                class="btn-ledger btn-ledger-outline-ink" @click="viewJob(job)" data-bs-toggle="modal" data-bs-target="#jobModal"
                            >

                                <i class="bi bi-eye me-2"></i>

                                View

                            </button>

                            <button
                                class="btn-ledger"
                                :class="job.applied ? 'btn-ledger-emerald' : 'btn-ledger-navy'"
                                :disabled="job.applied || applying.includes(job.id)"
                                @click="applyJob(job.id)"
                            >

                                <template v-if="applying.includes(job.id)">

                                    <span class="spinner-border spinner-border-sm me-2"></span>

                                    Applying...

                                </template>

                                <template v-else-if="job.applied">

                                    <i class="bi bi-check-circle-fill me-2"></i>

                                    Applied

                                </template>

                                <template v-else>

                                    <i class="bi bi-send-check me-2"></i>

                                    Apply Now

                                </template>

                            </button>

                        </div>
                    </div>
                </div>
            </div>

            <div v-else class="empty-state">
                <i class="bi bi-search"></i>
                <h4>No Jobs Found</h4>
                <p>Check back later for new placement opportunities.</p>
            </div>

        </div>
    </DashboardLayout>
</template>

<script setup>
import { onMounted, ref, computed } from "vue";

import DashboardLayout from "@/layouts/DashboardLayout.vue";
import { useJobStore } from "@/stores/jobs";
import { useApplicationStore } from "@/stores/application";

const applicationStore = useApplicationStore();
const store = useJobStore();

const applying = ref([]);
const search = ref("");
const showFilters = ref(false);
const jobTypeFilter = ref("");
const locationFilter = ref("");
const selectedJob = ref(null);

function viewJob(job){

    selectedJob.value = job;

}

onMounted(() => {
    store.loadJobs();
});

const jobTypes = computed(() => {
    return [...new Set(store.jobs.map(job => job.job_type).filter(Boolean))];
});

const locations = computed(() => {
    return [...new Set(store.jobs.map(job => job.location).filter(Boolean))];
});

const filteredJobs = computed(() => {
    let jobs = store.jobs;

    if (search.value.trim()) {
        const keyword = search.value.toLowerCase();
        jobs = jobs.filter(job =>
            job.title.toLowerCase().includes(keyword) ||
            job.company.toLowerCase().includes(keyword) ||
            job.location.toLowerCase().includes(keyword)
        );
    }

    if (jobTypeFilter.value) {
        jobs = jobs.filter(job => job.job_type === jobTypeFilter.value);
    }

    if (locationFilter.value) {
        jobs = jobs.filter(job => job.location === locationFilter.value);
    }

    return jobs;
});

const applyJob = async (jobId) => {

    applying.value.push(jobId);

    const success = await applicationStore.apply(jobId);

    if(success){

        await store.loadJobs();

    }

    applying.value = applying.value.filter(id => id !== jobId);

};
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
    border-radius: 1.25rem;
    padding: 2rem 2.5rem;
    background: linear-gradient(135deg, var(--ink) 0%, #2e3e63 100%);
    color: #fff;
}

.hero-title { font-family: "Fraunces", serif; font-weight: 600; margin-bottom: 0.4rem; }
.hero-sub { margin: 0; opacity: 0.85; }

.search-panel {
    background: #fff;
    border: 1px solid var(--line);
    border-radius: 1rem;
    padding: 1.25rem 1.5rem;
}

.search-row { display: flex; gap: 1rem; align-items: center; flex-wrap: wrap; }

.search-box {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    background: var(--paper);
    border: 1px solid var(--line);
    border-radius: 0.6rem;
    padding: 0.55rem 0.9rem;
    min-width: 260px;
}

.search-box i { color: var(--slate); }
.search-box input { border: none; outline: none; flex: 1; font-size: 0.9rem; background: transparent; }

.filter-row {
    display: flex;
    gap: 0.75rem;
    margin-top: 1rem;
    flex-wrap: wrap;
}

.filter-select {
    border: 1px solid var(--line);
    border-radius: 0.5rem;
    padding: 0.45rem 0.8rem;
    font-size: 0.85rem;
    color: var(--ink);
    background: #fff;
}

.job-card {
    background: #fff;
    border: 1px solid var(--line);
    border-radius: 1rem;
    padding: 1.5rem;
    height: 100%;
}

.job-card h4 { font-family: "Fraunces", serif; font-weight: 600; margin-bottom: 0.15rem; }
.job-card h6 { color: var(--brass); font-weight: 600; margin-bottom: 0.5rem; }
.job-desc { color: var(--slate); }

.tone-badge {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.72rem;
    padding: 0.25rem 0.65rem;
    border-radius: 1rem;
    height: fit-content;
}

.tone-emerald { background: #e7f3ec; color: var(--emerald); }

.btn-ledger {
    font-size: 0.85rem;
    padding: 0.5rem 1.1rem;
    border-radius: 0.5rem;
    border: 1px solid transparent;
    font-weight: 500;
    cursor: pointer;
}

.btn-ledger:disabled { opacity: 0.7; cursor: not-allowed; }

.btn-ledger-navy { background: var(--ink); color: #fff; }
.btn-ledger-emerald { background: var(--emerald); color: #fff; }
.btn-ledger-outline-ink { background: transparent; color: var(--ink); border-color: var(--ink); }

.empty-state {
    text-align: center;
    padding: 4rem 0;
    color: var(--slate);
}

.empty-state i {
    font-size: 2.5rem;
    margin-bottom: 0.75rem;
    display: block;
    color: var(--line);
}

.company-logo{

    width:64px;

    height:64px;

    border-radius:14px;

    border:1px solid #e5e5e5;

    object-fit:cover;

    flex-shrink:0;

}

.company-name{

    color:#777;

    font-size:.9rem;

    margin:0;

}

.salary-badge{

    background:#e7f3ec;

    color:#198754;

    padding:.5rem 1rem;

    border-radius:12px;

    font-weight:600;

    white-space:nowrap;

}

.job-info{

    display:flex;

    justify-content:space-between;

    font-size:.9rem;

}

.eligibility{

    display:flex;

    gap:.5rem;

    flex-wrap:wrap;

}

.chip{

    background:#f5f5f5;

    border:1px solid #ddd;

    border-radius:30px;

    padding:.3rem .8rem;

    font-size:.78rem;

}

.deadline{

    color:#666;

    font-size:.9rem;

}

.job-card{

    transition:.25s;

}

.job-card:hover{

    transform:translateY(-4px);

    box-shadow:0 10px 25px rgba(0,0,0,.08);

}
</style>
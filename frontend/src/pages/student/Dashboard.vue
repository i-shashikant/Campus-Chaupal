<template>

<DashboardLayout>

    <!-- Welcome Hero -->

    <div class="card border-0 shadow-sm rounded-4 mb-4">

        <div class="card-body d-flex justify-content-between align-items-center">

            <div>

                <h2 class="fw-bold mb-1">
                    👋 Welcome back, {{ student.full_name }}
                </h2>

                <p class="text-muted mb-0">
                    Complete your profile and start applying for your dream placements.
                </p>

            </div>

            <button
                class="btn btn-primary rounded-pill px-4"
            >
                Complete Profile
            </button>

        </div>

    </div>

    <!-- Dashboard Stats -->

    <div class="row g-4 mb-4">

        <div class="col-md-4">

            <div class="card border-0 shadow-sm rounded-4 h-100">

                <div class="card-body d-flex align-items-center">

                    <div class="rounded-circle bg-primary-subtle p-3 me-3">

                        <i class="bi bi-briefcase-fill fs-3 text-primary"></i>

                    </div>

                    <div>

                        <h3 class="fw-bold mb-0">

                            {{ stats.jobs }}

                        </h3>

                        <small class="text-muted">

                            Available Jobs

                        </small>

                    </div>

                </div>

            </div>

        </div>

        <div class="col-md-4">

            <div class="card border-0 shadow-sm rounded-4 h-100">

                <div class="card-body d-flex align-items-center">

                    <div class="rounded-circle bg-success-subtle p-3 me-3">

                        <i class="bi bi-file-earmark-check-fill fs-3 text-success"></i>

                    </div>

                    <div>

                        <h3 class="fw-bold mb-0">

                            {{ stats.applications }}

                        </h3>

                        <small class="text-muted">

                            Applications

                        </small>

                    </div>

                </div>

            </div>

        </div>

        <div class="col-md-4">

            <div class="card border-0 shadow-sm rounded-4 h-100">

                <div class="card-body d-flex align-items-center">

                    <div class="rounded-circle bg-warning-subtle p-3 me-3">

                        <i class="bi bi-trophy-fill fs-3 text-warning"></i>

                    </div>

                    <div>

                        <h3 class="fw-bold mb-0">

                            {{ stats.selected }}

                        </h3>

                        <small class="text-muted">

                            Selected

                        </small>

                    </div>

                </div>

            </div>

        </div>

    </div>



    <!-- Profile Row -->

    <div class="row g-4">

        <div class="col-lg-4">

            <ProfileCard
                :student="student"
            />

        </div>

        <div class="col-lg-8">

            <ProfileCompletionCard
                :completion="completion"
            />

        </div>

    </div>

    <!-- Academic + Professional -->

    <div class="row g-4 mt-1">

        <div class="col-lg-6">

            <AcademicCard
                :student="student"
            />

        </div>

        <div class="col-lg-6">

            <ProfessionalCard
                :student="student"
            />

        </div>

    </div>

    <!-- Latest Jobs -->

    <div class="card border-0 shadow-sm rounded-4 mt-4">

        <div class="card-body">

            <div class="d-flex justify-content-between align-items-center">

                <h5 class="fw-bold mb-0">
                    Latest Opportunities
                </h5>

                <RouterLink
                    to="/student/jobs"
                >
                    View All
                </RouterLink>

            </div>

            <div
                v-if="latestJobs.length"
                class="list-group list-group-flush mt-3"
            >

                <div
                    class="list-group-item px-0"
                    v-for="job in latestJobs"
                    :key="job.id"
                >

                    <div class="d-flex justify-content-between align-items-center">

                        <div>

                            <h6 class="mb-1">
                                {{ job.title }}
                            </h6>

                            <small class="text-muted">
                                {{ job.company_name }}
                            </small>

                        </div>

                        <button
                            class="btn btn-outline-primary btn-sm"
                        >
                            View
                        </button>

                    </div>

                </div>

            </div>

            <div
                v-else
                class="text-center py-5"
            >

                <i class="bi bi-search fs-1 text-muted"></i>

                <h5 class="mt-3">
                    No Jobs Available
                </h5>

                <p class="text-muted">
                    Check back later for new opportunities.
                </p>

            </div>

        </div>

    </div>

    <!-- Recent Placement Activity -->

    <div class="card border-0 shadow-sm rounded-4 mt-4">

        <div class="card-body">

            <h5 class="fw-bold mb-3">
                Recent Placement Activity
            </h5>

            <ul class="list-group list-group-flush">

                <li
                    class="list-group-item"
                    v-for="application in recentApplications"
                    :key="application.id"
                >

                    <div class="d-flex justify-content-between align-items-center">

                        <div>

                            <strong>
                                {{ application.job_title }}
                            </strong>

                            <div class="text-muted">
                                {{ application.company }}
                            </div>

                        </div>

                        <span
                            class="badge"
                            :class="{
                                'bg-warning': application.status === 'Applied',
                                'bg-primary': application.status === 'Shortlisted',
                                'bg-success': application.status === 'Selected',
                                'bg-danger': application.status === 'Rejected'
                            }"
                        >
                            {{ application.status }}
                        </span>

                    </div>

                </li>

            </ul>

        </div>

    </div>

</DashboardLayout>

</template>

<script setup>



import { onMounted, computed } from "vue";

import { useStudentProfileStore } from "@/stores/studentProfile";
import { useJobStore } from "@/stores/jobs";
import { useApplicationStore } from "@/stores/application";

const profileStore = useStudentProfileStore();
const jobStore = useJobStore();
const applicationStore = useApplicationStore();

onMounted(async () => {

    await profileStore.loadProfile();
    await jobStore.loadJobs();
    await applicationStore.loadApplications();

});
const student = computed(() => profileStore.profile);

const latestJobs = computed(() => jobStore.jobs.slice(0, 3));

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
    // temporary calculation
    return 80;
});
</script>
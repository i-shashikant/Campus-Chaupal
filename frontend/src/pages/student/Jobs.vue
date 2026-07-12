<template>
  <DashboardLayout>

    <div class="container-fluid">

      <h2 class="fw-bold mb-4">
        Available Jobs
      </h2>

      <div
        class="card mb-3"
        v-for="job in jobsStore.jobs"
        :key="job.id"
      >
        <div class="card-body">

          <h4>{{ job.title }}</h4>

          <h6 class="text-muted">
            {{ job.company }}
          </h6>

          <p>{{ job.description }}</p>

          <p>
            📍 {{ job.location }}
          </p>

          <p>
            💰 {{ job.salary_package }}
          </p>

          <button class="btn btn-primary">
            Apply
          </button>

        </div>
      </div>

    </div>

  </DashboardLayout>
</template>

<script setup>
import { onMounted } from "vue";

import StudentLayout from "@/layouts/StudentLayout.vue";

import { useJobsStore } from "@/stores/jobs";

const jobsStore = useJobsStore();

onMounted(() => {

    jobsStore.loadJobs();

});
</script>
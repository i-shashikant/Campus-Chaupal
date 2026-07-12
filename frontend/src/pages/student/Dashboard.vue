<template>

<DashboardLayout>

    <template #sidebar>

        <p>Dashboard</p>

        <p>Profile</p>

        <p>Jobs</p>

        <p>Applications</p>

    </template>

    <div class="mb-4">

        <h2>

            Welcome Back 👋

        </h2>

        <p class="text-muted">

            Ready to kickstart your career today?

        </p>

    </div>



    <ProfileCompletionCard />

</DashboardLayout>

</template>

<script setup>

import DashboardLayout from "@/layouts/DashboardLayout.vue";
import ProfileCompletionCard from "@/components/student/ProfileCompletionCard.vue";

</script>
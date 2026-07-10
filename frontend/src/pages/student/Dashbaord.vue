<template>

<DashboardLayout>

    <template #sidebar>

        <p>Dashboard</p>

        <p>Profile</p>

        <p>Jobs</p>

        <p>Applications</p>

    </template>

    <h2>

        Welcome Back 👋

    </h2>

    <ProfileCompletionCard />

</DashboardLayout>

</template>

<script setup>

import DashboardLayout from "@/layouts/DashboardLayout.vue";
import ProfileCompletionCard from "@/components/student/ProfileCompletionCard.vue";

</script>
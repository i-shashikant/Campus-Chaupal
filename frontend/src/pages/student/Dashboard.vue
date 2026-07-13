<template>

<DashboardLayout>

    <template #sidebar>

        <p>Dashboard</p>

        <p>Profile</p>

        <p>Jobs</p>

        <p>Applications</p>

    </template>

    <div class="row g-4">

        <div class="col-lg-4">

            <ProfileCard :student="student"/>

        </div>

        <div class="col-lg-8">

            <ProfileCompletionCard
                :completion="80"
            />

        </div>

    </div>

    <div class="row g-4 mt-1">

        <div class="col-lg-6">

            <AcademicCard :student="student"/>

        </div>

        <div class="col-lg-6">

            <ProfessionalCard :student="student"/>

        </div>

    </div>



    <ProfileCompletionCard />

</DashboardLayout>

</template>

<script setup>

import DashboardLayout from "@/layouts/DashboardLayout.vue";
import ProfileCompletionCard from "@/components/student/ProfileCompletionCard.vue";

</script>
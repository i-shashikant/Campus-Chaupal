<template>

<DashboardLayout>

    <div class="container-fluid">

        <h2 class="mb-4">

            My Profile

        </h2>

        <ProfileCard/>

        <AcademicCard/>

        <ProfessionalCard/>

    </div>

</DashboardLayout>

</template>

<script setup>

import DashboardLayout from "@/layouts/DashboardLayout.vue";

import ProfileCard from "@/components/student/ProfileCard.vue";

import AcademicCard from "@/components/student/AcademicCard.vue";

import ProfessionalCard from "@/components/student/ProfessionalCard.vue";

</script>


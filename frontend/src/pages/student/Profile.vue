<template>

<DashboardLayout>

<div class="container-fluid">

    <h2 class="fw-bold mb-4">

        My Profile

    </h2>

    <!-- Personal -->

    <div class="card profile-sm mb-4">

        <div class="profile-header">

            Personal Information

        </div>

        <div class="profile-body">

        </div>

    </div>

    <!-- Academic -->

    <div class="card profile-sm mb-4">

        <div class="profile-header">

            Academic Information

        </div>

        <div class="profile-body">

        </div>

    </div>

    <!-- Professional -->

    <div class="card profile-sm">

        <div class="profile-header">

            Professional Information

        </div>

        <div class="profile-body">

        </div>

    </div>

</div>

</DashboardLayout>

</template>

<script setup>

import DashboardLayout from "@/layouts/DashboardLayout.vue";

</script>

<style scoped>
@import "@/assets/css/profile.css";
</style>
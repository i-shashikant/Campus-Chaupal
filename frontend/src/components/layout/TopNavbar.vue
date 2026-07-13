<script>


import { useAuthStore } from "@/stores/auth";

const authStore = useAuthStore();


</script>

<template>

<nav class="navbar dashboard-navbar px-4">

    <h3 v-if="authStore.user?.role==='student'">
    Student Dashboard
    </h3>

    <h3 v-else-if="authStore.user?.role==='company'">
    Company Dashboard
    </h3>

    <h3 v-else>
    Admin Dashboard
    </h3>

    <div class="d-flex align-items-center gap-4">

        <i class="bi bi-bell fs-5"></i>

        <div class="d-flex align-items-center gap-2">

            <img
                src="https://ui-avatars.com/api/?name=Student"
                class="avatar"
            />

        </div>

    </div>

</nav>

</template>

<style scoped>

.dashboard-navbar{

    height:70px;

    background:white;

    box-shadow:0 3px 12px rgba(0,0,0,.05);

}

.avatar{

    width:42px;

    height:42px;

    border-radius:50%;

}

</style>
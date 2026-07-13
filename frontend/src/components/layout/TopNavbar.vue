<template>

<nav class="navbar dashboard-navbar px-4">

    <h3>
        {{ title }}
    </h3>

    <div class="d-flex align-items-center gap-4">

        <i class="bi bi-bell fs-5"></i>

        <div class="d-flex align-items-center gap-2">

            <img
                src="https://ui-avatars.com/api/?name=User"
                class="avatar"
            />

        </div>

    </div>

</nav>

</template>

<script setup>

import { computed } from "vue";
import { useAuthStore } from "@/stores/auth";

const authStore = useAuthStore();

const title = computed(() => {

    switch (authStore.user?.role) {

        case "student":
            return "Student Dashboard";

        case "company":
            return "Company Dashboard";

        case "admin":
            return "Admin Dashboard";

        default:
            return "CampusChaupal";

    }

});

</script>

<style scoped>

.dashboard-navbar {

    height:70px;
    background:white;
    box-shadow:0 3px 12px rgba(0,0,0,.05);

}

.avatar {

    width:42px;
    height:42px;
    border-radius:50%;

}

</style>
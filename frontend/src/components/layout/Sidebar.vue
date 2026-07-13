<template>

<div
    class="sidebar"
    :class="{ collapsed }"
>

    <div class="sidebar-header">

        <button
            class="toggle-btn"
            @click="$emit('toggle')"
        >
            <i class="bi bi-list"></i>
        </button>

        <span v-if="!collapsed">
            CampusChaupal
        </span>

    </div>

    <ul class="nav flex-column">

        <li
            v-for="item in menu"
            :key="item.route"
            class="nav-item"
        >
            <RouterLink
                :to="item.route"
                class="nav-link"
            >
                <i :class="`bi ${item.icon}`"></i>

                <span>
                    {{ item.title }}
                </span>

            </RouterLink>

        </li>

    </ul>

</div>

</template>

<script setup>
import {
    studentMenu,
    companyMenu,
    adminMenu
} from "@/config/sidebar";

import { computed } from "vue";
import { useAuthStore } from "@/stores/auth";

const authStore = useAuthStore();

const menu = computed(() => {

    switch (authStore.user?.role) {

        case "student":
            return studentMenu;

        case "company":
            return companyMenu;

        case "admin":
            return adminMenu;

        default:
            return [];
    }

});
</script>


<style scoped>
.router-link-active{

    background:#2563eb;

    border-radius:10px;

}
</style>

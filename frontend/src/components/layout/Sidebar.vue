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

    <ul class="nav flex-column mt-4">

    <!-- STUDENT -->

        <template v-if="role==='student'">

            <li class="nav-item">
                <RouterLink to="/student/dashboard" class="nav-link">
                    <i class="bi bi-house"></i>
                    <span v-if="!collapsed">Dashboard</span>
                </RouterLink>
            </li>

            <li class="nav-item">
                <RouterLink to="/student/profile" class="nav-link">
                    <i class="bi bi-person"></i>
                    <span v-if="!collapsed">Profile</span>
                </RouterLink>
            </li>

            <li class="nav-item">
                <RouterLink to="/student/jobs" class="nav-link">
                    <i class="bi bi-briefcase"></i>
                    <span v-if="!collapsed">Jobs</span>
                </RouterLink>
            </li>

            <li class="nav-item">
                <RouterLink to="/student/applications" class="nav-link">
                    <i class="bi bi-file-earmark-text"></i>
                    <span v-if="!collapsed">Applications</span>
                </RouterLink>
            </li>

        </template>

        <!-- COMPANY -->

        <template v-else-if="role==='company'">

            <li class="nav-item">
                <RouterLink to="/company/dashboard" class="nav-link">
                    <i class="bi bi-house"></i>
                    <span v-if="!collapsed">Dashboard</span>
                </RouterLink>
            </li>

            <li class="nav-item">
                <RouterLink to="/company/jobs/create" class="nav-link">
                    <i class="bi bi-plus-circle"></i>
                    <span v-if="!collapsed">Post Job</span>
                </RouterLink>
            </li>

            <li class="nav-item">
                <RouterLink to="/company/jobs" class="nav-link">
                    <i class="bi bi-briefcase"></i>
                    <span v-if="!collapsed">Manage Jobs</span>
                </RouterLink>
            </li>

            <li class="nav-item">
                <RouterLink to="/company/applications" class="nav-link">
                    <i class="bi bi-file-earmark-text"></i>
                    <span v-if="!collapsed">Applications</span>
                </RouterLink>
            </li>

        </template>

    </ul>

</div>

</template>

<script setup>


import { computed } from "vue";
import { useAuthStore } from "@/stores/auth";

const props = defineProps({
    collapsed: Boolean
});

defineEmits(["toggle"]);

const authStore = useAuthStore();

const role = computed(() => authStore.user?.role);
</script>


<style scoped>
.router-link-active{

    background:#2563eb;

    border-radius:10px;

}
</style>

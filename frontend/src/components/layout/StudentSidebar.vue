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

        <li class="nav-item">

            <RouterLink to="/student/dashboard" class="nav-link">

                <i class="bi bi-house"></i>

                <span v-if="!collapsed">

                    Dashboard

                </span>

            </RouterLink>

        </li>

        <li class="nav-item">

            <RouterLink to="/student/profile" class="nav-link">

                <i class="bi bi-person"></i>

                <span v-if="!collapsed">
                    Profile
                </span>

            </RouterLink>

        </li>

        <li class="nav-item">

            <RouterLink to="/student/jobs" class="nav-link">

                <i class="bi bi-briefcase"></i>

                <span v-if="!collapsed">
                    Jobs
                </span>

            </RouterLink>

        </li>

        <li class="nav-item">

            <RouterLink to="/student/application" class="nav-link">

                <i class="bi bi-file-earmark-text"></i>

                <span v-if="!collapsed">
                    Applications
                </span>

            </RouterLink>

        </li>

    </ul>

</div>

</template>

<script setup>

defineProps({
    collapsed:Boolean
});

defineEmits([
    "toggle"
]);

</script>

<style scoped>
.router-link-active{

    background:#2563eb;

    border-radius:10px;

}
</style>

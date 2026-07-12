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
            <RouterLink
                to="/company/dashboard"
                class="nav-link"
            >
                <i class="bi bi-house"></i>

                <span v-if="!collapsed">
                    Dashboard
                </span>

            </RouterLink>
        </li>

        <li class="nav-item">
            <RouterLink
                to="/company/jobs/create"
                class="nav-link"
            >
                <i class="bi bi-plus-circle"></i>

                <span v-if="!collapsed">
                    Post Job
                </span>

            </RouterLink>
        </li>

        <li class="nav-item">
            <RouterLink
                to="/company/jobs"
                class="nav-link"
            >
                <i class="bi bi-briefcase"></i>

                <span v-if="!collapsed">
                    Manage Jobs
                </span>

            </RouterLink>
        </li>

        <li class="nav-item">
            <RouterLink
                to="/company/applications"
                class="nav-link"
            >
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

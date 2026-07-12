<template>

<div class="d-flex">

    <CompanySidebar
        :collapsed="collapsed"
        @toggle="collapsed=!collapsed"
    />

    <div class="flex-grow-1">

        <TopNavbar/>

        <div class="p-4">

            <slot/>

        </div>

    </div>

</div>

</template>

<script setup>

import { ref } from "vue";
import CompanySidebar from "@/components/layout/CompanySidebar.vue";
import TopNavbar from "@/components/layout/TopNavbar.vue";

const collapsed = ref(false);

</script>

<style scoped>


@import "@/assets/css/dashboard.css";

</style>
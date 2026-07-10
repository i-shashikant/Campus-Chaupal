<template>

<div class="card auth-card p-5">

    <h2 class="fw-bold">
        Create Account
    </h2>

    <p class="text-muted mb-4">
        Join CampusChaupal
    </p>

    <div class="btn-group w-100 mb-4">

        <button
            class="btn"
            :class="registerStore.role=='student'
                ? 'btn-primary'
                : 'btn-outline-primary'"
        >
            Student
        </button>

        <button
            class="btn"
            :class="registerStore.role=='company'
                ? 'btn-primary'
                : 'btn-outline-primary'"
        >
            Company
        </button>

    </div>

    <StudentRegisterForm
    v-if="registerStore.role === 'student'"
    />

    <CompanyRegisterForm
        v-else
    />

</div>

</template>

<script setup>

import { useRegisterStore } from "@/stores/register";

import StudentRegisterForm from "./StudentRegisterForm.vue";
import CompanyRegisterForm from "./CompanyRegisterForm.vue";

const registerStore = useRegisterStore();


const registerStore = useRegisterStore();
</script>

<style scoped>

.auth-card{

    width:550px;

    border:none;

    border-radius:20px;

    background:rgba(255,255,255,.65);

    backdrop-filter:blur(20px);

}

</style>
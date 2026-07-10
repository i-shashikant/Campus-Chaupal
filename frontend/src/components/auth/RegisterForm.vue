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
            :class="role=='student'
                ? 'btn-primary'
                : 'btn-outline-primary'"
            @click="role='student'"
        >
            Student
        </button>

        <button
            class="btn"
            :class="role=='company'
                ? 'btn-primary'
                : 'btn-outline-primary'"
            @click="role='company'"
        >
            Company
        </button>

    </div>

    <RegisterStepper
        :role="role"
    />

</div>

</template>

<script setup>
import { ref } from "vue";
import RegisterStepper from "./RegisterStepper.vue";

const role = ref("student");
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
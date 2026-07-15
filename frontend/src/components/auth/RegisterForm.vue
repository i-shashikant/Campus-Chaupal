<template>
    <div class="auth-card">

        <div class="mobile-brand d-md-none">
            <i class="bi bi-mortarboard-fill"></i>
            <span>CampusChaupal</span>
        </div>

        <h2 class="auth-title">Create Account</h2>
        <p class="auth-sub">Join CampusChaupal</p>

        <div class="role-toggle mb-4">
            <button
                type="button"
                class="role-btn"
                :class="{ active: registerStore.role === 'student' }"
                @click="registerStore.role = 'student'"
            >
                Student
            </button>
            <button
                type="button"
                class="role-btn"
                :class="{ active: registerStore.role === 'company' }"
                @click="registerStore.role = 'company'"
            >
                Company
            </button>
        </div>

        <StudentRegisterForm v-if="registerStore.role === 'student'" />
        <CompanyRegisterForm v-else />

        <p class="auth-switch">
            Already have an account? <RouterLink to="/login">Login here</RouterLink>
        </p>

    </div>
</template>

<script setup>
import { useRegisterStore } from "@/stores/register";

import StudentRegisterForm from "./StudentRegisterForm.vue";
import CompanyRegisterForm from "./CompanyRegisterForm.vue";

const registerStore = useRegisterStore();
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=JetBrains+Mono:wght@500&display=swap');

.auth-card {
    --ink: #1b2a4a;
    --slate: #5b6478;
    --brass: #c89b3c;
    --paper: #fbfaf7;
    --line: #e4e1d8;

    width: 550px;
    max-width: 100%;
    background: #fff;
    border: 1px solid var(--line);
    border-radius: 1.25rem;
    padding: 3rem;
    box-shadow: 0 15px 40px rgba(27, 42, 74, 0.06);
}

.mobile-brand {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    color: var(--ink);
    font-family: "Fraunces", serif;
    font-weight: 600;
    font-size: 1.15rem;
    margin-bottom: 1.5rem;
}

.mobile-brand i {
    color: var(--brass);
    font-size: 1.4rem;
}

.auth-title {
    font-family: "Fraunces", serif;
    font-weight: 600;
    color: var(--ink);
    margin-bottom: 0.25rem;
}

.auth-sub {
    color: var(--slate);
    margin-bottom: 2rem;
}

.role-toggle {
    display: flex;
    gap: 0.4rem;
    background: var(--paper);
    border: 1px solid var(--line);
    border-radius: 0.7rem;
    padding: 0.3rem;
}

.role-btn {
    flex: 1;
    border: none;
    background: transparent;
    padding: 0.6rem 0;
    border-radius: 0.5rem;
    font-weight: 500;
    color: var(--slate);
    cursor: pointer;
}

.role-btn.active {
    background: var(--ink);
    color: #fff;
}

.auth-switch {
    text-align: center;
    margin-top: 1.5rem;
    color: var(--slate);
    font-size: 0.9rem;
}

.auth-switch a {
    color: var(--brass);
    font-weight: 500;
    text-decoration: none;
}
</style>
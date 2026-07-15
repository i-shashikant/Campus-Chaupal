<template>
    <form @submit.prevent="registerStudent" class="sub-form">
        <h5 class="section-label">Account Information</h5>

        <div class="row">
            <div class="col-md-6 mb-3">
                <label class="form-label">Email</label>
                <input v-model="registerStore.student.email" class="form-control" type="email">
            </div>

            <div class="col-md-6 mb-3">
                <label class="form-label">Password</label>
                <input v-model="registerStore.student.password" class="form-control" type="password">
            </div>
        </div>

        <div class="mb-3">
            <label class="form-label">Confirm Password</label>
            <input type="password" class="form-control" v-model="confirmPassword">
        </div>

        <button class="btn-ledger btn-ledger-navy w-100" type="submit">Register as Student</button>
    </form>
</template>

<script setup>
import { ref } from "vue";
const confirmPassword = ref("");

import { useRegisterStore } from "@/stores/register";

const registerStore = useRegisterStore();

import authService from "@/services/authService";
import { useRouter } from "vue-router";

const router = useRouter();
const registerStudent = async () => {

    if (registerStore.student.password !== confirmPassword.value) {
        alert("Passwords do not match.");
        return;
    }

    try {
        await authService.registerStudent(registerStore.student);

        alert("Registration Successful!");

        registerStore.reset();

        router.push("/login");

    } catch (error) {
        console.error(error);

        alert(
            error.response?.data?.message ||
            "Registration Failed"
        );
    }
};
</script>

<style scoped>
.sub-form {
    --ink: #1b2a4a;
    --slate: #5b6478;
    --line: #e4e1d8;

    max-height: 60vh;
    overflow-y: auto;
    padding-right: 6px;
}

.section-label {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--slate);
    margin-bottom: 1rem;
}

.form-label {
    font-size: 0.85rem;
    color: var(--slate);
}

.form-control {
    border-radius: 0.6rem;
    border: 1px solid var(--line);
}

.form-control:focus {
    border-color: #c89b3c;
    box-shadow: 0 0 0 3px rgba(200, 155, 60, 0.15);
}

.btn-ledger {
    height: 48px;
    border-radius: 0.7rem;
    border: none;
    font-weight: 500;
    cursor: pointer;
}

.btn-ledger-navy {
    background: var(--ink);
    color: #fff;
}
</style>
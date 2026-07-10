<template>
<form>
    <h5 class="mb-3">Account Information</h5>
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

        <label class="form-label">
            Confirm Password
        </label>

        <input
            type="password"
            class="form-control"
            v-model="confirmPassword"
        />

    </div>
    <button class="btn btn-primary w-100" type="submit"> Register as Student </button>

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

    try {

        await authService.registerStudent(
            registerStore.student
        );

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

form {
    max-height: 60vh;
    overflow-y: auto;
    padding-right: 6px;
}


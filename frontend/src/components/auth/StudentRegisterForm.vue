<template>

<form>

    <div class="row">

        <div class="col-md-6 mb-3">

            <label>Email</label>

            <input
                v-model="registerStore.student.email"
                class="form-control"
                type="email"
            >

        </div>

        <div class="col-md-6 mb-3">

            <label>Password</label>

            <input
                v-model="registerStore.student.password"
                class="form-control"
                type="password"
            >

        </div>

    </div>

</form>

</template>

<script setup>
import { useRegisterStore } from "@/stores/register";

const registerStore = useRegisterStore();
</script>
<template>

<form>

    <div class="row">

        <div class="col-md-6 mb-3">

            <label>Company Email</label>

            <input
                v-model="registerStore.company.email"
                class="form-control"
            >

        </div>

        <div class="col-md-6 mb-3">

            <label>Password</label>

            <input
                type="password"
                v-model="registerStore.company.password"
                class="form-control"
            >

        </div>

    </div>

</form>

</template>

<script setup>
import { useRegisterStore } from "@/stores/register";

const registerStore = useRegisterStore();
</script>
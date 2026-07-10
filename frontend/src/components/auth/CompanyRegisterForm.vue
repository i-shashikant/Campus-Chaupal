<!-- <template>

<form>

    <h5 class="mb-3">Account Information</h5>

    <div class="row">
        <div class="col-md-6 mb-3">
            <label class="form-label">Email</label>
            <input
                type="email"
                class="form-control"
                v-model="registerStore.company.email"
            />
        </div>

        <div class="col-md-6 mb-3">
            <label class="form-label">Password</label>
            <input
                type="password"
                class="form-control"
                v-model="registerStore.company.password"
            />
        </div>
    </div>

    <h5 class="mb-3 mt-4">Company Information</h5>

    <div class="row">

        <div class="col-md-6 mb-3">

            <label class="form-label">Company Name</label>

            <input
                class="form-control"
                v-model="registerStore.company.company_name"
            />

        </div>

        <div class="col-md-6 mb-3">

            <label class="form-label">Industry</label>

            <select
                class="form-select"
                v-model="registerStore.company.industry"
            >

                <option value="">Select Industry</option>

                <option>Information Technology</option>
                <option>Finance</option>
                <option>Healthcare</option>
                <option>Education</option>
                <option>Manufacturing</option>
                <option>Consulting</option>
                <option>Telecommunications</option>
                <option>Retail</option>
                <option>Other</option>

            </select>

        </div>

    </div>

    <div class="row">

        <div class="col-md-6 mb-3">

            <label class="form-label">Website</label>

            <input
                type="url"
                class="form-control"
                placeholder="https://example.com"
                v-model="registerStore.company.website"
            />

        </div>

        <div class="col-md-6 mb-3">

            <label class="form-label">Phone</label>

            <input
                class="form-control"
                v-model="registerStore.company.phone"
            />

        </div>

    </div>

    <h5 class="mb-3 mt-4">HR Contact</h5>

    <div class="row">

        <div class="col-md-6 mb-3">

            <label class="form-label">HR Name</label>

            <input
                class="form-control"
                v-model="registerStore.company.hr_name"
            />

        </div>

        <div class="col-md-6 mb-3">

            <label class="form-label">HR Email</label>

            <input
                type="email"
                class="form-control"
                v-model="registerStore.company.hr_email"
            />

        </div>

    </div>

    <h5 class="mb-3 mt-4">Company Description</h5>

    <div class="mb-3">

        <textarea
            rows="4"
            class="form-control"
            placeholder="Tell students about your company..."
            v-model="registerStore.company.description"
        ></textarea>

    </div>
    <button class="btn btn-primary w-100 mt-3" type="submit">Register as Company</button>
    

</form>

</template> -->

<template>
<form>
    <h5 class="mb-3">Account Information</h5>
    <div class="row">
        <div class="col-md-6 mb-3">
            <label class="form-label">Email</label>
            <input
                type="email"
                class="form-control"
                v-model="registerStore.company.email"
            />
        </div>

        <div class="col-md-6 mb-3">
            <label class="form-label">Password</label>
            <input
                type="password"
                class="form-control"
                v-model="registerStore.company.password"
            />
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
    <button class="btn btn-primary w-100 mt-3" type="submit">Register as Company</button>


</form>
</template>

<script setup>
import { ref } from "vue";

const confirmPassword = ref("");

import { useRegisterStore } from "@/stores/register";

const registerStore = useRegisterStore();
</script>
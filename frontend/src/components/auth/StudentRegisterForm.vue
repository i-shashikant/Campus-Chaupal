<template>

<form>

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

    <div class="row">

        <div class="col-md-6 mb-3">
            <label class="form-label">Full Name</label>
            <input v-model="registerStore.student.full_name" class="form-control">
        </div>

        <div class="col-md-6 mb-3">
            <label class="form-label">Roll Number</label>
            <input v-model="registerStore.student.roll_number" class="form-control">
        </div>
    </div>

    <div class="row">

        <div class="col-md-6 mb-3">
            <label class="form-label">Branch</label>
            <select v-model="registerStore.student.branch" class="form-select">

                <option value="">Select Branch</option>
                <option>CSE</option> 
                <option>IT</option> 
                <option>ECE</option> 
                <option>EEE</option> 
                <option>Mechanical</option> 
                <option>Civil</option> 
                <option>Biotechnology</option> 
            </select>
        </div>

        <div class="col-md-6 mb-3">
            <label class="form-label">Year</label>
            <select v-model="registerStore.student.year" class="form-select">

                <option value="">Select Year</option>
                <option>1</option> 
                <option>2</option> 
                <option>3</option> 
                <option>4</option> 
            </select>
        </div>
    </div>

    <div class="row">

        <div class="col-md-6 mb-3">
            <label class="form-label">CGPA</label>
            <input type="number" step="0.01" min="0" max="10" class="form-control" v-model="registerStore.student.cgpa"/>
        </div>

        <div class="col-md-6 mb-3">
            <label class="form-label">Graduation Year</label>
            <input type="number" class="form-control" v-model="registerStore.student.graduation_year"/>
        </div>

    </div>

    <div class="row">

        <div class="col-md-6 mb-3">
            <label class="form-label">Gender</label>
            <select class="form-select" v-model="registerStore.student.gender" >

                <option value="">Select</option>
                <option>Male</option>
                <option>Female</option>
                <option>Other</option>

            </select>
        </div>

        <div class="col-md-6 mb-3">
            <label class="form-label">Phone</label>
            <input class="form-control" v-model="registerStore.student.phone" />
        </div>

    </div>
        
    <div class="mb-3">

        <label class="form-label">
            Address
        </label>

        <textarea rows="3" class="form-control" v-model="registerStore.student.address"></textarea>
    </div>

    <button class="btn btn-primary w-100" type="submit"> Register as Student </button>

</form>

</template>

<script setup>
import { useRegisterStore } from "@/stores/register";

const registerStore = useRegisterStore();
</script>

form {
    max-height: 60vh;
    overflow-y: auto;
    padding-right: 6px;
}
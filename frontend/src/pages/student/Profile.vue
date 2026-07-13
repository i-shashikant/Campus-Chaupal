<template>

<DashboardLayout>

<div class="container-fluid">

    <h2 class="fw-bold mb-4">

        My Profile

    </h2>

    <div class="card border-0 shadow-sm rounded-4 mb-4">

        <div class="card-body">

            <div class="row align-items-center">

                <div class="col-md-2 text-center">

                    <img
                        src="https://ui-avatars.com/api/?name=Student"
                        class="rounded-circle shadow"
                        width="120"
                        height="120"
                    >

                </div>

                <div class="col-md-7">

                    <h3 class="fw-bold mb-1">
                        {{ profileStore.profile.full_name || "Student Name" }}
                    </h3>

                    <p class="text-muted mb-1">
                        {{ profileStore.profile.branch || "Branch" }}
                    </p>

                    <span class="badge bg-primary me-2">
                        CGPA {{ profileStore.profile.cgpa || "--" }}
                    </span>

                    <span class="badge bg-success">
                        {{ profileStore.profile.year || "--" }} Year
                    </span>

                </div>

                <div class="col-md-3 text-end">

                    <button class="btn btn-primary rounded-pill">

                        <i class="bi bi-pencil-square me-2"></i>

                        Edit Profile

                    </button>

                </div>

            </div>

        </div>

    </div>

    <div class="card profile-card mb-4">
        <div class="row g-4">
            <div class="col-lg-6">

                <div class="profile-header">
                    <i class="bi bi-person-circle me-2"></i>
                    Personal Information
                </div>

                <div class="profile-body">
                    <div class="row">
                        <div class="col-md-3 text-center mb-4">
                            <img src="https://ui-avatars.com/api/?name=Student" class="rounded-circle img-thumbnail mb-3" width="140" height="140">
                            <label class="btn btn-outline-primary btn-sm">Upload Photo <input type="file" hidden></label>
                        </div>

                        <div class="col-md-9">
                            <div class="row">

                                <div class="col-md-6 mb-3">
                                    <label class="form-label"> Full Name </label>
                                    <input class="form-control" v-model="profileStore.profile.full_name">
                                </div>

                                <div class="col-md-6 mb-3">
                                    <label class="form-label"> Gender </label>

                                    <select class="form-select" v-model="profileStore.profile.gender">
                                        <option>Male</option>
                                        <option>Female</option>
                                        <option>Other</option>
                                    </select>
                                </div>
                            </div>

                            <div class="row">
                                <div class="col-md-6 mb-3">

                                    <label class="form-label"> Phone </label>
                                    <input class="form-control" v-model="profileStore.profile.phone">

                                </div>

                                <div class="col-md-6 mb-3">
                                    <label class="form-label"> Email </label>

                                    <input class="form-control" disabled>

                                </div>

                            </div>

                            <div class="mb-3">
                                <label class="form-label"> Address </label>

                                <textarea rows="3" class="form-control" v-model="profileStore.profile.address"></textarea>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        
            <div class="col-lg-6">

                <div class="card profile-card mb-4">

                    <div class="profile-header">
                        <i class="bi bi-mortarboard me-2"></i>
                        Academic Information
                    </div>

                    <div class="profile-body">

                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label class="form-label">Roll Number</label>
                                <input v-model="profileStore.profile.roll_number" class="form-control">
                            </div>
                        </div>

                        <div class="row">

                            <div class="col-md-6 mb-3">
                                <label class="form-label">Branch</label>
                                <select v-model="profileStore.profile.branch" class="form-select">
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
                                <select v-model="profileStore.profile.year" class="form-select">

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
                                <input type="number" step="0.01" min="0" max="10" class="form-control" v-model="profileStore.profile.cgpa"/>
                            </div>

                            <div class="col-md-6 mb-3">
                                <label class="form-label">Graduation Year</label>
                                <input type="number" class="form-control" v-model="profileStore.profile.graduation_year"/>
                            </div>

                        </div>
                        
                    </div>    
                </div>
            </div>
        </div>
    </div>        

    <!-- Professional -->

    <div class="card profile-sm">

        <div class="profile-header"> 
            <i class="bi bi-briefcase me-2"></i>
            Professional Information 
        </div>

        <div class="profile-body">

            <div class="row">
                <div class="col-md-6 mb-3"> 
                    <label class="form-label">Skills</label>
                    <textarea rows="3" class="form-control" v-model="profileStore.profile.skills"></textarea>
                </div>

                <div class="col-md-6 mb-3"> 
                    <label class="form-label">Github URL</label>
                    <input type="text" class="form-control" v-model="profileStore.profile.github">
                </div>

                <div class="col-md-6 mb-3"> 
                    <label class="form-label">LinkedIn URL</label>
                    <input type="text" class="form-control" v-model="profileStore.profile.linkedin">
                </div>

                <div class="col-md-6 mb-3"> 
                    <label class="form-label">Portfolio URL</label>
                    <input type="text" class="form-control" v-model="profileStore.profile.portfolio">
                </div>

                <div class="border rounded-3 p-4 text-center">

                    <i class="bi bi-file-earmark-pdf fs-1 text-danger"></i>
                    <h6 class="mt-2">

                        Resume

                    </h6>
                    <input
                        type="file"
                        class="form-control mt-3"
                    >
                </div>
            
            </div>
        </div>             

    </div>

    <div class="text-end mt-4">

        <button class="btn btn-primary btn-lg px-5 rounded pill" @click="profileStore.saveProfile()">
             <i class="bi bi-check-circle me-2"></i>

                Save Changes
        </button>

    </div>

</div>

</DashboardLayout>

</template>

<script setup>

import DashboardLayout from "@/layouts/DashboardLayout.vue";


import { onMounted } from "vue";
import { useStudentProfileStore } from "@/stores/studentProfile";
const profileStore = useStudentProfileStore();


onMounted(() => {

    profileStore.loadProfile();

});

</script>

<style scoped>
@import "@/assets/css/profile.css";


</style>
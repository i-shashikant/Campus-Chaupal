<template>

<DashboardLayout>

<div class="container-fluid">

    <h2 class="fw-bold mb-4">

        My Profile

    </h2>


    <div class="card profile-card mb-4">

        <div class="profile-header">Personal Information</div>

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
                            <input class="form-control">
                        </div>

                        <div class="col-md-6 mb-3">
                            <label class="form-label"> Gender </label>

                            <select class="form-select">
                                <option>Male</option>
                                <option>Female</option>
                                <option>Other</option>
                            </select>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-md-6 mb-3">

                            <label class="form-label"> Phone </label>
                            <input class="form-control">

                        </div>

                        <div class="col-md-6 mb-3">
                            <label class="form-label"> Email </label>

                            <input class="form-control" disabled>

                        </div>

                    </div>

                    <div class="mb-3">
                        <label class="form-label"> Address </label>

                        <textarea rows="3" class="form-control"></textarea>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="card profile-card mb-4">

        <div class="profile-header">Academic Information</div>

        <div class="profile-body">

            <div class="card profile-sm mb-4">

                <div class="profile-header">
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label class="form-label">Roll Number</label>
                            <input v-model="registerStore.student.roll_number" class="form-control">
                        </div>
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
            </div>
        </div>    

    </div>

    <!-- Professional -->

    <div class="card profile-sm">

        <div class="profile-header"> Professional Information </div>

        <div class="profile-body">

            <div class="row">
                <div class="col-md-6 mb-3"> 
                    <label class="form-label">Skills</label>
                    <textarea rows="3" class="form-control"></textarea>
                </div>

                <div class="col-md-6 mb-3"> 
                    <label class="form-label">Github URL</label>
                    <input type="text" class="form-control" v-model="registerStore.student.github">
                </div>

                <div class="col-md-6 mb-3"> 
                    <label class="form-label">LinkedIn URL</label>
                    <input type="text" class="form-control" v-model="registerStore.student.linkedin">
                </div>

                <div class="col-md-6 mb-3"> 
                    <label class="form-label">Portfolio URL</label>
                    <input type="text" class="form-control" v-model="registerStore.student.portfolio">
                </div>

                <div class="col-md-6 mb-3"> 
                    <label class="form-label">Resume</label>
                    <input type="file" class="form-control" v-model="registerStore.student.resume">
                </div>
            
            </div>
        </div>             

    </div>

    <div class="text-end mt-4">

        <button class="btn btn-primary px-5">

            Save Changes

        </button>

    </div>

</div>

</DashboardLayout>

</template>

<script setup>

import DashboardLayout from "@/layouts/DashboardLayout.vue";

</script>

<style scoped>
@import "@/assets/css/profile.css";


</style>
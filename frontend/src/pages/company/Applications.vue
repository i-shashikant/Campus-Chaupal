<template>

<DashboardLayout>

<div class="container-fluid">

<h2 class="fw-bold mb-4">

Received Applications

</h2>

<table class="table">

<thead>

<tr>

<th>Student</th>
<th>Job</th>
<th>Status</th>

</tr>

</thead>

<tbody>

<tr
v-for="app in store.applications"
:key="app.id"
>

<td>{{app.student}}</td>
<td>{{app.job}}</td>
<td><select
    class="form-select form-select-sm"
    :value="application.status"
    @change="updateStatus(application.id, $event.target.value)"
>
    <option>Applied</option>
    <option>Shortlisted</option>
    <option>Selected</option>
    <option>Rejected</option>
</select></td>

</tr>

</tbody>

</table>

</div>

</DashboardLayout>

</template>

<script setup>

import { onMounted } from "vue";

import DashboardLayout from "@/layouts/DashboardLayout.vue";

import { useApplicationStore } from "@/stores/application";

const store = useApplicationStore();

onMounted(()=>{

store.loadCompanyApplications();
async function updateStatus(id, status) {

    await applicationStore.updateStatus(id, status);

    await applicationStore.loadCompanyApplications();

}

});

</script>
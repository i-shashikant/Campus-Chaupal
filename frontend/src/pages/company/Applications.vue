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
<td>{{app.status}}</td>

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

});

</script>
<template>

<DashboardLayout>

<div class="container-fluid">

<h2 class="fw-bold mb-4">

My Applications

</h2>

<table class="table">

<thead>

<tr>

<th>Company</th>
<th>Job</th>
<th>Status</th>
<th>Date</th>

</tr>

</thead>

<tbody>

<tr
v-for="app in store.applications"
:key="app.id"
>

<td>{{app.company}}</td>
<td>{{app.title}}</td>
<td>{{app.status}}</td>
<td>{{app.applied_at}}</td>

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

store.loadStudentApplications();

});

</script>
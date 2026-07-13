<template>

<DashboardLayout>

<div class="container-fluid">

<h2 class="fw-bold mb-4">

Applications

</h2>

<div class="card shadow-sm">

<div class="card-body">

<table class="table">

<thead>

<tr>

<th>Student</th>

<th>Company</th>

<th>Job</th>

<th>Status</th>

<th>Applied On</th>

</tr>

</thead>

<tbody>

<tr
v-for="application in admin.applications"
:key="application.id"
>

<td>

{{ application.student }}

</td>

<td>

{{ application.company }}

</td>

<td>

{{ application.job }}

</td>

<td>

<span class="badge bg-info">

{{ application.status }}

</span>

</td>

<td>

{{ application.applied_at }}

</td>

</tr>

</tbody>

</table>

</div>

</div>

</div>

</DashboardLayout>

</template>

<script setup>

import { onMounted } from "vue";

import DashboardLayout from "@/layouts/DashboardLayout.vue";

import { useAdminStore } from "@/stores/admin";

const admin = useAdminStore();

onMounted(() => {

admin.loadApplications();

});

</script>
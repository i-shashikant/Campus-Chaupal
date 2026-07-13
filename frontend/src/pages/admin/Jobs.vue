<template>

<DashboardLayout>

<div class="container-fluid">

<h2 class="fw-bold mb-4">

Jobs

</h2>

<div class="card shadow-sm">

<div class="card-body">

<table class="table">

<thead>

<tr>

<th>Title</th>

<th>Company</th>

<th>Location</th>

<th>Deadline</th>

<th>Applications</th>

<th>Status</th>

</tr>

</thead>

<tbody>

<tr
v-for="job in admin.jobs"
:key="job.id"
>

<td>{{ job.title }}</td>

<td>{{ job.company }}</td>

<td>{{ job.location }}</td>

<td>{{ job.deadline }}</td>

<td>{{ job.applications }}</td>

<td>

<span
class="badge"
:class="job.active ? 'bg-success' : 'bg-secondary'"
>

{{ job.active ? "Active" : "Closed" }}

</span>

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

admin.loadJobs();

});

</script>
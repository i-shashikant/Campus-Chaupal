<template>

<div class="card shadow-sm border-0 rounded-4 h-100">

<div class="card-body">

<h5 class="fw-bold mb-3">

Professional Profile

</h5>

<div class="info-row">
    <strong>Resume</strong>

    <span
        class="badge bg-success"
        v-if="student.resume"
    >
        Uploaded
    </span>

    <span v-else>-</span>
</div>

<div class="info-row">
    <strong>Skills</strong>
    <span>{{ student.skills || "-" }}</span>
</div>

<div class="info-row">
    <strong><i class="bi bi-github me-2"></i>GitHub</strong>
    <span>{{ student.github || "-" }}</span>
</div>

<div class="info-row">
    <strong><i class="bi bi-linkedin me-2"></i>LinkedIn</strong>
    <span>{{ student.linkedin || "-" }}</span>
</div>

<div class="info-row">
    <strong>Portfolio</strong>
    <span>{{ student.portfolio || "-" }}</span>
</div>

</div>

</div>

</template>

<script setup>

defineProps({

student:Object

})

</script>
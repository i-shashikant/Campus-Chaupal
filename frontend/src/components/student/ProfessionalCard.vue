<template>

<div class="card shadow-sm border-0 rounded-4 h-100">

<div class="card-body">

<h5 class="fw-bold mb-3">

Professional Profile

</h5>

<p>

Resume

<span class="badge bg-success float-end">

Uploaded

</span>

</p>

<p>

Projects

<span class="float-end">

{{ student.projects }}

</span>

</p>

<p>

Experience

<span class="float-end">

{{ student.experience }}

</span>

</p>

<p>

Certifications

<span class="float-end">

{{ student.certifications }}

</span>

</p>

</div>

</div>

</template>

<script setup>

defineProps({

student:Object

})

</script>
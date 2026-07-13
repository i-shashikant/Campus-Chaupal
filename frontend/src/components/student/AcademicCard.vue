<template>

<div class="card shadow-sm border-0 rounded-4 h-100">

<div class="card-body">

<h5 class="fw-bold mb-3">

Academic Details

</h5>

<p><strong>Degree:</strong> {{ student.degree }}</p>

<p><strong>Branch:</strong> {{ student.branch }}</p>

<p><strong>CGPA:</strong> {{ student.cgpa }}</p>

<p><strong>Graduation:</strong> {{ student.graduation_year }}</p>

</div>

</div>

</template>

<script setup>

defineProps({

student:Object

})

</script>
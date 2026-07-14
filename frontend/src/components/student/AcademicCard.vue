<template>

    <div class="card shadow-sm border-0 rounded-4 h-100">

        <div class="card-body">

            <h5 class="fw-bold mb-3">

            Academic Details

            </h5>

            <div class="info-row">
                <strong>Roll Number</strong>
                <span>{{ student.roll_number || "-" }}</span>
            </div>

            <div class="info-row">
                <strong>Branch</strong>
                <span>{{ student.branch || "-" }}</span>
            </div>

            <div class="info-row">
                <strong>Current Year</strong>
                <span>{{ student.year || "-" }}</span>
            </div>

            <div class="info-row">
                <strong>CGPA</strong>
                <span>{{ student.cgpa || "-" }}</span>
            </div>

            <div class="info-row">
                <strong>Graduation Year</strong>
                <span>{{ student.graduation_year || "-" }}</span>
            </div>

        </div>

    </div>

</template>

<script setup>

defineProps({

student:Object

})

</script>
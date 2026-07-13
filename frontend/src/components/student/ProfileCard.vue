<template>
    <div class="card shadow-sm border-0 rounded-4 h-100">

        <div class="card-body text-center">

            <img
                :src="student.avatar || 'https://ui-avatars.com/api/?name=' + student.full_name"
                class="rounded-circle mb-3"
                width="90"
                height="90"
            >

            <h5 class="fw-bold mb-1">
                {{ student.full_name }}
            </h5>

            <p class="text-muted mb-3">
                {{ student.degree }}
            </p>

            <div class="row text-center">

                <div class="col">
                    <h6 class="fw-bold mb-0">
                        {{ student.cgpa }}
                    </h6>
                    <small class="text-muted">CGPA</small>
                </div>

                <div class="col">
                    <h6 class="fw-bold mb-0">
                        {{ student.skills }}
                    </h6>
                    <small class="text-muted">Skills</small>
                </div>

            </div>

        </div>

    </div>
</template>

<script setup>

defineProps({
    student: Object
})

</script>
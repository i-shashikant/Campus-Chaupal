<template>

<div class="card shadow-sm border-0 rounded-4 h-100">

    <div class="card-body">

        <h5 class="fw-bold">
            Profile Completion
        </h5>

        <div class="progress my-3" style="height:12px">

            <div
                class="progress-bar"
                :style="{width: completion+'%'}"
            >
                {{ completion }}%
            </div>

        </div>

        <small class="text-muted">

            Complete your profile to increase visibility.

        </small>

    </div>

</div>

</template>

<script setup>

defineProps({

    completion:Number

})

</script>
<template>

<div class="card shadow-sm border-0 rounded-4 h-100">

    <div class="card-body">

        <h5 class="fw-bold">
            Profile Completion
        </h5>

       <div class="progress profile-progress">

            <div
                class="progress-bar"
                role="progressbar"
                :style="{ width: completion + '%' }"
            >
            </div>

        </div>

        <div class="completion-text">

            {{ completion }}% Complete

        </div>

        <p class="text-muted mt-3">

            <span v-if="completion === 100">
                Your profile is complete. You're ready to apply.
            </span>

            <span v-else>
                Complete your profile to increase visibility.
            </span>

        </p>


    </div>

</div>

</template>

<script setup>

defineProps({

    completion:Number

})

</script>
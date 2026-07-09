<style scoped>
@import "@/assets/css/auth.css";
</style>

<template>

<div class="container-fluid auth-wrapper">

    <div class="row min-vh-100">

        <div class="col-lg-6 d-none d-lg-flex auth-left">

            <AuthHero />

        </div>

        <div class="col-lg-6 d-flex align-items-center justify-content-center">

            <slot />

        </div>

    </div>

</div>

</template>

<script setup>
import AuthHero from "@/components/auth/AuthHero.vue";
</script>
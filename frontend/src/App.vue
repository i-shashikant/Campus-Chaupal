<template>
    <AppToast />
    <router-view :key="$route.fullPath" />
</template>

<script setup>
import AppToast from './components/AppToast.vue';

</script>
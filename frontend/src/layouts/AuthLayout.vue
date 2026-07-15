<template>
    <div class="auth-shell">
        <div class="auth-hero-panel">
            <AuthHero />
        </div>
        <div class="auth-form-panel">
            <div class="auth-form-wrap">
                <slot />
            </div>
        </div>
    </div>
</template>

<script setup>
import AuthHero from "@/components/auth/AuthHero.vue";
</script>

<style scoped>
.auth-shell {
    min-height: 100vh;
    display: flex;
}

.auth-hero-panel {
    flex: 0 0 42%;
    background: linear-gradient(135deg, #1b2a4a 0%, #2e3e63 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 3rem;
}

.auth-form-panel {
    flex: 1;
    background: #fbfaf7;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2rem;
}

.auth-form-wrap {
    width: 100%;
    display: flex;
    justify-content: center;
}

@media (max-width: 900px) {
    .auth-hero-panel {
        display: none;
    }

    .auth-form-panel {
        flex: 1;
    }
}
</style>
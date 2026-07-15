<template>
    <div class="auth-card">

        <div class="mobile-brand d-md-none">
            <i class="bi bi-mortarboard-fill"></i>
            <span>CampusChaupal</span>
        </div>

        <h2 class="auth-title">Welcome Back</h2>
        <p class="auth-sub">Login to your CampusChaupal account</p>

        <form @submit.prevent="handleLogin">

            <div class="mb-3">
                <label class="form-label">Email</label>
                <input v-model="form.email" type="email" class="form-control" placeholder="Enter email">
            </div>

            <div class="mb-3">
                <label class="form-label">Password</label>
                <input v-model="form.password" type="password" class="form-control" placeholder="Password">
            </div>

            <div class="d-flex justify-content-between mb-4">
                <div class="form-check">
                    <input class="form-check-input" type="checkbox">
                    <label class="form-check-label">Remember Me</label>
                </div>
                <a href="#" class="forgot-link">Forgot Password?</a>
            </div>

            <div v-if="authStore.error" class="auth-alert">
                {{ authStore.error }}
            </div>

            <button class="btn-ledger btn-ledger-navy w-100" :disabled="authStore.loading">
                {{ authStore.loading ? "Signing In..." : "Login" }}
            </button>

            <p class="auth-switch">
                Don't have an account? <RouterLink to="/register">Register here</RouterLink>
            </p>

        </form>

    </div>
</template>

<script setup>
import { reactive } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";

const router = useRouter();
const authStore = useAuthStore();

const form = reactive({
    email: "",
    password: "",
});

const handleLogin = async () => {
    try {
        const response = await authStore.login(form);

        switch (response.user.role) {
            case "student":
                router.push("/student/dashboard");
                break;

            case "company":
                router.push("/company/dashboard");
                break;

            case "admin":
                router.push("/admin/dashboard");
                break;

            default:
                router.push("/");
        }
    } catch (error) {
        console.error(error);
    }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=JetBrains+Mono:wght@500&display=swap');

.auth-card {
    --ink: #1b2a4a;
    --slate: #5b6478;
    --brass: #c89b3c;
    --crimson: #b4442e;
    --line: #e4e1d8;

    width: 430px;
    max-width: 100%;
    background: #fff;
    border: 1px solid var(--line);
    border-radius: 1.25rem;
    padding: 3rem;
    box-shadow: 0 15px 40px rgba(27, 42, 74, 0.06);
}

.mobile-brand {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    color: var(--ink);
    font-family: "Fraunces", serif;
    font-weight: 600;
    font-size: 1.15rem;
    margin-bottom: 1.5rem;
}

.mobile-brand i {
    color: var(--brass);
    font-size: 1.4rem;
}

.auth-title {
    font-family: "Fraunces", serif;
    font-weight: 600;
    color: var(--ink);
    margin-bottom: 0.25rem;
}

.auth-sub {
    color: var(--slate);
    margin-bottom: 2rem;
}

.form-label {
    font-size: 0.85rem;
    color: var(--slate);
}

.form-control {
    height: 48px;
    border-radius: 0.7rem;
    border: 1px solid var(--line);
}

.form-control:focus {
    border-color: var(--brass);
    box-shadow: 0 0 0 3px rgba(200, 155, 60, 0.15);
}

.forgot-link {
    color: var(--brass);
    text-decoration: none;
    font-size: 0.88rem;
}

.auth-alert {
    background: #fbe9e5;
    color: var(--crimson);
    border-radius: 0.6rem;
    padding: 0.7rem 1rem;
    font-size: 0.88rem;
    margin-bottom: 1.25rem;
}

.btn-ledger {
    height: 48px;
    border-radius: 0.7rem;
    border: none;
    font-weight: 500;
    cursor: pointer;
}

.btn-ledger:disabled {
    opacity: 0.7;
    cursor: not-allowed;
}

.btn-ledger-navy {
    background: var(--ink);
    color: #fff;
}

.auth-switch {
    text-align: center;
    margin-top: 1.5rem;
    color: var(--slate);
    font-size: 0.9rem;
}

.auth-switch a {
    color: var(--brass);
    font-weight: 500;
    text-decoration: none;
}
</style>
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

<template>

<div class="card auth-card p-5">

    <h2 class="fw-bold mb-2">
        Welcome Back
    </h2>

    <p class="text-muted mb-4">
        Login to your CampusChaupal account
    </p>

    <form>

        <div class="mb-3">

            <label>Email</label>

            <input
                v-model="form.email"
                type="email"
                class="form-control"
                placeholder="Enter email"
            >

        </div>

        <div class="mb-3">

            <label>Password</label>

            <input
                v-model="form.password"
                type="password"
                class="form-control"
                placeholder="Password"
            >

        </div>

        <div class="d-flex justify-content-between mb-4">

            <div class="form-check">

                <input
                    class="form-check-input"
                    type="checkbox"
                >

                <label class="form-check-label">

                    Remember Me

                </label>

            </div>

            <a href="#">

                Forgot Password?

            </a>

        </div>
        <div
            v-if="authStore.error"
            class="alert alert-danger"
        >
            {{ authStore.error }}
        </div>

        <button
            class="btn btn-primary w-100"
            :disabled="authStore.loading"
        >
            {{ authStore.loading ? "Signing In..." : "Login" }}
        </button>

    </form>

</div>

</template>

<style scoped>

.auth-card{

    width:430px;

    border:none;

    border-radius:20px;

    background:rgba(255,255,255,.60);

    backdrop-filter:blur(20px);

    box-shadow:
        0 15px 40px rgba(0,0,0,.10);

}

.form-control{

    height:48px;

    border-radius:12px;

}

.btn{

    border-radius:12px;
    height:48px;

}

</style>
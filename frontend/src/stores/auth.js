import { defineStore } from "pinia";
import authService from "@/services/authService";

export const useAuthStore = defineStore("auth", {
    state: () => ({
        user: JSON.parse(localStorage.getItem("user")) || null,
        loading: false,
        error: null,
    }),

    actions: {
        async login(credentials) {
            this.loading = true;
            this.error = null;

            try {
                const response = await authService.login(credentials);
                const data = response.data.data;

                localStorage.setItem(
                    "auth_token",
                    data.auth_token
                );

                this.user = data.user;
                localStorage.setItem(
                    "user",
                    JSON.stringify(data.user)
                );
                return data;
                
            } catch (err) {
                this.error =
                    err.response?.data?.message ||
                    "Login failed.";

                throw err;
            } finally {
                this.loading = false;
            }
        },

        logout() {
            localStorage.removeItem("auth_token");
            localStorage.removeItem("user");

            this.user = null;
            window.location.href = "/login";
        },
    },
});
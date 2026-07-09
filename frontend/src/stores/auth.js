import { defineStore } from "pinia";
import authService from "@/services/authService";

export const useAuthStore = defineStore("auth", {
    state: () => ({
        user: null,
        loading: false,
        error: null,
    }),

    actions: {
        async login(credentials) {
            this.loading = true;
            this.error = null;

            try {
                const response = await authService.login(credentials);

                localStorage.setItem(
                    "access_token",
                    response.data.access_token
                );

                this.user = response.data.user;

                return response.data;
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
            localStorage.removeItem("access_token");
            this.user = null;
        },
    },
});
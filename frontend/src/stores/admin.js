import { defineStore } from "pinia";
import adminService from "@/services/adminService";

export const useAdminStore = defineStore("admin", {

    state: () => ({
        dashboard: {},
        pendingCompanies: [],
        users: [],
        jobs: [],
        applications: [],
        loading: false,
    }),

    actions: {

        async loadDashboard() {

            this.loading = true;

            try {

                const response = await adminService.getDashboard();
                this.dashboard = response.data.data;

            } finally {

                this.loading = false;

            }

        },

        async loadPendingCompanies() {

            const response =
                await adminService.getPendingCompanies();

            this.pendingCompanies =
                response.data.data;

        },

        async approveCompany(id) {

            await adminService.approveCompany(id);

            await this.loadPendingCompanies();
            await this.loadDashboard();

        },

        async rejectCompany(id) {

            await adminService.rejectCompany(id);

            await this.loadPendingCompanies();
            await this.loadDashboard();

        }

    }

});
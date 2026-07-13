import { defineStore } from "pinia";
import adminService from "@/services/adminService";

export const useAdminStore = defineStore("admin", {

    state: () => ({
        dashboard: {},
        pendingCompanies: [],
        companies: [],
        users: [],
        jobs: [],
        pendingJobs: [],
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

        async loadCompanies() {

            const response =
                await adminService.getCompanies();

            this.companies =
                response.data.data;

        },

        async approveCompany(id) {

            await adminService.approveCompany(id);

            await this.loadCompanies();
            await this.loadPendingCompanies();
            await this.loadDashboard();

        },

        async rejectCompany(id) {

            await adminService.rejectCompany(id);

            await this.loadCompanies();
            await this.loadPendingCompanies();
            await this.loadDashboard();

        },

        async blacklistCompany(id) {

            await adminService.blacklistCompany(id);

            await this.loadCompanies();
            await this.loadDashboard();

        },

        async unblockCompany(id) {

            await adminService.unblockCompany(id);

            await this.loadCompanies();
            await this.loadDashboard();

        },

        async loadUsers() {

            const response =
                await adminService.getUsers();

            this.users =
                response.data.data;

        },

        async blacklistStudent(id) {

            await adminService.blacklistStudent(id);

            await this.loadUsers();

        },

        async unblockStudent(id) {

            await adminService.unblockStudent(id);

            await this.loadUsers();

        },

        async loadJobs() {

            const response =
                await adminService.getJobs();

            this.jobs =
                response.data.data;

        },

        async loadPendingJobs() {

            const response =
                await adminService.getPendingJobs();

            this.pendingJobs =
                response.data.data;

        },

        async approveJob(id) {

            await adminService.approveJob(id);

            await this.loadJobs();
            await this.loadPendingJobs();
            await this.loadDashboard();

        },

        async rejectJob(id, reason) {

            await adminService.rejectJob(id, reason);

            await this.loadJobs();
            await this.loadPendingJobs();
            await this.loadDashboard();

        },

        async loadApplications() {

            const response =
                await adminService.getApplications();

            this.applications =
                response.data.data;

        },

    }

});
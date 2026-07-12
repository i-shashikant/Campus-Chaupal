import { defineStore } from "pinia";
import authService from "@/services/authService";

export const useRegisterStore = defineStore("register", {

    state: () => ({

        role: "student",

        student: {

            email: "",
            password: "",

        },

        company: {

            email: "",
            password: "",

            company_name: "",
            industry: "",

            website: "",
            description: "",

            address: "",
            city: "",
            state: "",
            country: "",

            hr_name: "",
            hr_email: "",
            phone: ""

        }

    }),

    actions: {

    async registerStudent() {

        await authService.registerStudent(
            this.student
        );

        this.reset();

    },

    async registerCompany() {

        await authService.registerCompany(
            this.company
        );

        this.reset();

    },

    reset() {

        this.$reset();

    }

}

});
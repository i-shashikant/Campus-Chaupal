import { defineStore } from "pinia";

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

        reset() {

            this.$reset();

        }

    }

});
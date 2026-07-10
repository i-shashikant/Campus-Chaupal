import { defineStore } from "pinia";

export const useRegisterStore = defineStore("register", {

    state: () => ({

        role: "student",

        student: {

            email: "",
            password: "",

            full_name: "",
            roll_number: "",
            branch: "",
            year: "",

            cgpa: "",
            graduation_year: "",

            gender: "",
            phone: "",
            address: ""

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
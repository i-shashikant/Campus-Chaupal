import { defineStore } from "pinia";

export const useStudentProfileStore = defineStore("studentProfile", {

    state: () => ({

        profile: {

            full_name: "",

            gender: "",

            phone: "",

            address: "",

            roll_number: "",

            branch: "",

            year: "",

            cgpa: "",

            graduation_year: "",

            skills: "",

            linkedin: "",

            github: "",

            portfolio: "",

            resume: ""

        }

    }),

    actions: {

        reset() {

            this.$reset();

        }

    }

});
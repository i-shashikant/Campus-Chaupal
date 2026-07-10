<template>

<div>

    <div class="progress mb-4">

        <div
            class="progress-bar"
            :style="{width: progress + '%'}"
        ></div>

    </div>

    <component
        :is="currentComponent"
    />

    <div class="mt-4 d-flex justify-content-between">

        <button
            class="btn btn-outline-secondary"
            @click="previous"
            :disabled="step===1"
        >
            Previous
        </button>

        <button
            class="btn btn-primary"
            @click="next"
        >

            {{ step===4 ? "Register" : "Next" }}

        </button>

    </div>

</div>

</template>

<script setup>
import { computed, ref } from "vue";

import StudentAccountStep from "./student/AccountStep.vue";
import StudentAcademicStep from "./student/AcademicStep.vue";
import StudentPersonalStep from "./student/PersonalStep.vue";

import CompanyAccountStep from "./company/AccountStep.vue";
import CompanyStep from "./company/CompanyStep.vue";
import HRStep from "./company/HRStep.vue";

const props = defineProps({
    role:String
});

const step = ref(1);

const studentComponents=[
    StudentAccountStep,
    StudentAcademicStep,
    StudentPersonalStep,
    StudentPersonalStep
];

const companyComponents=[
    CompanyAccountStep,
    CompanyStep,
    HRStep,
    HRStep
];

const currentComponent=computed(()=>{

    return props.role==="student"
        ? studentComponents[step.value-1]
        : companyComponents[step.value-1];

});

const progress=computed(()=>step.value*25);

function next(){

    if(step.value<4)
        step.value++;

}

function previous(){

    if(step.value>1)
        step.value--;

}

</script>
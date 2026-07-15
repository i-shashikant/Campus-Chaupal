<template>

    <Transition name="toast">

        <div
            v-if="visible"
            class="toast-box"
            :class="type"
        >
            <i :class="icon"></i>

            <span>{{ message }}</span>

        </div>

    </Transition>

</template>

<script setup>
import { ref, computed, onMounted } from "vue";

const visible = ref(false);

const message = ref("");

const type = ref("success");

let timer = null;

const icon = computed(() => {

    switch (type.value) {

        case "success":
            return "bi bi-check-circle-fill";

        case "error":
            return "bi bi-x-circle-fill";

        case "warning":
            return "bi bi-exclamation-triangle-fill";

        default:
            return "bi bi-info-circle-fill";

    }

});

onMounted(() => {

    window.addEventListener("toast", (event) => {

        clearTimeout(timer);

        message.value = event.detail.message;

        type.value = event.detail.type || "success";

        visible.value = true;

        timer = setTimeout(() => {

            visible.value = false;

        }, 3000);

    });

});
</script>

<style scoped>

.toast-box{

    position:fixed;

    top:25px;

    right:25px;

    min-width:280px;

    max-width:380px;

    padding:15px 18px;

    border-radius:10px;

    color:white;

    display:flex;

    align-items:center;

    gap:12px;

    font-weight:500;

    z-index:99999;

    box-shadow:0 15px 35px rgba(0,0,0,.18);

}

.success{

    background:#2f855a;

}

.error{

    background:#c53030;

}

.warning{

    background:#d69e2e;

}

.info{

    background:#1b2a4a;

}

.toast-enter-active,
.toast-leave-active{

    transition:all .3s ease;

}

.toast-enter-from{

    opacity:0;

    transform:translateX(100%);

}

.toast-leave-to{

    opacity:0;

    transform:translateX(100%);

}

.toast-box i{

    font-size:20px;

}

</style>
<template>
    <div class="sidebar" :class="{ collapsed }">

        <div class="sidebar-header">
            <div class="brand" v-if="!collapsed">
                <i class="bi bi-mortarboard-fill brand-icon"></i>
                <span class="brand-name">CampusChaupal</span>
            </div>
            <i v-else class="bi bi-mortarboard-fill brand-icon-collapsed"></i>

            <button class="toggle-btn" @click="$emit('toggle')">
                <i class="bi bi-list"></i>
            </button>
        </div>

        <ul class="nav flex-column">
            <li v-for="item in menu" :key="item.route" class="nav-item">
                <RouterLink :to="item.route" class="nav-link" active-class="nav-link-active">
                    <i :class="`bi ${item.icon}`"></i>
                    <span v-if="!collapsed">{{ item.title }}</span>
                </RouterLink>
            </li>
        </ul>

        <div class="sidebar-footer" v-if="!collapsed">
            <span class="eyebrow">Placement Portal</span>
        </div>

    </div>
</template>

<script setup>
import { computed } from "vue";
import { useAuthStore } from "@/stores/auth";
import {
    studentMenu,
    companyMenu,
    adminMenu
} from "@/config/sidebar";

defineProps({
    collapsed: {
        type: Boolean,
        default: false
    }
});

defineEmits(["toggle"]);

const authStore = useAuthStore();

const menu = computed(() => {
    switch (authStore.user?.role) {
        case "student":
            return studentMenu;
        case "company":
            return companyMenu;
        case "admin":
            return adminMenu;
        default:
            return [];
    }
});


</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=JetBrains+Mono:wght@500&display=swap');

.sidebar {
    --ink: #1b2a4a;
    --ink-soft: #24345a;
    --brass: #c89b3c;
    --brass-soft: #e8d9b5;
    --slate-light: #a9b2c8;

    width: 260px;
    min-height: 100vh;
    background: var(--ink);
    color: #fff;
    display: flex;
    flex-direction: column;
    transition: width 0.2s ease;
}

.sidebar.collapsed {
    width: 76px;
}

.sidebar-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1.25rem 1.1rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.brand {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    overflow: hidden;
}

.brand-icon {
    color: var(--brass);
    font-size: 1.4rem;
    flex-shrink: 0;
}

.brand-icon-collapsed {
    color: var(--brass);
    font-size: 1.4rem;
}

.brand-name {
    font-family: "Fraunces", serif;
    font-weight: 600;
    font-size: 1.1rem;
    white-space: nowrap;
}

.toggle-btn {
    background: rgba(255, 255, 255, 0.08);
    border: none;
    color: #fff;
    width: 2rem;
    height: 2rem;
    border-radius: 0.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    cursor: pointer;
}

.toggle-btn:hover {
    background: rgba(255, 255, 255, 0.16);
}

.nav {
    padding: 1rem 0.75rem;
    flex: 1;
}

.nav-item {
    margin-bottom: 0.3rem;
}

.nav-link {
    display: flex;
    align-items: center;
    gap: 0.85rem;
    padding: 0.65rem 0.85rem;
    border-radius: 0.6rem;
    color: var(--slate-light);
    text-decoration: none;
    font-size: 0.92rem;
    transition: background 0.15s ease, color 0.15s ease;
}

.nav-link i {
    font-size: 1.05rem;
    width: 1.2rem;
    text-align: center;
}

.nav-link:hover {
    background: rgba(255, 255, 255, 0.06);
    color: #fff;
}

.nav-link-active {
    background: var(--brass);
    color: var(--ink);
    font-weight: 600;
}

.nav-link-active i {
    color: var(--ink);
}

.sidebar-footer {
    padding: 1rem 1.25rem 1.5rem;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
}

.eyebrow {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.68rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--brass-soft);
}

@media (prefers-reduced-motion: reduce) {
    .sidebar { transition: none; }
}
</style>
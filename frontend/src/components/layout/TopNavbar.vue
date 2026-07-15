<template>
    <nav class="dashboard-navbar px-4">

        <div class="navbar-title">
            <h3>{{ title }}</h3>
            <span class="role-badge" :class="roleTone">{{ roleLabel }}</span>
        </div>

        <div class="d-flex align-items-center gap-3">

            <button class="bell-btn">
                <i class="bi bi-bell fs-5"></i>
            </button>
            <button
                class="logout-btn"
                @click="logout"
                title="Logout"
            >
                <i class="bi bi-box-arrow-right fs-5"></i>
            </button>

        </div>

    </nav>
</template>

<script setup>
import { computed } from "vue";
import { useRouter } from "vue-router";
const router = useRouter(); 
import { useAuthStore } from "@/stores/auth";

const authStore = useAuthStore();

const title = computed(() => {
    switch (authStore.user?.role) {
        case "student":
            return "Student Dashboard";
        case "company":
            return "Company Dashboard";
        case "admin":
            return "Admin Dashboard";
        default:
            return "CampusChaupal";
    }
});

const roleLabel = computed(() => {
    const role = authStore.user?.role;
    if (!role) return "Guest";
    return role.charAt(0).toUpperCase() + role.slice(1);
});

const roleTone = computed(() => {
    switch (authStore.user?.role) {
        case "student":
            return "tone-navy";
        case "company":
            return "tone-emerald";
        case "admin":
            return "tone-crimson";
        default:
            return "tone-slate";
    }
});

const avatarUrl = computed(() => {
    const name = authStore.user?.name || roleLabel.value;
    return `https://ui-avatars.com/api/?name=${encodeURIComponent(name)}`;
});

const logout = () => {

    if (!confirm("Are you sure you want to logout?")) {
        return;
    }

    authStore.logout();

};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=JetBrains+Mono:wght@500&display=swap');

.dashboard-navbar {
    --ink: #1b2a4a;
    --slate: #5b6478;
    --brass: #c89b3c;
    --emerald: #2f855a;
    --crimson: #b4442e;
    --paper: #fbfaf7;
    --line: #e4e1d8;

    height: 70px;
    background: #fff;
    border-bottom: 1px solid var(--line);
    box-shadow: 0 2px 10px rgba(27, 42, 74, 0.03);
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.navbar-title {
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.navbar-title h3 {
    font-family: "Fraunces", serif;
    font-weight: 600;
    font-size: 1.25rem;
    color: var(--ink);
    margin: 0;
}

.role-badge {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.68rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    padding: 0.25rem 0.6rem;
    border-radius: 1rem;
}

.tone-navy { background: #e6e9f0; color: var(--ink); }
.tone-emerald { background: #e7f3ec; color: var(--emerald); }
.tone-crimson { background: #fbe9e5; color: var(--crimson); }
.tone-slate { background: #eef0f3; color: var(--slate); }

.bell-btn {
    background: var(--paper);
    border: 1px solid var(--line);
    color: var(--ink);
    width: 2.4rem;
    height: 2.4rem;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
}

.bell-btn:hover {
    background: #f0ede3;
}

.avatar {
    width: 42px;
    height: 42px;
    border-radius: 50%;
    border: 2px solid var(--line);
}

.user-name {
    font-size: 0.9rem;
    font-weight: 500;
    color: var(--ink);
}
.logout-btn {
    background: #fbe9e5;
    border: 1px solid #efc8bf;
    color: var(--crimson);

    width: 2.4rem;
    height: 2.4rem;

    border-radius: 50%;

    display: flex;
    align-items: center;
    justify-content: center;

    cursor: pointer;

    transition: .2s;
}

.logout-btn:hover {

    background: var(--crimson);
    color: white;

}
</style>
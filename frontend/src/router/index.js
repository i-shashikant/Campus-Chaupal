import { createRouter, createWebHistory } from 'vue-router'

import Login from '../pages/auth/Login.vue'
import Register from '../pages/auth/Register.vue'
import Jobs from "@/pages/student/Jobs.vue";
import CompanyDashboard from "@/pages/company/Dashboard.vue";
import CreateJob from "@/pages/company/CreateJob.vue";

const routes = [
    {
        path: '/',
        redirect: '/login'
    },

    {
        path: '/login',
        component: Login
    },

    {
        path: '/register',
        component: Register
    },

    {
    path: "/admin/dashboard",
    name: "AdminDashboard",
    component: () => import("@/pages/admin/Dashboard.vue"),
        meta: {
        requiresAuth: true,
        role: "admin"
        }
    },
    
    {
        path: "/admin/users",
        component: () => import("@/pages/admin/Users.vue"),
        meta: {
            requiresAuth: true,
            role: "admin"
        }

    },

    {
        path: "/admin/jobs",
        component: () => import("@/pages/admin/Jobs.vue"),
        meta: {
            requiresAuth: true,
            role: "admin"
        }
    },
    
    {
        path: "/admin/applications",
        component: () => import("@/pages/admin/Applications.vue"),
        meta: {
            requiresAuth: true,
            role: "admin"
        }
    },

    {
        path: "/admin/companies",
        component: () => import("@/pages/admin/Companies.vue"),
        meta: {
            requiresAuth: true,
            role: "admin"
        }
    },

    {
        path: "/student/dashboard",
        component: () => import("@/pages/student/Dashboard.vue"),
        meta: {
            requiresAuth: true,
            role: "student"
        }
    },

    {
        path: "/student/profile",
        component: () => import("@/pages/student/Profile.vue"),
        meta: {
            requiresAuth: true,
            role: "student"
        }
    },

    {
        path: "/student/applications",
        component: () => import("@/pages/student/Applications.vue"),
        meta: {
            requiresAuth: true,
            role: "student"
        }
    },

    { 
        path: "/student/jobs",
        component: () => import("@/pages/student/Jobs.vue"),
        meta: {
            requiresAuth: true,
            role: "student"
        }
    },

    {
        path: "/company/dashboard",
        component: () => import("@/pages/company/Dashboard.vue"),
        meta: {
            requiresAuth: true,
            role: "company"
        }
    },

    {
        path: "/company/profile",
        component: () => import("@/pages/company/Profile.vue"),
        meta: {
            requiresAuth: true,
            role: "company"
        }
    },

    {
        path: "/company/jobs",
        component: () => import("@/pages/company/ManageJobs.vue"),
        meta: {
            requiresAuth: true,
            role: "company"
        }
    },

    {
        path: "/company/jobs/create",
        component: () => import("@/pages/company/CreateJob.vue"),
    },
    

    {
        path: "/company/applications",
        component: () => import("@/pages/company/Applications.vue"),
        meta: {
            requiresAuth: true,
            role: "company"
        }
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})


router.beforeEach((to, from, next) => {

    const token = localStorage.getItem("auth_token");
    const user = JSON.parse(localStorage.getItem("user"));

    // Protected page but not logged in
    if (to.meta.requiresAuth && !token) {
        return next("/login");
    }

    // Already logged in, don't allow login/register
    if ((to.path === "/login" || to.path === "/register") && token) {

        if (user?.role === "admin")
            return next("/admin/dashboard");

        if (user?.role === "company")
            return next("/company/dashboard");

        if (user?.role === "student")
            return next("/student/dashboard");
    }

    // Wrong role
    if (to.meta.role && user && to.meta.role !== user.role) {

        if (user.role === "admin")
            return next("/admin/dashboard");

        if (user.role === "company")
            return next("/company/dashboard");

        if (user.role === "student")
            return next("/student/dashboard");
    }

    next();
});


export default router
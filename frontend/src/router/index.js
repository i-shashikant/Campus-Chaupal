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
        path: "/student/dashboard",
        component: () => import("@/pages/student/Dashboard.vue")
    },

    {
        path: "/student/profile",
        component: () => import("@/pages/student/Profile.vue")
    },

    {
    path: "/company/dashboard",
    component: CompanyDashboard
    },

    {
        path: "/company/jobs/create",
        component: CreateJob
    },
    
    {
    path: "/student/jobs",
    component: Jobs
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
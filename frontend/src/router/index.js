import { createRouter, createWebHistory } from 'vue-router'

import Login from '../pages/auth/Login.vue'
import Register from '../pages/auth/Register.vue'

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
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
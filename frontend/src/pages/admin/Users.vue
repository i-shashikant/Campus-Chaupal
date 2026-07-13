<template>

<DashboardLayout>

<div class="container-fluid">

    <h2 class="fw-bold mb-4">
        Users
    </h2>

    <div class="card shadow-sm">

        <div class="card-body">

            <table class="table align-middle">

                <thead>

                    <tr>

                        <th>Name</th>
                        <th>Email</th>
                        <th>Role</th>
                        <th>Status</th>

                    </tr>

                </thead>

                <tbody>

                    <tr
                        v-for="user in admin.users"
                        :key="user.id"
                    >

                        <td>
                            {{ user.name || "-" }}
                        </td>

                        <td>
                            {{ user.email }}
                        </td>

                        <td>

                            <span class="badge bg-primary">

                                {{ user.role }}

                            </span>

                        </td>

                        <td>

                            {{ user.status }}

                        </td>

                    </tr>

                </tbody>

            </table>

        </div>

    </div>

</div>

</DashboardLayout>

</template>

<script setup>

import { onMounted } from "vue";

import DashboardLayout from "@/layouts/DashboardLayout.vue";

import { useAdminStore } from "@/stores/admin";

const admin = useAdminStore();

onMounted(() => {

    admin.loadUsers();

});

</script>
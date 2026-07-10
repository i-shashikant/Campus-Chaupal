<template>

<div class="container-fluid">

    <div class="row">

        <div class="col-md-2 bg-dark text-white min-vh-100 p-3">

            <h4>CampusChaupal</h4>

            <hr>

            <slot name="sidebar" />

        </div>

        <div class="col-md-10 p-4">

            <slot />

        </div>

    </div>

</div>

</template>
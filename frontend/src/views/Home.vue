<template>
    <div class="home">

        <nav class="home-nav">
            <div class="brand">
                <i class="bi bi-mortarboard-fill"></i>
                <span>CampusChaupal</span>
            </div>
            <div class="nav-actions">
                <RouterLink to="/login" class="nav-link">Login</RouterLink>
                <RouterLink to="/register" class="nav-cta">Get Started</RouterLink>
            </div>
        </nav>

        <section class="hero">
            <span class="eyebrow">Placement Portal</span>
            <h1>Bridging the Gap Between Campus and Corporate</h1>
            <p>
                A modern placement portal that empowers students, recruiters, and placement officers to manage the complete campus recruitment lifecycle from one unified platform.
            </p>
            <div class="hero-actions">
                <RouterLink to="/register" class="btn-ledger btn-ledger-brass">
                    Create an Account
                </RouterLink>
                <RouterLink to="/login" class="btn-ledger btn-ledger-outline">
                    Login
                </RouterLink>
            </div>
        </section>

        <section class="stats-band">
            <div class="stat">
                <h2>1500+</h2>
                <small>Students Placed</small>
            </div>
            <div class="stat">
                <h2>100+</h2>
                <small>Recruiting Companies</small>
            </div>
            <div class="stat">
                <h2>300+</h2>
                <small>Placement Drives Run</small>
            </div>
            <div class="stat">
                <h2>92%</h2>
                <small>Placement Rate</small>
            </div>
        </section>

        <section class="roles">
            <div class="role-card">
                <div class="role-icon role-icon-navy"><i class="bi bi-mortarboard-fill"></i></div>
                <h5>Students</h5>
                <p>Browse eligible drives, apply in a click, and track every application in one place.</p>
            </div>
            <div class="role-card">
                <div class="role-icon role-icon-emerald"><i class="bi bi-building"></i></div>
                <h5>Companies</h5>
                <p>Post placement drives, review applicants, and manage your hiring pipeline end to end.</p>
            </div>
            <div class="role-card">
                <div class="role-icon role-icon-brass"><i class="bi bi-award-fill"></i></div>
                <h5>Institute</h5>
                <p>Approve companies, oversee every drive, and keep a clean record of placement outcomes.</p>
            </div>
        </section>

        <section class="partners">
            <span class="eyebrow partners-eyebrow">Trusted by recruiters from</span>
            <div class="marquee">
                <div class="marquee-track">
                    <span v-for="company in [...partnerCompanies, ...partnerCompanies]" :key="company" class="partner-chip">
                        <i class="bi bi-building"></i>
                        {{ company }}
                    </span>
                </div>
            </div>
        </section>

        <section class="how-it-works">
            <h3>How It Works</h3>
            <div class="steps">
                <div class="step">
                    <span class="step-number">01</span>
                    <h6>Register &amp; Get Verified</h6>
                    <p>Students build their profile, companies register and wait for institute approval.</p>
                </div>
                <div class="step">
                    <span class="step-number">02</span>
                    <h6>Drives Go Live</h6>
                    <p>Approved companies post placement drives; eligible students get matched instantly.</p>
                </div>
                <div class="step">
                    <span class="step-number">03</span>
                    <h6>Apply &amp; Track</h6>
                    <p>Students apply in one click and follow their status from applied to selected.</p>
                </div>
            </div>
        </section>

        <footer class="home-footer">
            <span>CampusChaupal — built for the placement cell.</span>
        </footer>

    </div>
</template>

<script setup>
const partnerCompanies = [
    "TCS",
    "Infosys",
    "Wipro",
    "Google",
    "Microsoft",
    "Amazon",
    "Accenture",
    "Cognizant",
    "IBM",
    "Deloitte",
];
</script>

<style scoped>
@import "@/assets/css/landing.css";
</style>

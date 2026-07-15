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
            <p>One platform for students, companies, and the institute placement cell to run the entire recruitment cycle, together.</p>
            <div class="hero-actions">
                <RouterLink to="/register" class="btn-ledger btn-ledger-brass">
                    Create an Account
                </RouterLink>
                <RouterLink to="/login" class="btn-ledger btn-ledger-outline">
                    Login
                </RouterLink>
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

        <footer class="home-footer">
            <span>CampusChaupal — built for the placement cell.</span>
        </footer>

    </div>
</template>

<script setup>
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=JetBrains+Mono:wght@500&display=swap');

.home {
    --ink: #1b2a4a;
    --slate: #5b6478;
    --brass: #c89b3c;
    --emerald: #2f855a;
    --paper: #fbfaf7;
    --line: #e4e1d8;

    min-height: 100vh;
    background: var(--paper);
    color: var(--ink);
}

.home-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.5rem 3rem;
}

.brand {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    font-family: "Fraunces", serif;
    font-weight: 600;
    font-size: 1.2rem;
}

.brand i {
    color: var(--brass);
    font-size: 1.5rem;
}

.nav-actions {
    display: flex;
    align-items: center;
    gap: 1.5rem;
}

.nav-link {
    color: var(--ink);
    text-decoration: none;
    font-weight: 500;
}

.nav-cta {
    background: var(--ink);
    color: #fff;
    padding: 0.55rem 1.3rem;
    border-radius: 2rem;
    text-decoration: none;
    font-weight: 500;
}

.hero {
    max-width: 720px;
    margin: 5rem auto 6rem;
    text-align: center;
    padding: 0 1.5rem;
}

.eyebrow {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.75rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--brass);
}

.hero h1 {
    font-family: "Fraunces", serif;
    font-weight: 600;
    font-size: 2.6rem;
    margin: 1rem 0 1.25rem;
    line-height: 1.2;
}

.hero p {
    color: var(--slate);
    font-size: 1.1rem;
    margin-bottom: 2rem;
}

.hero-actions {
    display: flex;
    justify-content: center;
    gap: 1rem;
    flex-wrap: wrap;
}

.btn-ledger {
    padding: 0.75rem 1.75rem;
    border-radius: 2rem;
    font-weight: 500;
    text-decoration: none;
    display: inline-block;
}

.btn-ledger-brass {
    background: var(--brass);
    color: var(--ink);
}

.btn-ledger-outline {
    background: transparent;
    color: var(--ink);
    border: 1px solid var(--line);
}

.roles {
    max-width: 1000px;
    margin: 0 auto 5rem;
    padding: 0 1.5rem;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5rem;
}

.role-card {
    background: #fff;
    border: 1px solid var(--line);
    border-radius: 1rem;
    padding: 2rem 1.75rem;
    text-align: center;
}

.role-icon {
    width: 3.25rem;
    height: 3.25rem;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.4rem;
    color: #fff;
    margin: 0 auto 1rem;
}

.role-icon-navy { background: var(--ink); }
.role-icon-emerald { background: var(--emerald); }
.role-icon-brass { background: var(--brass); }

.role-card h5 {
    font-family: "Fraunces", serif;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.role-card p {
    color: var(--slate);
    font-size: 0.92rem;
    margin: 0;
}

.home-footer {
    text-align: center;
    padding: 2rem;
    color: var(--slate);
    font-size: 0.85rem;
    border-top: 1px solid var(--line);
}

@media (max-width: 768px) {
    .roles {
        grid-template-columns: 1fr;
    }

    .home-nav {
        padding: 1.25rem 1.5rem;
    }
}
</style>
<template>
    <div class="hero">
        <div class="hero-emblem"><i class="bi bi-mortarboard-fill"></i></div>
        <span class="eyebrow">Placement Portal</span>
        <h1>CampusChaupal</h1>
        <p>Bridging the Gap Between Campus and Corporate.</p>

        <div class="feature-list">
            <div class="feature">
                <i class="bi bi-building"></i>
                <span>Connect with Recruiters</span>
            </div>
            <div class="feature">
                <i class="bi bi-briefcase"></i>
                <span>Explore Opportunities</span>
            </div>
            <div class="feature">
                <i class="bi bi-people"></i>
                <span>Build Your Professional Network</span>
            </div>
        </div>
    </div>
</template>

<script setup>
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=JetBrains+Mono:wght@500&display=swap');

.hero {
    --brass: #c89b3c;
    --brass-soft: #e8d9b5;
    color: #fff;
    max-width: 420px;
}

.hero-emblem {
    font-size: 2.5rem;
    color: var(--brass);
    margin-bottom: 1rem;
}

.eyebrow {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.72rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--brass-soft);
}

.hero h1 {
    font-family: "Fraunces", serif;
    font-weight: 600;
    font-size: 2.4rem;
    margin: 0.4rem 0 0.75rem;
}

.hero p {
    opacity: 0.85;
    font-size: 1.05rem;
    margin-bottom: 2.5rem;
}

.feature-list {
    display: flex;
    flex-direction: column;
    gap: 1.1rem;
}

.feature {
    display: flex;
    align-items: center;
    gap: 0.85rem;
    font-size: 0.95rem;
}

.feature i {
    width: 2.25rem;
    height: 2.25rem;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.1);
    color: var(--brass);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
</style>
<script setup lang="ts">
import { ref } from 'vue'
</script>

<template>
  <header class="navbar">
    <div class="title">MySite</div>
    <nav class="nav-links">
      <a href="#">Home</a>
      <a href="#">About</a>
      <a href="#">Projects</a>
      <a href="#">Contact</a>
    </nav>
  </header>
</template>

<style scoped>
.navbar {
  position: fixed;
  width: 100%;
  background-color: #8b8bd4;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  z-index: 1000;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.title {
  color: white;
  font-size: 1.5rem;
  font-weight: bold;
}

.nav-links a {
  color: white;
  margin-left: 1.5rem;
  text-decoration: none;
  font-size: 1rem;
  transition: color 0.2s;
}

.nav-links a:hover {
  color: #61dafb;
}
</style>

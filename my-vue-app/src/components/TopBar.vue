<script setup lang="ts">
import { ref } from 'vue'
</script>

<template>
  <header class="navbar">
    <div class="navbar-left">
      <a href="#" class="nav-button">About Me</a>
    </div>

    <div class="navbar-center">
      <h1 class="title">AiRockPaperS</h1>
    </div>

    <div class="navbar-right">
      <a href="#">Login</a>
    </div>
    </header>
</template>

<style scoped>
.navbar {
  position: fixed;
  width: 100%;
  background-color: #C79746;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  z-index: 99;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.navbar-left,
.navbar-center,
.navbar-right {
  flex: 1;
  display: flex;
  align-items: center;
}

.navbar-left {
  justify-content: flex-start;
}

.navbar-center {
  justify-content: center;
}

.navbar-right {
  justify-content: flex-end;
}

.nav-button {
  padding: 0.5rem 1rem;
  border: 2px solid white;
  color: white;
  text-decoration: none;
  border-radius: 6px;
  font-weight: bold;
  transition: background-color 0.3s, color 0.3s;
}

.nav-button:hover {
  background-color: white;
  color: #C79746; /* matches your navbar gold */
}

.title {
  font-size: 2rem;          /* make it big */
  font-weight: bold;
  color: white;
  letter-spacing: 1px;
  margin: 0;                /* remove default margin */
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3); /* optional for depth */
}
</style>

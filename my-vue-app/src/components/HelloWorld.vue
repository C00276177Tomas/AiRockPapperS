<script setup lang="ts">
import { ref } from 'vue'

defineProps<{ msg: string }>()

const count = ref(0)
</script>

<template>
  <header class="navbar">
    <div class="logo">MySite</div>
    <nav class="menu">
      <a href="#">Home</a>
      <a href="#">About</a>
      <a href="#">Projects</a>
      <a href="#">Contact</a>
    </nav>
  </header>


  <h1>{{ msg }}</h1>

  <div class="card">
    <button type="button" @click="count += 5">count is {{ count }}</button>
    <p>
      Edit
      <code>components/HelloWorld.vue</code> to test HMR HelloWorld
    </p>
  </div>

  <p>
    Check out
    <a href="https://vuejs.org/guide/quick-start.html#local" target="_blank"
      >create-vue</a
    >, the official Vue + Vite starter
  </p>
  <p>
    Learn more about IDE Support for Vue in the
    <a
      href="https://vuejs.org/guide/scaling-up/tooling.html#ide-support"
      target="_blank"
      >Vue Docs Scaling up Guide</a
    >.
  </p>
  <p class="read-the-docs">Click on the Vite and Vue logos to learn more</p>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}

.navbar {
  position: fixed;
  top: 0;
  width: 100%;
  background-color: #194dc7;
  color: white;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 10;
  box-shadow: 0 2px 4px rgba(197, 6, 6, 0.1);
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.menu a {
  color: white;
  margin-left: 1.5rem;
  text-decoration: none;
  font-size: 1rem;
  transition: color 0.2s;
}

.menu a:hover {
  color: #61dafb;
}
</style>

<script setup lang="ts">
import { ref } from "vue";
</script>

<template>
  <header class="navbar">
    <div class="navbar-left"></div>

    <div class="navbar-center">
      <h4>
        This project could be open source or I might copy right it, we will see
      </h4>
    </div>

    <div class="navbar-right"></div>
  </header>
</template>

<style scoped>
.navbar {
  margin-top: 94vh;
  position: fixed;
  width: 100%;
  background-color: #c79746;
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
</style>

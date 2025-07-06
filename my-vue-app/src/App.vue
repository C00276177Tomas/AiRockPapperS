<script setup lang="ts">
import TopBar from "./components/TopBar.vue";
</script>

<template>
  <TopBar />
  <div class="container">
    <div class="main-content">
      <div class="top-row">
        <div class="half-box-left">Player 1</div>
        <div class="half-box-right">Player 2</div>
      </div>
      <div class="full-box"></div>

      <div class="top-square-left"></div>
      <div class="top-square-right"></div>
      <div class="camera-container"></div>
    </div>
  </div>
</template>

<style scoped>
.main-content {
  margin: 100px 300px;
  width: 80%;
}
.container {
  display: flex;
  align-items: center;
  justify-content: center;
  align-items: center;
  height: 100%;
  padding-top: 80px;
  width: 100%;
}
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
.top-row {
  display: flex;
}
.half-box-left {
  flex: 1;
  height: 50px;
  border-style: solid;
  border-width: 5px 2.5px 0px 5px;
  border-color: #c79746;
  font-size: 2em;
}
.half-box-right {
  flex: 1;
  height: 50px;
  border-style: solid;
  border-width: 5px 5px 0px 2.5px;
  border-color: #c79746;
  font-size: 2em;
}
.full-box {
  width: 100%;
  height: 400px;
  border: 5px solid #c79746;
}
</style>

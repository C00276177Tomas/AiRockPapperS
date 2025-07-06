<script setup lang="ts">
import { ref } from "vue";
</script>

<template>
  <header class="navbar">
    <div class="navbar-left">
      <div class="nav-button">
        About Me
        <span class="tooltip">
          <p>
            My name is Tomas Smitas, a Full Stack Developer and Data Science
            Enthusiast.
          </p>
          <p>Feel free to contact me with any of the links provided.</p>
          <p>
            <a
              href="https://c00276177tomas.github.io/MachineLearningPortfolio/"
              target="_blank"
              >Visit My Website</a
            >
          </p>
        </span>
      </div>
      <a
        href="https://www.linkedin.com/in/tomassmitas/"
        target="_blank"
        rel="noopener noreferrer"
        class="icon-link"
      >
        <img src="/linkedIn.png" alt="LinkedIn" class="nav-icon-linkedin" />
      </a>
      <a
        href="https://github.com/C00276177Tomas"
        target="_blank"
        rel="noopener noreferrer"
        class="icon-link"
      >
        <img src="/githubCropped.png" alt="LinkedIn" class="nav-icon-github" />
      </a>
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
  background-color: #c79746;
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

.title {
  font-size: 2rem; /* make it big */
  font-weight: bold;
  color: white;
  letter-spacing: 1px;
  margin: 0; /* remove default margin */
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3); /* optional for depth */
}

.nav-icon-linkedin {
  height: 48px;
  width: 48px;
  margin-left: 1rem;
  cursor: pointer;
}
.nav-icon-github {
  height: 48px;
  width: 48px;
  margin-left: 1rem;
  cursor: pointer;
}
a {
  display: inline-flex;
  align-items: center;
}

.nav-button {
  position: relative;
  text-decoration: none;
  color: white;
  padding: 0.5rem 1rem;
  border: 2px solid white;
  border-radius: 4px;
  cursor: pointer;
  display: inline-block;
}

.nav-button:hover {
  background-color: white;
  color: #c79746; /* matches your navbar gold */
}

/* Initially hide tooltip */
.tooltip {
  visibility: hidden;
  opacity: 0;
  width: max-content;
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 0.4rem 0.6rem;
  border-radius: 4px;

  position: absolute;
  left: 50%;
  transform: translateX(-9.5%);
  top: 100%; /* right under the button */
  white-space: nowrap;

  transition: opacity 0.3s ease;
  pointer-events: none; /* so it doesn’t block hover when hidden */
  z-index: 10;
}

/* Show tooltip when hovering the button or the tooltip */
.nav-button:hover .tooltip,
.nav-button .tooltip:hover {
  visibility: visible;
  opacity: 1;
  pointer-events: auto;
}

.tooltip p {
  margin: 0.5rem 0;
}
</style>

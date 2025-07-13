<script setup lang="ts">
import TopBar from "./components/TopBar.vue";
import BottomBar from "./components/BottomBar.vue";
</script>

<template>
  <TopBar />
  <BottomBar />
  <div class="container">
    <div class="main-content">
      <button class="control-button">Connect Camera</button>
      <div class="top-row">
        <div class="half-box-left-upper">Player 1</div>
        <div class="half-box-right-upper">Player 2</div>
      </div>
      <div class="bottom-row">
        <div class="half-box-left-lower"></div>
        <div class="half-box-right-lower"></div>
      </div>
      <div class="nav-button">Learn how I made this project</div>
    </div>
    <div class="project-info-content">
      <div class="project-info-section">
        <h1>Why is this project so spacial?</h1>
        this project is about creating an ai project that runs completely on the
        users side computational power. This has the ability to drastically
        reduce the amount of resources required to run large scale Ai models
        making it afordable even for small companies.
      </div>
      <div class="project-info-section">
        <h1>Why I made it</h1>
        While developing my final year project SiteSafeAi, I saw the major
        issues of deploying Ai models into backends. My vision was to deploy my
        backend that would possibly make multiple image classifications each
        second which would have put a massive load onto the server, making the
        project undeployable for a student with a tight budget. Estimated cost
        to run on a local server would add up quick and on a cloud hosting
        website would have put me into bankrupcy. My solution. Run the Ai model
        in the frontend utalizing the users computational power instead of
        relying on the backend. It is an amazing solution for smaller companies
        and start ups that want to inergrate Ai models into their project but
        dont have the resources to do it.
      </div>
      <div class="project-info-section">
        <h1>Weaknesses</h1>
        This is not a perfect solution without any weakneses. The model does
        requre a longer initial loading time that does put a biggers strain on
        the frontend. Since the js models are so highly optimised this is still
        significantly lower than using standart models, and once the model is
        loaded in the users computer takes over all of the lifting. This
        solution priorisises efficiency, if accuracy is critical then using a js
        model wont be as effectivne compared to a full size model, in a critical
        project this could be inssuficient. Converting the model to a js model
        can create extra complexity to creating the model.
      </div>
      <div class="project-info-section">
        <h1>The Ai model</h1>
        this project is about creating an ai project that runs completely on the
        users side computational power. This has the ability to drastically
        reduce the amount of resources required to run large scale Ai models
        making it afordable even for small companies.
      </div>
      <div class="project-info-section">
        <h1>What was learned</h1>
        Learned how to train and fine-tune a .js model for the first time. Got a
        refresher by using typrescipt which is also the language that I used in
        my internship. I wanted to include a new technology that I havnt used
        before, so I decided to use Vue and Vite.
      </div>
    </div>
  </div>
</template>

<style scoped>
.main-content {
  padding: 100px 350px;
  width: 100%;
  height: 100vh;
  box-sizing: border-box;
}
.project-info-content {
  padding: 100px 350px;
  width: 100%;
  box-sizing: border-box;
}
.container {
  display: block;
  align-items: center;
  justify-content: center;
  align-items: center;
  height: 100%;
  padding-top: 40px;
  width: 100%;
  box-sizing: border-box;
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
.bottom-row {
  display: flex;
}
.half-box-right-upper {
  flex: 1;
  height: 50px;
  border-style: solid;
  border-width: 5px 5px 0px 2.5px;
  border-color: #c79746;
  font-size: 2em;
}
.half-box-left-upper {
  flex: 1;
  height: 50px;
  border-style: solid;
  border-width: 5px 2.5px 0px 5px;
  border-color: #c79746;
  font-size: 2em;
}
.half-box-right-lower {
  flex: 1;
  height: 500px;
  border-style: solid;
  border-width: 5px 5px 5px 2.5px;
  border-color: #c79746;
  font-size: 2em;
}
.half-box-left-lower {
  flex: 1;
  height: 500px;
  border-style: solid;
  border-width: 5px 2.5px 5px 5px;
  border-color: #c79746;
  font-size: 2em;
}
.control-button {
  background-color: #c79746;
  margin-bottom: 10px;
}
.nav-button {
  margin-top: 30px;
}
.project-info-section {
  margin-bottom: 20px;
}
</style>

<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import app-settings from './components/app-settings.vue'
import Feedback from './components/Feedback.vue'
import generator-settings from './components/generator-settings.vue'
import homepage from './components/homepage.vue'
import instrument-selection from './components/instrument-selection.vue'
import login from './components/login.vue'
import practice from './components/practice.vue'
import signup from './components/signup.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    app-settings,
    Feedback,
    generator-settings,
    homepage,
    instrument-selection,
    login,
    practice,
    signup
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

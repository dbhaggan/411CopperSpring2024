<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <app-settings></app-settings>
    <Feedback></Feedback>
    <generator-settings></generator-settings>
    <homepage></homepage>
    <instrument-selection></instrument-selection>
    <login></login>
    <practice></practice>
    <signup></signup>

    <!-- Render fetched data from backend -->
    <div v-if="loaded">
      <div v-for="item in items" :key="item.id">
        {{ item.name }}
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
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
  },

  data() {
    return {
      items: [], // hold fetched data
      loaded: false, //flag to track if data is loaded
    };
  },

  mounted() {
    // fetch data from Django backend when component is mounted
    axios.get('http://localhost:8080/api/items')
      .then(response => {
        // asign fetched data to items array
        this.items = response.data;

        // set loaded flag to true
        this.loaded = true;
      })

      .catch(error => {
        console.error('Error fetching items:', error);
        // handle error if needed
      });
  },
};
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

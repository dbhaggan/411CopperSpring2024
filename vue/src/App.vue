<template>
  <div id="app">
    <img alt="PercussAtSight" src="./assets/logo.png" />
    <h2>Users</h2>
    <div v-if="!loaded">Loading users...</div>
    <div v-if="loaded">
      <div v-for="user in users" :key="user.id">
        <ul>
          <li>{{ user.userName }}</li>
          <li>{{ user.firstName }}</li>
          <li>{{ user.lastName }}</li>
          <li>{{ user.emailAddress }}</li>
        </ul>
      </div>
    </div>
    <app-settings></app-settings>
    <SmartFeedback></SmartFeedback>
    <generator-settings></generator-settings>
    <HomePage></HomePage>
    <instrument-selection></instrument-selection>
    <login></login>
    <PracticePage></PracticePage>
    <signup></signup>
  </div>
</template>

<script>
import axios from "axios";
// import app-settings from './components/app-settings.vue'
// import generator-settings from './components/generator-settings.vue'
import HomePage from "./components/HomePage.vue";
// import instrument-selection from './components/instrument-selection.vue'
import login from "./components/LogIn.vue";
import signup from "./components/SignUp.vue";
import SmartFeedback from "./components/SmartFeedback.vue";
import PracticePage from "./components/PracticePage.vue";

export default {
  name: "App",
  components: {
    // app-settings,
    SmartFeedback,
    // generator-settings,
    HomePage,
    // instrument-selection,
    login,
    PracticePage,
    signup,
  },

  data() {
    return {
      users: [], // hold fetched data
      loaded: false, //flag to track if data is loaded
    };
  },

  mounted() {
    // fetch data from Django backend when component is mounted
    axios
      .get("http://localhost:8080/api/user/")
      .then((response) => {
        this.users = response.data;

        this.loaded = true;
      })

      .catch((error) => {
        console.error("Error fetching users:", error);
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

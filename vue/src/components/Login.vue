<template>
  <div class="login-container"
    ><div class="login-container1"
      ><div class="login-container2"
        ><router-link to="/" class="login-navlink"
          ><img
            alt="image"
            src="../assets/PercussAtSight_Logo.png"
            class="login-image" /></router-link></div
      ><div class="login-container3"
        ><input
          type="text"
          placeholder="Password"
          class="login-textinput input"
        /><input
          type="text"
          placeholder="Username "
          class="login-textinput1 input"
        /><label class="login-text">Username:</label
        ><label class="login-text1">Password:</label
        ><button type="submit" class="login-button button">Log-In</button></div
      ></div
    ></div
  >
</template>

<script>
export default {
  name: 'Login',
  props: {},
  metaInfo: {
    title: 'login - PercussAtSight',
    meta: [
      {
        property: 'og:title',
        content: 'login - PercussAtSight',
      },
    ],
  },
}
</script>

<style scoped>
.login-container {
  width: 100%;
  display: flex;
  overflow: auto;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
}
.login-container1 {
  width: 100%;
  display: flex;
  overflow: auto;
  position: relative;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
}
.login-container2 {
  flex: 0 0 auto;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: var(--dl-color-gray-white);
}
.login-navlink {
  display: contents;
}
.login-image {
  width: 400px;
  object-fit: cover;
  text-decoration: none;
}
.login-container3 {
  width: 760px;
  height: 727px;
  display: flex;
  position: relative;
  align-self: center;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}
.login-textinput {
  top: 395px;
  left: 0px;
  right: 0px;
  width: 252px;
  height: 72px;
  margin: auto;
  position: absolute;
}
.login-textinput1 {
  top: 195px;
  left: 0px;
  right: 0px;
  width: 252px;
  height: 72px;
  margin: auto;
  position: absolute;
}
.login-text {
  top: 151px;
  left: 298px;
  margin: auto;
  position: absolute;
  font-size: 32px;
}
.login-text1 {
  top: 358px;
  left: 298px;
  margin: auto;
  position: absolute;
  font-size: 32px;
}
.login-button {
  top: 503px;
  left: 0px;
  right: 0px;
  width: 164px;
  height: 48px;
  margin: auto;
  position: absolute;
}
</style>

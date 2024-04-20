<template>
  <div class="signup-container"
    ><div class="signup-container1"
      ><div class="signup-container2"
        ><router-link to="/" class="signup-navlink"
          ><img
            alt="image"
            src="../assets/PercussAtSight_Logo.png"
            class="signup-image" /></router-link></div
      ><div class="signup-container3"
        ><input
          type="text"
          placeholder="Last Name"
          class="signup-textinput input"
        /><input
          type="text"
          placeholder="First Name"
          class="signup-textinput1 input"
        /><input
          type="text"
          placeholder="Email "
          class="signup-textinput2 input"
        /><label class="signup-text">First Name:</label
        ><label class="signup-text1">Email:</label
        ><label class="signup-text2">Password:</label
        ><button type="submit" class="signup-button button">Sign-Up</button></div
      ></div
    ></div
  >
</template>

<script>
export default {
  name: 'Signup',
  props: {},
  metaInfo: {
    title: 'signup - PercussAtSight',
    meta: [
      {
        property: 'og:title',
        content: 'signup - PercussAtSight',
      },
    ],
  },
}
</script>

<style scoped>
.signup-container {
  width: 100%;
  display: flex;
  overflow: auto;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
}
.signup-container1 {
  width: 100%;
  display: flex;
  overflow: auto;
  position: relative;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
}
.signup-container2 {
  flex: 0 0 auto;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: var(--dl-color-gray-white);
}
.signup-navlink {
  display: contents;
}
.signup-image {
  width: 400px;
  object-fit: cover;
  text-decoration: none;
}
.signup-container3 {
  width: 760px;
  height: 727px;
  display: flex;
  position: relative;
  align-self: center;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}
.signup-textinput {
  top: 299px;
  left: 256px;
  width: 252px;
  height: 72px;
  margin: auto;
  position: absolute;
}
.signup-textinput1 {
  top: 137px;
  left: 262px;
  width: 252px;
  height: 72px;
  margin: auto;
  position: absolute;
}
.signup-textinput2 {
  top: 457px;
  left: 256px;
  width: 252px;
  height: 72px;
  margin: auto;
  position: absolute;
}
.signup-text {
  top: 91px;
  left: 298px;
  margin: auto;
  position: absolute;
  font-size: 32px;
}
.signup-text1 {
  top: 401px;
  left: 296px;
  margin: auto;
  position: absolute;
  font-size: 32px;
}
.signup-text2 {
  top: 248px;
  left: 302px;
  margin: auto;
  position: absolute;
  font-size: 32px;
}
.signup-button {
  top: 559px;
  left: 300px;
  width: 164px;
  height: 48px;
  margin: auto;
  position: absolute;
}
</style>

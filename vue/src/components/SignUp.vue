<template>
  <div class="signup-container">
    <div class="signup-container1">
      <div class="signup-container3">
        <input
         type="text"
         placeholder="Last Name"
         class="signup-textinput input" />
       <input
        type="text"
        placeholder="First Name"
        class="signup-textinput1 input" />
       <input
        type="text"
        placeholder="Email "
        class="signup-textinput2 input" />
      <label class="signup-text">First Name:</label>
      <label class="signup-text1">Email:</label>
      <label class="signup-text2">Last Name:</label>
      <button type="submit" class="signup-button button">Sign-Up</button>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'SignupPage',
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
  align-items: center;
  flex-direction: column;
}
.signup-container1 {
  width: 100%;
  display: flex;
  overflow: auto;
  position: relative;
  align-items: center;
  flex-direction: column;
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
  height: 36px;
  margin: auto;
  position: absolute;
}
.signup-textinput1 {
  top: 137px;
  left: 256px;
  width: 252px;
  height: 36px;
  margin: auto;
  position: absolute;
}
.signup-textinput2 {
  top: 457px;
  left: 256px;
  width: 252px;
  height: 36px;
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

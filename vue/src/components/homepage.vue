<template>
  <div class="homepage-container">
    <div class="homepage-logo-placement">
      <div class="homepage-container1">
        <router-link to="/login" class="homepage-login button">Login</router-link>
        <button name="sign-up" class="homepage-sign-up button">Sign-up</button>
        <button name="practice" class="homepage-practice button">Practice</button>
        <router-link to="/" class="homepage-navlink">
          <img
            alt="image"
            src="./assets/PercussAtSight_logo.png"
            class="homepage-image"
          />
        </router-link>
      </div>
    </div>
    <img
      alt="image"
      src="./assets/backdrop.png"
      loading="eager"
      class="homepage-image1"
    />
  </div>
</template>

<script>
export default {
  name: 'Homepage',
  props: {},
  metaInfo: {
    title: 'PercussAtSight',
    meta: [
      {
        property: 'og:title',
        content: 'PercussAtSight',
      },
    ],
  },
}
</script>

<style scoped>
.homepage-container {
  width: 100%;
  display: flex;
  overflow: auto;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
}
.homepage-logo-placement {
  width: 100%;
  height: 143px;
  display: flex;
  align-items: flex-start;
}
.homepage-container1 {
  flex: 0 0 auto;
  width: 100%;
  height: 100%;
  display: flex;
  position: relative;
  align-items: center;
  justify-content: center;
  background-image: linear-gradient(90deg, rgba(153, 86, 29, 0.94) 1.00%,rgba(240, 144, 53, 0) 83.00%);
}
.homepage-login {
  top: 53px;
  left: left;
  color: var(--dl-color-gray-white);
  right: 290px;
  width: var(--dl-size-size-large);
  position: absolute;
  font-style: normal;
  font-family: "Arial";
  font-weight: 700;
  text-decoration: none;
  background-color: #1e2f86;
}
.homepage-sign-up {
  top: 53px;
  color: var(--dl-color-gray-white);
  right: 146px;
  width: var(--dl-size-size-large);
  position: absolute;
  font-style: normal;
  font-family: "Arial";
  font-weight: 700;
  text-decoration: none;
  background-color: var(--dl-color-primary-pasblue);
}
.homepage-practice {
  top: 53px;
  color: var(--dl-color-gray-white);
  right: 0px;
  width: var(--dl-size-size-large);
  position: absolute;
  align-self: center;
  font-style: normal;
  font-family: "Arial";
  font-weight: 700;
  background-color: var(--dl-color-primary-pasblue);
}
.homepage-navlink {
  display: contents;
}
.homepage-image {
  top: 9px;
  left: 846px;
  width: 200px;
  margin: auto;
  position: absolute;
  align-self: center;
  object-fit: cover;
  text-decoration: none;
}
.homepage-image1 {
  width: 100%;
  height: 1120px;
  object-fit: cover;
}
</style>

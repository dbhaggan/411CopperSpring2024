<template>
  <div>
    <link href="./login.css" rel="stylesheet" />
    <div class="login-container">
      <div class="login-container1">
        <div class="login-container2">
          <a href="homepage.html" class="login-navlink">
            <img alt="image" src="./assets/PercussAtSight_logo.png" class="login-image" />
          </a>
        </div>
        <header data-thq="thq-navbar" class="login-navbar-interactive">
          <div data-thq="thq-navbar-nav" class="login-desktop-menu">
            <div class="login-buttons">
              <a href="login.html" class="login-login button">Login</a>
              <button name="sign-up" class="login-sign-up button">Sign-up</button>
              <button name="practice" class="login-practice button">Practice</button>
            </div>
          </div>
        </header>
        <form class="login-form">
          <input type="text" placeholder="Username" class="login-textinput input" />
          <input type="text" placeholder="Password" class="login-textinput1 input" />
          <label class="login-text5">Username:</label>
          <label class="login-text6">Password:</label>
          <img src="./assets/PercussAtSight_logo.png" alt="image" class="login-image1" />
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginPage',
};
</script>

<style scoped>
/* Your CSS styles go here */
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
  background-image: linear-gradient(
    90deg,
    rgb(153, 86, 29) 31.00%,
    rgba(240, 203, 53, 0) 100.00%
  );
}
.login-container2 {
  flex: 0 0 auto;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-image: linear-gradient(
    90deg,
    rgba(153, 86, 29, 0.94) 3.00%,
    rgba(240, 144, 53, 0) 85.00%
  );
}
.login-navlink {
  display: contents;
}
.login-image {
  width: 200px;
  object-fit: cover;
  text-decoration: none;
}
.login-navbar-interactive {
  width: 100%;
  display: flex;
  align-items: center;
  padding-top: var(--dl-space-space-twounits);
  padding-left: var(--dl-space-space-threeunits);
  padding-right: var(--dl-space-space-threeunits);
  padding-bottom: var(--dl-space-space-twounits);
  justify-content: space-between;
  background-image: linear-gradient(
    90deg,
    rgba(153, 86, 29, 0.94) 2.00%,
    rgba(115, 74, 8, 0) 78.00%
  );
}
.login-desktop-menu {
  flex: 1;
  display: flex;
  justify-content: space-between;
  background-image: linear-gradient(
    90deg,
    rgb(153, 86, 29) 0.00%,
    rgba(240, 144, 53, 0) 14.00%
  );
}
.login-buttons {
  display: flex;
  align-items: center;
  flex-direction: row;
  justify-content: space-between;
}
.login-login {
  color: var(--dl-color-gray-white);
  width: var(--dl-size-size-large);
  font-style: normal;
  font-family: "Arial";
  font-weight: 700;
  text-decoration: none;
  background-color: rgb(30, 47, 134);
}
.login-sign-up {
  color: var(--dl-color-gray-white);
  width: var(--dl-size-size-large);
  font-style: normal;
  font-family: "Arial";
  font-weight: 700;
  text-decoration: none;
  background-color: var(--dl-color-primary-pasblue);
}
.login-practice {
  color: var(--dl-color-gray-white);
  width: var(--dl-size-size-large);
  height: 100%;
  align-self: stretch;
  font-style: normal;
  font-family: "Arial";
  font-weight: 700;
  background-color: var(--dl-color-primary-pasblue);
}
.login-form {
  width: 100%;
  height: 769px;
  display: flex;
  position: relative;
  align-items: center;
  justify-content: flex-end;
}
.login-textinput {
  top: 204px;
  left: 473px;
  position: absolute;
  align-self: center;
}
.login-textinput1 {
  top: 366px;
  left: 473px;
  position: absolute;
  align-self: center;
}
.login-text5 {
  top: 182px;
  left: 475px;
  color: #000000;
  position: absolute;
  align-self: center;
  font-style: normal;
  font-family: "Arial";
  font-weight: 700;
}
.login-text6 {
  top: 349px;
  left: 476px;
  position: absolute;
  align-self: center;
  font-style: normal;
  font-family: "Arial";
  font-weight: 700;
}
.login-image1 {
  top: 111px;
  right: 2px;
  width: 658px;
  height: 396px;
  position: absolute;
  align-self: center;
  object-fit: cover;
}
@media (max-width: 991px) {
  .login-desktop-menu {
    display: none;
  }
}
</style>

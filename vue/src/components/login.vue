<template>
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="utf-8" />
      <title>login - PercussAtSight</title>
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <link rel="stylesheet" href="./style.css" />
      <link rel="stylesheet" href="./login.css" />
    </head>
    <body>
      <div class="login-container">
        <div class="login-container1">
          <div class="login-container2">
            <a href="homepage.html" class="login-navlink">
              <img
                src="../assets/PercussAtSight_Logo.png"
                alt="logo"
                class="login-image"
              />
            </a>
          </div>
          <header class="login-navbar-interactive">
            <div class="login-desktop-menu">
              <div class="login-buttons">
                <a href="login.html" class="login-login button">Login</a>
              </div>
              <a href="signup.html" name="sign-up" class="login-sign-up button"
                >Sign-up</a
              >
              <button name="practice" class="login-practice button">
                Practice
              </button>
            </div>
          </header>
          <form class="login-form">
            <label class="login-text5">Username:</label>
            <input
              type="text"
              placeholder="Username"
              class="login-textinput input"
            />

            <label class="login-text6">Password:</label>
            <input
              type="password"
              placeholder="Password"
              class="login-textinput1 input"
            />

            <img
              alt="logo"
              src="../assets/PercussAtSight_Logo.png"
              class="login-image1"
            />

            <button type="submit" name="log-in" class="login-button button">
              Log-In
            </button>
          </form>
        </div>
      </div>
    </body>
  </html>
</template>

<style>
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
  background-image: white;
}
.login-container2 {
  flex: 0 0 auto;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: white;
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
  background-color: white;
}
.login-desktop-menu {
  flex: 1;
  display: flex;
  justify-content: space-between;
  background-color: white;
}
.login-buttons {
  display: flex;
  align-items: center;
  flex-direction: row;
  justify-content: space-between;
}
.login-login {
  color: white;
  width: var(--dl-size-size-large);
  font-style: normal;
  font-family: "Arial";
  font-weight: 700;
  text-decoration: none;
  background-color: #1e2f86;
}
.login-sign-up {
  color: white;
  width: var(--dl-size-size-large);
  font-style: normal;
  font-family: "Arial";
  font-weight: 700;
  text-decoration: none;
  background-color: #1e2f86;
}
.login-practice {
  color: white;
  width: var(--dl-size-size-large);
  height: 100%;
  align-self: stretch;
  font-style: normal;
  font-family: "Arial";
  font-weight: 700;
  background-color: #1e2f86;
}
.login-burger-menu {
  display: none;
}
.login-icon {
  width: var(--dl-size-size-medium);
  height: var(--dl-size-size-xsmall);
}
.login-mobile-menu {
  top: 0px;
  left: 0px;
  width: 100%;
  height: 100vh;
  display: none;
  padding: 32px;
  z-index: 100;
  position: absolute;
  flex-direction: column;
  justify-content: space-between;
  background-color: #fff;
}
.login-nav {
  display: flex;
  align-items: flex-start;
  flex-direction: column;
}
.login-top {
  width: 100%;
  display: flex;
  align-items: center;
  margin-bottom: var(--dl-space-space-threeunits);
  justify-content: space-between;
}
.login-logo {
  height: 2rem;
}
.login-close-menu {
  display: flex;
  align-items: center;
  justify-content: center;
}
.login-icon02 {
  width: var(--dl-size-size-xsmall);
  height: var(--dl-size-size-xsmall);
}
.login-links {
  flex: 0 0 auto;
  display: flex;
  align-self: flex-start;
  align-items: flex-start;
  flex-direction: column;
}
.login-text {
  margin-bottom: var(--dl-space-space-unit);
}
.login-text1 {
  margin-bottom: var(--dl-space-space-unit);
}
.login-text2 {
  margin-bottom: var(--dl-space-space-unit);
}
.login-text3 {
  margin-bottom: var(--dl-space-space-unit);
}
.login-text4 {
  margin-bottom: var(--dl-space-space-unit);
}
.login-buttons1 {
  display: flex;
  margin-top: var(--dl-space-space-unit);
  align-items: center;
  flex-direction: row;
  justify-content: space-between;
}
.login-login1 {
  margin-right: var(--dl-space-space-twounits);
}
.login-icon04 {
  width: var(--dl-size-size-xsmall);
  height: var(--dl-size-size-xsmall);
  margin-right: var(--dl-space-space-twounits);
}
.login-icon06 {
  width: var(--dl-size-size-xsmall);
  height: var(--dl-size-size-xsmall);
  margin-right: var(--dl-space-space-twounits);
}
.login-icon08 {
  width: var(--dl-size-size-xsmall);
  height: var(--dl-size-size-xsmall);
}
.login-form {
  width: 100%;
  height: 769px;
  display: flex;
  position: relative;
  align-items: center;
  justify-content: flex-end;
  background-color: var(--dl-color-gray-white);
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

.login-button {
  top: 430px;
  left: 475px;
  position: absolute;
}

@media (max-width: 991px) {
  .login-desktop-menu {
    display: none;
  }
  .login-burger-menu {
    display: flex;
  }
}
@media (max-width: 767px) {
  .login-navbar-interactive {
    padding-left: var(--dl-space-space-twounits);
    padding-right: var(--dl-space-space-twounits);
  }
  .login-burger-menu {
    align-items: center;
    justify-content: center;
  }
  .login-text {
    margin-bottom: var(--dl-space-space-unit);
  }
  .login-text1 {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
  .login-text2 {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
  .login-text3 {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
  .login-text4 {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
}
@media (max-width: 479px) {
  .login-navbar-interactive {
    padding: var(--dl-space-space-unit);
  }
  .login-mobile-menu {
    padding: 16px;
  }
}
</style>

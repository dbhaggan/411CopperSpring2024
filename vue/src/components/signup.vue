<template>
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="utf-8">
      <title>signup - PercussAtSight</title>
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <link rel="stylesheet" href="./style.css">
      <link rel="stylesheet" href="./signup.css">
  </head>
  <body>
    <div class="signup-container">
      <div class="signup-container1">
          <div class="signup-container2">
              <a href="homepage.html" class="login-navlink">
                  <img src="/vue/src/assets/logo.png" alt="logo" class="login-image">
              </a>
          </div>
          <header class="signup-navbar-interactive">
              <div class="signup-desktop-menu">
                  <div class="signup-buttons">
                      <a href="login.html" class="signup-login button">Login</a>
                  </div>
                  <a href="signup.html" name="sign-up" class="signup-sign-up button">Sign-up</a>
                  <button name="practice" class="login-practice button">Practice</button>
              </div>
          </header>
          <form class="signup-form">
              <label class="signup-text5">First Name:</label>
              <input type="text" placeholder="First Name" class="signup-textinput input" />
  
              <label class="signup-text6">Last Name:</label>
              <input type="text" placeholder="Last Name" class="signup-textinput1 input" />
  
              <label class="signup-text7">Email:</label>
              <input type="email" placeholder="Email" class="signup-textinput2 input" />
  
              <img
              alt="logo"
              src="/vue/src/assets/logo.png"
              class="login-image1"
              />
  
              <button name="signup" type="submit" class="signup-signup button">Sign Up</button>
          </form>
      </div>
    </div>
  </body>
  </html>
</template>

<style>
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
  background-image: white;
}
.signup-container2 {
  flex: 0 0 auto;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-image: white;
}
.signup-navlink {
  display: contents;
}
.signup-image {
  width: 200px;
  object-fit: cover;
  text-decoration: none;
}
.signup-navbar-interactive {
  width: 100%;
  display: flex;
  align-items: center;
  padding-top: var(--dl-space-space-twounits);
  padding-left: var(--dl-space-space-threeunits);
  padding-right: var(--dl-space-space-threeunits);
  padding-bottom: var(--dl-space-space-twounits);
  justify-content: space-between;
  background-image: white;
}
.signup-desktop-menu {
  flex: 1;
  display: flex;
  justify-content: space-between;
  background-image: white;
}
.signup-buttons {
  display: flex;
  align-items: center;
  flex-direction: row;
  justify-content: space-between;
}
.signup-login {
  color: white;
  width: var(--dl-size-size-large);
  font-style: normal;
  font-family: "Arial";
  font-weight: 700;
  text-decoration: none;
  background-color: #1e2f86;
}
.signup-sign-up {
  color: white;
  width: var(--dl-size-size-large);
  font-style: normal;
  font-family: "Arial";
  font-weight: 700;
  text-decoration: none;
  background-color: #1e2f86;
}
.signup-practice {
  color: white;
  width: var(--dl-size-size-large);
  height: 100%;
  align-self: stretch;
  font-style: normal;
  font-family: "Arial";
  font-weight: 700;
  background-color: #1e2f86;
}
.signup-burger-menu {
  display: none;
}
.signup-icon {
  width: var(--dl-size-size-medium);
  height: var(--dl-size-size-xsmall);
}
.signup-mobile-menu {
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
.signup-nav {
  display: flex;
  align-items: flex-start;
  flex-direction: column;
}
.signup-top {
  width: 100%;
  display: flex;
  align-items: center;
  margin-bottom: var(--dl-space-space-threeunits);
  justify-content: space-between;
}
.signup-logo {
  height: 2rem;
}
.signup-close-menu {
  display: flex;
  align-items: center;
  justify-content: center;
}
.signup-icon02 {
  width: var(--dl-size-size-xsmall);
  height: var(--dl-size-size-xsmall);
}
.signup-links {
  flex: 0 0 auto;
  display: flex;
  align-self: flex-start;
  align-items: flex-start;
  flex-direction: column;
}
.signup-text {
  margin-bottom: var(--dl-space-space-unit);
}
.signup-text1 {
  margin-bottom: var(--dl-space-space-unit);
}
.signup-text2 {
  margin-bottom: var(--dl-space-space-unit);
}
.signup-text3 {
  margin-bottom: var(--dl-space-space-unit);
}
.signup-text4 {
  margin-bottom: var(--dl-space-space-unit);
}
.signup-buttons1 {
  display: flex;
  margin-top: var(--dl-space-space-unit);
  align-items: center;
  flex-direction: row;
  justify-content: space-between;
}
.signup-login1 {
  margin-right: var(--dl-space-space-twounits);
}
.signup-icon04 {
  width: var(--dl-size-size-xsmall);
  height: var(--dl-size-size-xsmall);
  margin-right: var(--dl-space-space-twounits);
}
.signup-icon06 {
  width: var(--dl-size-size-xsmall);
  height: var(--dl-size-size-xsmall);
  margin-right: var(--dl-space-space-twounits);
}
.signup-icon08 {
  width: var(--dl-size-size-xsmall);
  height: var(--dl-size-size-xsmall);
}
.signup-form {
  width: 100%;
  height: 769px;
  display: flex;
  position: relative;
  align-items: center;
  justify-content: center;
}
.signup-textinput {
  top: 204px;
  left: 473px;
  position: absolute;
  align-self: center;
}
.signup-textinput1 {
  top: 299px;
  left: 473px;
  position: absolute;
  align-self: center;
}
.signup-textinput2 {
  top: 393px;
  left: 473px;
  position: absolute;
  align-self: center;
}
.signup-text5 {
  top: 182px;
  left: 475px;
  color: rgb(0, 0, 0);
  position: absolute;
  align-self: center;
  font-style: normal;
  font-family: "Arial";
  font-weight: 700;
}
.signup-text6 {
  top: 274px;
  left: 475px;
  position: absolute;
  align-self: center;
  font-style: normal;
  font-family: "Arial";
  font-weight: 700;
}
.signup-text7 {
  top: 370px;
  left: 476px;
  color: rgb(0, 0, 0);
  position: absolute;
  align-self: center;
  font-style: normal;
  font-family: "Arial";
  font-weight: 700;
}
.signup-image1 {
  top: 111px;
  right: 2px;
  width: 658px;
  height: 396px;
  position: absolute;
  align-self: center;
  object-fit: cover;
}
.signup-signup {
  left: 472px;
  bottom: 282px;
  position: absolute;
}
@media(max-width: 991px) {
  .signup-desktop-menu {
    display: none;
  }
  .signup-burger-menu {
    display: flex;
  }
}
@media(max-width: 767px) {
  .signup-navbar-interactive {
    padding-left: var(--dl-space-space-twounits);
    padding-right: var(--dl-space-space-twounits);
  }
  .signup-burger-menu {
    align-items: center;
    justify-content: center;
  }
  .signup-text {
    margin-bottom: var(--dl-space-space-unit);
  }
  .signup-text1 {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
  .signup-text2 {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
  .signup-text3 {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
  .signup-text4 {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
}
@media(max-width: 479px) {
  .signup-navbar-interactive {
    padding: var(--dl-space-space-unit);
  }
  .signup-mobile-menu {
    padding: 16px;
  }
}

</style>

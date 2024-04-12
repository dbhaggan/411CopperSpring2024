<template>
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8" />
        <title>request-my-instrument - PercussAtSight</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <link rel="stylesheet" href="../assets/style.css" />
        <link rel="stylesheet" href="../assets/request-my-instrument.css" />
      </head>
      <body>
        <div class="request-my-instrument-container">
          <div class="request-my-instrument-container1">
            <div class="request-my-instrument-container2">
              <a href="index.html" class="request-my-instrument-navlink">
                <img
                  src="../assets/PercussAtSight_Logo.png"
                  alt="logo"
                  class="request-my-instrument-image"
                />
              </a>
            </div>
            <header class="request-my-instrument-navbar-interactive">
              <div class="request-my-instrument-desktop-menu">
                <div class="request-my-instrument-buttons">
                  <a href="login.html" class="request-my-instrument-login button">Login</a>
                </div>
                <a href="signup.html" name="sign-up" class="request-my-instrument-sign-up button">
                  Sign-up</a>
                <button name="practice" class="request-my-instrument-practice button">
                  Practice
                </button>
              </div>
            </header>
            <form class="request-my-instrument-form">
              <img
                alt="image"
                src="../assets/PercussAtSight_Logo.png"
                class="request-my-instrument-image1"
              />
              <button
                name="log in"
                type="submit"
                class="request-my-instrument-button button"
              >
                Make Request
              </button>
              <input
                type="text"
                placeholder="Instrument Name"
                enctype="Instrument Name"
                class="request-my-instrument-textinput input"
              />
              <label class="request-my-instrument-text5">
                What instrument would you like to request?
              </label>
            </form>
          </div>
        </div>
      </body>
    </html>
</template>

<script>
  export default {
    name: 'InstrumentRequest',
  }
</script>

<style>

.request-my-instrument-container {
  width: 100%;
  display: flex;
  overflow: auto;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
}
.request-my-instrument-container1 {
  width: 100%;
  display: flex;
  overflow: auto;
  position: relative;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
}
.request-my-instrument-container2 {
  flex: 0 0 auto;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: var(--dl-color-gray-white);
}
.request-my-instrument-navlink {
  display: contents;
}
.request-my-instrument-image {
  width: 200px;
  object-fit: cover;
  text-decoration: none;
}
.request-my-instrument-navbar-interactive {
  width: 100%;
  display: flex;
  align-items: center;
  padding-top: var(--dl-space-space-twounits);
  padding-left: var(--dl-space-space-threeunits);
  padding-right: var(--dl-space-space-threeunits);
  padding-bottom: var(--dl-space-space-twounits);
  justify-content: space-between;
  background-color: var(--dl-color-gray-white);
}
.request-my-instrument-desktop-menu {
  flex: 1;
  display: flex;
  justify-content: space-between;
  background-color: var(--dl-color-gray-white);
}
.request-my-instrument-buttons {
  display: flex;
  align-items: center;
  flex-direction: row;
  justify-content: space-between;
}
.request-my-instrument-login {
  color: var(--dl-color-gray-white);
  width: var(--dl-size-size-large);
  font-style: normal;
  font-family: "Arial";
  font-weight: 700;
  text-decoration: none;
  background-color: rgb(30, 47, 134);
}
.request-my-instrument-sign-up {
  color: var(--dl-color-gray-white);
  width: var(--dl-size-size-large);
  font-style: normal;
  font-family: "Arial";
  font-weight: 700;
  text-decoration: none;
  background-color: var(--dl-color-primary-pasblue);
}
.request-my-instrument-practice {
  color: var(--dl-color-gray-white);
  width: var(--dl-size-size-large);
  height: 100%;
  align-self: stretch;
  font-style: normal;
  font-family: "Arial";
  font-weight: 700;
  background-color: var(--dl-color-primary-pasblue);
}
.request-my-instrument-burger-menu {
  display: none;
}
.request-my-instrument-icon {
  width: var(--dl-size-size-medium);
  height: var(--dl-size-size-xsmall);
}
.request-my-instrument-mobile-menu {
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
.request-my-instrument-nav {
  display: flex;
  align-items: flex-start;
  flex-direction: column;
}
.request-my-instrument-top {
  width: 100%;
  display: flex;
  align-items: center;
  margin-bottom: var(--dl-space-space-threeunits);
  justify-content: space-between;
}
.request-my-instrument-logo {
  height: 2rem;
}
.request-my-instrument-close-menu {
  display: flex;
  align-items: center;
  justify-content: center;
}
.request-my-instrument-icon02 {
  width: var(--dl-size-size-xsmall);
  height: var(--dl-size-size-xsmall);
}
.request-my-instrument-links {
  flex: 0 0 auto;
  display: flex;
  align-self: flex-start;
  align-items: flex-start;
  flex-direction: column;
}
.request-my-instrument-text {
  margin-bottom: var(--dl-space-space-unit);
}
.request-my-instrument-text1 {
  margin-bottom: var(--dl-space-space-unit);
}
.request-my-instrument-text2 {
  margin-bottom: var(--dl-space-space-unit);
}
.request-my-instrument-text3 {
  margin-bottom: var(--dl-space-space-unit);
}
.request-my-instrument-text4 {
  margin-bottom: var(--dl-space-space-unit);
}
.request-my-instrument-buttons1 {
  display: flex;
  margin-top: var(--dl-space-space-unit);
  align-items: center;
  flex-direction: row;
  justify-content: space-between;
}
.request-my-instrument-login1 {
  margin-right: var(--dl-space-space-twounits);
}
.request-my-instrument-icon04 {
  width: var(--dl-size-size-xsmall);
  height: var(--dl-size-size-xsmall);
  margin-right: var(--dl-space-space-twounits);
}
.request-my-instrument-icon06 {
  width: var(--dl-size-size-xsmall);
  height: var(--dl-size-size-xsmall);
  margin-right: var(--dl-space-space-twounits);
}
.request-my-instrument-icon08 {
  width: var(--dl-size-size-xsmall);
  height: var(--dl-size-size-xsmall);
}
.request-my-instrument-form {
  width: 100%;
  height: 596px;
  display: flex;
  position: relative;
  align-items: center;
  justify-content: flex-start;
  background-color: var(--dl-color-gray-white);
}
.request-my-instrument-image1 {
  top: 111px;
  right: 2px;
  width: 658px;
  height: 396px;
  position: absolute;
  align-self: center;
  object-fit: cover;
}
.request-my-instrument-button {
  top: 372px;
  left: 470px;
  position: absolute;
}
.request-my-instrument-textinput {
  top: 306px;
  left: 414px;
  position: absolute;
}
.request-my-instrument-text5 {
  top: 269px;
  left: 376px;
  position: absolute;
  font-size: 16px;
  font-style: normal;
  font-weight: 700;
}
@media(max-width: 991px) {
  .request-my-instrument-desktop-menu {
    display: none;
  }
  .request-my-instrument-burger-menu {
    display: flex;
  }
}
@media(max-width: 767px) {
  .request-my-instrument-navbar-interactive {
    padding-left: var(--dl-space-space-twounits);
    padding-right: var(--dl-space-space-twounits);
  }
  .request-my-instrument-burger-menu {
    align-items: center;
    justify-content: center;
  }
  .request-my-instrument-text {
    margin-bottom: var(--dl-space-space-unit);
  }
  .request-my-instrument-text1 {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
  .request-my-instrument-text2 {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
  .request-my-instrument-text3 {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
  .request-my-instrument-text4 {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
}
@media(max-width: 479px) {
  .request-my-instrument-navbar-interactive {
    padding: var(--dl-space-space-unit);
  }
  .request-my-instrument-mobile-menu {
    padding: 16px;
  }
}


</style>
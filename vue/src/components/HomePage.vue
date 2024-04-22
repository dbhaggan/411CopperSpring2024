<template>
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <title>PercussAtSight</title>
      <meta property="og:title" content="PercussAtSight" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <meta charset="utf-8" />
      <meta property="twitter:card" content="summary_large_image" />
    </head>
    <body>
      <link rel="stylesheet" href="../assets/style.css" />
      <div>
        <link href="../assets/homepage.css" rel="stylesheet" />
        <div class="homepage-container">
          <div class="homepage-logo-placement">
            <div class="homepage-container1">
              <!--<a href="login.html" class="homepage-login button">Login</a> -->
              <RouterLink to="/login" class="homepage-login button">Login</RouterLink>
              <!--<a href="signup.html" class="homepage-sign-up button">Sign-up</a>-->
              <RouterLink to="/signup" class="homepage-sign-up button">Sign Up</RouterLink>
              <button name="practice" class="homepage-practice button">
                <RouterLink to="/practice" name="practice">Practice</RouterLink>
              </button>
               <!-- <a href="homepage.html" class="homepage-navlink"> -->
              <RouterLink to="/home">
                <img
                  alt="logo"
                  src="../assets/PercussAtSight_Logo.png"
                  class="homepage-image"
                />
              </RouterLink>
             <!--</a>--> 
            </div>
          </div>
          <img
            alt="back drop"
            src="../assets/backdrop.png"
            loading="eager"
            class="homepage-image1"
          />
        </div>
      </div>
    </body>
  </html>
  <RouterView />
</template>

<script>
  export default {
    name: "HomePage"
  }
</script>

<style>
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
  background-image: white;
}
.homepage-login {
  top: 53px;
  left: left;
  color: white;
  right: 290px;
  width: var(--dl-size-size-large);
  position: absolute;
  align-self: center;
  font-style: normal;
  font-family: "Arial";
  font-weight: 700;
  text-decoration: none;
  background-color: #1e2f86;
}
.homepage-sign-up {
  top: 53px;
  color: white;
  right: 146px;
  width: var(--dl-size-size-large);
  position: absolute;
  align-self: center;
  font-style: normal;
  font-family: "Arial";
  font-weight: 700;
  text-decoration: none;
  background-color: #1e2f86;
}
.homepage-practice {
  top: 53px;
  color: white;
  right: 0px;
  width: var(--dl-size-size-large);
  position: absolute;
  align-self: center;
  font-style: normal;
  font-family: "Arial";
  font-weight: 700;
  text-decoration: none;
  background-color: #1e2f86;
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

<template>
<!DOCTYPE html>
<html>
<body style="background-color:#003e7d">

<div>
  <link href="./practice.css" rel="stylesheet" />
  <div class="practice-container">
    <div class="practice-container1">
      <button type="button" class="practice-button button">
        <span class="practice-text">
          <span>Practice</span>
          <br />
        </span>
      </button>
      <button type="button" class="practice-button1 button">
        <span class="practice-text03">
          <span>Collaborative Learning</span>
          <br />
        </span>
      </button>
      <button type="button" class="practice-button2 button">
        <span>
          <span>Settings</span>
          <br />
        </span>
      </button>
      <button type="button" class="practice-button3 button">
        <span class="practice-text09">
          <span>Home</span>
          <br />
        </span>
      </button>
    </div>
    <button type="button" class="practice-button4 button">
      <span>
        <br />
        <br />
      </span>
    </button>
  </div>
</div>

</body>
</html>
</template>

<style>
.practice-container {
  width: 100%;
  display: flex;
  overflow: auto;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
  background-color: #003e7d;
}
.practice-container1 {
  width: 181px;
  height: 1080px;
  display: flex;
  position: relative;
  align-self: flex-start;
  align-items: center;
  flex-direction: column;
  justify-content: flex-start;
  background-color: #0055FF;
}
.practice-button {
  color: rgb(128, 170, 255);
  width: 181px;
  height: 90px;
  opacity: 1;
  font-size: 24px;
  border-color: #80AAFF;
  border-width: 3px;
  text-transform: capitalize;
  background-color: rgb(0, 85, 255);
}
.practice-text {
  text-align: center;
}
.practice-button1 {
  color: rgb(128, 170, 255);
  width: 181px;
  height: 90px;
  opacity: 1;
  border-color: #80AAFF;
  border-width: 3px;
  background-color: rgb(0, 85, 255);
}
.practice-text03 {
  font-size: 24px;
  text-align: center;
}
.practice-button2 {
  color: rgb(128, 170, 255);
  width: 181px;
  height: 90px;
  opacity: 1;
  font-size: 24px;
  border-color: #80AAFF;
  border-width: 3px;
  background-color: rgb(0, 85, 255);
}
.practice-button3 {
  color: rgb(128, 170, 255);
  right: 0px;
  width: 181px;
  bottom: 0px;
  height: 90px;
  opacity: 1;
  position: absolute;
  border-color: #80AAFF;
  border-width: 3px;
  background-color: rgb(0, 85, 255);
}
.practice-text09 {
  font-size: 24px;
}
.practice-button4 {
  left: 935px;
  width: 160px;
  bottom: 42px;
  height: 160px;
  position: absolute;
  border-radius: 80px;
  background-color: rgb(26, 143, 221);
}
</style>

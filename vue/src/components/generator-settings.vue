<template>
<div>
  <link href="./generator-settings.css" rel="stylesheet" />
  <div class="generator-settings-container">
    <div class="generator-settings-container1">
      <button type="button" class="generator-settings-button button">
        <span class="generator-settings-text">
          <span>Practice</span>
          <br />
        </span>
      </button>
      <button type="button" class="generator-settings-button1 button">
        <span class="generator-settings-text03">
          <span>Collaborative Learning</span>
          <br />
        </span>
      </button>
      <button type="button" class="generator-settings-button2 button">
        <span>
          <span>Settings</span>
          <br />
        </span>
      </button>
      <button type="button" class="generator-settings-button3 button">
        <span class="generator-settings-text09">
          <span>Home</span>
          <br />
        </span>
      </button>
    </div>
    <div class="generator-settings-container2">
      <span class="generator-settings-text12">Music Settings</span>
      <input
        type="checkbox"
        checked="true"
        class="generator-settings-checkbox"
      />
      <span class="generator-settings-text13">Metronome:</span>
      <span class="generator-settings-text14">Hard</span>
      <span class="generator-settings-text15">
        <span>Medium</span>
        <br />
      </span>
      <span class="generator-settings-text18">
        <span>Easy</span>
        <br />
      </span>
      <span class="generator-settings-text21">
        <span>Difficulty</span>
        <br />
      </span>
      <span class="generator-settings-text24">
        <span>Tempo</span>
        <br />
      </span>
      <span class="generator-settings-text27">Key</span>
    </div>
    <button type="button" class="generator-settings-button4 button">
      <span>
        <br />
        <br />
      </span>
    </button>
  </div>
</div>
</template>

<script>
export default {
  name: 'GeneratorSettingsPage',
};
</script>

<style>
.generator-settings-container {
  width: 100%;
  display: flex;
  overflow: auto;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
  background-color: #003e7d;
}
.generator-settings-container1 {
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
.generator-settings-button {
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
.generator-settings-text {
  text-align: center;
}
.generator-settings-button1 {
  color: rgb(128, 170, 255);
  width: 181px;
  height: 90px;
  opacity: 1;
  border-color: #80AAFF;
  border-width: 3px;
  background-color: rgb(0, 85, 255);
}
.generator-settings-text03 {
  font-size: 24px;
  text-align: center;
}
.generator-settings-button2 {
  color: rgb(128, 170, 255);
  width: 181px;
  height: 90px;
  opacity: 1;
  font-size: 24px;
  border-color: #80AAFF;
  border-width: 3px;
  background-color: rgb(0, 85, 255);
}
.generator-settings-button3 {
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
.generator-settings-text09 {
  font-size: 24px;
}
.generator-settings-container2 {
  right: 0px;
  width: 356px;
  bottom: 0px;
  height: 571px;
  display: flex;
  position: absolute;
  align-self: flex-end;
  align-items: center;
  flex-direction: column;
  justify-content: flex-start;
  background-color: #001f3e;
}
.generator-settings-text12 {
  color: #ffffff;
  font-size: 32px;
}
.generator-settings-checkbox {
  top: 355px;
  left: 191px;
  position: absolute;
}
.generator-settings-text13 {
  top: 352px;
  left: 83px;
  color: #ffffff;
  position: absolute;
}
.generator-settings-text14 {
  top: 263px;
  color: #ffffff;
  right: 23px;
  position: absolute;
}
.generator-settings-text15 {
  top: 264px;
  left: 145px;
  color: #ffffff;
  position: absolute;
}
.generator-settings-text18 {
  top: 263px;
  left: 10px;
  color: #ffffff;
  position: absolute;
}
.generator-settings-text21 {
  top: 218px;
  left: 8px;
  color: #ffffff;
  position: absolute;
}
.generator-settings-text24 {
  top: 132px;
  left: 10px;
  color: #ffffff;
  position: absolute;
}
.generator-settings-text27 {
  top: 43px;
  left: 14px;
  color: #ffffff;
  position: absolute;
}
.generator-settings-button4 {
  left: 935px;
  width: 160px;
  bottom: 42px;
  height: 160px;
  position: absolute;
  border-radius: 80px;
  background-color: rgb(26, 143, 221);
}
</style>

<template>
<div>
  <link href="../assets/generator-settings.css" rel="stylesheet" />
  <div class="generator-settings-container">
    <div class="generator-settings-container1">
      <span class="generator-settings-text">Settings</span>
      <select class="generator-settings-select">
        <option value="Option 1">Option 1</option>
        <option value="Option 2">Option 2</option>
        <option value="Option 3">Option 3</option>
      </select>
      <textarea
        placeholder="placeholder"
        class="generator-settings-textarea textarea"
      ></textarea>
      <textarea
        placeholder="placeholder"
        class="generator-settings-textarea1 textarea"
      ></textarea>
      <span class="generator-settings-text01">Rudiments in Score:</span>
      <span class="generator-settings-text02">Change Octaves:</span>
      <span class="generator-settings-text03">Instruments in Score:</span>
      <input type="checkbox" checked="true" class="generator-settings-checkbox" />
      <span class="generator-settings-text04">Pick Instrument:</span>
      <span class="generator-settings-text05">
        <span>Tempo</span>
        <br />
      </span>
      <span class="generator-settings-text08">Metronome:</span>
      <span class="generator-settings-text09">Key</span>
      <span class="generator-settings-text10">Number of Measures:</span>
      <span class="generator-settings-text11">Change Clef:</span>
      <span class="generator-settings-text12">Randomize Stitching:</span>
      <input
        type="checkbox"
        checked="true"
        class="generator-settings-checkbox1"
      />
    </div>
    <div class="generator-settings-container2">
      <button type="button" class="generator-settings-button button">
        <span class="generator-settings-text13">
          <span>Practice</span>
          <br />
        </span>
      </button>
      <button type="button" class="generator-settings-button1 button">
        <span class="generator-settings-text16">
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
        <span class="generator-settings-text22">
          <span>Home</span>
          <br />
        </span>
      </button>
    </div>
    <button type="button" class="generator-settings-button4 button">
      <span>
        <br />
        <br />
      </span>
    </button>
  </div>
</template>

<script>
export default {
  name: 'GeneratorSettings',
  props: {},
  metaInfo: {
    title: 'Generator-Settings',
    meta: [
      {
        property: 'og:title',
        content: 'Generator-Settings',
      },
    ],
  },
}
</script>

<style scoped>
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
  right: 0px;
  width: 518px;
  bottom: 0px;
  height: 739px;
  display: flex;
  position: absolute;
  align-self: flex-end;
  align-items: center;
  flex-direction: column;
  justify-content: flex-start;
  background-color: #001f3e;
}
.generator-settings-text {
  color: rgb(255, 255, 255);
  font-size: 32px;
}
.generator-settings-select {
  top: 122px;
  left: 141px;
  position: absolute;
}
.generator-settings-textarea {
  top: 163px;
  left: 144px;
  width: 59px;
  position: absolute;
  padding-top: 0px;
  padding-left: 0px;
  padding-right: 0px;
  padding-bottom: 0px;
}
.generator-settings-textarea1 {
  top: 68px;
  left: 175px;
  width: 59px;
  position: absolute;
  padding-top: 0px;
  padding-left: 0px;
  padding-right: 0px;
  padding-bottom: 0px;
}
.generator-settings-text01 {
  top: 314px;
  left: 5px;
  color: rgb(255, 255, 255);
  position: absolute;
}
.generator-settings-text02 {
  top: 169px;
  left: 3px;
  color: #ffffff;
  position: absolute;
}
.generator-settings-text03 {
  top: 220px;
  left: 5px;
  color: #ffffff;
  position: absolute;
}
.generator-settings-checkbox {
  top: 613px;
  left: 177px;
  position: absolute;
}
.generator-settings-text04 {
  top: 36px;
  left: 7px;
  color: rgb(255, 255, 255);
  position: absolute;
}
.generator-settings-text05 {
  top: 461px;
  left: 3px;
  color: #ffffff;
  position: absolute;
}
.generator-settings-text08 {
  left: 62px;
  color: #ffffff;
  bottom: 113px;
  position: absolute;
}
.generator-settings-text09 {
  top: 410px;
  left: 8px;
  color: rgb(255, 255, 255);
  position: absolute;
}
.generator-settings-text10 {
  top: 76px;
  left: 7px;
  color: white;
  position: absolute;
}
.generator-settings-text11 {
  top: 121px;
  left: 7px;
  color: #ffffff;
  position: absolute;
}
.generator-settings-text12 {
  top: 266px;
  left: 3px;
  color: #ffffff;
  position: absolute;
}
.generator-settings-checkbox1 {
  top: 268px;
  left: 192px;
  position: absolute;
}
.generator-settings-container2 {
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
.generator-settings-text13 {
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
.generator-settings-text16 {
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
.generator-settings-text22 {
  font-size: 24px;
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

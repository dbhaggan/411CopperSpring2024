<template>
<!DOCTYPE html>
<html>
<body style="background-color:#ffffff">

<div>
  <link href="./instrument-selection.css" rel="stylesheet" />
  <div class="instrument-selection-container">
    <div class="instrument-selection-container1">
      <button type="button" class="instrument-selection-button button">
        <span>
          <span>[Instrument 1]</span>
          <br />
        </span>
      </button>
      <button type="button" class="instrument-selection-button01 button">
        [Instrument 2]
      </button>
      <button type="button" class="instrument-selection-button02 button">
        [Instrument 3]
      </button>
      <button type="button" class="instrument-selection-button03 button">
        [Instrument 4]
      </button>
      <button type="button" class="instrument-selection-button04 button">
        [Instrument 5]
      </button>
    </div>
    <div class="instrument-selection-container2">
      <button type="button" class="instrument-selection-button05 button">
        <span class="instrument-selection-text03">
          <span>Practice</span>
          <br />
        </span>
      </button>
      <button type="button" class="instrument-selection-button06 button">
        <span class="instrument-selection-text06">
          <span>Collaborative Learning</span>
          <br />
        </span>
      </button>
      <button type="button" class="instrument-selection-button07 button">
        <span>
          <span>Settings</span>
          <br />
        </span>
      </button>
      <button type="button" class="instrument-selection-button08 button">
        <span class="instrument-selection-text12">
          <span>Home</span>
          <br />
        </span>
      </button>
    </div>
    <button type="button" class="instrument-selection-button09 button">
      Don&apos;t see your instrument? Request to add it!
    </button>
  </div>
</div>

</body>
</html>
</template>

<script>
export default {
  name: 'InstrumentPage',
};
</script>

<style>
.instrument-selection-container {
  width: 100%;
  display: flex;
  overflow: auto;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
  justify-content: flex-start;
  background-color: #ffffff;
}
.instrument-selection-container1 {
  top: 186px;
  flex: 0 0 auto;
  left: 346px;
  width: 1457px;
  height: 327px;
  display: flex;
  position: absolute;
  align-items: center;
  justify-content: center;
  scroll-behavior: smooth;
}
.instrument-selection-button {
  top: 0px;
  left: 55px;
  width: 226px;
  bottom: 0px;
  height: 226px;
  margin: auto;
  position: absolute;
  font-size: 29px;
}
.instrument-selection-button01 {
  top: 0px;
  left: 349px;
  width: 226px;
  bottom: 0px;
  height: 226px;
  margin: auto;
  position: absolute;
  font-size: 28px;
}
.instrument-selection-button02 {
  top: 49px;
  left: 637px;
  width: 226px;
  height: 226px;
  margin: auto;
  position: absolute;
  font-size: 28px;
}
.instrument-selection-button03 {
  top: 49px;
  left: 909px;
  width: 226px;
  height: 226px;
  margin: auto;
  position: absolute;
  font-size: 28px;
}
.instrument-selection-button04 {
  right: 37px;
  width: 226px;
  bottom: 56px;
  height: 226px;
  margin: auto;
  position: absolute;
  font-size: 28px;
}
.instrument-selection-container2 {
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
.instrument-selection-button05 {
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
.instrument-selection-text03 {
  text-align: center;
}
.instrument-selection-button06 {
  color: rgb(128, 170, 255);
  width: 181px;
  height: 90px;
  opacity: 1;
  border-color: #80AAFF;
  border-width: 3px;
  background-color: rgb(0, 85, 255);
}
.instrument-selection-text06 {
  font-size: 24px;
  text-align: center;
}
.instrument-selection-button07 {
  color: rgb(128, 170, 255);
  width: 181px;
  height: 90px;
  opacity: 1;
  font-size: 24px;
  border-color: #80AAFF;
  border-width: 3px;
  background-color: rgb(0, 85, 255);
}
.instrument-selection-button08 {
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
.instrument-selection-text12 {
  font-size: 24px;
}
.instrument-selection-button09 {
  left: 903px;
  color: rgb(255, 255, 255);
  width: 233px;
  bottom: 231px;
  height: 95px;
  position: absolute;
  font-size: 18px;
  text-align: center;
  background-color: rgb(0, 0, 0);
}
</style>

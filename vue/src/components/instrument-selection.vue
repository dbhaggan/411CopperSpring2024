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
.instrument-selection-text03 {
  text-align: center;
}
.instrument-selection-text06 {
  font-size: 24px;
  text-align: center;
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

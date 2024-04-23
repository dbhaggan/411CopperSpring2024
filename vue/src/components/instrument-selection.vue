<template>
<!DOCTYPE html>
<html>
<body style="background-color:#ffffff">

<div>
  <link href="./instrument-selection.css" rel="stylesheet" />
  <div class="instrument-selection-container">
    <div class="instrument-selection-scrolling-container">
      <button type="button" class="instrument-1 button">
        [Instrument 1]
      </button>
      <button type="button" class="instrument-2 button">
        [Instrument 2]
      </button>
      <button type="button" class="instrument-3 button">
        [Instrument 3]
      </button>
      <button type="button" class="instrument-4 button">
        [Instrument 4]
      </button>
      <button type="button" class="instrument-5 button">
        [Instrument 5]
      </button>
    </div>
    <button type="button" class="request-instrument button">
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
  align-items: center;
  flex-direction: column;
  justify-content: flex-start;
  background-color: #ffffff;
}
.instrument-selection-scrolling-container {
  top: 400px;
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
.instrument-1 {
  top: 0px;
  left: 55px;
  width: 226px;
  height: 226px;
  margin: auto;
  position: absolute;
  font-size: 29px;
}
.instrument-2 {
  top: 0px;
  left: 349px;
  width: 226px;
  height: 226px;
  margin: auto;
  position: absolute;
  font-size: 28px;
}
.instrument-3 {
  top: 0px;
  left: 637px;
  width: 226px;
  height: 226px;
  margin: auto;
  position: absolute;
  font-size: 28px;
}
.instrument-4 {
  top: 0px;
  left: 909px;
  width: 226px;
  height: 226px;
  margin: auto;
  position: absolute;
  font-size: 28px;
}
.instrument-5 {
  top: 0px;
  right: 37px;
  width: 226px;
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
.request-instrument {
  left: 903px;
  color: rgb(255, 255, 255);
  width: 233px;
  top: 700px;
  height: 95px;
  position: absolute;
  font-size: 18px;
  text-align: center;
  background-color: rgb(0, 0, 0);
}
</style>

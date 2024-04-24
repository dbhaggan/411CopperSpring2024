<template>
  <div class="instrument-request-container">
      <div class="instrument-request-container3">
        <input
          type="text"
          placeholder="Instrument Name"
          class="instrument-request-textinput input"/>
        <label class="instrument-request-text">
          What instrument would you like to add?
        </label>
        <button type="submit" class="instrument-request-button button">
          Request
        </button>
      </div>
  </div>
</template>

<script>
export default {
  name: 'InstrumentRequest',
  props: {},
  metaInfo: {
    title: 'InstrumentRequest - PercussAtSight',
    meta: [
      {
        property: 'og:title',
        content: 'InstrumentRequest - PercussAtSight',
      },
    ],
  },
}
</script>

<style scoped>
.instrument-request-container {
  width: 100%;
  display: flex;
  overflow: auto;
  align-items: center;
  flex-direction: column;
}
.instrument-request-navlink {
  display: contents;
}
.instrument-request-container3 {
  width: 760px;
  height: 500px;
  display: flex;
  position: relative;
  align-self: center;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}
.instrument-request-textinput {
  top: 164px;
  left: 0px;
  right: 0px;
  width: 252px;
  height: 36px;
  margin: auto;
  position: absolute;
}
.instrument-request-text {
  top: 100px;
  color: var(--dl-color-gray-black);
  right: 75px;
  margin: auto;
  position: absolute;
  font-size: 32px;
}
.instrument-request-button {
  top: 264px;
  left: 0px;
  right: 0px;
  width: 164px;
  height: 48px;
  margin: auto;
  position: absolute;
}
</style>

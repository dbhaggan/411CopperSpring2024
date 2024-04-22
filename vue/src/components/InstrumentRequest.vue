<template>
  <div class="instrument-request-container"
    ><div class="instrument-request-container1"
      ><div class="instrument-request-container2"
        ><router-link to="/" class="instrument-request-navlink"
          ><img
            alt="image"
            src="/percussatsight_logo-1500h.png"
            class="instrument-request-image" /></router-link></div
      ><div class="instrument-request-container3"
        ><input
          type="text"
          placeholder="Instrument Name"
          class="instrument-request-textinput input"
        /><label class="instrument-request-text"
          >What instrument would you like to add?</label
        ><button type="submit" class="instrument-request-button button"
          >Request</button
        ></div
      ></div
    ></div
  >
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
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
}
.instrument-request-container1 {
  width: 100%;
  display: flex;
  overflow: auto;
  position: relative;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
}
.instrument-request-container2 {
  flex: 0 0 auto;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: var(--dl-color-gray-white);
}
.instrument-request-navlink {
  display: contents;
}
.instrument-request-image {
  width: 400px;
  object-fit: cover;
  text-decoration: none;
}
.instrument-request-container3 {
  width: 760px;
  height: 727px;
  display: flex;
  position: relative;
  align-self: center;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}
.instrument-request-textinput {
  top: 313px;
  left: 0px;
  right: 0px;
  width: 252px;
  height: 72px;
  margin: auto;
  position: absolute;
}
.instrument-request-text {
  top: 249px;
  color: var(--dl-color-gray-black);
  right: 75px;
  margin: auto;
  position: absolute;
  font-size: 32px;
}
.instrument-request-button {
  top: 413px;
  left: 0px;
  right: 0px;
  width: 164px;
  height: 48px;
  margin: auto;
  position: absolute;
}
</style>

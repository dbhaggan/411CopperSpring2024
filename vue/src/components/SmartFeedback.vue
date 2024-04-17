<template>
  <!DOCTYPE html>
  <html>
    <body> <!--style="background-color: #ffffff">-->
      <div>
        <link href="../assets/feedback.css" rel="stylesheet" />
        <div class="feedback-container">
          <span class="feedback-text">Feedback Report </span> 
          <span class="feedback-text01">Play Time: </span> 
          <span class="feedback-text02">Missed Notes: </span> 
          <span class="feedback-text03">Accuracy: </span> 
          <span class="feedback-text04">Tempo: </span> 
          <span class="feedback-text05">Here&apos;s what our AI had to say!</span>
          <span class="feedback-text06">Note Consistency: </span>
          <span class="feedback-text07">Dynamics: </span>
          <span class="feedback-text08">Tips: </span>
          <div class="feedback-container1">
            <button type="button" class="feedback-button button">
              <span class="feedback-text09">
                <span>Practice</span>
                <br />
              </span>
            </button>
            <button type="button" class="feedback-button1 button">
              <span class="feedback-text12">
                <span>Collaborative Learning</span>
                <br />
              </span>
            </button>
            <button type="button" class="feedback-button2 button">
              <span>
                <span>Settings</span>
                <br />
              </span>
            </button>
            <button type="button" class="feedback-button3 button">
              <RouterLink to="/home">
                <span class="feedback-text18">
                  <span>Home</span>
                  <br />
                </span>
              </RouterLink>
            </button>
          </div>
        </div>
      </div>
    </body>
    <RouterView/>
  </html>
</template>

<script>
export default {
  name: 'SmartFeedback',
};
</script>

<style>
.container {
  width: 100%;
  display: flex;
  overflow: auto;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  background-color: #ffffff;
}
.text {
  top: 34px;
  left: 606px;
  color: rgb(255, 255, 255);
  position: absolute;
  font-size: 96px;
  text-decoration: underline;
}
.text01 {
  top: 300px;
  left: 739px;
  color: rgb(255, 255, 255);
  position: absolute;
  font-size: 28px;
}
.text02 {
  top: 382px;
  left: 738px;
  color: #000000;
  position: absolute;
  font-size: 28px;
}
.text03 {
  top: 491px;
  left: 930px;
  color: rgb(255, 255, 255);
  position: absolute;
  font-size: 28px;
}
.text04 {
  top: 557px;
  left: 763px;
  color: rgb(255, 255, 255);
  position: absolute;
  font-size: 28px;
}
.text05 {
  top: 216px;
  left: 835px;
  color: #000000;
  position: absolute;
  font-size: 28px;
}
.text06 {
  top: 608px;
  left: 760px;
  color: rgb(255, 255, 255);
  position: absolute;
  font-size: 28px;
}
.text07 {
  top: 661px;
  left: 760px;
  color: rgb(255, 255, 255);
  position: absolute;
  font-size: 28px;
}
.text08 {
  top: 800px;
  left: 939px;
  color: rgb(255, 255, 255);
  position: absolute;
  font-size: 28px;
}
.container1 {
  width: 181px;
  height: 1080px;
  display: flex;
  position: relative;
  align-self: flex-start;
  align-items: center;
  flex-direction: column;
  justify-content: flex-start;
  background-color: #0055ff;
}
.button {
  color: rgb(128, 170, 255);
  width: 181px;
  height: 90px;
  opacity: 1;
  font-size: 24px;
  border-color: #80aaff;
  border-width: 3px;
  text-transform: capitalize;
  background-color: rgb(0, 85, 255);
}
.text09 {
  text-align: center;
}
.button1 {
  color: rgb(128, 170, 255);
  width: 181px;
  height: 90px;
  opacity: 1;
  border-color: #80aaff;
  border-width: 3px;
  background-color: rgb(0, 85, 255);
}
.text12 {
  font-size: 24px;
  text-align: center;
}
.button2 {
  color: rgb(128, 170, 255);
  width: 181px;
  height: 90px;
  opacity: 1;
  font-size: 24px;
  border-color: #80aaff;
  border-width: 3px;
  background-color: rgb(0, 85, 255);
}
.button3 {
  color: rgb(128, 170, 255);
  right: 0px;
  width: 181px;
  bottom: 0px;
  height: 90px;
  opacity: 1;
  position: absolute;
  border-color: #80aaff;
  border-width: 3px;
  background-color: rgb(0, 85, 255);
}
.text18 {
  font-size: 24px;
}
</style>

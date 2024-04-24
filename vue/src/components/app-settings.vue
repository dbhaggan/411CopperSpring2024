<template>
<div>
  <div class="app-settings-container">
    <h1 class="title-text">Settings</h1>
    <span class="trial-info-text">Trial Info:</span>
    <button type="button" class="subscribe button">
      Become a Subscriber!
    </button>
    <span class="subscription-info-text">
      <span>Subscription Info:</span>
      <br />
    </span>
    <span class="profile-info-text">Profile Info:</span>
    <span class="peripheral-settings-text">Peripheral Settings:</span>
    <span class="subscription-plan-text">Subscription Plan: _______________</span>
    <span class="payment-info-text">Payment Info: ****************************</span>
    <button type="button" class="change-plan button">
      Change Your Plan?
    </button>
    <button type="button" class="cancel button">
      Cancel Subscription
    </button>
    <button type="button" class="change-payment button">
      Change Payment Details
    </button>
    <span class="username-text">Username: ____________</span>
    <button type="button" class="edit button">Edit</button>
    <span class="email-text">
      <span>Email: *************@*********</span>
      <br />
    </span>
    <button type="button" class="change-password button">
      Change Password
    </button>
    <span class="midi-device-text">MIDI Device:</span>
    <span class="microphone-text">Microphone:</span>
    <button type="button" class="change-device-1 button">
      Change Device
    </button>
    <button type="button" class="change-device-2 button">
      Change Device
    </button>
    <span class="buffer-text">Help! I'm trapped in a drum practice website!</span>
  </div>
</div>
</template>

<script>
export default {
  name: 'AppSettingsPage',
};
</script>

<style>
.app-settings-container {
  width: 100%;
  display: flex;
  overflow: auto;
  /*min-height: 700px;*/
  align-items: flex-start;
  flex-direction: column;
  justify-content: flex-end;
  background-color: #ffffff;
}
.title-text {
  top: 360px;
  left: 810px;
  color: #000000;
  position: absolute;
  font-size: 4em;
}
.trial-info-text {
  top: 520px;
  left: 160px;
  color: #000000;
  position: absolute;
  font-size: 36px;
  text-decoration: underline;
}
.subscribe {
  top: 595px;
  left: 160px;
  color: #000000;
  font-size: 16px;
  width: 185px;
  height: 35px;
  display: flex;
  position: absolute;
  flex-direction: row;
  background-color: #dddddd;
}
.subscription-info-text {
  top: 670px;
  left: 160px;
  color: #000000;
  position: absolute;
  font-size: 36px;
  text-decoration: underline;
}
.profile-info-text {
  top: 890px;
  left: 160px;
  color: #000000;
  position: absolute;
  font-size: 36px;
  text-decoration: underline;
}
.peripheral-settings-text {
  top: 1080px;
  left: 160px;
  color: #000000;
  position: absolute;
  font-size: 36px;
  text-decoration: underline;
}
.subscription-plan-text {
  top: 725px;
  left: 160px;
  color: #000000;
  position: absolute;
  font-size: 24px;
}
.payment-info-text {
  top: 835px;
  left: 160px;
  color: #000000;
  position: absolute;
  font-size: 24px;
}
.change-plan {
  top: 780px;
  left: 160px;
  color: #000000;
  width: 157px;
  height: 38px;
  font-size: 16px;
  position: absolute;
  padding-top: 0px;
  padding-left: 0px;
  padding-right: 0px;
  padding-bottom: 0px;
  background-color: #dddddd;
}
.cancel {
  top: 780px;
  left: 363px;
  font-size: 16px;
  color: #000000;
  width: 170px;
  height: 40px;
  position: absolute;
  padding-left: 0px;
  padding-right: 0px;
  background-color: #dddddd;
}
.change-payment {
  top: 835px;
  left: 590px;
  color: #000000;
  font-size: 16px;
  width: 200px;
  height: 40px;
  position: absolute;
  background-color: #dddddd;
}
.username-text {
  top: 952px;
  left: 160px;
  color: #000000;
  position: absolute;
  font-size: 24px;
}
.edit {
  top: 952px;
  left: 466px;
  font-size: 16px;
  width: 74px;
  height: 30px;
  color: #000000;
  background-color: #dddddd;
  position: absolute;
}
.email-text {
  top: 994px;
  left: 160px;
  color: #000000;
  position: absolute;
  font-size: 24px;
}
.change-password {
  top: 1023px;
  left: 160px;
  font-size: 16px;
  width: 200px;
  height: 40px;
  position: absolute;
  color: #000000;
  background-color: #dddddd;
}
.midi-device-text {
  top: 1125px;
  left: 160px;
  color: #000000;
  position: absolute;
  font-size: 24px;
}
.microphone-text {
  top: 1215px;
  left: 160px;
  color: #000000;
  position: absolute;
  font-size: 24px;
}
.change-device-1 {
  top: 1170px;
  left: 160px;
  height: 40px;
  font-size: 16px;
  position: absolute;
  color: #000000;
  background-color: #dddddd;
}
.change-device-2 {
  top: 1260px;
  left: 160px;
  height: 40px;
  font-size: 16px;
  position: absolute;
  color: #000000;
  background-color: #dddddd;
}
.buffer-text {
  top: 1350px;
  left: 0px;
  color: #ffffff;
  position: absolute;
  font-size: 9px;
}
</style>

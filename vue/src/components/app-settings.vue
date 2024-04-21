<template>
<div>
  <div class="app-settings-container">
    <h1 class="app-settings-text">Settings</h1>
    <span class="trial-info">Trial Info:</span>
    <button type="button" class="subscribe button">
      Become a Subscriber!
    </button>
    <span class="subscription-info">
      <span>Subscription Info:</span>
      <br />
    </span>
    <span class="app-settings-text08">Profile Info:</span>
    <span class="app-settings-text09">Peripheral Settings:</span>
    <span class="app-settings-text10">Subscription Plan:</span>
    <span class="app-settings-text11">Payment Info:</span>
    <button type="button" class="change-plan button">
      Change Your Plan?
    </button>
    <button type="button" class="cancel button">
      Cancel Subscription
    </button>
    <button type="button" class="change-payment button">
      Change Payment Details
    </button>
    <span class="app-settings-text12">Username:</span>
    <button type="button" class="edit button">Edit</button>
    <span class="app-settings-text13">
      <span>Email:</span>
      <br />
    </span>
    <button type="button" class="change-password button">
      Change Password
    </button>
    <span class="app-settings-text16">MIDI Device:</span>
    <span class="app-settings-text17">Microphone:</span>
    <button type="button" class="change-device-1 button">
      Change Device
    </button>
    <button type="button" class="change-device-2 button">
      Change Device
    </button>
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
  min-height: 100vh;
  align-items: flex-start;
  flex-direction: column;
  justify-content: flex-end;
  background-color: #ffffff;
}
.app-settings-text {
  top: 60px;
  left: 826px;
  color: #000000;
  position: absolute;
  font-size: 4em;
}
.trial-info {
  top: 177px;
  left: 167px;
  color: #000000;
  position: absolute;
  font-size: 36px;
  text-decoration: underline;
}
.subscribe {
  top: 227px;
  left: 160px;
  color: #000000;
  font-size: 16px;
  width: 175px;
  height: 27px;
  display: flex;
  position: absolute;
  flex-direction: row;
  background-color: #ffffff;
}
.subscription-info {
  top: 334px;
  left: 156px;
  color: #000000;
  position: absolute;
  font-size: 36px;
  text-decoration: underline;
}
.app-settings-text08 {
  top: 551px;
  left: 167px;
  color: #000000;
  position: absolute;
  font-size: 36px;
  text-decoration: underline;
}
.app-settings-text09 {
  top: 748px;
  left: 154px;
  color: #000000;
  position: absolute;
  font-size: 36px;
  text-decoration: underline;
}
.app-settings-text10 {
  top: 383px;
  left: 161px;
  color: #000000;
  position: absolute;
  font-size: 24px;
}
.app-settings-text11 {
  top: 467px;
  left: 158px;
  color: #000000;
  position: absolute;
  font-size: 24px;
}
.change-plan {
  top: 418px;
  left: 157px;
  color: #000000;
  width: 157px;
  height: 38px;
  font-size: 16px;
  position: absolute;
  padding-top: 0px;
  padding-left: 0px;
  padding-right: 0px;
  padding-bottom: 0px;
  background-color: #ffffff;
}
.cancel {
  top: 417px;
  left: 363px;
  font-size: 16px;
  color: #000000;
  width: 170px;
  height: 40px;
  position: absolute;
  padding-left: 0px;
  padding-right: 0px;
  background-color: #ffffff;
}
.change-payment {
  top: 463px;
  left: 636px;
  color: #000000;
  font-size: 16px;
  width: 200px;
  height: 40px;
  position: absolute;
  background-color: #ffffff;
}
.app-settings-text12 {
  top: 606px;
  left: 170px;
  color: #000000;
  position: absolute;
  font-size: 24px;
}
.edit {
  top: 597px;
  left: 466px;
  font-size: 16px;
  width: 74px;
  height: 30px;
  color: #000000;
  background-color: #ffffff;
  position: absolute;
}
.app-settings-text13 {
  top: 648px;
  left: 167px;
  color: #000000;
  position: absolute;
  font-size: 24px;
}
.change-password {
  top: 686px;
  left: 168px;
  font-size: 16px;
  width: 200px;
  height: 40px;
  position: absolute;
  color: #000000;
  background-color: #ffffff;
}
.app-settings-text16 {
  top: 808px;
  left: 162px;
  color: #000000;
  position: absolute;
  font-size: 24px;
}
.app-settings-text17 {
  left: 165px;
  color: #000000;
  bottom: 221px;
  position: absolute;
  font-size: 24px;
}
.change-device-1 {
  left: 156px;
  bottom: 265px;
  height: 40px;
  font-size: 16px;
  position: absolute;
  color: #000000;
  background-color: #ffffff;
}
.change-device-2 {
  left: 160px;
  bottom: 160px;
  height: 40px;
  font-size: 16px;
  position: absolute;
  color: #000000;
  background-color: #ffffff;
}
</style>

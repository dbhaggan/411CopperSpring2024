<template>
  <!DOCTYPE html>
  <html>
    <body> <!--style="background-color: #ffffff">-->
      <div>
        <link href="../assets/feedback.css" rel="stylesheet" />
        <div class="feedback-container">
          <p>Audio score</p>
          <div id="exampleAudioScore"></div> 
          <p>MIDI score</p>
          <div id="exampleMIDIScore"></div> 
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

/* global Vex */
export default {
  name: 'SmartFeedback',
  mounted(){
    this.displayAudioExample();
    this.displayMidiExample(); 
  },
    methods: {
    displayAudioExample(){

      const {        
      Renderer, Stave, StaveNote, Voice, Formatter, Beam, KeySignature} = Vex.Flow; 

      const div = document.getElementById('exampleAudioScore');
      const renderer = new Renderer(div, Renderer.Backends.SVG);

      renderer.resize(600, 600);
      const context = renderer.getContext();
      const stave = new Stave(10, 40, 420);
      stave.addClef("treble").addTimeSignature('4/4');

      const keySignature = new KeySignature('G');    
      keySignature.addToStave(stave); 

      stave.setContext(context).draw(); 

      const notes = [
          new StaveNote({
              keys: ['D/4'],
              duration: '8'
          }),
          new StaveNote({
              keys: ['D/5'],
              duration: '8'
          }),
          new StaveNote({
              keys: ['G/5'],
              duration: '8'
          }),
          new StaveNote({
              keys: ['A/5'], 
              duration: '8'
          }),
          new StaveNote({
              keys: ['B/5'],
              duration: 'q'
          }),
          new StaveNote({
              keys: ['G/5'],
              duration: 'q'
          }),
      ];

      const beamGroups1 = [
      notes[0], notes[1] 
      ];

      const beamGroups2 = [
      notes[2], notes[3]
      ];

      const beams = [new Beam(beamGroups1)]; 
      const beams2 = [new Beam(beamGroups2)]; 

      const voices = [
      new Voice({
          num_beats: 4,
          beat_value: 4
      }).addTickables(notes),
      ];

      new Formatter().joinVoices(voices).format(voices, 350);

      voices.forEach(function(v) {
      v.draw(context, stave);
      }); 

      beams.forEach((b) => {
      b.setContext(context).draw();
      });

      beams2.forEach((b) => {
      b.setContext(context).draw();
      });

      // Positioning score in middle of page 
      const scorePosition = document.getElementById('exampleAudioScore');
      const centerScore = () => {
      scorePosition.style.marginLeft = window.innerWidth/1.75 - scorePosition.clientWidth/1.75 + 'px'; 
      scorePosition.style.marginTop = window.innerHeight/40- scorePosition.clientHeight/40 + 'px'; 
      }

      centerScore();
      window.addEventListener('resize', centerScore); 

    },

    displayMidiExample(){

      const {        
      Renderer, Stave, StaveNote, Voice, Formatter, StaveTie, KeySignature} = Vex.Flow; 

      const div = document.getElementById('exampleMIDIScore');
      const renderer = new Renderer(div, Renderer.Backends.SVG);

      renderer.resize(600, 600);
      const context = renderer.getContext();
      const stave = new Stave(10, 40, 420);
      stave.addClef("treble").addTimeSignature('4/4');

      const keySignature = new KeySignature('Db');    
      keySignature.addToStave(stave); 

      stave.setContext(context).draw(); 

      const notes = [
          new StaveNote({
              keys: ['B/3'],
              duration: '8'
          }),
          new StaveNote({
              keys: ['A/3'],
              duration: 'q'
          }),
          new StaveNote({
              keys: ['B/3'],
              duration: '8'
          }),
          new StaveNote({
              keys: ['C/4'],
              duration: 'q'
          }),
          new StaveNote({
              keys: ['D/4'],
              duration: 'q'
          }),
      ];

      const ties = [
          new StaveTie({
              first_note: notes[1],
              last_note: notes[2],
              first_indices: [0],
              last_indices: [0],
          }),
      ];

      const voices = [
      new Voice({
          num_beats: 4,
          beat_value: 4
      }).addTickables(notes),
      ];

      new Formatter().joinVoices(voices).format(voices, 350);

      voices.forEach(function(v) {
      v.draw(context, stave);
      });

      ties.forEach((t) => {
          t.setContext(context).draw();
      });    

      // Positioning score in middle of page 
      const scorePosition = document.getElementById('exampleMIDIScore');
      const centerScore = () => {
      scorePosition.style.marginLeft = window.innerWidth/1.75 - scorePosition.clientWidth/1.75 + 'px'; 
      scorePosition.style.marginTop = window.innerHeight/40- scorePosition.clientHeight/40 + 'px'; 
      }

      centerScore();
      window.addEventListener('resize', centerScore); 

    }


  },

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

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
            <div>
              <button @click="fetchData" class="feedback-button" v-on:click = "generateExampleNumericalScore">
                Generate Feedback Report
              </button>
            </div>
          <span class="feedback-report-text">Feedback Report </span> 
          <span class="playtime-text">Play Time: </span> 
          <span class="missed-notes-text">Missed Notes: </span> 
          <span class="accuracy-text">Accuracy: </span> 
          <span class="tempo-text">Tempo: </span> 
          <span class="ai-text">Here&apos;s what our AI had to say!</span>
          <span class="note-consistency-text">Note Consistency: </span>
          <span class="dynamics-text">Dynamics: </span>
          <span class="tips-text">Tips: </span>
          <div v-if="showScores">
            <p>Numerical score for audio piece: {{ audioScore }}</p>
            <p>Numerical score for midi piece: {{ midiScore }}</p>
          </div>
          <div v-else>
            <p>Numerical score for audio piece: Not yet generated</p>
            <p>Numerical score for midi piece: Not yet generated</p>
          </div>
        </div>
      </div>
    </body>
    <RouterView/>
  </html>
</template>

<script>
import axios from 'axios';

/* global Vex */
/* eslint-disable no-unused-vars */
export default {
  name: 'SmartFeedback',
  mounted(){
    this.displayAudioExample();
    this.displayMidiExample(); 
  },
  data() {
    return {
        feedbackData: null,
        showData: false,
        audioScore: 0,
        midiScore: 0,
        showScores: false
    };
  },
  methods: {
    fetchData() {
      axios.get('http://localhost:8080/api-feedback')
        .then(response => {
          this.feedbackData = response.data;
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },

    displayAudioExample(){

      const {        
      Renderer, Stave, StaveNote, Voice, Formatter, Beam, KeySignature} = Vex.Flow; 

      const div = document.getElementById('exampleAudioScore');
      const renderer = new Renderer(div, Renderer.Backends.SVG);

      renderer.resize(600, 300);
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

      renderer.resize(600, 300);
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

    },
    
    /* eslint-disable no-unused-vars */
    generateExampleNumericalScore() {
        
        class Note { //class that encodes a Note
            constructor(time, duration, note, octave, scale) {
                this.time=time; this.duration=duration; //(in seconds)
               this.note=note; this.octave=octave; this.scale=scale;
            }
            
            getPitch() { //combines note and octave into the objective pitch
                return this.octave*this.scale+this.note;
            }
            
            timeDiff(note2) { //difference between two notes in terms of time
                return Math.abs(this.time-note2.time);
            }
        }

        function comparePercussionNotes(note1_orig, note2_orig, note1_comp, note2_comp) {
            return Math.abs(Math.log( note1_orig.timeDiff(note2_orig) / note1_comp.timeDiff(note2_comp)));
            //EXPLANATION: Human perception of time is logarithmic. That is to say, if you were supposed to play two notes 1 second apart,
            //but you mess up, playing them 1/4 second apart is twice as bad as playing them 1/2 second apart. This code reflects that,
            //judging the time between notes on a logarithmic scale.
        }

        function compareSheetMusic(sheet_orig, sheet_comp) { //compares two arrays that represent sheet music
            if(sheet_orig.length!=sheet_comp.length) {
                throw new Error("Sheets must have the same number of notes!"); //We cannot yet process music with missing or added notes.
                //Doing so would require implementation of the Myers diff algorithm, which is very intricate and complicated.
            }
            
            var err = 0; //initialize error to 0
            for(var n=1;n<sheet_orig.length;n++) { //loop through all sets of notes
                err += comparePercussionNotes(sheet_orig[n-1],sheet_orig[n],sheet_comp[n-1],sheet_comp[n]); //for each pair of notes, add how bad they match up on the original vs the one we're comparing
            }
            
            return err / (sheet_orig.length-1); //divide by # of pairs of notes & return
        }

        function noteByNoteAnalysis(sheet_orig, sheet_comp) { //compares two pieces of sheet music and returns an array saying how bad each pair of sequential notes is
            if(sheet_orig.length!=sheet_comp.length) {
                throw new Error("Sheets must have the same number of notes!");
            }
            
            var comp = []; //array of all the note-by-note comparisons
            for(var n=0;n<sheet_orig.length-1;n++) { //loop through all sets of notes
                comp[n] = comparePercussionNotes(sheet_orig[n],sheet_orig[n+1],sheet_comp[n],sheet_comp[n+1]);
            }
            
            return comp; //return the array
        }

        function error_to_score(error, strictness=1) { //takes error, and converts that to a numerical score (optional: specify strictness, a positive number)
          return 100*(1-Math.tanh(strictness*error))+"%";
        }

        var audio_sheet_orig = [new Note(0,'8','D',6,6), new Note(0.75,'8','D',7,6), new Note(1.5,'8','G',7,6), new Note(2.25,'8','A',7,6), new Note(3,'q','B',7,6), new Note(3.75,'q','G',7,6)];

        var midi_sheet_orig = [new Note(0,'8','C',3,6), new Note(0.6,'q','A',3,6), new Note(1.2,'8','C',3,6), new Note(1.8,'q','C',4,6), new Note(2.4,'q','D',4,6)];


        var audio_sheet_user = [new Note(0,'8','D',6,6), new Note(0.74679,'8','D',7,6), new Note(1.49535,'8','G',7,6), new Note(2.25050,'8','A',7,6), new Note(2.99385,'q','B',7,6), new Note(3.74076,'q','F',7,6)];

        var midi_sheet_user = [new Note(0,'8','C',3,6), new Note(0.61758,'q','A',3,6), new Note(1.27523,'8','C',3,6), new Note(1.86144,'q','B',4,6), new Note(2.40894,'q','D',4,6)];
        
        this.audioScore = error_to_score(compareSheetMusic(audio_sheet_orig, audio_sheet_user));
        this.midiScore  = error_to_score(compareSheetMusic( midi_sheet_orig,  midi_sheet_user));
        this.showScores = true;
    }
  },

};

</script>

<style>

.container {
  width: 100%;
  display: flex;
  overflow: auto;
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
.text09 {
  text-align: center;
}
.text12 {
  font-size: 24px;
  text-align: center;
}
.text18 {
  font-size: 24px;
}
</style>

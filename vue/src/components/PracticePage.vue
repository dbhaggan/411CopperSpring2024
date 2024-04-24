<template>
  <!DOCTYPE html>
  <html>
    <body style="background-color: #ffffff">
      <div>
        <link href="../assets/practice.css" rel="stylesheet" />
        <div class="practice-container">
          <button type="button" class="practice-button4 button" v-on:click = "runSheetGenerator">
            <span>
              Play
            </span>
          </button>
        </div>
      </div>
    </body>
  </html>
</template>

<script>
  /* global Vex */

export default {
  name: 'VexflowComponent',
  beforeRouteLeave(to, from, next) {
      this.handleDivDeletion(); 
      next(); 
  }, 
  methods: {  
  //mounted(){

    handleDivDeletion() {
        let existingScore = document.getElementById("generatedScore"); 
        if(existingScore){
        existingScore.parentNode.removeChild(existingScore); 
        } 
      }, 
    
    runSheetGenerator (){ 

      let existingScore = document.getElementById("generatedScore"); 
      if(existingScore){
      existingScore.parentNode.removeChild(existingScore); 
      }

      // Adds a new div/svg element with same name to house Score 
      let newScore = document.createElement("div"); 
      newScore.id = "generatedScore"; 
      document.body.appendChild(newScore); 



      const {        
      Renderer, Stave, Voice, Formatter} = Vex.Flow; 

      // For generator settings 
      let clefVal = 'percussion';  // percussion, treble, bass 
                                      // SET CLEF BY REFRESHING PAGE (HAVE A BUTTON FOR THIS) 


      // Create an SVG renderer and attach it to the DIV element named "generatedScore".
      const div = document.getElementById('generatedScore');
      const renderer = new Renderer(div, Renderer.Backends.SVG);

      // Configure the rendering context.
      const context = renderer.getContext();


      let notePool = ['A', 'B', 'C', 'D', 'E', 'F', 'G']; 
      let octavePool = ['/4', '/5'];              
      let durationPool = ['q','8'];    

      // Represents Snare Drum data 
      let snareDrumNotePool = ['C']; 
      let snareDrumOctavePool = ['/5']; 

      let random1, random2, random3; 

      let beatsTotal = 8; 


      let staveArray = []; 


      let randomNote; 
      let randomDuration; 
      let stave; 
      let currentInstrument; 
      let previousInstrument; 
      let switchedInstrumentFlag = false; 
      let lastStickingElement; 
      let secondToLastStickingElement; 

      let measureLength = 40; 
      let maxMeasuresInRow = 5; 



      // Generator Settings 
      let instrumentArray = ["snare_drum", "glock"]; 
      let initialInstrument = instrumentArray[1];   
      let numberOfMeasures = 16; 
      let stickingIsOn = true; 
          let stickingBelowMeasure = false; 
      let randomAccentsAreOne = true;  



      function randomizeNoteAndOctaveForSnare(){
          let Note = snareDrumNotePool[pickRandomArrayIndex(snareDrumNotePool)]; 
          let Octave = snareDrumOctavePool[pickRandomArrayIndex(snareDrumOctavePool)]; 
          
          return Note + Octave; 
      }

      function randomizeNoteAndOctave(){
              let Note = notePool[pickRandomArrayIndex(notePool)];  
              let Octave = octavePool[pickRandomArrayIndex(octavePool)]; 
              
          return Note + Octave; 
          }


      function randomizeAccentsAndNotes (randomNote, randomDuration) {
          if (randomAccentsAreOne === true){
              if (Math.random() < 0.50){
                  return addNotes(randomNote, randomDuration);
              }
              else {
                  return addAccentedNotes(randomNote, randomDuration); 
              }
          }
          else {
              return addNotes(randomNote, randomDuration);
          }   
      }

      function addNotes (randomNote, randomDuration) {
          return new Vex.Flow.StaveNote ({
          keys: [randomNote],
          duration: randomDuration
          });  
      }

      function addAccentedNotes (randomNote, randomDuration) {
          return new Vex.Flow.StaveNote ({
          keys: [randomNote],
          duration: randomDuration
          }).addModifier(new Vex.Flow.Articulation('a>').setPosition(3), 0);  
      }

      function randomizeSticking (storeDurationForSticking, randomSticking) {
          let stickingPool = ['R', 'L']; 
          

          for (let i = 0; i < storeDurationForSticking.length; i++){
              randomSticking.push(stickingPool[pickRandomArrayIndex(stickingPool)]); 
              
              // catch unique cases 
              if ((randomSticking[i-2] === randomSticking[i] && randomSticking[i-1] === randomSticking[i]) ||
                      (i === 0 && randomSticking[0] === lastStickingElement && randomSticking[0] === secondToLastStickingElement)  ||
                      (i === 1 && randomSticking[0] === lastStickingElement && randomSticking[1] === lastStickingElement)    
                      ){
                      randomSticking[i] = (randomSticking[i] === 'R') ? 'L' : 'R';
                  } 
          }
          lastStickingElement = randomSticking[randomSticking.length-1];  
          secondToLastStickingElement = randomSticking[randomSticking.length-2];  
      }

      function createStickingText (tempDurationVar, tempStickingVar) {

          let stickingTextPos = (stickingBelowMeasure === true) ? 9 : -1;  

          return new Vex.Flow.TextNote({ 
              text: tempStickingVar,
              font: {
                  family: "Arial",
                  size: 13,
                  weight: "", 
              },
              duration: tempDurationVar               
              })
              .setLine(stickingTextPos) 
              .setStave(stave)
              .setJustification(Vex.Flow.TextNote.Justification.LEFT)  
      }

      function checkToMakeNewRow () {
          measureLength+=140;  
          addStave(10, measureLength, 280); 
      }

      function splitMeasuresRandomly(totalNumOfMeasures) {

          if (totalNumOfMeasures < instrumentArray.length || totalNumOfMeasures < 3) { 
              alert("Error! Pick a measure count that's higher than the total number of instruments you've selected!"); 
          }
          else if (totalNumOfMeasures <= 12) { 
              do {
                  random1 = Math.floor(Math.random() * totalNumOfMeasures);
                  random2 = Math.floor(Math.random() * (totalNumOfMeasures - random1));
                  random3 = totalNumOfMeasures - random1 - random2;
                  } while (random1 === 0 || random2 === 0 || random3 === 0);  
              }  
          else {
              do {
                random1 = Math.floor(Math.random() * totalNumOfMeasures);
                random2 = Math.floor(Math.random() * (totalNumOfMeasures - random1));
                random3 = totalNumOfMeasures - random1 - random2;
              } while (random1 <= 3 || random2 <= 3 || random3 <= 3
                          || random1 === 0 || random2 === 0 || random3 === 0);
              } 

      return [random1, random2, random3]; 
      }


      function drawSwitchInstrumentText (){
          if ((switchedInstrumentFlag != true && staveArray.length != 2) || switchedInstrumentFlag != false){
              return new Vex.Flow.TextNote({ // Added TextNote at top, initially declare it here 
              text: currentInstrument,
              font: {
                  family: "Arial",
                  size: 13,
                  weight: "", 
                  style: "italic"
              },
              duration: 'w'               
              })
              .setLine(-3) 
              .setStave(stave)
              .setJustification(Vex.Flow.TextNote.Justification.LEFT)  
          }
      }

      function checkToUpdateClef() {
          if(previousInstrument === currentInstrument){
              switchedInstrumentFlag = false;  
              return; 
          }
          else if (previousInstrument != currentInstrument){
              if (currentInstrument === "snare_drum" || currentInstrument === "drumset"){ // test drumset later 
                  clefVal = "percussion"; 
                  previousInstrument = currentInstrument; 
                  switchedInstrumentFlag = true; 
                  return stave.addClef(clefVal).addTimeSignature('4/4'); 
              }
              else if (currentInstrument === "glock")
                  clefVal = "treble"; 
                  previousInstrument = currentInstrument; 
                  switchedInstrumentFlag = true;  
                  return stave.addClef(clefVal).addTimeSignature('4/4'); 
              // CHANGE CLEF, check each instrument to determine the clef 
          }
      }

      function addStave(x,y,width) { 
        stave = new Stave (x,y,width)
        checkToUpdateClef(); 
        // stave.addClef(clefVal).addTimeSignature('4/4'); 
        stave.setContext(context).draw(); 
        staveArray.push(stave); 
      }  

      function addInitialStave(x,y,width) {  // invisible stave 
        stave = new Stave (x,y,width)
        staveArray.push(stave); 
      }  



      function pickRandomArrayIndex(Array){   
      // picks a random array index 
      return Math.floor(Math.random() * Array.length); 
      }

      function randomizeDuration(){
      let Duration = durationPool[pickRandomArrayIndex(durationPool)];  

      return Duration; 
      }



      function setBeatsLeftInMeasure (durationToSet) {
      if ( beatsTotal === 1 && durationToSet == 'q'){  // catches situation if beatsTotal = 1, but the note randomize is 'q' 
          beatsTotal = beatsTotal - 1; 
          return '8';     // Changes Duration so there's a sufficient number of notes in measure 
      }
      else if(durationToSet == 'q'){
          beatsTotal = beatsTotal - 2; 
      }
      else if (durationToSet == '8') {
          beatsTotal = beatsTotal - 1; 
      }
      }

      function addVoices(Array){
        console.log(Array); 
        return new Voice({
        num_beats: 4,
        beat_value: 4
        }).addTickables(Array);            
      }

      // creates the random Note and Duration then outputs it into Vexflow API 
      function createRandomGlockNote(){        
          randomNote = randomizeNoteAndOctave();  
          randomDuration =  randomizeDuration(); 

          if (beatsTotal === 1 && randomDuration === "q"){
          let durationInQuestion = randomDuration; 
          randomDuration = setBeatsLeftInMeasure(durationInQuestion); 
          }
          else{
              setBeatsLeftInMeasure (randomDuration); 
          }

      return randomizeAccentsAndNotes (randomNote, randomDuration); 

      }

      function createMeasureForGlock(numOfMeasures){
          currentInstrument = "glock"; 

          for (let i = 1; i <= numOfMeasures; i++){ 
              if (staveArray.length === maxMeasuresInRow) { 
                  maxMeasuresInRow+=4;  
                  checkToMakeNewRow (); 
              }
              else {
                  const prevStave = staveArray[staveArray.length - 1]; 
                  addStave(prevStave.width + prevStave.x, measureLength, 280); 
              }

              // reinitialize variables with new measure 
              let notes = []; 
              let voices = []; 
              let storeArrayForVoices = []; 
              let textNoteArray = []; 
              beatsTotal = 8; 
              while(beatsTotal != 0) {
                  randomNote = createRandomGlockNote(); 
                  console.log(beatsTotal); 
                  if (notes.length > 7){    // Catches error where generated notes surpass array limit, Will make this more dynamic 
                      console.log("ERROR MAX ARRAY LIMIT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   " + notes.length); 
                      break;  
                  }
                  else {
                      notes.push(randomNote); // push created notes in array for vexflow to format and render to screen 
                  }
              }
              storeArrayForVoices.push(notes); // store array for voices 
          
              let tempTextVar = drawSwitchInstrumentText (); 

              if (switchedInstrumentFlag === true && staveArray.length != 2){
                  textNoteArray.push(tempTextVar); 
                  storeArrayForVoices.push(textNoteArray);
              }

              let tempVoiceVar = []; 

              for (let k = 0; k < storeArrayForVoices.length; k++){
                  tempVoiceVar = addVoices(storeArrayForVoices[k]);
                      console.log("TESTING THE tempVoiceVar " + tempVoiceVar); 
                  voices.push(tempVoiceVar);     
              }

              new Formatter().joinVoices(voices).format(voices, 200);

              // Render voices.
              voices.forEach(function(v) {
              v.draw(context, stave);
              });
          }
      }



      function createRandomSnareDrumNote(storeDurationForSticking){

          randomNote = randomizeNoteAndOctaveForSnare();  
          randomDuration =  randomizeDuration(); 

          if (beatsTotal === 1 && randomDuration === "q"){
          let durationInQuestion = randomDuration; 
          randomDuration = setBeatsLeftInMeasure(durationInQuestion); 
          storeDurationForSticking.push(randomDuration); 
          }
          else{
              setBeatsLeftInMeasure (randomDuration); 
              storeDurationForSticking.push(randomDuration); 
          }

      return randomizeAccentsAndNotes (randomNote, randomDuration); 

      }

      function createMeasureForSnareDrum(numOfMeasures){
          currentInstrument = "snare_drum"; 

          for (let i = 1; i <= numOfMeasures; i++){
              if (staveArray.length === maxMeasuresInRow) { 
                  maxMeasuresInRow+=4;  
                  checkToMakeNewRow (); 
              }
              else {
                  const prevStave = staveArray[staveArray.length - 1]; 
                  addStave(prevStave.width + prevStave.x, measureLength, 280); 
              }

              // reinitialize variables with new measure 
              let notes = []; 
              let voices = []; 
              let storeArrayForVoices = []; 
              let textNoteArray = []; 
              
              let storeDurationForSticking = []; 
              let randomStickings = []; 
              let stickingTextArray = []; 
              beatsTotal = 8; 
              while(beatsTotal != 0) {
                  randomNote = createRandomSnareDrumNote(storeDurationForSticking); 
                  console.log(beatsTotal); 
                  if (notes.length > 7){    
                      console.log("ERROR MAX ARRAY LIMIT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   " + notes.length); 
                      break;  
                  }
                  else {
                      notes.push(randomNote); 
                  }
              }
              storeArrayForVoices.push(notes); 

              let tempTextVar = drawSwitchInstrumentText (); 

              if (switchedInstrumentFlag === true && staveArray.length != 2){
                  textNoteArray.push(tempTextVar); 
                  storeArrayForVoices.push(textNoteArray);
              }

            
              if (stickingIsOn === true){
                  // sticking 
                  randomizeSticking(storeDurationForSticking, randomStickings); 

                  for (let j = 0; j < storeDurationForSticking.length; j++){
                      let tempDurationVar = storeDurationForSticking[j]; 
                      let tempStickingVar = randomStickings[j]; 
                      let stickingText = createStickingText(tempDurationVar, tempStickingVar); 

                      stickingTextArray.push(stickingText); 
                  }
                  storeArrayForVoices.push(stickingTextArray); 
              }

              let tempVoiceVar = []; 

              for (let k = 0; k < storeArrayForVoices.length; k++){
                  tempVoiceVar = addVoices(storeArrayForVoices[k]);
                      console.log("TESTING THE tempVoiceVar " + tempVoiceVar); 
                  voices.push(tempVoiceVar);     
              }

              new Formatter().joinVoices(voices).format(voices, 200);

              // Render voices.
              voices.forEach(function(v) {
              v.draw(context, stave);
              });
          }
      }

      renderer.resize(1200, 2000); 
      addInitialStave(0,0,0); 



      let [section1, section2, section3] = splitMeasuresRandomly(numberOfMeasures);



      if(initialInstrument === "snare_drum"){
          createMeasureForSnareDrum(section1); 
          createMeasureForGlock(section2);     
          createMeasureForSnareDrum(section3); 
      }
      else if(initialInstrument === "glock"){
          createMeasureForGlock(section1);     
          createMeasureForSnareDrum(section2); 
          createMeasureForGlock(section3);  
      }


      // Positioning score in middle of page 
      const scorePosition = document.getElementById('generatedScore');
      const centerScore = () => {
        scorePosition.style.marginLeft = window.innerWidth/1.75 - scorePosition.clientWidth/1.75 + 'px'; 
        scorePosition.style.marginTop = window.innerHeight/40- scorePosition.clientHeight/40 + 'px'; 
        /*const windowWidth = window.innerWidth; //CHRIS, tried centering the sheet music, did not work...
        const windowHeight = window.innerHeight;
        const scoreWidth = scorePosition.clientWidth;
        const scoreHeight = scorePosition.clientHeight;
        
        const marginLeft = 0.5 * (windowWidth - scoreWidth);
        const marginTop = 0.5 * (windowHeight - scoreHeight);
        
        scorePosition.style.marginLeft = marginLeft + 'px';
        scorePosition.style.marginTop = marginTop + 'px';*/
      }

      centerScore();
      window.addEventListener('resize', centerScore); 

}
    }
  }

      </script>

<style>
.practice-container {
  width: 100%;
  display: flex;
  overflow: auto;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
  background-color: #ffffff;
}
.practice-text {
  text-align: center;
}
.practice-text03 {
  font-size: 24px;
  text-align: center;
}
.practice-text09 {
  font-size: 24px;
}
.practice-button4 {
  left: 935px;
  width: 160px;
  bottom: 42px;
  height: 160px;
  position: absolute;
  border-radius: 80px;
  background-color: rgb(26, 143, 221);
}
</style>



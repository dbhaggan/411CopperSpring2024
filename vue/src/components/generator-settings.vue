<template>
  <div>
    <link href="../assets/generator-settings.css" rel="stylesheet" />
    <div class="generator-settings-container">
      <div id="generatedScore"></div> 
      <div class="generator-settings-container1">
        <span class="generator-settings-text">Settings</span>
        <select class="generator-settings-select" v-model = "selectedClef">
          <option value="">default</option>
          <option value="percussion">percussion</option>
          <option value="treble">treble</option>
          <option value="bass">bass</option>
        </select>
        <textarea
          placeholder="Enter numbers separated by commas"
          v-model = "octaveInput"
          @blur = "addOctavesToArray"
          class="generator-settings-textarea textarea"
        ></textarea>
        <textarea
          placeholder=""
          class="generator-settings-textarea1 textarea"
          v-model = "measuresInput"
        ></textarea>
        <span class="generator-settings-text01">Rudiments in Score:</span>
        <select class="selection2 " v-model = "conceptIsolationVar">
          <option value="">default</option>
          <option value="accents">Accents</option>
          <option value="sticking">Sticking Text Position</option>
        </select> 
        <span class="generator-settings-text02">Change Octaves:</span>
        <span class="generator-settings-text03">Instruments in Score: 1: Snare, 2: Glockinspiel</span>
        <input type="checkbox" checked="false" class="generator-settings-checkbox" />
        <span class="generator-settings-text04">Pick Instrument:</span>
        <select class="selection" v-model = "selectedInstrVar">
          <option value="snare_drum">Snare Drum</option>
          <option value="glock">Glockinspiel</option>
        </select> 
        <span class="generator-settings-text05">
          <span>Tempo:  120</span>
          <br />
        </span>
        <span class="generator-settings-text08">Metronome:</span>
        <span class="generator-settings-text09">Key:  C Major</span>
        <span class="generator-settings-text10">Number of Measures:</span>
        <span class="generator-settings-text11">Change Clef:</span>
        <span class="generator-settings-text12">Randomize Stitching:</span>
        <input
          type="checkbox"
          class="generator-settings-checkbox1" 
          v-model = "checked" 
        />
        <label for = "checkbox">{{ checked }}</label> 
      </div>
      <div class="generator-settings-container2">
        <button type="button" class="generator-settings-button button">
          <span class="generator-settings-text13">
            <span>Practice</span>
            <br />
          </span>
        </button>
        <button type="button" class="generator-settings-button1 button">
          <span class="generator-settings-text16">
            <span>Collaborative Learning</span>
            <br />
          </span>
        </button>
        <button type="button" class="generator-settings-button2 button">
          <span>
            <span>Settings</span>
            <br />
          </span>
        </button>
        <button type="button" class="generator-settings-button3 button">
          <span class="generator-settings-text22">
            <span>Home</span>
            <br />
          </span>
        </button>
      </div>
      <button type="button" class="practice-button4 button" v-on:click = "runSheetGenerator"> 
        <span>
          <br />
          <br />
        </span>
      </button>
    </div>
    </div>
  </template>
  
  <script>
  /* global Vex */
  
  export default {
  
    name: 'GeneratorSettings',
    props: {},
    metaInfo: {
      title: 'Generator-Settings',
      meta: [
        {
          property: 'og:title',
          content: 'Generator-Settings',
        },
      ],
    },
    data (){
      return { 
        checked: false,
        measuresInput: '16',
        octaveInput: '',
        octaveInputArray: [],
        tempOctaveArray: [], 
        selectedClef: '', 
        selectedInstrVar: '', 
        conceptIsolationVar: '', 
      }
    }, 
    watch: {
      selectedClef(newValue) {
        this.performActionBasedOnClef(newValue); 
      }
    },
    methods:{

      performActionBasedOnClef(clef) {
        if (clef === 'percussion') {
          this.selectedClef = 'percussion'
        } else if (clef === 'treble') {
          this.selectedClef = 'treble'
        } else if (clef === 'bass') {
          this.selectedClef = 'bass'
        }
        else {
          this.selectedClef = 'percussion'
        }
      },

      addOctavesToArray () {
        let octVar = this.octaveInput.split(',')
        .map(num => `/${num.trim()}`);
  
        this.octaveInputArray.push(...octVar);
        this.octaveInput = ''; 
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
        // let octavePool = ['/4', '/5'];              
        let octavePool = [];  
        
          if(this.octaveInputArray.length === 0 && this.tempOctaveArray.length === 0) {
            alert("Please pick an Octave (enter a number between 1-7) \n (and pick an Instrument if not selecte already)");           
          } 
          if(this.octaveInputArray.length === 0) {
            octavePool = [...this.tempOctaveArray];    
          }
          else {
            octavePool = []; 
            octavePool = [...this.octaveInputArray]; 
            this.tempOctaveArray.length = [];   
            this.tempOctaveArray = [...this.octaveInputArray];              
            this.octaveInputArray.length = []; 
          }
        
        
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
        let startFlag = true; 
        let tempClef = this.selectedClef; 
  
        let measureLength = 40; 
        let maxMeasuresInRow = 5; 
  
  
  
        // Generator Settings 
        let instrumentArray = ["snare_drum", "glock"]; 
        let initialInstrument = this.selectedInstrVar;   
        let numberOfMeasures = this.measuresInput; 
        let stickingIsOn = this.checked; 
          let stickingBelowMeasure = false; 
        let randomAccentsAreOne = false;    

        if (this.conceptIsolationVar === 'accents'){
            randomAccentsAreOne = true; 
        }
        else if (this.conceptIsolationVar === 'sticking'){
            stickingBelowMeasure = true; 
        }
        else {
          stickingBelowMeasure = false; 
          randomAccentsAreOne = false;   
        }
        
        
  
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
            if (startFlag === true && tempClef != "") {
                startFlag = false; 
                clefVal = tempClef; 
              return stave.addClef(clefVal).addTimeSignature('4/4'); 
            }
            else if(previousInstrument === currentInstrument){
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
        }
  
        centerScore();
        window.addEventListener('resize', centerScore); 
  
  }
    },
  }
  
  </script>
  
  <style scoped>
 .generator-settings-container {
  width: 100%;
  display: flex;
  overflow: auto;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
  background-color: #ffffff;
}
.generator-settings-container1 {
  right: 0px;
  width: 518px;
  bottom: 0px;
  height: 739px;
  display: flex;
  position: relative;
  align-self: flex-end;
  align-items: center;
  flex-direction: column;
  justify-content: flex-start;
  background-color: #001f3e;
}
.generator-settings-text {
  color: rgb(255, 255, 255);
  font-size: 32px;
}
.generator-settings-select {
  top: 122px;
  left: 141px;
  position: relative;
}
.generator-settings-textarea {
  top: 163px;
  left: 144px;
  width: 59px;
  position: relative;
  padding-top: 0px;
  padding-left: 0px;
  padding-right: 0px;
  padding-bottom: 0px;
}
.generator-settings-textarea1 {
  top: 68px;
  left: 175px;
  width: 59px;
  position: relative;
  padding-top: 0px;
  padding-left: 0px;
  padding-right: 0px;
  padding-bottom: 0px;
}
.generator-settings-text01 {
  top: 314px;
  left: 5px;
  color: rgb(255, 255, 255);
  position: absolute;
}
.generator-settings-text02 {
  top: 169px;
  left: 3px;
  color: #ffffff;
  position: absolute;
}
.generator-settings-text03 {
  top: 220px;
  left: 5px;
  color: #ffffff;
  position: absolute;
}
.generator-settings-checkbox {
  top: 613px;
  left: 177px;
  position: absolute;
}
.generator-settings-text04 {
  top: 36px;
  left: 7px;
  color: rgb(255, 255, 255);
  position: absolute;
}
.generator-settings-text05 {
  top: 461px;
  left: 3px;
  color: #ffffff;
  position: absolute;
}
.generator-settings-text08 {
  left: 62px;
  color: #ffffff;
  bottom: 113px;
  position: absolute;
}
.generator-settings-text09 {
  top: 410px;
  left: 8px;
  color: rgb(255, 255, 255);
  position: absolute;
}
.generator-settings-text10 {
  top: 76px;
  left: 7px;
  color: white;
  position: absolute;
}
.generator-settings-text11 {
  top: 121px;
  left: 7px;
  color: #ffffff;
  position: relative;
}
.generator-settings-text12 {
  top: 266px;
  left: 3px;
  color: #ffffff;
  position: relative;
}
.generator-settings-checkbox1 {
  top: 268px;
  left: 192px;
  position: relative;
}
.generator-settings-container2 {
  width: 181px;
  height: 1080px;
  display: flex;
  position: relative;
  align-self: flex-start;
  align-items: center;
  flex-direction: column;
  justify-content: flex-start;
  background-color: #0055FF;
}
.generator-settings-button {
  color: rgb(128, 170, 255);
  width: 181px;
  height: 90px;
  opacity: 1;
  font-size: 24px;
  border-color: #80AAFF;
  border-width: 3px;
  text-transform: capitalize;
  background-color: rgb(0, 85, 255);
}
.generator-settings-text13 {
  text-align: center;
}
.generator-settings-button1 {
  color: rgb(128, 170, 255);
  width: 181px;
  height: 90px;
  opacity: 1;
  border-color: #80AAFF;
  border-width: 3px;
  background-color: rgb(0, 85, 255);
}
.generator-settings-text16 {
  font-size: 24px;
  text-align: center;
}
.generator-settings-button2 {
  color: rgb(128, 170, 255);
  width: 181px;
  height: 90px;
  opacity: 1;
  font-size: 24px;
  border-color: #80AAFF;
  border-width: 3px;
  background-color: rgb(0, 85, 255);
}
.generator-settings-button3 {
  color: rgb(128, 170, 255);
  right: 0px;
  width: 181px;
  bottom: 0px;
  height: 90px;
  opacity: 1;
  position: relative;
  border-color: #80AAFF;
  border-width: 3px;
  background-color: rgb(0, 85, 255);
}
.generator-settings-text22 {
  font-size: 24px;
}
.generator-settings-button4 {
  left: 935px;
  width: 160px;
  bottom: 42px;
  height: 160px;
  position: relative;
  border-radius: 80px;
  background-color: rgb(26, 143, 221);
}
  </style>
  


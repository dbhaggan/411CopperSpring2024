<template>
  <!DOCTYPE html>
  <html>
    <body style="background-color: #003e7d">
      <div>
        <link href="./practice.css" rel="stylesheet" />
        <div class="practice-container">
          <div class="practice-container1">
            <button type="button" class="practice-button button">
              <span class="practice-text">
                <span>Practice</span>
                <br />
              </span>
            </button>
            <button type="button" class="practice-button1 button">
              <span class="practice-text03">
                <span>Collaborative Learning</span>
                <br />
              </span>
            </button>
            <button type="button" class="practice-button2 button">
              <span>
                <span>Settings</span>
                <br />
              </span>
            </button>
            <button type="button" class="practice-button3 button"> 
              <span class="practice-text09">
                <span>Home</span>
                <br />
              </span>
            </button>
          </div>
          <button type="button" class="practice-button4 button" @click = "runSheetGenerator">
            <span>
              <br />
              <br />
            </span>
          </button>
        </div>
        <div id="generatedScore"></div> 
      </div>
    </body>
  </html>
</template>

<style>
.practice-container {
  width: 100%;
  display: flex;
  overflow: auto;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
  background-color: #003e7d;
}
.practice-container1 {
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
.practice-button {
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
.practice-text {
  text-align: center;
}
.practice-button1 {
  color: rgb(128, 170, 255);
  width: 181px;
  height: 90px;
  opacity: 1;
  border-color: #80aaff;
  border-width: 3px;
  background-color: rgb(0, 85, 255);
}
.practice-text03 {
  font-size: 24px;
  text-align: center;
}
.practice-button2 {
  color: rgb(128, 170, 255);
  width: 181px;
  height: 90px;
  opacity: 1;
  font-size: 24px;
  border-color: #80aaff;
  border-width: 3px;
  background-color: rgb(0, 85, 255);
}
.practice-button3 {
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
<script>


      /* global Vex */

  export default {
    name: 'VexflowComponent',
    mounted(){
   // methods: {
      
     // data: function runSheetGenerator(){

// Check if a Score exists and deletes it 
let existingScore = document.getElementById("generatedScore"); 
if(existingScore){
  existingScore.parentNode.removeChild(existingScore); 
}

// Adds a new div/svg element with same name to house Score 
let newScore = document.createElement("div"); 
newScore.id = "generatedScore"; 
document.body.appendChild(newScore); 


const {        
  Renderer, Stave, StaveNote, Voice, Formatter} = Vex.Flow; 

  // For generator settings 
  let clefVal = 'percussion';  // percussion, treble, bass 
                                // SET CLEF BY REFRESHING PAGE (HAVE A BUTTON FOR THIS) 


// Create an SVG renderer and attach it to the DIV element named "generatedScore".
const div = document.getElementById('generatedScore');
const renderer = new Renderer(div, Renderer.Backends.SVG);

// Configure the rendering context.
renderer.resize(500, 500);
const context = renderer.getContext();

// Create a stave of width 420 at position 10, 40 on the canvas.
const stave = new Stave(10, 40, 420);

// Add a clef and time signature. // This will be dynamic later in generator settings algorithm 
stave.addClef(clefVal).addTimeSignature('4/4');

// Connect it to the rendering context and draw!
stave.setContext(context).draw();





  // TODO: Add 16th notes and half notes 

  // I have left alot of console.logs for debugging, but will delete them later 


  // random notes in the future about this data: 
  // the contents of these three pools can by changed by generator settings 
  // in instrument catalog we'll have to include more note pools to represent different key signatures 

  // for now we're sticking to the key of C major/ A minor and 8th notes as the highest subdivision 
  
  let notePool = ['A', 'B', 'C', 'D', 'E', 'F', 'G']; 
  let octavePool = ['/4', '/5'];              // excluding octaves 1-3 and 6-8 to prevent creating several ledger lines 
  let durationPool = ['q','8'];    // DELETE LATER, for testing   q = quarter notes, 8 = eigth notes 
    //durationPool = ['w', 'q','8', '16']   # USE THIS LATER 
  let randomIndex; 

  const notes = []; 
  let beatsTotal = 8;  // Total number of beats in the measure, will change this to make it dynamic later 

  // For Feedback algorithm 
  let generatedNotesArray = []; 


function pickRandomArrayIndex(Array){   
// ensure randomness with just 2 values in array 
  if (Array.length == 2){ 
    let randDecimalVal = Math.random(); // outputs decimal value, instead of whole number 
    randDecimalVal = randDecimalVal < 0.50 ? 0 : 1; 

    randomIndex = randDecimalVal; 
  }  
  else {
    randomIndex = Math.floor(Math.random() * Array.length) + 0; // subtracting 1 to match the max array index 
    if(randomIndex != 0){ // to prevent -1 index and undefined error 
        randomIndex--; 
      }
  }

  return randomIndex; 
}


function randomizeNoteAndOctave(){
  let Note = notePool[pickRandomArrayIndex(notePool)];  
  let Octave = octavePool[pickRandomArrayIndex(octavePool)]; 
  // percussNoteHead = percussionNoteHeadPool[pickRandomArrayIndex(percussionNoteHeadPool)]; // TAKE OUT PERCUSSION STUFF, HAVE TO BE IF STATEMENT 

  // return Note + Octave + percussNoteHead; // TAKE OUT PERCUSSION STUFF, HAVE TO BE IF STATEMENT 
  return Note + Octave; //+ percussNoteHead  
}


function randomizeDuration(){
  let Duration = durationPool[pickRandomArrayIndex(durationPool)];  

  return Duration; 
}


function setBeatsLeftInMeasure (durationToSet) {
  if ( beatsTotal == 1 && durationToSet == 'q'){  // catches situation if beatsTotal = 1, but the note randomize is 'q' 
    beatsTotal = beatsTotal - 1; 
    //let randomDuration = '8';     // Changes Duration so there's a sufficient number of notes in measure 
    durationToSet = '8';     // Changes Duration so there's a sufficient number of notes in measure 
  }
  else if(durationToSet == 'q'){
    beatsTotal = beatsTotal - 2; 
  }
  else if (durationToSet == '8') {
    beatsTotal = beatsTotal - 1; 
  }
}


// let randomizedNote;
// let randomizedDuration; 

// creates the random Note and Duration then outputs it into Vexflow API 
function createRandomNote(){
  let randomNote = randomizeNoteAndOctave();  
  let randomDuration =  randomizeDuration(); 

  setBeatsLeftInMeasure (randomDuration); 
  
  generatedNotesArray.push(randomNote, randomDuration); // store notes to use for Smart Feedback Algorithm 

    return new Vex.Flow.StaveNote ({
    keys: [randomNote],
    duration: randomDuration
  });
}


let randomNote; 

while(beatsTotal != 0) {
  randomNote = createRandomNote();
    console.log(beatsTotal); 
  if (notes.length > 7){    // Catches error where generated notes surpass array limit, Will make this more dynamic 
    console.log("ERROR MAX ARRAY LIMIT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   " + notes.length); 
    break;  
  }
  else {
    notes.push(randomNote); // push created notes in array for vexflow to format and render to screen 
  }
}

// For Feedback Algorithm 
// Show Stored Notes of Array in Console Log, DELETE LATER 
let it = 0; 
console.log("Array's Content that's storing Generated Notes: ")
while (it < generatedNotesArray.length){
  console.log(generatedNotesArray[it]); 
  it++; 
}

const notes2 = [new StaveNote({
  keys: [randomizeNoteAndOctave()],  
  duration: 'w'
})];

// Create a voice in 4/4 and add above notes
const voices = [
  new Voice({
    num_beats: 4,
    beat_value: 4
  }).addTickables(notes),
  new Voice({
    num_beats: 4,
    beat_value: 4
  }).addTickables(notes2),
];

// Format and justify the notes to 400 pixels.
new Formatter().joinVoices(voices).format(voices, 350);

// Render voices.
voices.forEach(function(v) {
  v.draw(context, stave);
});


// Positioning score in middle of page 
const scorePosition = document.getElementById('generatedScore');
const centerScore = () => {
  scorePosition.style.marginLeft = window.innerWidth/1.75 - scorePosition.clientWidth/1.75 + 'px'; 
  scorePosition.style.marginTop = window.innerHeight/40- scorePosition.clientHeight/40 + 'px'; 
}

centerScore();
window.addEventListener('resize', centerScore); 
}
    }
  }


</script>

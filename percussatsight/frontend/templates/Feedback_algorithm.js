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
    
    error = 0; //initialize error to 0
    for(var n=1;n<sheet_orig.length;n++) { //loop through all sets of notes
        error += comparePercussionNotes(sheet_orig[n-1],sheet_orig[n],sheet_comp[n-1],sheet_comp[n]); //for each pair of notes, add how bad they match up on the original vs the one we're comparing
    }
    
    return error / (sheet_orig.length-1); //divide by # of pairs of notes & return
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



///HERE WE HAVE THE CODE FOR THE SPECIFIC SHEET MUSIC JEREMIAH GENERATED

var audio_sheet_orig = [new Note(0,'8','D',6,6), new Note(0.75,'8','D',7,6), new Note(1.5,'8','G',7,6), new Note(2.25,'8','A',7,6), new Note(3,'q','B',7,6), new Note(3.75,'q','G',7,6)];

var midi_sheet_orig = [new Note(0,'8','C',3,6), new Note(0.6,'q','A',3,6), new Note(1.2,'8','C',3,6), new Note(1.8,'q','C',4,6), new Note(2.4,'q','D',4,6)];


var audio_sheet_user = [new Note(0,'8','D',6,6), new Note(0.74679,'8','D',7,6), new Note(1.49535,'8','G',7,6), new Note(2.25050,'8','A',7,6), new Note(2.99385,'q','B',7,6), new Note(3.74076,'q','F',7,6)];

var midi_sheet_user = [new Note(0,'8','C',3,6), new Note(0.61758,'q','A',3,6), new Note(1.27523,'8','C',3,6), new Note(1.86144,'q','B',4,6), new Note(2.40894,'q','D',4,6)];


console.log("Audio: "+error_to_score(compareSheetMusic(audio_sheet_orig, audio_sheet_user)));
console.log("MIDI: "+error_to_score(compareSheetMusic(midi_sheet_orig, midi_sheet_user)));



///HERE WE HAVE THE CODE TO PROVE THIS WORKS FOR ANY TWO PIECES OF SHEET MUSIC

/*var sheet1 = [];
var sheet2 = [];
var dev = 0.05;  ///THIS IS HOW BAD THE PERCUSSIONIST IS
var freq = 0.6;  ///THIS IS THE BPS (beats per second)
for(var n=0;n<64;n++) {
    sheet1[n] = new Note(n*freq, 0.2, 'c', 0, 7);
    sheet2[n] = new Note(n*freq+dev*(2*Math.random()-1), 0.2, 'c', 0, 7);
}

console.log(compareSheetMusic(sheet1, sheet2));
console.log(noteByNoteAnalysis(sheet1, sheet2));
console.log(error_to_score(compareSheetMusic(sheet1,sheet2)));*/

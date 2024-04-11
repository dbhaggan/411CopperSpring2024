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
    for(var n=1;n<sheet_orig.length;n++) { //loop through all sets of note
        error += comparePercussionNotes(sheet_orig[n-1],sheet_orig[n],sheet_comp[n-1],sheet_comp[n]); //for each pair of notes, add how bad they match up on the original vs the one we're comparing
    }
    
    return error / (sheet_orig.length-1); //divide by # of pairs of notes & return
}

/*var sheet1 = [];
var sheet2 = [];
var dev = 0.05;
var freq = 0.6;
for(var n=0;n<64;n++) {
    sheet1[n] = new Note(n*freq, 0.2, 'c', 0, 7);
    sheet2[n] = new Note(n*freq+dev*(2*Math.random()-1), 0.2, 'c', 0, 7);
}

console.log(compareSheetMusic(sheet1, sheet2));*/

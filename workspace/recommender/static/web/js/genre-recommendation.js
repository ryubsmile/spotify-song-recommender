let GENRE_DICT; // from the HTML file, get the genre list as dictionary
let GENRE; // the genre user clicked on the previous page
const NUMBER_OF_TILES = 6; // self-explanatory.

// when html body is loaded, make tiles.
window.onload = function(){
    showTiles(NUMBER_OF_TILES);
};

// pick 6 random numbers between 0~genre.length, and show them as tiles
function showTiles(tileAmount){
    const randomIntArray = pickRandomIndices(GENRE.length, tileAmount);

    for(var i = 0; i < tileAmount; i++){
        createTile(randomIntArray[i]);
    }
}

function createTile(genreIndex){
    var tile = document.createElement('a');
    tile.className = "tile";

    var textString = GENRE[genreIndex].toUpperCase();
    tile.textContent = "#"+textString;

    tile.href = "javascript:;";
    tile.style.backgroundImage = "url(../../static/" + GENRE_DICT[GENRE[genreIndex]] + ")";
    tile.setAttribute('onclick', 'sendTextAsInput(\"' + textString + '\")');
    tile.setAttribute('onmouseover', 'toggleAlpha(this);');
    tile.setAttribute('onmouseout', 'toggleAlpha(this);');

    var parent = document.getElementById('tile-container');
    parent.appendChild(tile);
}

function toggleAlpha(selfElement){
    selfElement.id = (selfElement.id === "")? "highlighted" : "";
}

//creates non duplicate 0~max random integers array size of size
//indices => used to access genre[index]
function pickRandomIndices(max, size){
    var existingElements = [];
    var indices = [];
    var pointer = -1;
    
    //random number between 0 ~ max
    for(var i = 0; i < size;){
        pointer = Math.floor(Math.random() * max);
        if(!existingElements.includes(pointer)){
            existingElements.push(pointer);
            indices.push(pointer);
            i++;
        }
    }
    return indices;
}
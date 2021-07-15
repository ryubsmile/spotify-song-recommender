function renderTiles(tileAmount){
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
    tile.style.backgroundImage = "url(../static/" + GENRE_DICT[GENRE[genreIndex]] + ")";
    tile.setAttribute('onclick', 'sendTextAsInput(\"' + textString + '\")');

    var parent = document.getElementById('tile-container');
    parent.appendChild(tile);
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

function sendTextAsInput(inputText){
    setInputAs(inputText);
    submitInput();
}

//set input hidden value as the text
function setInputAs(input){
    var inputSender = document.getElementById('input-send');
    inputSender.value = input;
}

//submit input as form data
function submitInput(){
    var form = document.getElementById('tile-data');
    form.submit();
}


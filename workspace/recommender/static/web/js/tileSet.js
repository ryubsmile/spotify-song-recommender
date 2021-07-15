const COLORS = [
    {r: 240, g: 159, b: 164}, //pastel red
    {r: 243, g: 186, b: 180}, //pastel orange
    {r: 249, g: 219, b: 195}, //pastel pink
    {r: 229, g: 241, b: 204}, //pastel lightgreen
    {r: 191, g: 232, b: 216}, //pastel green
    {r: 201, g: 206, b: 232}, //pastel blue
];

function renderTiles(tileAmount){
    for(var i = 0; i < tileAmount; i++){
        makeSingleTile();
    }
}

//draw HTML of a single tile
function makeSingleTile(){
    /* 
     * <div class="tile" onmouseover="setTileAnimation(this);">
     *     <a href="javascript:;" onclick="parseStringOfButton(this); clickedTile(this);">TILE 1</a>
     * </div> 
     */
    var tile = document.createElement('div');
    tile.className = "tile";
    var parent = document.getElementById('tile-container');
    parent.appendChild(tile);

    tile.innerHTML = 
    (
        "<a href=\"javascript:;\" onclick=\"setInputAs(this); clickedTile(this);\">TILE</a>"
    );

    tile.setAttribute('onmouseover',"setTileAnimation(this);");
}

//set tile color
function setTileStyle(){
    var tileContainer = document.querySelector('#tile-container');
    var tileList = document.querySelectorAll('.tile');
    
    for(var i = 0; i < tileList.length; i++){
        var color = COLORS[i];
        var colorString = "rgba(" + color.r + ", " + color.g + ", " + color.b + ", " + 1 + "); ";

        var tileBorder = "border-color: " + colorString + "; ";
        var tileTextColor = "color: " + colorString + "; ";
        var styleString = tileBorder + tileTextColor;

        tileList[i].setAttribute('style', styleString);
    }
}

/*
* sets tile text contents according to the value given by the 'obj' object.
 * 'obj' is a json value of genre strings parsed into array.
 */
function setTileText(){
    var tiles = document.getElementsByTagName('a');
    var randomIndices = pickRandomIndices(obj.length, 6);

    for(var i = 0; i < tiles.length; i++){
        var tile = tiles[i];
        var genre = obj[randomIndices[i]].toUpperCase();
        tile.textContent = (genre !== null)? genre : "";
    }
}

/* 
 * creates an array called 'indices,'  
 * of 'times' size 
 * which consists of 0~'max' exclusive (non-duplicate) integer values
 */
function pickRandomIndices(max, times){
    var existingElements = [];
    var indices = [];
    var pointer = -1;
    
    //random number between 0 ~ max
    for(var i = 0; i < times;){
        pointer = Math.floor(Math.random() * max);
        if(!existingElements.includes(pointer)){
            existingElements.push(pointer);
            indices.push(pointer);
            i++;
        }
    }

    return indices;
}

//tile animation that changes color of tiles when hover
function setTileAnimation(self){
    var selfColor = self.style.color;
    var target = document.getElementById('color-save');

    target.innerText = ':root{--theme-color: ' + selfColor + '}';
}
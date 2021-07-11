const COLORS = [
    {r: 240, g: 159, b: 164}, //pastel red
    {r: 243, g: 186, b: 180}, //pastel orange
    {r: 249, g: 219, b: 195}, //pastel pink
    {r: 229, g: 241, b: 204}, //pastel lightgreen
    {r: 191, g: 232, b: 216}, //pastel green
    {r: 201, g: 206, b: 232} //pastel blue
];

//set tile height equal to tile width
function tileHeightSetting(){
    var tileContainer = document.querySelector('#tile-container');
    var tileList = document.querySelectorAll('.tile');
    var sampleTile = tileList[0];

    for(var i = 0; i < tileList.length; i++){
        var color = COLORS[i];
        var r = color.r;
        var g = color.g;
        var b = color.b;
        var colorString = "rgba(" + r + ", " + g + ", " + b + ", " + 1 + "); ";

        var tileBorder = "border-color: " + colorString + "; ";
        var tileTextColor = "color: " + colorString + "; ";
        var styleString = tileBorder + tileTextColor;

        tileList[i].setAttribute('style', styleString);
    }
    
}

window.onload = function(){
    tileHeightSetting();
}

function setTileAnimation(self){
    var selfColor = self.style.color;
    var target = document.getElementById('color-save');

    target.innerText = ':root{--saved-color: ' + selfColor + '}';
}
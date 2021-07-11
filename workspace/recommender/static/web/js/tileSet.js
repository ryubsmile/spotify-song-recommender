const COLORS = [
    {r: 102, g: 172, b: 161}, //cyan
    {r: 192, g: 152, b: 95}, //mustard yellow
    {r: 73, g: 95, b: 167}, //pastel blue
    {r: 152, g: 113, b: 123}, //pastel red
    {r: 128, g: 79, b: 55}, //orange darker
    {r: 168, g: 180, b: 196} //white cloud
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
        
        var tileColor = "background: " + "rgba(" + r + ", " + g + ", " + b + ", " + 1 + "); ";
        var tileBorder = "border-color: rgba(" + 0 + ", " + 0 + ", " + 0 + ", " + 0.3 + "); " +
                         "border-style: solid; ";
        var styleString = tileBorder + tileColor;

        tileList[i].setAttribute('style', styleString);
    }
    
}



window.onload = function(){
    tileHeightSetting();
}
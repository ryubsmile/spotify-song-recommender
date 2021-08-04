function setTitleFirstLetterCap(){
    title = title.replace(title[0], title[0].toUpperCase());
    target = document.getElementById('title');
    target.textContent = title;
}

// create n=playlist.length song rows 
function createPlaylist(){
    for(var i = 0; i < playlist.length; i++){
        createSingleSongCell(i);
    }
}

// creates a single row for the song in a playlist data
function createSingleSongCell(index){
    // the row
    var aSongRow = document.createElement('div');
    aSongRow.className = 'a-song song-cell';

    // a small line that gives space between displayed songs
    var hr = document.createElement('hr');
    //
    var target = document.getElementById('result');
    target.appendChild(aSongRow);
    target.appendChild(hr);

    let rawTime = playlist[index].duration;
    let minutes = add0(Math.floor(rawTime));
    let seconds = add0(Math.floor((rawTime - minutes) * 60));

    //draw html
    aSongRow.innerHTML = (
       `<index>${index + 1}</index>
        <div class="main">
            <img class="image" src="${playlist[index].image}">
            <song-info>
                <name>${playlist[index].songName}</name>
                <artist>${playlist[index].artistName}</artist>
            </song-info>
        </div>
        <div class="album">${playlist[index].albumName}</div> 
        <div class="length">${minutes}:${seconds}</div>
        <div class="img"> 
            <a target="_blank" rel="noopener noreferrer" href="${playlist[index].link}">
                <img class="play" src="../../static/web/images/images.png">
            </a>
        </div>`
    );
    //attribute for hover
    aSongRow.setAttribute('onmouseover', 'displayButton(this);');
    aSongRow.setAttribute('onmouseout', 'hideButton(this);');
    //if selected, make it brighter
    aSongRow.setAttribute('onclick', 'selectedRow(this);');
}

function add0(num){
    if(num < 10) return "0" + num;
    return num;
}

//show button on mouse over
function displayButton(self){
    self.lastElementChild.lastElementChild.lastElementChild.style.display = "inline";
}

//hide button on mouse out
function hideButton(self){
    //if the button is selected, don't hide.
    if(self.id !== 'selected'){
        self.lastElementChild.lastElementChild.lastElementChild.style.display = "";
    }
}

//select row
function selectedRow(rowSelected){
    var rowSelectedBefore = document.getElementById('selected');

    //null check, for initial none-selected.
    if(rowSelectedBefore !== null){ 
        //'row before' loses the id,
        // and its button gets hidden
        rowSelectedBefore.id = '';
        hideButton(rowSelectedBefore); 
    }
    //for the case of same row getting clicked again, lose (not gain) its property.
    if(rowSelected !== rowSelectedBefore){
        rowSelected.id = 'selected';
    }

}

function setBgColor(){
    const COLORS = [
        {r: 240, g: 159, b: 164}, //pastel red
        {r: 243, g: 186, b: 180}, //pastel orange
        {r: 249, g: 219, b: 195}, //pastel pink
        {r: 229, g: 241, b: 204}, //pastel lightgreen
        {r: 191, g: 232, b: 216}, //pastel green
        {r: 201, g: 206, b: 232}, //pastel blue
    ];

    random = Math.floor(Math.random() * COLORS.length);
    const color = COLORS[random];

    var target = document.getElementById('bg-color');
    target.innerText = ':root{--bg-color: ' + color.r + "," + color.g + "," + color.b + '}';
}
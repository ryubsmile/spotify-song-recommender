const searchArea = document.querySelector('.search-area');
const searchBox = searchArea.querySelector('input');
const suggBox = searchArea.querySelector('.autocom-box');

const testDiv = document.getElementById('test');
const NUMBER_OF_AUTOCOMS = 5;
let autoComCell;

function renderAutocom(){
    for(var i = 0; i < NUMBER_OF_AUTOCOMS; i++){
        if(autoComCell[i]){
            makeAutocom(i);
        }
    }
}

function makeAutocom(index){
    var autoComCell = document.createElement('li');
    suggBox.appendChild(autoComCell);

    var rawTime = autoComList[index]["duration"];
    var minutes = add0(Math.floor(rawTime));
    var seconds = add0(Math.floor((rawTime - minutes) * 60));

    autoComCell.innerHTML = (
        "<img src=\"" + autoComList[index]["image"] + "\">" +
        "<song-info>" +
            "<name>" + autoComList[index]["songName"] + "</name>" +
            "<artist>" + autoComList[index]["artistName"] + "</artist>" + 
        "</song-info>" +
        "<length>" + minutes + ":" + seconds + "</length>"
    );
}

//if select, save the data onto the right side
function select(selfElement){
    let selectData = selfElement.textContent;
    searchBox.value = selectData;
}

searchBox.onkeyup = (e) => {
    let userData = e.target.value;

    if(userData){
        searchArea.classList.add('active');
        /*
         * 
         */


    }else{
        searchArea.classList.remove('active');
    }
}
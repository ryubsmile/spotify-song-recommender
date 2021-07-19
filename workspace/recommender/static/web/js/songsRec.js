const searchArea = document.querySelector('.search-area');
const searchBox = document.getElementById('search');
const suggBox = searchArea.querySelector('.autocom-box');

const selectArea= document.querySelector('.select-area');
const selectBoxes = selectArea.querySelectorAll('li');

const testDiv = document.getElementById('test');
let autoComCell;

const NUMBER_OF_AUTOCOMS = 10;
function renderAutocom(){
    for(var i = 0; i < Math.min(NUMBER_OF_AUTOCOMS, autoComCell.length); i++){
        if(autoComCell[i]) // null check
            makeAutocom(i);
    }
}

function makeAutocom(index){
    let autoComCell = document.createElement('li');
    suggBox.appendChild(autoComCell);

    let rawTime = autoComList[index]["duration"]; // e.g. 230.3242 (min)
    let minutes = add0(Math.floor(rawTime)); // 230 min
    let seconds = add0(Math.floor((rawTime - minutes) * 60)); // 19s
    let time = minutes + ":" + seconds; // 230:19

    let imgSrc = autoComList[index]["image"];
    let songName = autoComList[index]["songName"];
    let artistName = autoComList[index]["artistName"];
    let trackID = autoComList[index]["trackID"];

    autoComCell.innerHTML = (
        "<img src=\"" + imgSrc + "\">" +
        "<song-info>" +
            "<name>" + songName + "</name>" +
            "<artist>" + artistName + "</artist>" + 
        "</song-info>" +
        "<length>" + time + "</length>"
        // + "<input type=\"hidden\" name=\"song\" value=\"" + trackID + "\">"
    );

    autoComCell.setAttribute('onclick','select(this)');
}

// if select, save the data onto the right side
// and make the input box blank
const NUMBER_OF_SELECTIONS = 3;
let numOfSelections = 0;

function select(selfElement){
    for(var i = 0; i < NUMBER_OF_SELECTIONS; i++){
        if(numOfSelections >= NUMBER_OF_SELECTIONS || numOfSelections > i){
            continue;
        }
        
        let selectHTML = (selfElement)? selfElement.innerHTML : "";
        selectBoxes[i].innerHTML = selectHTML;
        
        
        numOfSelections++;
        break;
    }
    
    searchBox.value = "";
    searchArea.classList.remove('active');
}

//track ids to send to the server-side
let trackIds = [];

function submitForm(){
    let inputs = selectArea.querySelectorAll('input');
    for(var i = 0; i < NUMBER_OF_SELECTIONS; i++){
        if(inputs[i]){
            trackIds[i] = inputs[i].value;
        }else{
            alert('not enough songs!');
            break;
        }
    }

    let inputTag = document.getElementById('trackIds');
    inputTag.value = trackIds;
}

searchBox.onkeyup = (e) => {
    let userData = e.target.value;
    if(userData){
        searchArea.classList.add('active');
        /*
         * submit keyword and 
         * receive data
         */
    }else{
        searchArea.classList.remove('active');
    }
}

function add0(num){
    if(num < 10){
        return "0" + num;
    }

    return num;
}
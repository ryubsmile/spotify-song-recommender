const searchArea = document.querySelector('.search-area');
const searchBox = document.getElementById('search');
const searchForm = document.getElementById('search-form');

const suggBox = searchArea.querySelector('.autocom-box');

const selectArea= document.querySelector('.select-area');
const selectBoxes = selectArea.querySelectorAll('li');
let autoComList;

const NUMBER_OF_AUTOCOMS = 5;
window.onload = function(){
    setupSuggBox();
}

function setupSuggBox(){
    for(var i = 0; i < NUMBER_OF_AUTOCOMS; i++){
        let autoComCell = document.createElement('li');
        suggBox.appendChild(autoComCell);
    }
}

searchBox.onkeyup = (e) => {
    let keyPressed = e.target.value;
    if(keyPressed){
        searchArea.classList.add('active');
        console.log(searchBox.value);
        let searchKeyword = searchBox.value;
        postKeyword(searchKeyword);
    }else{
        searchArea.classList.remove('active');
        // while(suggBox.firstChild){
        //     suggBox.removeChild(suggBox.firstChild);
        // }
    }
}

var test; // type 'text' in dev tool console to look at the response of keywords

function postKeyword(userData){
    let csrfToken = getCookie('csrftoken');
    fetch('../reload/', {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            "X-CSRFToken": csrfToken,
            "Content-Type": "application/json"
        },
        body: userData,
    })
    .then(function(response){
        console.log('2');
        console.log('3');
            return response.json();
    })
    .then(function(data){
        console.log('4');
        console.log(data);
        test = data;
        renderAutoCom(data);
    });
}

function renderAutoCom(autoComList){
    console.log('5');
    let autoComBoxes = suggBox.querySelectorAll('li');
    if(autoComList != undefined){
        for(var i = 0; i < Math.min(NUMBER_OF_AUTOCOMS, autoComList.length); i++){
            let autoComBox = autoComBoxes[i];
            console.log('6');
            makeAutocom(i, autoComList, autoComBox);
        }
    }
}

function makeAutocom(index, autoComList, autoComCell){
    console.log('7');

    let rawTime = autoComList[index]["duration"]; // e.g. 230.3242 (min)
    let minutes = add0(Math.floor(rawTime)); // 230 min
    let seconds = add0(Math.floor((rawTime - minutes) * 60)); // 19s
    let time = minutes + ":" + seconds; // 230:19

    let imgSrc = autoComList[index]["image"];
    let songName = autoComList[index]["songName"];
    let artistName = autoComList[index]["artistName"];
    let songID = autoComList[index]["songId"];
    let artistID = autoComList[index]["artistId"];

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

function add0(num){
    if(num < 10){
        return "0" + num;
    }

    return num;
}

// used to get csrfToken for POST method
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
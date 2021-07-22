const searchArea = document.querySelector('.search-area'); // the whole area where searching happens
const searchBox = document.getElementById('search'); // the box where keywords are put in
const suggBox = searchArea.querySelector('.autocom-box'); // the drop-down box for auto completion

const selectArea= document.querySelector('.select-area'); // the whole area where selected songs are listed
const selectBoxes = selectArea.querySelectorAll('li'); // each box that contains selected songs

// when body loads, 'setUpSuggBox' function is immediately called.
window.onload = function(){
    setupSuggBox(); 
}

/* <li> tags are created according to the 'NUMBER_OF_AUTOCOMS' variable.
each tag is put inside the 'suggBox' element as a child */
const NUMBER_OF_AUTOCOMS = 5; // if this is to be changed, back-end edit is required beforehand. 
function setupSuggBox(){
    for(var i = 0; i < NUMBER_OF_AUTOCOMS; i++){
        let autoComCell = document.createElement('li');
        suggBox.appendChild(autoComCell);
    }
}

/* every time a key is pressed on the search box, this function is called. 
Checks if the 'keyPressed' is a valid key (not null, empty, or not giving any inputs).
If valid: set the search area class as 'active' & sends(posts) the value in search box and waits for search result. 
If invalid: set the search area class as not 'active' and returns. */
searchBox.onkeyup = (e) => {
    let keyPressed = e.target.value;
    if(keyPressed){
        searchArea.classList.add('active');
        let searchKeyword = searchBox.value;
        postKeyword(searchKeyword);
    }else{
        searchArea.classList.remove('active');
    }
}

/* posts the parameter to the server to 'recommender/reload/' url. 
1. csrfToken is issued to allow POST action
2. sends the 'userData'(=search keyword) parameter to the server.
3. as the server returns a response, parses the result list of jsons into usable form.
4. use the correctly formatted response data to show auto completion on the client-side. */
function postKeyword(userData){
    let csrfToken = getCookie('csrftoken'); //(1) get cookie for POST method verification
    fetch('../reload/', {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            "X-CSRFToken": csrfToken,
            "Content-Type": "application/json"
        },
        body: userData, //(2) data to be sent to the server: text inside search box
    })
    .then(function(response){ //(3) server responds with raw search result data using Spotify API
        return response.json();
    })
    .then(function(data){ //(4) data here is list of json files. [{},{}...{}]
        showAutoComBoxes(data); 
    });
}

/* for each of the <li> tags in suggBox, 
execute 'fillAutoComBox' function if the data responded is valid. */
function showAutoComBoxes(autoComList){
    let autoComBoxes = suggBox.querySelectorAll('li');
    if(autoComList != undefined){
        for(var i = 0; i < Math.min(NUMBER_OF_AUTOCOMS, autoComList.length); i++){
            let autoComBox = autoComBoxes[i];
            let autoComInfo = autoComList[i];
            fillAutoComBox(autoComInfo, autoComBox);
        }
    }
}

/* using the search result data, update auto completion boxes
by editing the inner HTML of each <li> tag. */
function fillAutoComBox(autoComInfo, autoComCell){
    let rawTime = autoComInfo["duration"]; // e.g. 230.3242 (min)
    let minutes = add0(Math.floor(rawTime)); // 230 min
    let seconds = add0(Math.floor((rawTime - minutes) * 60)); // 19s
    let time = minutes + ":" + seconds; // 230:19

    autoComCell.innerHTML = (
        "<img src=\"" + autoComInfo["image"] + "\">" +
        "<song-info>" +
            "<name>" + autoComInfo["songName"] + "</name>" +
            "<artist>" + autoComInfo["artistName"] + "</artist>" + 
        "</song-info>" +
        "<length>" + time + "</length>" + 
        "<input type=\"hidden\" name=\"songId\" value=\"" + autoComInfo["songId"] + "\">" +
        "<input type=\"hidden\" name=\"artistId\" value=\"" + autoComInfo["artistId"] + "\">"
    );

    autoComCell.setAttribute('onclick','select(this)'); //if each auto com is clicked, execute 'select' function
}

/* if an auto completed suggestion is selected, 
1. save the data onto the right side,
2. make the input box blank 
3. make the search area inactive => to hide suggestion(=auto completion) boxes. */
const NUMBER_OF_SELECTIONS = 3;
let numOfSelections = 0;
function select(selfElement){
    for(var i = 0; i < NUMBER_OF_SELECTIONS; i++){
        if(numOfSelections >= NUMBER_OF_SELECTIONS || numOfSelections > i) continue;
        
        let selectHTML = (selfElement)? selfElement.innerHTML : "";
        selectBoxes[i].innerHTML = selectHTML;
        numOfSelections++;
        break;
    }
    
    searchBox.value = "";
    searchArea.classList.remove('active');
}

//to send song id & artist id to server, which are needed to recommend songs. 
let trackIds = [];
function submitForm(){
    let songInfo = selectArea.querySelectorAll("input[name='songId']");
    let artistInfo = selectArea.querySelectorAll("input[name='artistId']");
    for(var i = 0; i < NUMBER_OF_SELECTIONS; i++){
        if(songInfo[i]){
            /*//using json
            var info = new Object();
            info.songId = songInfo[i].value;
            info.artistId = artistInfo[i].value;
            trackIds[i] = JSON.stringify(info); //or just info
            */
            trackIds[i] = new Array(2);
            trackIds[i][0] = songInfo[i].value;
            trackIds[i][1] = artistInfo[i].value;
        }else{
            alert('not enough songs!');
            break;
        }
    }
    let inputTag = document.getElementById('tracksToSend');
    inputTag.value = trackIds;
}

function add0(num){
    if(num < 10) return "0" + num;
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
const searchArea = document.querySelector('.search-area');
const searchBox = document.getElementById('search');
const suggBox = searchArea.querySelector('.autocom-box');

const testDiv = document.getElementById('test');
const NUMBER_OF_AUTOCOMS = 10;
let autoComCell;

function renderAutocom(){
    for(var i = 0; i < Math.min(NUMBER_OF_AUTOCOMS, autoComCell.length); i++){
        if(autoComCell[i]) // null check
            makeAutocom(i);
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

    autoComCell.setAttribute('onclick','select(this)');
}

// if select, save the data onto the right side
// and make the input box blank
function select(selfElement){
    let selectHTML = selfElement.innerHTML;


    searchBox.value = "";
    searchArea.classList.remove('active');
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
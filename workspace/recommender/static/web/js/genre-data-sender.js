/* set these two variables in the html <script> tag. */
const INPUT_TAG_ID = 'input-send';
const FORM_TAG_ID = 'tile-data';

//embedded to the texts that send info
function sendTextAsInput(inputText){
    setInputAs(inputText);
    submitInput();
}

//set input hidden value as the text
function setInputAs(input){
    var inputSender = document.getElementById(INPUT_TAG_ID);
    inputSender.value = input;
}

//submit input as form data
function submitInput(){
    var form = document.getElementById(FORM_TAG_ID);
    form.submit();
}


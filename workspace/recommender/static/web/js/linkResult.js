function sendTextAsInput(inputElement){
    setInputAs(inputElement.textContent);
    submitInput();
}
//set input hidden value as the text
function setInputAs(input){
    var inputSender = document.getElementById('button-kind');
    inputSender.value = input;
}
//submit input as form data
function submitInput(){
    var form = document.getElementById('tile-data');
    form.submit();
}




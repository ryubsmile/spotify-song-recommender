//gets this as parameter
function parseStringOfButton(self){
    var buttonRawString = self.textContent;

    while(buttonRawString.includes('\n')){ buttonRawString = buttonRawString.replace('\n',''); }
    while(buttonRawString.includes(' ')){ buttonRawString = buttonRawString.replace(' ',''); }

    setInputAs(buttonRawString);
}

//set input hidden value as the text
function setInputAs(text){
    var target = document.getElementById('button-kind');
    target.value = text;
}

function setAsSpecialOne(self){
    var parent = self.parentElement;

    parent.className = "special-one";
    self.className = "special-one-text";

    parent.addEventListener('animationend', () =>{
        submitValue();
    });
}

function submitValue(){
    var target = document.getElementById('tile-data');
    target.submit();
}





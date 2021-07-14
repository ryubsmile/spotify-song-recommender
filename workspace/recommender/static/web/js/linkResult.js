//set input hidden value as the text
function setInputAs(self){
    var target = document.getElementById('button-kind');
    target.value = self.textContent;
}

function clickedTile(self){
    var parent = self.parentElement;

    parent.id = "clicked-tile";
    self.id = "clicked-tile-text";

    //at the end of this animation, submit data
    parent.addEventListener('animationend', () =>{
        submitValue();
    });
}

function submitValue(){
    var target = document.getElementById('tile-data');
    target.submit();
}





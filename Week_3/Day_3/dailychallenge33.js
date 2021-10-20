// Create an input type text that takes/shows only letters.
// Hint: use the keyup or the keydown events and remove any character that is not a letter.
// Hint : Check out keycodes in Javascript or Regular Expressions

let wish = document.getElementById("userinput");
let button = document.getElementById("enter");
let list = document.querySelector("ul");

function wishLength() {
	return (wish.value.length);
}

function createListElement() {
		let li = document.createElement("li")
		li.appendChild(document.createTextNode(wish.value));
		list.appendChild(li);
		wish.value=""
}		

button.addEventListener("click", function(){
	if (wishLength() >0){
	createListElement();
	}else if (wishLength ===0){
		alert("enter a wish!")
}

})

wish.addEventListener("keypress", function(event){
	if (wishLength() >0 && event.keyCode === 13){
		createListElement();
}	else if (wishLength ===0){
		alert("enter a wish!")
}

})

wish.addEventListener("keydown", checkKeyPress);
	function checkKeyPress(event){
		if(event.keyCode >= 49 && event.keyCode <=57){
		alert("no numbers please!")
		
	}

}


// In todays exercise we will be creating a Mad Libs game.
// If you’ve never played this game, a mad lib is a game where you fill in a bunch of blank inputs with different word types (ie : noun, adjective, verb), and then a story is generated based on the words you chose, and sometimes the story is surprisingly funny.
// In this exercise you will complete the functionality with event listeners.

// Follow these steps :

// Get the value of each of the inputs in the HTML file when the button is clicked.
// Make sure the values are not empty
// Write a story that uses each of the values.
// Make sure you check the console for errors when playing the game.
// Bonus: Add a “shuffle” button to the HTML file, when clicked the button should change the story currently displayed (but keep the values entered by the user). The user could click the button at least three times and get a new story. Display the stories randomly.

// let noun = document.getElementById("noun");
// let adjective = document.getElementById("adjective");
// let person = document.getElementById("person");
// let place = document.getElementById("place");

let userInput = document.getElementsByTagName("input")
let button = document.getElementById("lib-button")

	button.addEventListener("click", function(){
for(let i=0; i< userInput.length; i++){
		let fieldsarr = [i];
		fieldsarr.push("userInput") 
		console.log(fieldsarr)
}



let madlib = document.getElementById("story")
madlib.innerHTML= "There once was a " + userInput.adjective.value + " person named " + userInput.person.value + " who had a pet " + userInput.noun.value + " and loved to " + userInput.verb.value + " in " + userInput.place.value


})
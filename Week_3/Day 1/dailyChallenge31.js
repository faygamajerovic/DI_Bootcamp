// In this exercise we will be creating a webpage with a black background as the universe and we will fill the universe with planets and their moons.
// We will provide the HTML page.
// You only have to work with a JS file.

// Create an array which value is the planets of the solar system.
// For each planet in the array, create a <div> using createElement. This div should have a class named "planet".
// Each planet should have a different background color. (Hint: add a new class to each planet).
// Finally append each div to the <section> in the HTML (presented below).
// Bonus: Do the same process to create the moons.
// Be careful, each planet has a certain amount of moons. How should you display them?
// Should you still use an array for the planets ? Or an array of objects ?

function addPlanet(){

let planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"];
	for (i =0; i < planets.length; i++){
		let planetDiv = document.createElement(.planet);
		let newText = document.createTextNode(planets[i]);
		planetDiv.style.backgroundColor = "yellow";
		planetDiv.appendChild(newText);
		newDiv.classList.add("planet");
	}
}

addPlanet();

// for (i = 0; i < arrayLength; i++) {
//   $('<div class="results" />').text(arrayVariable[i]).appendTo('body');
// }


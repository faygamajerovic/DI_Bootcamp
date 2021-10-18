// NUMBER 1
// Using DOM methods, remove the last paragraph in the <article> tag from the DOM.
// Add an event listener which will change the background color of the h2 tag from the DOM when clicked on.
// Set the font size of the h1 tag to a random pixel size between 0 to 100.(Check out this documentation)
// Add an event listener which will hide the h3 when it’s clicked on (use the display property).
// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
// When the “Submit” button of the form is clicked:
// get the values of the input tags
// make sure that they are not empty,
// then append them to a HTML table, in the div, below the form.
// When you hoover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google) 

// let btnForm =document.getElementById("submit")
// let NameInput =  document.getElementById("fname")
// let LastNameInput =  document.getElementById("lname")
// btnForm.addEventListener("click", function () {
//     if( LastNameInput.value===''||NameInput.value==='') {
//         alert("Input empty. Fill all the input of the form.")
//     }

//     let table = document.createElement('table');
//     let thead = document.createElement('thead');
//     let tbody = document.createElement('tbody');
// ++



let article = document.body.firstElementChild;
console.log(article)

let lastP = document.getElementsByTagName("p")[3];
lastP.remove();

let headingTwo = document.querySelector("h2");
console.log(headingTwo)

headingTwo.addEventListener("click",function(){
    this.style.backgroundColor = "red"
});

headingTwo.addEventListener("mouseover",function(){
    this.style.cursor = "pointer"
});

let h1 = document.querySelector("h1")
let fontRandom = Math.floor(Math.random() * 100) + 1;
h1.style.fontSize = fontRandom + "px"

let h3 = document.querySelector("h3")
h3.addEventListener("click", function () {
    this.style.display = "none"
});

h3.addEventListener("mouseover",function(){
    this.style.cursor = "pointer"
});

let button = document.createElement("button")
button.innerHTML = "rawr"
document.body.appendChild(button);

let paragraph = document.querySelectorAll("p")

for (let i=0; i<paragraph.length; i++){
	button.addEventListener("click", function(){
	paragraph[i].style.fontWeight = "bold"
})
}

let nameForm = document.forms[0];
console.log(nameForm)

let subBtn = document.getElementById("submit")
let firstName = document.getElementById("fname")
	let lastName = document.getElementById("lname")

// function addName (event) {
// 	event.preventDefault();
// 	let firstName = event.target.elements.fname;
// 	let lastName = event.target.elements.lname;
// 	let fnameValue = firstName.value
// 	let lnameValue = lastName.value

// }




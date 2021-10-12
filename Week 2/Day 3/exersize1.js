// NUMBER ONE
// Create an array called colors where the value is a list of your favorite colors.
// Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .


// let colors = ["orange", "green", "black", "blue"];

// for (let i = 0; i < colors.length; i++){
// 	console.log('my #' + (i+1) + ' choice is ' + colors[i]);
// } 

// NUMBER TWO
// let people = ["Greg", "Mary", "Devon", "James"]
// Write code to remove “Greg” from the people array.
// Write code to replace “James” to “Jason”.
// Write code to add your name to the end of the people array.
// Using a loop, iterate through the people array and console.log each person.
// Using a loop, iterate through the people array and after you console.log “Jason” exit the loop.
// Write code to make a copy of the people array using slice. The copy should NOT include “Mary” or your name.
// Write code that console.logs Mary’s index. take a look at indexOf on google.
// Write code that gives the indexOf “Foo” (this should return -1). Why does it return -1
// Create a variable called last which value is the last element of the array.
// Hint: What is the relationship between the index of the last element in the array and the length of the array?

// let people = ["Greg", "Mary", "Devon", "James"]
// people.splice(0, 1,)
// people.splice(2, 1, "Jason")
// people.push("Fayga")
// // console.log(people)

// for (let i = 1; i< people.length; i++){

// }
// console.log(people)

// NUMBER THREE

// Prompt the user for a number, while the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?
// Hint : Check the data type you receive from the prompt (ie. typeof method)

// let text = ""
// let i = 0;

// do {
//   text += "<br>The number is " + i;
//   i++;
// }
// while (i < 10)

// let count = parseInt(prompt("enter a number that is less than 10"))

// do{
// 	count;
// }
// while (count < 10){
	
// }
// console.log(count)

// NUMBER FOUR

// Given the object above where the key is the students name and the value is the country they are from.

// Prompt the student for their name :
// If the name is in the object, console.log the name of the student and the country they come from.
// example: "Hi! I'm [name], and I'm from [country]."
// Hint: Look up the statement if ... in
// If the name is not in the object, console.log: "Hi! I'm a guest."

// let guestList = {
//   randy: "Germany",
//   karla: "France",
//   wendy: "Japan",
//   norman: "England",
//   sam: "Argentina"
// }

// let guestName = prompt("what is your name")

// for (let i = 0; guestName ===  in guestList){
// 	console.log('hi! im', guestName , and i am from [i])
// }

// NUMBER FIVE DONE
// Create an object called family with a few key value pairs.
// Console.log the keys. (using a for loop).
// Console.log the values. (using a for loop).

// let family = {
// 	lName: "Smith",
// 	city: "New York",
// 	members: 7,
// };

// for (let element in family){
// 	console.log([element])
// }

// // for (let element in family){
// // 	console.log(family[element])
// // }

// NUMBER SIX DONE


// Given the object above, console.log “my name is Rudolf the raindeer”

// const details = {
//   my: 'name',
//   is: 'Rudolf',
//   the: 'raindeer'
// }
// const myJSON = JSON.stringify(details);

// // console.log(myJSON)

// let noPunc = myJSON.replace(/[,":]/g , " ");

// console.log(noPunc)

// NUMBER SEVEN

// A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
// Hint: a string is an array of letters
// Console.log the name of their secret society.

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
let str = '' 
for (let i = 0; i < names.length; i++) {
  	str = str + names[i];
  	console.log(str)

  // console.log(names[i][0]);
}

// let secretClub = (names[i][0]);
// let clubName = JSON.stringify(secretClub);

// console.log(clubName)



 // let s = 'hello world'
// let str = ""
// for (let i = 0; i < s.length; i++) {
//         // h- + e + - 
//         // h-e-
//     str = str + s[i] + '-'




















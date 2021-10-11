// Given the years two people were born, find the date when the younger one is exactly half the age of the older.
// Notes: The dates are given in the format YYYY

// NUMBER ONE NOT DONE HIGHLY CONFUSED :/

// let ageOne = parseInt(prompt("what year were you born in?"))
// let ageTwo = parseInt(prompt("what year were you born in?"))


// function fnCalculateAge(){
	 
//      // convert user input value into date object
// 	 var birthDate = new Date(userDateinput);
// 	  console.log(" birthDate"+ birthDate);
	 
// 	 // get difference from current date;
// 	 var difference=Date.now() - birthDate.getTime(); 
	 	 
// 	 var  ageDate = new Date(difference); 
// 	 var calculatedAge=   Math.abs(ageDate.getUTCFullYear() - 1970);
// 	 alert(calculatedAge);
// }


// function calculate_age(dob) { 
//     var diff_ms = Date.now() - dob.getTime();
//     var age_dt = new Date(diff_ms); 
  
//     return Math.abs(age_dt.getUTCFullYear() - 1970);
// }

// console.log(calculate_age(new Date("ageOne")));

// console.log(calculate_age(new Date("ageTwo")));






// if (ageOne > ageTwo){
// 	console.log(ageTwo*2 = ageOne)
// }

// 


// NUMBER TWO NOT DONE YET

// Hint : This exercise has 2 parts. First, do this exercise without Regular Expressions, then do it using Regular Expressions

// While working in a Post Office you must have the clients’ zip code in order to send them their letters.
// Ask the client for their zip code and console.log “success” or “error” based on the following rules.
// Zip codes consists of 5 numbers
// Must only contain numbers
// Must not contain any whitespace (spaces)
// Must not be greater than 5 digits in length

let zipCode = (prompt("enter your zip code"))

if (zipCode.length === 5 && ) {
	console.log("success")
}

else {
	console.log("error")
}



// NUMBER THREE

// let userWord = prompt("insert a word")
// noVowel = userWord.replace( /[aeiou]/g, '')
// console.log(noVowel);


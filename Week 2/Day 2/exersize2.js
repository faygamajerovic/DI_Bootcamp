// NUMBER ONE

// let userLang = prompt("what language do you speak?").toLowerCase()
// switch(userLang) {
// 	case "french":
// 	console.log("bonjour")
// 	break;
// 	case "english":
// 	console.log("hello")
// 	break;
// 	case "hebrew":
// 	console.log("shalom")
// 	break;
// 	default:
// 	console.log("01110011 01101111 01110010 01110010")
// }

// NUMBER TWOHI\

// let userGrade = parseInt(prompt("what is your grade?"))
//  if (userGrade > 90){
//  	console.log("A")
//  }

//  else if (userGrade > 80){
//  	console.log("B")
//  }

//   else if (userGrade >= 70){
//  	console.log("C")
//  }

//  else {
//  	console.log("D")
//  };

// NUMBER THREE
// Prompt the user for a string. It must be a verb.
// If the length of the string is at least 3 and the string doesn’t end with “ing”, add ‘ing’ to the end of the string.
// If the length of the string is at least 3 and the string ends with “ing” add “ly” to it’s end.
// If the length of the string is less than 3, leave it unchanged.

let userVerb = prompt("give me a verb")

if (userVerb.length >= 3 && userVerb.slice(-3)!=="ing"){
	console.log(userVerb +="ing")
};

if (userVerb.length >= 3 && userVerb.slice(-3) ==="ing"){
	console.log(userVerb +="ly")
};

if (userVerb.length < 3){
	console.log(userVerb)
};








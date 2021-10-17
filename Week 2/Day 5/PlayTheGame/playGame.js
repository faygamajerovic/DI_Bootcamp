

 function playTheGame (){
 let userReply = confirm("would you like to play?")
 	if(userReply === false){
 		console.log(alert("No problem, Goodbye"))
 	} else if(userReply===true){
 		let number = parseInt(prompt("enter a number between 0 and 10"))
 	 		 if(isNaN(number)){
 				alert("sorry its not a number, goodbye")
 	} else if(number > 10 || number < 0){
 				alert("sorry its not a good number, goodbye")
 	} else if (number >=0 && number <=10) {
 		let computerNumber = Math.round(Math.floor((Math.random() * 10) + 1))
 		console.log(computerNumber)
 		logic(computerNumber, number)
 	} return number;
} 
 } 
 playTheGame()


function logic (comp, user) {
		for (let i=0; i < 3; i++) {
			if(comp === user){
				alert("WINNER")
				break;
			}
				
		 	if(user > comp){
 				comp=prompt("Your number is bigger than the computer's, try again")
 			} else if(user< comp){
 				comp=prompt("Your number is smaller than the computer's, try again")
 			} else {
 				alert("out of chances")
 			}
 }
	 }

logic()


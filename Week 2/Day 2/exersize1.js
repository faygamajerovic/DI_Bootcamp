
// NUMBER ONE

let x = 5;
let y = 2;

if (x > y){
	console.log("x is the biggest number")
}

if (y > x){
	console.log("y is the biggest number")
}

// NUMBER TWO

let newDog = "Chihuahua";
console.log(newDog.length)
console.log(newDog.toUpperCase())
console.log(newDog.toLowerCase())

if (newDog === "Chihuahua") {
	console.log("I love Chihuahuas, it's my favorite dog breed");
} else {
	console.log("i dont care i prefer cats");

}

// NUMBER THREE

let usrnumb = (prompt("choose a number"));

if (usrnumb %2==0){
	console.log(usrnumb + ' is an even number');
}

if (usrnumb %2!==0){
	console.log(usrnumb + ' is an odd number');
}

// NUMBER FOUR


let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]
console.log(users.length)

if (!users){
	console.log("no one is online")
}

else if (users < 2) {
	console.log("name of user")
}

else if (users < 3) {
	console.log("name of user" + "name of user")

}

else {
	console.log("Lea123", "Princess45", "and 2 others")
}


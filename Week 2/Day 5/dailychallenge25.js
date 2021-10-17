// / Prompt the user for a number to begin counting down bottles.
// // In the song everytime a bottle falls we subtract the bottles by 1.
// // What your code should do is:
// instead of subtracting by 1, everytime a bottle drops the subtracted number should go up by 1
// For example the first time a bottle drops we subtract by 1, the second time we subtract by 2 and so on.
// Take a look below for more help.
// 99 bottles of beer on the wall
// 99 bottles of beer
// Take 1 down, pass it around
// 98 bottles of beer on the wall
// 98 bottles of beer on the wall
// 98 bottles of beer
// Take 2 down, pass them around
// 96 bottles of beer on the wall
// 96 bottles of beer on the wall
// 96 bottles of beer
// Take 3 down, pass them around
// 93 bottles of beer on the wall

// ==============================

// How will you choose to make the song end?
// Make sure you get the grammar correct.




// let startNumber = parseInt(prompt("choose a number to begin with"))
// let bottle = 1
 
// 	 for (let i = startNumber; i >=1; (i=i-1)+1) {
//  		if( i=== 1){
//  		console.log(i, "bottle of beer on the wall");
 		
//  	} 	else if(i>1){
//  		console.log(i, "bottles of beer on the wall", i, "bottles of beer take", (bottle + 1), "down pass it around", (i-(bottle+1)), "bottles of beers on the wall");
//  	}	

// 	 }

let userPrompt = prompt('Welcome to the "99 Bottles of Beer" song!\nEnter a number:');

const isValidNum = (numberV) => numberV !== undefined && numberV !== null && numberV.length > 0 && !isNaN(numberV);

while (!isValidNum(userPrompt)) userPrompt = prompt('InuserPromptalid try again?!\nEnter a number:');

const sing = (userPrompt) => {

    let total = userPrompt;

    for (let i = 1; i <= total; i++) {
        console.log(`${total} ${total > 1 ? 'bottles' : 'bottle'} of beer on the wall`);
        console.log(`${total} ${total > 1 ? 'bottles' : 'bottle'} of beer`);
        console.log(`Take ${i} down, pass ${i > 1 ? 'them' : 'it'} around`);
        total -= i;
        console.log(`${total - i < 1 ? 'Not enough' : total > 1 ? 'bottles' : 'bottle'} bottles of beer on the wall`);
    }
    console.log(`Not enough bottles of beer on the wall`);
    console.log(`Not enough bottles of beer`);
    console.log(`Go to the store and buy some more`);
    console.log(`${userPrompt} bottles of beer on the wall`);
}


sing(Number(userPrompt));

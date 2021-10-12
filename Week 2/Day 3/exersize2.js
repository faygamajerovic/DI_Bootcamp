// NUMBER ONE

// let building = {
//     numberLevels : 4,
//     numberOfAptByLevel : {
//         "1": 3,
//         "2": 4,
//         "3": 9,
//         "4": 2,
//     },
//     nameOfTenants : ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         "Sarah": [3, 990],
//         "Dan":  [4, 1000],
//         "David": [1, 500],
//     },
// }

// Console.log the number of levels in the building.
// Console.log how many apartments are on levels 1 and 3.
// Console.log the name of the second tenant and the number of rooms he has in his apartment.
// Check if the sum of Sarah and David’s rent is bigger than Dan’s rent.
// If it is than increase Dan’s rent.

// console.log(building[0])

// NUMBER TWO

// Loop through the array above and determine whether or not each number is divisible by three.
// Each time you loop console.log “true” or “false”.
 
//  let number = [123, 8409, 100053, 333333333, 7]



// Teaching Assistant JavaScript11:56 AM
// let s = 'hello world'
// let str = ""
// for (let i = 0; i < s.length; i++) {
//         // h- + e + - 
//         // h-e-
//     str = str + s[i] + '-'
// }

// console.log(str)
// console.log(s)

// '**'
let num = 2
let str = ''
for( let i = 0; i < num; i++) {
    str = str + "*"
}
console.log(str)















 // NUMBER THREE

//  Requirements : Don’t use built-in Javascript methods to answer the following questions. You have to create the logic by yourself. Use simple for and while loops.
// 1. Console.log the sum of all the numbers in the age array.
// 2. Console.log the largest age in the array.

let age = [20,5,12,43,98,55];

    let sum = age.reduce(function(a, b){
        return a + b;
    }, 0);

    console.log(sum)
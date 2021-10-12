// NUMBER ONE

// Write a JavaScript program that recreates the pattern below.
// Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out “nested for loops” on Google).
// Do this Daily Challenge by youself, without looking at the answers on the internet

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
// let num = [1, 2, 3, 4, 5, 6,]
// let str = ''
// for( let i = 0; i < num; i++) {
//     str = str + "*"
//     console.log(str)
// }

let num = ["*", "*", "*", "*", "*", "*"]
let str = '' 
for (let i = 0; i < num.length; i++) {
  	str = str + num[i];
  	console.log(str)
  }


// NUMBER TWO

// Using the .toString() method convert the array to a string.
// Using the .join()method convert the array to a string. Try passing different values into the join.
// Eg .join(“+”), .join(” “), .join(“”)
// Bonus : To do this Bonus look up how to work with nested for loops
// Sort the numbers array in descending order, do so using for loops (Not using built-in sort methods).
// The output should be: [9,8,7,6,5,4,3,2,1,0]
// Hint: The algorithm is called “Bubble Sort”
// Use a temporary variable to swap values in the array.
// Use 2 “nested” for loops (Nested means one inside the other).
// Add comments and console.log the result for each step, this will help you understand.
// Requirement: Don’t copy paste solutions from Google

// const numbers = [5,0,9,1,7,4,2,6,3,8]
// let str = numbers.toString()
// 	console.log (str)


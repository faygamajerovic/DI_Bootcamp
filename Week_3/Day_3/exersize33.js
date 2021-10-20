// Move the box from left to right
// Tip: use setInterval



// setInterval
// let section = document.getElementById("animate")
// let button = document.querySelector("p")

// button.addEventListener("click", stopAnimation)


// function myMove() {
//   let box = "animate";
//   let elem = document.getElementById("animate");   
//   let pos = 0;
//   clearInterval(box);
//   box = setInterval(frame, 5);
//   function frame() {
//     if (pos == 350) {
//       clearInterval(box);
//     } else if (state == 1){
//         thisLeft += 100;
// }
//  thisText.style.left=thisLeft +"px";
//     // else {
//     //   pos++; 
//     //   elem.style.top = pos + "px"; 
//     //   elem.style.left = pos + "px"; 
//     // }
//   }
// }

let button = document.querySelector("p")
function myMove() {
    button.addEventListener("click", function () {
        let e = document.getElementById("animate");
        let s = .5;
        setInterval(function(){
            let eLeftPos = e.offsetLeft;
            e.style.left = (eLeftPos + s) + 'px';

        }, 1000);

    })
}

myMove()
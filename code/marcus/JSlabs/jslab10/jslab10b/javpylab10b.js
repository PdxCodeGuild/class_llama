// let user_num = document.getElementById("user_num");
let submit = document.getElementById("submit");
let average = document.getElementById("average");
let averaged = document.getElementById("averaged")

let nums = [];

// alert("Welcome to the Number Averager!")

submit.addEventListener("click", function(){
    let user_num = document.getElementById("user_num").value;
    
    nums.push(parseInt(user_num));
    console.log(user_num)
    console.log(nums)
})

    
    
average.addEventListener("click", function(){
    console.log(nums)
    // reduce = a + b returns a+b
    // a= the current total b = the current itterator
    let average_num = nums.reduce((a,b) => (a + b)) / nums.length;
 
    
    let the_average = document.createElement("p")
    the_average.innerText = average_num

    averaged.appendChild(the_average)



})
        


    

// function average(nums) {
//     let average_num = nums.reduce((a,b) => (a + b)) / nums.length;
//     console.log(nums)
//     alert(average_num)
//     // return nums.reduce((a,b) => (a + b)) / nums.length;
// }

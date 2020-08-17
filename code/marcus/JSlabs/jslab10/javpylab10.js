let nums = [];

alert("Welcome to the Number Averager!")

let i = 0;
while (i < 1) {

    let user_num = prompt("Please submit a number");

    
    if (user_num !== "done"){
        nums.push(parseInt(user_num));
    }
    else {
        
        average(nums)
        i++;
    }
    
}
function average(nums) {
    let average_num = nums.reduce((a,b) => (a + b)) / nums.length;
    console.log(nums)
    alert(average_num)
    // return nums.reduce((a,b) => (a + b)) / nums.length;
}









let nums = [];

alert("Welcome to the Number Averager!")

let i = 0;
while (i < 1) {

    let user_num = prompt("Please submit a number");

    nums.push(user_num);
    if (user_num == "done");
    i++;
}
function average(nums) {
    return nums.reduce((a,b) => (a + b)) / nums.length;
}









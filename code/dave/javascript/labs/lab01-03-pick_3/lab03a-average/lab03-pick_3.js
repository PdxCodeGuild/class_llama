// This program will take a list of integers(nums) and return the average

// version #1
// """
// This program will ask user for number inputs
// until the user terminates with done. Then all numbers 
// will be added as a running total. 
// """

// # initialize an empty list nums to store user input
let nums = [];

// # create while loops that prompts user to input a number until 'done' is entered
let input = true;
while (input) {
    input_number = prompt("Enter a number, or 'done': ");
    if (input_number == 'done') {
        input = false;
    }
    else {
        nums.push(input_number);
    }
}

// while True:
//     input_number = input("enter a number, or 'done': ")
//     if input_number == 'done':
//         break
//     // # add all user input numbers to the nums list
//     nums.append(int(input_number))

// # print list of numbers added for user to view
console.log(nums);
// print(nums)

// # create variable that calculates the average by dividing the sum of all input numbers by the length of input numbers.
let sum = 0;
for (let i=0; i<nums.length; i++) {
    sum += parseInt(nums[i], 10); // base10
}
let average = sum/nums.length;

// print("average:",average)
console.log("The average of nums is: " + average);
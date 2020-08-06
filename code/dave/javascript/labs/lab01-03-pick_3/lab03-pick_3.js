// This program will take a list of integers(nums) and return the average

// version #1
// let nums = [5, 0, 8, 3, 4, 1, 6];

// // loop over the elements
// nums.forEach(function(num) {
//     console.log(num);
// });
// for num in nums:
//     print(num)

// loop over the indices
// for (let i=0; i<nums.length; i++) {
//     console.log(nums[i]);
// }
// for i in range(len(nums)):
//     print(nums[i])


// initialize the variable total to hold the sum of all numbers in list
// let total = 0;

// // loop through each indices of nums list
// for (let i=0; i<nums.length; i++) {
//     total=total+nums[i];
//     console.log(total);
// }
// total = total / nums.length;
// console.log("The average is: " + total);
// for i in range(len(nums)):
//     total=total+nums[i]
//     print(total)
// print("The average is: ",total / len(nums))

// version #2
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
// average = sum(nums) / len(nums)
console.log("The average of nums is: " + average);
// print("average:",average)
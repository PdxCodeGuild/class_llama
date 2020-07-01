"""
This program will ask user for number inputs
until the user terminates with done. Then all numbers 
will be added as a running total. 
"""

# initialize an empty list nums to store user input
nums = []

# create while loops that prompts user to input a number until 'done' is entered
while True:
    input_number = input("enter a number, or 'done': ")
    if input_number == 'done':
        break
    # add all user input numbers to the nums list
    nums.append(int(input_number))

# print list of numbers added for user to view
print(nums)

# create variable that calculates the average by dividing the sum of all input numbers by the length of input numbers.
average = sum(nums) / len(nums)
print("average:",average)

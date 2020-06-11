"""
This program will take a list of integers(nums) and return the average
"""

nums = [5, 0, 8, 3, 4, 1, 6]

# loop over the elements
for num in nums:
    print(num)

# loop over the indices
for i in range(len(nums)):
    print(nums[i])


# initialize the variable total to hold the sum of all numbers in list
total = 0

# loop through each indices of nums list
for i in range(len(nums)):
    total=total+nums[i]
    print(total)
print("The average is: ",total / len(nums))
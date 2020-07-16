# Credit Card Validation


# convert the string into a list of ints
nums = 4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5
nums = list(nums)
print(nums)

check_digit = nums[15]
print(check_digit)
 
# remove the last digit (this is the check digit)
del nums[15]
print(nums)

# reverse the digits
nums.reverse()
print(nums)

# double every other element in the reversed list
nums[0::2] = [x*2 for x in nums[0::2]]
print(nums)

# subtract nine from numbers over nine
nums = [x-9 if x > 9 else x for x in nums]
print(nums)

# get the sum of all values
number = sum(nums)
print(number)

# take the second digit of the sum
verify = str(number)
digit = verify[1]
# print(verify)
print(digit)

# if the second digit matches the check digit, the whole card number is valid
if int(digit) == int(check_digit):
    print("Valid!")
else:
    print("Not valid.")
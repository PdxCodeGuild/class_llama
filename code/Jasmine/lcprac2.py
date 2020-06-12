''' 
Problem 2
Write a comprehension to generate the first 10 even numbers.

[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

'''
nums = [n for n in range(2,21,2)]
nums = [n*2 for n in range(1,11)]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print(nums)

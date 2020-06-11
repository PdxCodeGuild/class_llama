# Average Numbers

# Please enter this list of numbers: 5, 0, 8, 3, 4, 1, 6

"""
 nums = [5, 0, 8, 3, 4, 1, 6]
 avg = sum(nums)/len(nums)
 print(avg)
 """

nums = []

lst_size = int(input('Enter list size: ' ))

for i in range(0, lst_size):
    nums.append(int(input('Enter numbers: ')))

avg = sum(nums)/lst_size

print('Average: ', avg)
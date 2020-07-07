# Lab 10, Average Number finder
# Remove ''' between versions.

# Version 1

'''
nums = [5, 0, 8, 3, 4, 1, 6]
average = sum(nums) / len(nums)

print(f"Our list of numbers is {nums}.")
print(f"The average of the list is {round(average)}.")
'''

# Version 2

'''
user_list = []
count = 0

print("Welcome to the averager.")

while count < 1:
    entered = input("Type a number, or \"done\" if you're finished. ").lower()
    if entered == 'done':
        count += 1
        break
    else:
        user_list.append(float(entered))
    
    
average = sum(user_list) / len(user_list)

print(f"The average of your list is {round(average)}.")
'''
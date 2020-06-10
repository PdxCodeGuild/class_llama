# Average Numbers

nums = [5, 0, 8, 3, 4, 1, 6]


while True:

    new_num = input("Please enter a new number, or 'done': ")

    if new_num == "done":
        average = sum(nums) / len(nums)
        print(f"The final average is: {average}.")

    else:
        nums.append(float(new_num))
        print(nums)
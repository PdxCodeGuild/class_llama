def main():
    nums = []
    done = False
    while done == False:
        new_item = input("type a number to put into the list, or type done when you've input all the numbers: ")
        if new_item == "done":
            done = True
        else:
            new_item = int(new_item)
            nums.append(new_item)

    sum = 0
    for number in nums:
        sum = sum + number

    length = len(nums)
    average = sum/length
    print(f"the average of the numbers input is {average}")

if __name__ == "__main__":
    main()

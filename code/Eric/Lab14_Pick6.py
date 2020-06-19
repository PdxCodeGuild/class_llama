import random

def generateRandomNumber():
    random_num = random.randint(0,9)
    return random_num

def generateLotteryNumbers(num_of_numbers):
    lottery_numbers = []

    for lottery_numbers in range(num_of_numbers):
        random_num = generateRandomNumber()
        lottery_numbers.append(random_num)

    return lottery_numbers

    def printLotteryNumbers(lottery_numbers):
        for lottery_numbers in range(len(lottery_numbers)):
            print(lottery_numbers[lottery_numbers])

    

   


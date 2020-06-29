import random

#Create an empty list that will be used to store the 6 random numbers
lotteryNumbers = []

for i in range (0,6):
  number = random.randint(1,99)
  #Check if this number has already been picked
  
while number in lotteryNumbers:
  loop_run = 
  number = random.randint(1,99)
  loop_run <= 100000  
    
  #Now that we have a unique number, let's append it to our list.
  lotteryNumbers.append(number)

  #Sort the list in ascending order
  lotteryNumbers.sort()

#Display the list on screen:
print(">>> Today's lottery numbers are: ") 
print(lotteryNumbers)
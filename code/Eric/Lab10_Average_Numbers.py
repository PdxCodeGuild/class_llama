
num = int(input('Please enter how many numbers to average: '))

total_sum = 0

for n in range(num):

    numbers = float(input('Input a number : '))

    total_sum += numbers

avg = total_sum/num

print('Average of the', num, ' numbers is :', avg)
# Pick-6 Lottery

import random

# use randint to generate the winning ticket as well as user ticket(s)
winning_nums = [random.randint(1,99) for x in range(6)]
print(winning_nums)


for i in range(100000):
    user_nums = [random.randint(1,99) for x in range(6)]
    # I don't want to look at this 100,000 times
    # print(user_nums)

# zip(winning_nums,user_nums)?




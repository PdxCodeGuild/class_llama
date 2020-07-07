# PROBLEM 1

# Write a function that tells whether a 
# number is even or odd.
def is_even(a):
    if a%2 == 0:
        return True
    else:
        return False

# TEST
# print(is_even(5))
# print(is_even(6))

# PROBLEM 2

# Write a function that takes two ints, a and 
# b, and returns True if one is positive 
# and the other is negative.

def opposite(a, b):
    if a < 0 and b >= 0:
        return True
    elif a >= 0 and b < 0:
        return True
    else:
        return False

# TEST
# print(opposite(10, -1))
# print(opposite(10, 10))

# PROBLEM 3

# Write a function that returns True
# if a number is within 10 of 100.

def near_100(num):
    if num <= 110 and num >= 90:
        return True
    else:
        return False

# TEST
# print(near_100(50))
# print(near_100(99))
# print(near_100(105))

# PROBLEM 4

# Write a function that returns the
# maximum of 3 parameters
def maximum_of_three(a, b, c):
    if a >= b and a >= c:
        highest_num = a
    elif b >= a and b >= c:
        highest_num = b
    else:
        highest_num = c
    return highest_num

# Same function but turn parameters
# into a list then use max()
def maximum_of_three_version2(a, b, c):
    list = [a, b, c]
    return max(list)

# TEST
# print(maximum_of_three(5, 6, 2))
# print(maximum_of_three(-4, 3, 10))
# print(maximum_of_three_version2(4, 4, 2))


# PROBLEM 5

# Print out the powers of 2 from 2^0 to 2^20

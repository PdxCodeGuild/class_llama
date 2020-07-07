# Lab 20
# CC validation

# Turn string of C numbers into integer list
def lister(cc):
    cc = cc.split()
    for i in range(len(cc)):
        cc[i] = int(cc[i])
    return cc

# Return last digit as check digit
def slicer(cc):
    return cc[-1]
       
# Remove check digit and reverse remaining numbers
def reverser(cc):
    del cc[-1]
    cc.reverse()
    return cc

# Double every other number
def doubler(cc):
    for i in range(0,len(cc),2):
        cc[i] *= 2
    return cc
        
# Subtract 9 if digits are greater than 9
def subtract_nine(cc):
    for i in range(len(cc)):
        if cc[i] > 9:
            cc[i] -= 9
    return cc

# Add all remaining values together
def total(cc):
    return sum(cc)
    
# Return second digit of sum
def second(cc):
    stringed = str(cc)
    digit = stringed[1]
    return int(digit)
    

entered = input("Enter your unusually formatted credit card: ")

# Turns input to list
cc_list = lister(entered)
# Establishes last digit as check digit variable
check_digit = slicer(cc_list)
# Remove check digit and reverse digits
backward_cc = reverser(cc_list)
# Double every other element
dubbed = doubler(backward_cc)
# Subtract 9 from numbers over 9
smol = subtract_nine(dubbed)
# Add all values
added = total(smol)
# Check second digit
valid_digit = second(added)

if valid_digit == check_digit:
    print("It's valid here!")
else: 
    print("It's invalid!")


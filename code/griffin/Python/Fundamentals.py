def even_or_odd(number):
    if number % 2 == 0:
        return "that number is even"
    elif number % 2 == 1:
        return "that number is odd"

def opposite(x,y):
    if x<0<y or y<0<x:
        return True
    else:
        return False

def near_100(x):
    if 0 < 110 - x < 20:
        return True
    else:
        return False


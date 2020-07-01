import turtle

## magic code don't forget
wn = turtle.Screen()

# initialize this turtle in variable 't'
t = turtle.Turtle()


# # create code that draws a pattern
# for i in range(20):
#     t.forward(i*2)
#     t.left(90)
#     t.forward(i*2)
#     t.left(45)
#     t.forward(i*3)

my_range = input("What is the range: ")

# create func that using recursion of previous for loop above this
def recursive_shape():

    # set speed to see it move quickly
    t.speed(20)

    for i in range(my_range):
        t.forward(i*2)
        t.left(90)
        t.forward(i*2)
        t.left(45)
        t.forward(i*3)

recursive_shape()



## magic code to keep graphical interpretation open
wn.exitonclick()
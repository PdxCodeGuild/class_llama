import turtle

## magic code don't forget
wn = turtle.Screen()
wn.bgcolor("black")

# initialize this turtle in variable 't'
t = turtle.Turtle()
t.shape("turtle")
t.color("green", "green")

'''
Speed is determined by:

    'fastest'   :   0
    'fast'      :   10
    'normal'    :   6
    'slow'      :   3
    'slowest'   :   1
'''

# speed determines how fast the turtle 'draws'
t.speed(3)

# # create square box outline with turtle :METHOD1 'noob'
# t.forward(300)
# t.left(90)
# t.forward(300)
# t.left(90)
# t.forward(300)
# t.left(90)
# t.forward(300)

# begin_fill needs to come before the shape
t.begin_fill()

# fillcolor also needs to be declared before
t.fillcolor("red")

# # create square box outline with turtle :METHOD2 'for loop'
for i in range(4):
    t.forward(300)
    t.left(90)

# end_fill comes after you draw your shape
t.end_fill()

# hide turtle
t.hideturtle()


## magic code to keep graphical interpretation open
wn.exitonclick()
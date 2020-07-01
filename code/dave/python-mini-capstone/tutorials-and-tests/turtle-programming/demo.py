

# import turtle library
import turtle

# # basic example of drawing line, assigning bgcolor, moving turtle
# my_window = turtle.Screen()
# my_window.bgcolor("blue")       # creates a graphics window
# my_pen = turtle.Turtle()
# my_pen.forward(150)
# my_pen.left(90)
# my_pen.forward(75)
# my_pen.color("white")
# my_pen.pensize(12)
# turtle.done()                   # this stops the graphics window from closing automatically


## DRAW SQUARE ##
# my_pen = turtle.Turtle()      
# for i in range(4):
#    my_pen.forward(50)           
#    my_pen.right(90)               
# turtle.done()

## DRAW STAR ##
my_pen = turtle.Turtle()
my_pen.speed(30)
for i in range(500):
    my_pen.forward((i*30)^3)
    my_pen.right(144)
turtle.done()

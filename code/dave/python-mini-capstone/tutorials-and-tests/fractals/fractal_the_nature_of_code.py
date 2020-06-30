from turtle import *


# set static screen color
setup(width=750, height=500)
bgcolor("black")
shape("circle")
shapesize(10,10)
fillcolor("orange")
fillcolor()

exitonclick()

'''
# prints fractal image of sun with points
speed(4)
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
'''
















'''# Method #1
import turtle
turtle.Turtle()

# # Method #2
# from turtle import *

nw = turtle.getscreen()

# create t2 turtle
t2 = turtle.Turtle()
t2.color('red', 'yellow')
t2.begin_fill()
while True:
    t2.fd(200)
    t2.lt(170)
    if t2.abs(pos()) < 1:
        break
t2.end_fill()
t2.done()'''











'''
## creates a square by moving forward, turing right, then backing up. This is repeated until a square is formed.
new_window = turtle.getscreen()
t1 = turtle.Turtle()

# determine speed of turtle
t1.speed(1)

# movement action for turtle
t1.fd(200)
t1.rt(90)
t1.bk(200)
t1.rt(90)
t1.fd(200)
t1.rt(90)
t1.bk(200)
t1.rt(90)
'''



# add to end of turtle code to stop from closing
# input('Press ENTER to exit')
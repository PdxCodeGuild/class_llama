from turtle import *

# initialize turtle into a variable
dave = Turtle()

# select color of cursor "turtle"
dave.color("red")
dave.shape("turtle")

# create variable to store screen in
wn = Screen()

# change bg color of the screen from white to black
wn.bgcolor("black")

# change color
colormode(255)
wn.bgcolor(170,30,20)

# add background image to screen
wn.bgpic("./img/python_logo_300x300.gif")

# change title
wn.title("Dave's World!!")

#stop turtle shell from closing after code executes
wn.exitonclick()
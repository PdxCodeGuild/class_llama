import turtle

## magic code don't forget
wn = turtle.Screen()

# initialize this turtle in variable 't'
t = turtle.Turtle()

'''
directions for setheading() are as follows (from starting point):

Start >>>   EAST  = 0   degrees
      ^^^   NORTH = 90  degrees
      <<<   WEST  = 180 degrees
      vvv   SOUTH = 270 degrees
'''

# set heading 90 degrees (NORTH)
t.setheading(90)

# move forwared 200 pixels
t.fd(200)

# move turtle right by 90 degrees
t.rt(90)

# move backward 200 pixels
t.bk(200)

# turn left 180 degrees then back 300 pixels
t.lt(90)
t.bk(300)


## magic code to keep graphical interpretation open
wn.exitonclick()
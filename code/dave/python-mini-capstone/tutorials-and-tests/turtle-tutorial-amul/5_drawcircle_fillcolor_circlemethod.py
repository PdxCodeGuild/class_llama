from turtle import Turtle, Screen

## magic code don't forget
screen = Screen()

TURTLE_SIZE = 20

# initialize this turtle in variable 't'
t = Turtle(shape="turtle", visibility=False)

t.penup()
t.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/2 - TURTLE_SIZE/2)
t.pendown()
t.showturtle()

screen.mainloop()

# draw circles
t.speed(1)
t.circle(50)
t.circle(-70)
t.circle(100, 180)

t.circle(150)
t.circle(-70)
t.circle(100, 180)

'''
# # iterate circles increasing step each loop
def fractal_test():
    t = turtle.Turtle()
    t.speed(0)

    for i in range(50):
        t.circle(30,steps=2**i)
        fractal_test()
        t.circle(-50,steps=2**i)
        t.circle(70,steps=2**i)

fractal_test()
'''

## magic code to keep graphical interpretation open
screen.exitonclick()
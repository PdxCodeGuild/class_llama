''' 
Pillow can also be used to draw, the code below demonstrates some functions that 
Pillow provides. Use these functions to draw a stick figure.
'''
from PIL import Image, ImageDraw

# draw circle for head, attach retangle for body, add two lines for arms, two lines for legs

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill="gray")

circle_x = width/2
circle_y = height/2
circle_radius = 100
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')


# draw a line from x0, y0, x1, y1
# using the color pink
color = (256, 128, 128)  # pink
#arms
draw.line((0, 0, width, height), fill="red")
draw.line((0, height, width, 0), fill="red")
#legs
draw.line((0, 0, width, height), fill="red")
draw.line((0, height, width, 0), fill="red")

# draw a rectangle from x0, y0 to x1, y1
draw.rectangle(((100, 100), (300, 300)), fill="lightblue")






img.show()